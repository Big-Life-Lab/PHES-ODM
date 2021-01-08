







mappers <- wbe_read_mappers()






wbe_read_data <- function(..., nm, .mappers = "mappers"){
    #' master function that will call a given mappers reader function
    get(.mappers)[[nm]]$reader(...)
}



wbe_map_data <- function(..., nm, .mappers = "mappers"){
    #' master function that will call a given mappers mapper function
    get(.mappers)[[nm]]$mapper(...)
}

mappers <- wbe_read_mappers(){
}




mappers$UW$mapdir


# read all config files
mappers <-
    file.path("data") %>%
    list.files(pattern = "mapper.r", full.names = TRUE, recursive = TRUE) %>%
        map(function(x) {
            e <- parse(x)[[1]]
            eval(e)
        }) %>%
        set_names(map(., ~.$name))



dfs <- wbe_xlsx_to_dfs(full_fn = file.path("data", "NML", "NML_TEMPLATE_v0.1.2.xlsx"))
dfs2 <- wbe_xlsx_to_dfs(full_fn = file.path("data", "Ottawa", "Ottawa_TEMPLATE_v0.1.2.xlsx"))
dfs3 <- wbe_xlsx_to_dfs(full_fn = file.path("data", "UW", "u_w_wwtp_data_V2.xlsx"))




dfs2 <- wbe_files_to_dfs(dir = file.path("data", "db"))


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
