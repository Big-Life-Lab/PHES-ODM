source(file.path(getwd(), "R", "odm-dictionary-file.R"))
source(file.path(getwd(), "R", "files.R"))
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
    tmp <-
      validate_files_sheet(dictionary_info$dictionary_name,
                           dictionary_info$dictionary_version, dictionary_path)
    return(tmp)
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
  summary_sheet <- readxl::read_excel(file.path(
    getwd(),
    dictionary_path,
    file_names
  ),
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
validate_files_sheet <- function(dictionary_name, version, dictionary_path) {
  files_sheet <- readxl::read_excel(
    file.path(
      getwd(),
      dictionary_path,
      dictionary_name
    ),
    sheet = odm_dictionary$files_sheet_name
  )
  sets_sheet <- readxl::read_excel(
    file.path(
      getwd(),
      dictionary_path,
      dictionary_name
    ),
    sheet = odm_dictionary$sets_sheet_name
  )
  
  # Remove any rows with not supported fileType.
  files_sheet_formatted <-
    files_sheet[files_sheet$fileType %in% files$file_type$categories, unlist(files_sheet_column_names)]
  # insert version
  files_sheet_formatted$name <-
    gsub('\\{version\\}', version, files_sheet_formatted$name)
  csv_to_extract <- c()
  excel_to_extract <- list()
  errors <- ""
  for (row_index in 1:nrow(files_sheet_formatted)) {
    working_row <- files_sheet_formatted[row_index,]
    partID <- working_row[[files$part_ID$name]]
    fileType <- working_row[[files$file_type$name]]
    if (fileType == files$file_type$categories$csv) {
      sets_info <- sets_sheet[sets_sheet$setID == partID, "partID"]
      if (nrow(sets_info) >= 1) {
        # Append error
        errors <-
          paste0(errors,
                 " \n",
                 partID,
                 " is recorded for csv but is found in sets.")
      } else{
        csv_to_extract <- c(csv_to_extract, partID)
      }
    } else if (fileType == files$file_type$categories$excel) {
      sets_info <- sets_sheet[sets_sheet$setID == partID, "partID"]
      if (nrow(sets_info) >= 1) {
        excel_to_extract[[partID]] <- sets_info
      } else{
        # Append error
        errors <-
          paste0(errors,
                 " \n",
                 partID,
                 " is recorded for excel but is not found in sets.")
      }
    }
  }
  # Will move with development 
  # Will become stop once function development is finished
  if (errors != "") {
    warning(errors)
  }
  return(list(csv = csv_to_extract, excel = excel_to_extract))
}