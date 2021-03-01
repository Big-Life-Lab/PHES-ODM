


################################################
# This script will generate sql for db creation based on tables.



library(tidyverse)
library(DBI)
library(RSQLite)
library(glue)
library(magrittr)
library(stringr)

#########################
# default location for the DB creation file
#wbe_CREATE_TABLES_SQL_FN <- file.path("src", "wbe_create_tables.sql")
#wbe_META_DATA <- file.path("metadata.md")
#wbe_META_DATA_TEMLATE <- file.path("metadata_template.md")


WBE_DEFAULT_FN <- db_fn <- file.path("template" ,"WBE.db")

wbe_CONNS <- c()   # Keeps a list of connections to the db

wbe_meta_data_template <- function(lang = "en"){
    paste0("metadata_template_", lang, ".md")
}


####################################
#'
wbe_meta_data <- function(lang = "en"){
    paste0("metadata_", lang, ".md")
}

####################################
#'
wbe_create_tables_sql_fn <- function(lang = "en"){
    paste0("wbe_create_table_", lang, ".sql") %>%
        file.path("src", .)
}


####################################
#'
#'
#'
#'
wbe_create_tables <- function(base_tbl, base_var, variableCat){
    base_tbl = "Sample"
    base_var = "type"


    vals <-
        variableCat %>%
        filter(tableName == base_tbl &
               variableName == base_var) %>%
        pull(variableValue)

}



####################################
#'
#'
#'
#'
wbe_metadata_generation <- function(curr_wd = getwd(), lang = "fr"){
    tbls <- read_csv(file.path(curr_wd, "Tables.csv"))
    variables <- read_csv(file.path(curr_wd, "Variables.csv"))
    variableCat <- read_csv(file.path(curr_wd, "VariableCategory.csv"))


    variableDesc_var_nm <- paste0("variableDesc", "_", lang)
    tableDesc_var_nm<- paste0("tableDesc", "_", lang)
    cats_desc_nm <- paste0("desc", "_", lang)

    md_str <-
        tbls$tableName %>%
        unique() %>%
        lapply(function(curr_tbl){

            tbldesc <-
                tbls %>%
                filter(tableName == curr_tbl) %>%
                pull(!!sym(tableDesc_var_nm))

            cols <-
                variables %>%
                filter(tableName == curr_tbl) %>%
                pull(variableName)




            md_cols <-
                cols %>%
                lapply(function(curr_col){
                    cur_col_details <-
                        variables %>%
                        filter(tableName == curr_tbl &
                                variableName == curr_col)

                    key_str <- if(is.na(cur_col_details$key) | nchar(cur_col_details$key) == 0){""}else{glue(" ({cur_col_details$key})")}

                    type_str <- if(is.na(cur_col_details$variableType) | nchar(cur_col_details$variableType) == 0){""}else{glue(" [{cur_col_details$variableType}]")}

                    vals_str <-
                        if(cur_col_details$variableType == "category"){

                            cats_det <-
                                variableCat %>%
                                filter(tableName == curr_tbl &
                                           variableName == curr_col)


                            cats_det$variableValue %>% unique() %>%
                                lapply(function(curr_val){
                                    curdesc <-
                                        cats_det %>%
                                        filter(variableValue == curr_val) %>%
                                        pull(!!sym(cats_desc_nm))
                                    glue("\t-\t`{curr_val}`: {curdesc}")
                                }) %>% paste0(collapse = "\n")

                        } else{""}

                    glue("-\t**{curr_col}**:{key_str}{type_str} {cur_col_details[[variableDesc_var_nm]]}\n{vals_str}")
                })

            md_cols_all <- md_cols %>% paste0(collapse = "\n\n")
            glue("## {curr_tbl}\n\n{tbldesc}\n\n{md_cols_all}")
        })



    md_str %>% paste0(collapse = "\n")
}

########################################
#'
#'
#'
#'
wbe_metadata_generation_tbl_list <-function(lang = "en", curr_wd = getwd()){
    tbls <- read_csv(file.path(curr_wd, "Tables.csv"))
    tbl_list <-
        tbls$tableName %>%
        unique() %>%
        lapply(function(curr_tbl){
            glue("-\t[{curr_tbl}](#{curr_tbl})")
        }) %>% paste0(collapse = "\n")
    tbl_list
}


