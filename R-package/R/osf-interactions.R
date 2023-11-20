# Load utility functions
source(file.path(getwd(), "R", "create-release-files.R"))
source('R/logging.R')

#' Update OSF files
#'
#' This function updates files on the Open Science Framework (OSF) using the provided OSF link and token.
#' It downloads the dictionary file, validates the dictionary version and files sheet, and stages the files to be uploaded to OSF.
#'
#' @param osf_repo_link The link to the OSF repo.
#' @param osf_token The OSF token used to authenticate the user.
#' @param dictionary_path The path to the dictionary file. If NULL, the file will be downloaded from OSF.
#' @param past_dictionary_path The path to the past dictionary file. If NULL, the file will be downloaded from OSF.
#'
update_osf <- function(osf_repo_link,
                       osf_token,
                       dictionary_path = NULL,
                       past_dictionary_path = NULL){
  setup_logging()

  # Download file using passed credentials
  dictionary_path <- download_dictionary(dictionary_path, osf_token, osf_repo_link, odm_dictionary$tmp_dictionary_directory, origin_directory = "dev-release")
  
  # Validate dictionary version
  dictionary_info <- get_dictionary(dictionary_path)
  
  dictionary <- dictionary_info[[1]]
  dictionary_version <- dictionary_info[[2]]
  
  # Validate files sheet
  validation_return <-
    validate_and_parse_files_sheet(dictionary,
                                   dictionary_version)
  files_to_make <- validation_return[[1]]
  fatal_errors_flag <- validation_return[[2]]
  
  # Will move with development
  # Will become stop once function development is finished
  if (fatal_errors_flag) {
    warning(
      "Errors were detected further building cannot continue please check the log for additional info"
    )
  }
  
  stage_osf_files(files_to_make,
               dictionary)

  # Download previous release dictionary
  past_dictionary_path <- download_dictionary(past_dictionary_path, osf_token, osf_repo_link, odm_dictionary$tmp_dictionary_directory_past_release, origin_directory = "Current Release")
  
  # Validate dictionary version
  past_dictionary_info <- get_dictionary(past_dictionary_path)
  
  past_dictionary <- past_dictionary_info[[1]]
  past_dictionary_version <- past_dictionary_info[[2]]
  
  archive_previous_release(osf_token, osf_repo_link, past_dictionary_version)
  
}

#' Stage OSF files
#'
#' This function stages the files to be uploaded to OSF. It loops over the files to extract based on fileID, creates a write directory based on destination and saving location, and saves the files in the appropriate directory.
#'
#' @param files_to_extract A list of files to extract.
#' @param dictionary The dictionary file.
#'
stage_osf_files <- function(files_to_extract,
                            dictionary) {
  reused_storage_prefix <- file.path(getwd(),"osf-stage")
  # Loop over files to extract based on fileID
  for (fileID in names(files_to_extract)) {
    current_file_info <- files_to_extract[[fileID]]
    
    # Create a write directory based on destination and saving location
    write_dir <- ""
    if (current_file_info$destination == "osf") {
      write_dir <- file.path(reused_storage_prefix,
                             current_file_info$osf_location)
      dir.create(write_dir,
                 showWarnings = FALSE,
                 recursive = TRUE)
      
    }
    
    
    if(write_dir != ""){
      if (current_file_info$file_type == "excel") {
        # Use parts as names of sheets to extract
        sheets_to_copy <- current_file_info$sheet_names
        tmp_workbook <- openxlsx::copyWorkbook(dictionary)
        # Loop over sheets removing unnecessary sheets
        existing_sheets <- names(tmp_workbook)
        for (sheet_name in existing_sheets) {
          if (!(sheet_name %in% sheets_to_copy)) {
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
        sheet_name <- current_file_info$sheet_names
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
}


#' Archive previous release
#' 
#' This function archives the previous release on OSF. It creates a new archive folder, moves the previous release to the archive folder.
#' 
#' @param osf_token The OSF token used to authenticate the user.
#' @param OSF_LINK The OSF link to the main repo.
archive_previous_release <- function(osf_token, OSF_LINK, past_dictionary_version){
  # Authenticate with OSF, in case a local file is used
  osfr::osf_auth(osf_token)
  # Retrieve information from OSF
  osf_info <- osfr::osf_retrieve_node(OSF_LINK)
  # Get info on current release
  root_info <- osfr::osf_ls_files(osf_info)
  current_release_info <- root_info[root_info$name == "Current Release", ]
  # Get info on archieve folder
  archive_info <- root_info[root_info$name == "Archived releases", ]
  # Make new archive dir
  new_archive <- osfr::osf_mkdir(archive_info, paste0("release_", past_dictionary_version))
  
  # Move contents of current_release_info into archive
  current_release_info_content <- osfr::osf_ls_files(current_release_info)
  for (release_index in seq(nrow(current_release_info_content))) {
    osfr::osf_mv(current_release_info_content[release_index, ], new_archive)
  }
  
  # Upload staged files
  osfr::osf_upload(current_release_info, "osf-stage/.", recurse = TRUE, conflicts = "overwrite")
  # Upload dev dictionary
  osfr::osf_upload(current_release_info, paste0(odm_dictionary$tmp_dictionary_directory, "/."), conflicts = "overwrite")
}
