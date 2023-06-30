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
    
    # Validate files sheet
    files_to_make <-
      validate_files_sheet(
        dictionary_info$dictionary_name,
        dictionary_info$dictionary_version,
        dictionary_path
      )
    
    create_files(files_to_make,
                 dictionary_info$dictionary_name,
                 dictionary_path)
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
  
  # Acquire version number from summary sheet
  summary_sheet <- readxl::read_excel(file.path(getwd(),
                                                dictionary_path,
                                                file_names),
                                      sheet = odm_dictionary$summary_sheet_name)
  # Read the first column
  summary_versions <- summary_sheet[[1]]
  # Strip off any NA rows
  summary_versions <- summary_versions[!is.na(summary_versions)]
  # Select the last version
  summary_version <- summary_versions[[length(summary_versions)]]
  matching_versions <- FALSE
  # Compare if the versions match
  if (summary_version == dictionary_file_name_version_number) {
    matching_versions <- TRUE
  }
  
  return(
    list(
      dictionary_name = file_names,
      dictionary_version = summary_version,
      matching_versions = matching_versions
    )
  )
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
  function(dictionary_name,
           version,
           dictionary_path) {
    files_sheet <- readxl::read_excel(file.path(getwd(),
                                                dictionary_path,
                                                dictionary_name),
                                      sheet = odm_dictionary$files_sheet_name)
    sets_sheet <- readxl::read_excel(file.path(getwd(),
                                               dictionary_path,
                                               dictionary_name),
                                     sheet = odm_dictionary$sets_sheet_name)
    
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
    for (row_index in 1:nrow(files_sheet_formatted)) {
      working_row <- files_sheet_formatted[row_index, ]
      
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
      if (file_type == files$file_type$categories$csv) {
        sets_info <- sets_sheet[sets_sheet$setID == partID, "partID"]
        if (nrow(sets_info) >= 1) {
          # Append error
          errors <-
            paste0(errors,
                   " \n",
                   partID,
                   " is recorded for csv but is found in sets.")
        } else{
          validated_file <- TRUE
        }
      } else if (file_type == files$file_type$categories$excel) {
        sets_info <- sets_sheet[sets_sheet$setID == partID, "partID"]
        if (nrow(sets_info) >= 1) {
          # Replace partID with the partIDs belonging to the set
          partID <- sets_info[["partID"]]
          partID <- strsplit(partID, ",")[[1]]
          validated_file <- TRUE
        } else{
          # Append error
          errors <-
            paste0(errors,
                   " \n",
                   partID,
                   " is recorded for excel but is not found in sets.")
        }
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
#' @param dictionary_name String containing the dictionary name
#' @param dictionary_path String containing the path to the dictionary
create_files <-
  function(files_to_extract,
           dictionary_name,
           dictionary_path) {
    # Loop over files to extract based on fileID
    for (fileID in names(files_to_extract)) {
      current_file_info <- files_to_extract[[fileID]]
      
      # Use parts as names of sheets to extract
      sheets_to_read <- current_file_info$partID
      read_sheets <- list()
      print(sheets_to_read)
      print(length(sheets_to_read))
      # In case of multiple sheets loop over the parts and read into list
      if (length(sheets_to_read) > 1) {
        for (sheet_name in sheets_to_read) {
          read_sheets[[sheet_name]] <- readxl::read_excel(file.path(getwd(),
                                                                    dictionary_path,
                                                                    dictionary_name),
                                                          sheet = sheet_name)
          if (current_file_info$add_headers != odm_dictionary$dictionary_missing_value) {
            # If custom headers are present more current headers down into first row and replace header
            read_sheets[[sheet_name]] <- rbind(colnames(read_sheets[[sheet_name]]), read_sheets[[sheet_name]])
            colnames(read_sheets[[sheet_name]]) <-
              strsplit(current_file_info$add_headers, ";")[[1]]
          }
        }
      } else{
        read_sheets[[sheets_to_read]] <-
          files_sheet <- readxl::read_excel(file.path(getwd(),
                                                      dictionary_path,
                                                      dictionary_name),
                                            sheet = sheets_to_read)
        if (current_file_info$add_headers != odm_dictionary$dictionary_missing_value) {
          read_sheets[[sheets_to_read]] <- rbind(colnames(read_sheets[[sheets_to_read]]), read_sheets[[sheets_to_read]])
          colnames(read_sheets[[sheets_to_read]]) <-
            strsplit(current_file_info$add_headers, ";")[[1]]
        }
      }
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
                   showWarnings = TRUE)
        
      } else if (current_file_info$destination == "osf") {
        write_dir <- file.path(
          getwd(),
          odm_dictionary$tmp_dictionary_directory,
          "osf",
          current_file_info$osf_location
        )
        dir.create(write_dir,
                   showWarnings = TRUE)
      }
      if (current_file_info$file_type == "excel") {
        for (sheet_name in names(read_sheets)) {
          xlsx::write.xlsx(
            read_sheets[[sheet_name]],
            file = file.path(
              write_dir,
              paste0(current_file_info$file_name, ".xlsx")
            ),
            sheetName = sheet_name,
            row.names = FALSE,
            append = TRUE
          )
        }
      }else if(current_file_info$file_type == "csv"){
        write.csv(read_sheets[[1]], file = file.path(
          write_dir,
          paste0(current_file_info$file_name, ".csv")
        ), row.names = FALSE)
      }
    }
    
  }