########################################
#'
#'
#'
#'
wbe_metadata_write <- function(lang = "fr",
                               full_fn = wbe_meta_data(lang = lang),
                               full_fn_template = wbe_meta_data_template(lang = lang),
                               encoding = "UTF-8" , ...){

    fileConn_tmp<-file(full_fn_template, encoding = encoding)
    tmplt <- readLines(full_fn_template, encoding = encoding)
    close(fileConn_tmp)


    md_str <- wbe_metadata_generation(lang = lang, ...)

    #newstr <- gsub(pattern = "FOR_REPLACE_LIST_OF_TABLES_DETAILS", replacement = md_str, x = tmplt)
    newstr <- str_replace(string = tmplt, pattern = "FOR_REPLACE_LIST_OF_TABLES_DETAILS", replacement = md_str)

    md_tbls <- wbe_metadata_generation_tbl_list()
    # newstr <- gsub(pattern = "FOR_REPLACE_LIST_OF_TABLES", replacement = md_tbls, x = newstr)
    newstr <- str_replace( string = newstr, pattern = "FOR_REPLACE_LIST_OF_TABLES", replacement = md_tbls)


    fileConn<-file(full_fn, encoding = encoding)
    writeLines(text = c(newstr), con = fileConn)
    close(fileConn)
}


###########################################
#' based on the variable type given in the table, this maps to a type in SQL
#'
#'
#'
wbe_sql_dataType_2_sql_type <- function(var_type){
    var_type %>%
        switch("string" = "char",
               "boolean" = "integer",
               "category" = "char",
               "float" = "float",
               "date" = "integer",
               "datetime" = "integer",
               "blob" = "integer",
               "integer" = "integer")
}

############################################
#'
#' generates SQL string that will create a database.
#'
#' @param curr_wd the directory to read in the
#'
#'
#'
wbe_sql_generate_db_creation <- function(curr_wd = getwd(), lang = "en"){

    tbls <- read_csv(file.path(curr_wd, "Tables.csv"))
    variables <- read_csv(file.path(curr_wd, "Variables.csv"))
    variableCat <- read_csv(file.path(curr_wd, "VariableCategory.csv"))

    variableDesc_var_nm <- paste0("variableDesc", "_", lang)
    tableDesc_var_nm<- paste0("tableDesc", "_", lang)
    sql_str <-
        tbls$tableName %>%
            unique() %>%
            lapply(function(curr_tbl){

                contraints_tbl <- c()

                cols <-
                    variables %>%
                    filter(tableName == curr_tbl) %>%
                    pull(variableName)

                sql_str <-
                    cols %>%
                    lapply(function(curr_col){

                        var_type <-
                            variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(variableType) %>%  trimws() %>% tolower()




                        ###########################################
                        # based on the variable type given in the table, this maps to a type in SQL
                        curr_type <- wbe_sql_dataType_2_sql_type(var_type)


                        keyType <- variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(key) %>% trimws() %>% tolower()


                        ###########################################
                        # based on the key information select the pk info
                        pk <-
                            keyType %>%
                            switch("foreign key" = "",
                                   "primary key" = " NOT NULL PRIMARY KEY",
                                   ""
                                   )

                        if((!is.na(keyType))  &keyType == "foreign key"){
                            #print(keyType)
                            ref_tabl <-
                                variables %>%
                                filter(tableName == curr_tbl &
                                           variableName == curr_col) %>%
                                pull(foreignKeyTable)

                            ref_var <-
                                variables %>%
                                filter(tableName == curr_tbl &
                                           variableName == curr_col) %>%
                                pull(foreignKeyVariable)

                            contraints_tbl <<- c(
                                contraints_tbl,
                                glue("\tFOREIGN KEY ([{curr_col}]) REFERENCES {ref_tabl}({ref_var}) DEFERRABLE INITIALLY DEFERRED")
                            )
                        }




                        comment  <-
                            variables %>%
                            filter(tableName == curr_tbl &
                                    variableName == curr_col) %>%
                            pull(!!sym(variableDesc_var_nm))
                        glue("\t[{curr_col}] {curr_type}{pk}")

                    }) %>%
                    unlist()

                #get a list of comments from the description field
                # this is language specific now
                sql_str_comments <-
                    cols %>%
                    lapply(function(curr_col){
                        variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(!!sym(variableDesc_var_nm))
                    }) %>% unlist()

                contraints_tbl_all <- contraints_tbl %>% paste0(collapse = ",\n")


                sql_tbl_create <-
                    1:length(sql_str) %>%
                    lapply(function(i_sql){
                        curr_sql = sql_str[[i_sql]]
                        curr_comment <- sql_str_comments[[i_sql]]

                        ret_val <-
                            if (i_sql < length(sql_str)){
                                glue("{curr_sql}, --{curr_comment}")
                            }else{
                                print(curr_tbl)
                                print(nchar(contraints_tbl_all))
                                print(contraints_tbl_all)
                                print("---------")
                                if (nchar(contraints_tbl_all) == 0){
                                    glue("{curr_sql} --{curr_comment}")
                                }else{
                                    glue("{curr_sql}, --{curr_comment}\n{contraints_tbl_all}")
                                }
                            }
                    })%>% unlist() %>%
                        paste0(collapse = "\n")

                tbldesc <-
                    tbls %>%
                    filter(tableName == curr_tbl) %>%
                    pull(tableDesc_var_nm)
                glue::glue("CREATE TABLE IF NOT EXISTS [{curr_tbl}] (\n/*{tbldesc}*/\n{sql_tbl_create}\n)")
        }) %>% unlist() %>%
        paste0(collapse = ";\n\n")

    sql_str
}

