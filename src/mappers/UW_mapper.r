


#source("src/wbe_db_func.r")


UW <- list(
    nm = "UW",
    fn = "u_w_wwtp_data_V2.xlsx",
    mapdir = file.path("data", "UW"),

    #full_fn = file.path(mapdir, fn)
    reader = function(full_fn){
        #'
        #'
        #'   Returns a list of dataframes
        #'
        #'
        dfs <- wbe_xlsx_to_dfs(full_fn = full_fn)
        return(dfs)
    },

    validate = function(dfs){
        #' Returns TRUE if this file is really in the format specified by the UW file
        #' Otherwise returns false
        #'


        return(TRUE)
    },

    mapper = function(dfs){
        #' takes a list of dataframes and returns a list of dataframes
        #' the returned list should match exactly a subset of the database tables.
        #'
        dfs<-
            dfs$SampleMeasurementWide %>%
            wbe_sample_measurments_wide_2_long() %>%
            c(dfs)
        dfs$SampleMeasurementWide <- NULL
        return(dfs)
    }
)


