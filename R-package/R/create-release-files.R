source(file.path(getwd(), "R", "odm-dictionary-file.R"))
source(file.path(getwd(), "R", "files.R"))
#' Create release files
#'
#' Creates release files given the user OSF link and auth token.
#'
#' @param OSF_LINK_RELEASE link to the dictionary stored on OSF used for updating.
#' @param OSF_LINK_PAST_RELEASE link to the dictionary stored on OSF used for removal of previous release files.
#' @param OSF_TOKEN OSF auth token used for modifying OSF directories
#' @param dictionary_path optional string containing path to the dictionary directory. When provided no dictionary is downloaded.
#' @param past_dictionary_path optional string containing path to the previous release dictionary directory. When provided no dictionary is downloaded.
#'
#' @export
create_release_files <-
  function(OSF_LINK_RELEASE,
           OSF_LINK_PAST_RELEASE,
           OSF_TOKEN,
           dictionary_path = NULL,
           past_dictionary_path = NULL) {
    # Setup logging
    # Remove previous log
    file.remove(odm_dictionary$log_path)
    # Set logger appending
    logger::log_appender(logger::appender_file(odm_dictionary$log_path))
    
    # Download file using passed credentials
    if (is.null(dictionary_path)) {
      dictionary_path <- odm_dictionary$tmp_dictionary_directory
      osfr::osf_auth(OSF_TOKEN)
      osfr::osf_retrieve_file(OSF_LINK_RELEASE) %>%
        osfr::osf_download(path = dictionary_path)
    }
    # Validate dictionary version
    dictionary_info <- validate_version(dictionary_path)
    
    dictionary <- dictionary_info[[1]]
    dictionary_version <- dictionary_info[[2]]
    
    # Validate files sheet
    files_to_make <-
      validate_files_sheet(dictionary,
                           dictionary_version)
    
    create_files(files_to_make,
                 dictionary)
    
    # Download previous release dictionary
    if (is.null(past_dictionary_path)) {
      past_dictionary_path <-
        odm_dictionary$tmp_dictionary_directory_past_release
      osfr::osf_auth(OSF_TOKEN)
      osfr::osf_retrieve_file(OSF_LINK_PAST_RELEASE) %>%
        osfr::osf_download(path = past_dictionary_path)
    }
    # Validate dictionary version
    past_dictionary_info <- validate_version(past_dictionary_path)
    
    past_dictionary <- past_dictionary_info[[1]]
    past_dictionary_version <- past_dictionary_info[[2]]
    
    # Validate files sheet
    files_to_remove <-
      validate_files_sheet(past_dictionary,
                           past_dictionary_version)
    
    remove_files(files_to_make,
                 dictionary)
  }

#' Validate Version
#'
#' Validate dictionary version between file name and summary sheets.
#'
#' @param dictionary_path string containing path to the dictionary directory.
#'
#' @return list with: Dictionary file name, Dictionary version, Boolean representing if the versions match.
validate_version <- function(dictionary_path) {
  # Acquire version number from file name
  dictionary_version_pattern <- "ODM_dictionary_(\\d.*?).xlsx"
  file_names <-
    list.files(file.path(getwd(), dictionary_path),
               pattern = dictionary_version_pattern)
  # Display error and stop execution for multiple dictionaries
  if (length(file_names) > 1) {
    stop('Multiple dictionaries found, only one dictionary should be stored.')
  } else if (length(file_names) == 0) {
    stop("No valid files were detected. Make sure the dictionary file is named correctly.")
  }
  dictionary_file_name_version_number <-
    regmatches(file_names,
               regexec(dictionary_version_pattern, file_names))[[1]][2]
  
  # Read in the dictionary workbook
  dictionary <- openxlsx::loadWorkbook(file.path(getwd(),
                                                 dictionary_path,
                                                 file_names))
  
  # Acquire version number from summary sheet
  summary_sheet <-
    openxlsx::readWorkbook(dictionary, odm_dictionary$summary_sheet_name)
  # Read the first column
  summary_versions <- summary_sheet[[1]]
  # Strip off any NA rows
  summary_versions <- summary_versions[!is.na(summary_versions)]
  # Select the last version
  summary_version <- summary_versions[[length(summary_versions)]]
  # Compare if the versions match
  if (summary_version != dictionary_file_name_version_number) {
    logger::log_warn("Dictionary file name version does not reflect version in summary sheet")
  }
  
  return(list(dictionary = dictionary,
              dictionary_version = summary_version))
}

