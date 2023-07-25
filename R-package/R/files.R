files <- list(
  file_name = list(
    name = "name"
  ),
  file_id = list(
    name = "fileID"
  ),
  file_type = list(
    name = "fileType",
    categories = list(
      excel = "excel",
      csv = "csv"
    )
  ),
  part_ID = list(
    name = "partID"
  ),
  add_headers = list(
    name = "addHeaders"
  ),
  destinations = list(
    name = "destinations",
    categories = list(
      osf = "osf",
      github = "github"
    )
  ),
  osf_locations = list(
    name = "osfLocation"
  ),
  github_location = list(
    name = "githubLocation"
  )
)

files_sheet_column_names <- lapply(files[names(files)], `[[`, 1)