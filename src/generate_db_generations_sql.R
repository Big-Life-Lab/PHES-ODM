
# This script will generate sql for db creation based on tables.
library(tidyverse)
library(DBI)
library(RSQLite)
library(glue)

#########################
# default location for the DB creation file
wbe_CREATE_TABLES_SQL_FN <- file.path("src", "wbe_create_tables.sql")


WBE_DEFAULT_FN <- db_fn <- file.path("data", "db" ,"WBE.db")

wbe_CONNS <- c()   # Keeps a list of connections to the db


############################################
#'
#' generates SQL string that will create a database.
#'
#' @param curr_wd the directory to read in the
#'
#'
#'
wbe_sql_generate_db_creation <- function(curr_wd = getwd()){

    tbls <- read_csv(file.path(curr_wd, "Table.csv"))
    variables <- read_csv(file.path(curr_wd, "Variable.csv"))


    sql_str <-
        tbls$tableName %>%
            unique() %>%
            lapply(function(curr_tbl){

                cols <-
                    variables %>%
                    filter(tableName == curr_tbl) %>%
                    pull(variableName)

                sql_str <-
                    cols %>%
                    lapply(function(curr_col){
                        curr_type   <- variables %>%
                                filter(tableName == curr_tbl &
                                        variableName == curr_col) %>%
                                       pull(variableType) %>%  trimws() %>% tolower() %>%
                            switch("string" = "char",
                                   "boolean" = "integer",
                                   "category" = "char",
                                   "float" = "float",
                                   "date" = "integer",
                                   "datetime" = "integer",
                                   "blob" = "integer",
                                   "integer" = "integer")

                        pk <-
                            variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(key) %>% trimws() %>% tolower() %>%
                            switch("foreign key" = "",
                                   "primary key" = " NOT NULL PRIMARY KEY",
                                   ""
                                   )


                        comment  <-
                            variables %>%
                            filter(tableName == curr_tbl &
                                    variableName == curr_col) %>%
                            pull(variableDesc)
                        glue("\t[{curr_col}] {curr_type}{pk}")

                    }) %>%
                    unlist()

                sql_str_comments <-
                    cols %>%
                    lapply(function(curr_col){
                        variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(variableDesc)
                    }) %>% unlist()

                sql_tbl_create <-
                    1:length(sql_str) %>%
                    lapply(function(i_sql){
                        curr_sql = sql_str[[i_sql]]
                        curr_comment <- sql_str_comments[[i_sql]]

                        ret_val <-
                            if (i_sql < length(sql_str)){
                                glue("{curr_sql}, --{curr_comment}")
                            }else{
                                glue("{curr_sql} --{curr_comment}")
                            }
                    })%>% unlist() %>%
                        paste0(collapse = "\n")

                tbldesc <-
                    tbls %>%
                    filter(tableName == curr_tbl) %>%
                    pull(tableDesc)

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
wbe_sql_write_db_creation <- function(full_fn = wbe_CREATE_TABLES_SQL_FN, ...){
    sql_str <- wbe_sql_generate_db_creation(...)

    fileConn<-file(full_fn)
    writeLines(c(sql_str), fileConn)
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
wbe_create_db_from_script <- function(drv = RSQLite::SQLite(),
                                      full_fn = wbe_CREATE_TABLES_SQL_FN,
                                      db_fn = wbe_default_fn(),
                                      ...
){
    #' creates a wbe_db from a script
    #'
    #' @param drv driver for the db
    #' @param full_fn filename for where the database creation script is
    #' @param db_fn filename for where the database is saved
    #' @param ... passed to dbConnect


    `conn` <- dbConnect(drv = drv, db_fn, ...)
    wbe_CONNS <<- c(wbe_CONNS, conn)

    sql_str <- readChar(con = full_fn,
                        nchars = file.info(full_fn)$size)

    queries1 = str_replace_all(sql_str,'--.*$'," ")  ### remove any commented lines
    queries2 = paste(queries1, collapse = '\n') ### collapse with new lines
    queries3 = unlist(str_split(queries2,"(?<=;)")) ### separate individual queries


    for (i in 1:length(queries3)) {
        dbExecute(conn, queries3[i])
    }

    tbls <- paste0(dbListTables(conn), collapse = ", ")
    message(glue("database created at:{db_fn}\nWith tables:{tbls}."))
}

########################################
#'
#' create a db from an SQL script
#'
wbe_db_setup <- function(){
    wbe_sql_write_db_creation()
    wbe_create_db_from_script()
}

wbe_db_setup()





