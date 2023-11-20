sets_sheet_metadata <- list(
  part_ID = list(
    name = "partID"
  )
)

sets_sheet_column_names <- lapply(
    sets_sheet_metadata[names(sets_sheet_metadata)], `[[`, 1)

