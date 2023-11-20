parts_sheet_metadata <- list(
  part_ID = list(
    name = "partID"
  )
)

parts_sheet_column_names <- lapply(
    parts_sheet_metadata[names(parts_sheet_metadata)], `[[`, 1)

