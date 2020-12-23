

source("src/wbe_db_func.r")
wbe_delete_whole_DB()

dfs <- wbe_xlsx_to_dfs(full_fn = file.path("data", "NML", "TEMPLATE_v0.1.2.xlsx"))


wbe_append_lookups(df = dfs$Lookups)
dfs$Lookups <- NULL
wbe_append_from_dfs(dfs = dfs)


to_add <- wbe_sample_measurments_wide_2_long(df = dfs$SmplMsr)

wbe_append_from_dfs(dfs = to_add)


to_add$Measurement %>% count(measurementID,sort = T)
to_add$Sample %>% count(sampleID,sort = T)

wbe_tbl("sample")


wbe_tbl("Measurement") %>% count(measureCat,  measureUnit)

wbe_create_db_from_script(db_fn = db_fn )