#' Validate files sheet
#'
#' Validate files sheet and its internal content for proper file creation.
#'
#' @param dictionary_name string containing the file dictionary name.
#' @param version string containing the dictionary version.
#' @param dictionary_path string containing path to the dictionary directory.
#'
#' @return 2 lists containing csvs to export and another list containing excels to export.
validate_files_sheet <-
  function(dictionary,
           version) {
    files_sheet <-
      openxlsx::readWorkbook(dictionary, odm_dictionary$files_sheet_name)
    sets_sheet <-
      openxlsx::readWorkbook(dictionary, odm_dictionary$sets_sheet_name)
    parts_sheet <-
      openxlsx::readWorkbook(dictionary, odm_dictionary$parts_sheet_name)
    
    # Remove any rows with not supported file_type.
    files_sheet_formatted <-
      files_sheet[files_sheet[[files$file_type$name]] %in% files$file_type$categories, unlist(files_sheet_column_names)]
    # insert version
    files_sheet_formatted$name <-
      gsub('\\{version\\}', version, files_sheet_formatted$name)
    files_sheet_formatted[[files$add_headers$name]] <-
      gsub('\\{version\\}', version, files_sheet_formatted[[files$add_headers$name]])
    files_sheet_formatted[[files$osf_locations$name]] <-
      gsub('\\{version\\}', version, files_sheet_formatted[[files$osf_locations$name]])
    files_to_extract <- list()
    errors <- FALSE
    for (row_index in seq_len(nrow(files_sheet_formatted))) {
      working_row <- files_sheet_formatted[row_index,]
      
      # File extraction info
      fileID <- working_row[[files$file_id$name]]
      file_name <- working_row[[files$file_name$name]]
      file_type <- working_row[[files$file_type$name]]
      partID <- working_row[[files$part_ID$name]]
      add_headers <- working_row[[files$add_headers$name]]
      destination <- working_row[[files$destinations$name]]
      osf_location <- working_row[[files$osf_locations$name]]
      github_location <- working_row[[files$github_location$name]]
      
      validated_file <- FALSE
      
      # Validate destination
      if (!(destination %in% files$destinations$categories)) {
        logger::log_warn(paste0("File ID: ",
                                fileID,
                                " has an invalid destination set"))
        errors <- TRUE
      }
      
      set_info <- sets_sheet[sets_sheet$setID == partID, ]
      # Determine if the partID supplied is set or part.
      if (file_type == files$file_type$categories$excel) {
        # If part exists in sets its a set therefore all parts belonging to the set are used as partID for sheet creation.
        if (nrow(set_info) >= 1) {
          set_name <- partID
          set_parts <- set_info[["partID"]]
          partID <- set_parts
          # Set names for elements to allow removal of invalid parts
          names(set_parts) <- set_parts
          for (single_part in partID) {
            if (single_part %in% parts_sheet[["partID"]]) {
              # Check that a sheet with this part exists
              if (single_part %in% names(dictionary)) {
                next()
              } else{
                logger::log_warn(
                  paste0(
                    single_part,
                    " does not have a matching sheet but is part of ",
                    set_name,
                    " set, which was selected to be exported."
                  )
                )
                errors <- TRUE
                # Remove missing part
                set_parts <-
                  set_parts[names(set_parts) != single_part]
              }
              
            } else{
              logger::log_warn(paste0(single_part,
                                      " is missing from the parts sheet but is present in the ",
                                      set_name,
                                      " set."))
              errors <- TRUE
              # Remove missing part
              set_parts <-
                set_parts[names(set_parts) != single_part]
            }
          }
          partID <- unname(set_parts)
          # Check if any valid parts remain
          if (length(partID) >= 1) {
            validated_file <- TRUE
          }
        } else{
          if (partID %in% parts_sheet[["partID"]]) {
            if (partID %in% names(dictionary)) {
              validated_file <- TRUE
            } else{
              logger::log_warn(paste0(single_part,
                                      " does not have a matching sheet."))
              errors <- TRUE
            }
            
          } else {
            logger::log_warn(paste0(partID,
                                    " is not found in parts sheet."))
            errors <- TRUE
          }
        }
      } else if (file_type == files$file_type$categories$csv) {
        if (nrow(set_info) >= 1) {
          logger::log_warn(paste0(partID,
                                  " is recorded for csv but is found in sets."))
          errors <- TRUE
        } else{
          if (partID %in% parts_sheet[["partID"]]) {
            if (partID %in% names(dictionary)) {
              validated_file <- TRUE
            } else{
              logger::log_warn(paste0(single_part,
                                      " does not have a matching sheet."))
              errors <- TRUE
            }
            
          } else {
            logger::log_warn(paste0(partID,
                                    " is not found in parts sheet."))
            errors <- TRUE
          }
          
        }
      } else{
        logger::log_warn(paste0(partID,
                                " has an unrecognized fileType of ",
                                file_type))
        errors <- TRUE
      }
      
      # Append valid files list
      if (validated_file) {
        files_to_extract[[fileID]] <- list(
          file_name = file_name,
          file_type = file_type,
          partID = partID,
          add_headers = add_headers,
          destination = destination,
          osf_location = osf_location,
          github_location = github_location
        )
      }
    }
    # Will move with development
    # Will become stop once function development is finished
    if (errors != "") {
      
      warning("Errors were detected further building cannot continue please check the log for additional info")
    }
    return(files_to_extract)
  }