########################################
#'
#' Writes the SQL DB creation to a *.sql file
#'
#'
wbe_sql_write_db_creation <- function(lang = "en",
                                      full_fn = wbe_create_tables_sql_fn(lang),
                                      encoding = "UTF-8" ,
                                      ...){
    sql_str <- wbe_sql_generate_db_creation(lang = lang, ...)

    fileConn<-file(full_fn,  encoding = encoding)
    writeLines(text = c(sql_str), con = fileConn)
    close(fileConn)
}



########################################
#'
#' default file name for the WBE db
#'
#'
wbe_default_fn <- function(){
    # default filename for where the data base goes

    dir <- dirname(path =WBE_DEFAULT_FN)

    if ( ! dir.exists(dir) ){
        dir.create(dir ,recursive = T)
    }

    return(WBE_DEFAULT_FN)
}






########################################
#'
#' create a db from an SQL script
#'
wbe_create_db_from_script <- function(lang = "en",
                                    drv = RSQLite::SQLite(),
                                      full_fn = wbe_create_tables_sql_fn(lang = lang),
                                      db_fn = wbe_default_fn(),
                                      ...
){
    #' creates a wbe_db from a script
    #'
    #' @param drv driver for the db
    #' @param full_fn filename for where the database creation script is
    #' @param db_fn filename for where the database is saved
    #' @param ... passed to dbConnect


    conn <- dbConnect(drv = drv, db_fn, ...)
    wbe_CONNS <<- c(wbe_CONNS, conn)

    sql_str <- readChar(con = full_fn,
                        nchars = file.info(full_fn)$size)

    queries1 = str_replace_all(sql_str,'--.*$'," ")  ### remove any commented lines
    queries2 = paste(queries1, collapse = '\n') ### collapse with new lines
    queries3 = unlist(str_split(queries2,"(?<=;)")) ### separate individual queries


    for (i in 1:length(queries3)) {
        print(i)
        cat(queries3[i])
        print("---------------")
        dbExecute(conn, queries3[i])
    }

    tbls <- paste0(dbListTables(conn), collapse = ", ")
    message(glue("database created at:{db_fn}\nWith tables:{tbls}."))


    dbDisconnect(conn)

}

########################################
#'
#' create a db from an SQL script
#'
wbe_db_setup <- function(lang = "en"){
    wbe_sql_write_db_creation(lang = lang)
    wbe_create_db_from_script(lang = lang)
}
#
# wbe_db_setup("en")
# wbe_metadata_write("en")
# wbe_metadata_write("")
langs <- c("en", "fr")

lapply(langs, wbe_db_setup)
lapply(langs, wbe_metadata_write)




