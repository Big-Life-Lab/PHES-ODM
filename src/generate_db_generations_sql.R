
# This script will generate sql for db creation based on tables.
library(tidyverse)


############################################
#'
#' generates SQL string that will create a database.
#'
#' @param curr_wd the directory to read in the
#'
#'
#'
wbe_generate_SQL_for_db_creation <- function(curr_wd = getwd()){

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
                                   "date" = "",
                                   "datetime" = "",
                                   "blob" = "",
                                   "integer" = "integer")

                        pk <-
                            variables %>%
                            filter(tableName == curr_tbl &
                                       variableName == curr_col) %>%
                            pull(key) %>% trimws() %>% tolower() %>%
                            switch("foreign key" = "",
                                   "primary key" = "NOT NULL PRIMARY KEY",
                                   ""
                                   )
                        glue::glue("\t[{curr_col}] {curr_type} {pk}")

                    }) %>%
                    unlist() %>%
                    paste0(collapse = ",\n")
                    glue::glue("CREATE TABLE  IF NOT EXISTS [Polygon] (\n {sql_str} \n)")
        }) %>% unlist() %>%
        paste0(collapse = ";\n\n")

    sql_str
}