#' Create Files
#'
#' Function responsible for creating the release files based on output from validate_files_sheet
#'
#' @param files_to_extract List output from validate_files_sheet
#' @param dictionary openxlsx environment object storing the dictionary
create_files <-
  function(files_to_extract,
           dictionary) {
    # Loop over files to extract based on fileID
    for (fileID in names(files_to_extract)) {
      current_file_info <- files_to_extract[[fileID]]
      
      # Create a write_directory based on destination and saving location
      write_dir <- ""
      if (current_file_info$destination == "github") {
        write_dir <- file.path(
          getwd(),
          odm_dictionary$tmp_dictionary_directory,
          "github",
          current_file_info$github_location
        )
        dir.create(write_dir,
                   showWarnings = FALSE,
                   recursive = TRUE)
        
      } else if (current_file_info$destination == "osf") {
        write_dir <- file.path(
          getwd(),
          odm_dictionary$tmp_dictionary_directory,
          "osf",
          current_file_info$osf_location
        )
        dir.create(write_dir,
                   showWarnings = FALSE,
                   recursive = TRUE)
      }
      
      
      if (current_file_info$file_type == "excel") {
        # Use parts as names of sheets to extract
        sheets_to_read <- current_file_info$partID
        
        # Create vector to track recorded sheets
        sheet_was_copied <- rep(FALSE, length(sheets_to_read))
        names(sheet_was_copied) <- sheets_to_read
        
        tmp_workbook <- openxlsx::copyWorkbook(dictionary)
        
        # Loop over sheets removing unnecessary sheets
        existing_sheets <- names(tmp_workbook)
        for (sheet_name in existing_sheets) {
          if (sheet_name %in% names(sheet_was_copied)) {
            sheet_was_copied[sheet_name] <- TRUE
          } else{
            openxlsx::removeWorksheet(tmp_workbook, sheet_name)
          }
        }
        
        # Save the workbook in the appropriate directory
        openxlsx::saveWorkbook(tmp_workbook,
                               file = file.path(
                                 write_dir,
                                 paste0(current_file_info$file_name, ".xlsx")
                               ),
                               overwrite = TRUE)
        
      } else if (current_file_info$file_type == "csv") {
        sheet_name <- current_file_info$partID
        output_sheet <-
          openxlsx::readWorkbook(dictionary, sheet_name)
        if (current_file_info$add_headers != odm_dictionary$dictionary_missing_value) {
          new_headers <- strsplit(current_file_info$add_headers, ";")[[1]]
          output_sheet <-
            rbind(colnames(output_sheet), output_sheet)
          if (length(colnames(output_sheet)) > length(new_headers)) {
            length_to_append <-
              length(colnames(output_sheet)) - length(new_headers)
            new_headers <- c(new_headers, rep("", length_to_append))
          } else if (length(colnames(output_sheet)) < length(new_headers)) {
            length_to_append <-
              length(new_headers) - length(colnames(output_sheet))
            for (col_counter in 1:length_to_append) {
              output_sheet <- cbind(output_sheet, "")
            }
          }
          colnames(output_sheet) <- new_headers
        }
        
        write.csv(output_sheet,
                  file = file.path(write_dir,
                                   paste0(
                                     current_file_info$file_name, ".csv"
                                   )),
                  row.names = FALSE)
      }
    }
  }


#' Remove Files
#' 
#' Helper function to remove files based on output from validate_files_sheet.
#' 
#' @param files_to_remove List output from validate_files_sheet
#' @param dictionary openxlsx environment object storing the dictionary
remove_files <- function(files_to_remove, dictionary) {
  # Loop over files to remove based on fileID
  for (fileID in names(files_to_remove)) {
    current_file_info <- files_to_remove[[fileID]]
    # Skip OSF files
    if (current_file_info$destination == "OSF") {
      next()
    } else if (current_file_info$destination == "github") {
      # Create full file path
      file_extension <- switch (current_file_info$file_type,
                                "excel" = ".xlsx",
                                "csv" = ".csv")
      file_path <- paste0(
        current_file_info$github_location,
        paste0(current_file_info$file_name, file_extension)
      )
      # Check if file exists
      if (file.exists(file_path)) {
        file.remove(file_path)
      }
    }
  }
}