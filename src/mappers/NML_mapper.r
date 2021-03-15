


#source("src/wbe_db_func.r")


NML <- list(
    nm = "NML",




    fn = function(dat_dir = file.path("data", "NML"),
                  fn_pattern = c("national_export.*xlsx","2021-02-25_WW_mastersheet_V3.xlsx"),
                  decreasing = T,
                  full.names = T){

        lapply(fn_pattern, function(p){
            list.files(path = dat_dir ,
                       pattern = p,
                       full.names = full.names) %>%
                sort(decreasing = decreasing) %>%
                extract2(1)


        }) %>% unlist()



    },

    #full_fn = mapper$fn()
    reader = function(full_fn){
        #'
        #'
        #'   Returns a list of dataframes
        #'
        #'
        lapply(full_fn, wbe_xlsx_to_dfs) %>% unlist(recursive=FALSE)
    },

    validate = function(dfs){
        #'
        #' Returns TRUE if this file is really in the format specified by the NML file
        #' Otherwise returns false
        #'


        return(TRUE)
    },

    mapper = function(dfs){
        #'
        #' takes a list of dataframes and returns a list of dataframes
        #' the returned list should match exactly a subset of the database tables.
        #'


        #wbe_tbl_col_nms("AssayMethod")
        #wbe_tbl_list()

        names(dfs)
        #rename "Measurement"
        dfs[["WWMeasure"]] <- dfs[["Measurement"]]
        dfs[["Measurement"]] <- NULL

        dfs$AssayMethod <-
            dfs$AssayMethod %>%
            rename(name := assayID) %>%
            rename(version := assayVersion) %>%
            rename(date := assayDate)

        # reporter_id = "NML"
        #
        #
        #
        # wbe_ensure_primary_key(df = ,tbl_nm = ,reporter_id = , reporter_id = )
        #
        # wbe_primary_key("AssayMethod")
        # dfs$AssayMethod %>%
        #     rename(name := assayID) %>%
        #     mutate(., assayMethodID = wbe_generate_key(., reporter_id = "NML"))

        return(dfs)
    }
)


