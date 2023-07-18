#source(file.path(getwd(), "R", "odm-dictionary-file.R"))
#source(file.path(getwd(), "R", "files.R"))
#' Create release files
#'
#' Creates release files given the user OSF link and auth token.
#'
#' @param OSF_LINK link to the dictionary stored on OSF used for updating.
#' @param OSF_TOKEN OSF auth token used for modifying OSF directories
#' @param dictionary_path optional string containing path to the dictionary directory. When provided no dictionary is downloaded.
#'
#' @export
create_release_files <-
  function(OSF_LINK, OSF_TOKEN, dictionary_path = NULL) {
    # Download file using passed credentials
    if (is.null(dictionary_path)) {
      dictionary_path <- odm_dictionary$tmp_dictionary_directory
      osfr::osf_auth(OSF_TOKEN)
      osfr::osf_retrieve_file(OSF_LINK) %>%
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
    warning("Dictionary file name version does not reflect version in summary sheet")
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
    errors <- ""
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
                errors <- paste0(
                  errors,
                  " \n",
                  single_part,
                  " does not have a matching sheet but is part of ",
                  set_name,
                  " set, which was selected to be exported."
                )
                # Remove missing part
                set_parts <-
                  set_parts[names(set_parts) != single_part]
              }
              
            } else{
              errors <- paste0(
                errors,
                " \n",
                single_part,
                " is missing from the parts sheet but is present in the ",
                set_name,
                " set."
              )
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
        }else{
          if (partID %in% parts_sheet[["partID"]]) {
            if(partID %in% names(dictionary)){
              validated_file <- TRUE  
            }else{
              errors <- paste0(
                errors,
                " \n",
                single_part,
                " does not have a matching sheet.")
            }
            
          } else {
            errors <-
              paste0(errors,
                     " \n",
                     partID,
                     " is not found in parts sheet.")
          }
        }
      } else if (file_type == files$file_type$categories$csv) {
        if (nrow(set_info) >= 1) {
          # Append error
          errors <-
            paste0(errors,
                   " \n",
                   partID,
                   " is recorded for csv but is found in sets.")
        } else{
          if (partID %in% parts_sheet[["partID"]]) {
            if(partID %in% names(dictionary)){
              validated_file <- TRUE  
            }else{
              errors <- paste0(
                errors,
                " \n",
                single_part,
                " does not have a matching sheet.")
            }
            
          } else {
            errors <-
              paste0(errors,
                     " \n",
                     partID,
                     " is not found in parts sheet.")
          }
          
        }
      } else{
        errors <-
          paste0(errors,
                 " \n",
                 partID,
                 " has an unrecognized fileType of ",
                 file_type)
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
      warning(errors)
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
                   showWarnings = FALSE)
        
      } else if (current_file_info$destination == "osf") {
        write_dir <- file.path(
          getwd(),
          odm_dictionary$tmp_dictionary_directory,
          "osf",
          current_file_info$osf_location
        )
        dir.create(write_dir,
                   showWarnings = FALSE)
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
          output_sheet <-
            rbind(colnames(output_sheet), output_sheet)
          colnames(output_sheet) <-
            strsplit(current_file_info$add_headers, ";")[[1]]
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