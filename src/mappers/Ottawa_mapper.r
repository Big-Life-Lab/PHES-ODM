


#source("src/wbe_db_func.r")


Ottawa <- list(
    nm = "Ottawa",
    fn = "Ottawa_TEMPLATE_v0.1.2.xlsx",
    mapdir = file.path("data", "Ottawa"),

    #full_fn = file.path(mapdir, fn)
    reader = function(full_fn){
        #'
        #'
        #'   Returns a list of dataframes
        #'
        #'
        wbe_xlsx_to_dfs(full_fn = full_fn)
    },

    validate = function(dfs){
        #'
        #' Returns TRUE if this file is really in the format specified by the UW file
        #' Otherwise returns false
        #'


        return(TRUE)
    },

    mapper = function(dfs){
        #'
        #' takes a list of dataframes and returns a list of dataframes
        #' the returned list should match exactly a subset of the database tables.
        #'
        dfs<-
            dfs$SmplMsr %>%
            wbe_sample_measurments_wide_2_long() %>%
            c(dfs)
        dfs$SmplMsr <- NULL
        return(dfs)
    }
)


