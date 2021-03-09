


#source("src/wbe_db_func.r")


NML <- list(
    nm = "STATSCAN",




    fn = function(dat_dir = file.path("data", "statscan"),
                  fn_pattern = c("NML_results.csv"),
                  decreasing = T,
                  full.names = T){

        cities <- c("Edmonton", "Halifax", "MetroVancouver" , "Montreal", "Toronto")

        fn_pattern_2 <-
            expand_grid(cities, fn_pattern) %>%
            mutate(tmp = paste0(cities, ".*", fn_pattern)) %>%
            pull(tmp)
        lapply(fn_pattern_2, function(p){
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
        csv_files <- full_fn %>% grep(x = ., pattern = ".csv", value = T)
        df <- map(csv_files, read_csv, col_types = cols(.default = "c")) %>% bind_rows()
        dfs <- list(All = df)

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

        df <- dfs$All
        df %>% count(Region)
        df %>% count(Location)

        renames <-read_csv(file.path("src", "mappers", "STATSCAN_Variables.csv"))


        walk2(renames$fromColumn, renames$toColumn,   function(f,t){
            df<<-
                df %>%
                {if (t == "NA") . else rename(., !!sym(t) := !!sym(f))}
        })

              , ...)
        df %>%
            rename_with()

        dfs2 <- wbe_tbls_db_blank()

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


