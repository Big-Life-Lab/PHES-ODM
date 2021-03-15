

##################################
# conversion script from long table to wide
#
# data model v0.1.1
#
library(tidyverse)
library(readxl)
library(DBI)
library(RSQLite)
library(stringr)
library(glue)
library(janitor)
library(docstring)
library(hash)
library(dbplyr)
library(digest)
library(magrittr)
library(snakecase)
library(docstring)
library(anytime)
library(tools)
library(assertthat)
library(stringi)


wbe_CONNS <- c()   # Keeps a list of connections to the db

#########################
# default location for the DB creation file
wbe_CREATE_TABLES_SQL_FN <- file.path("src", "wbe_create_table_en.sql")





##############################
# call digest_vect for a vectorized version of digest
digest_vect <- Vectorize(digest)




WBE_DEFAULT_FN <- db_fn <- file.path("data", "db" ,"WBE.db")
wbe_default_fn <- function(){
  # default filename for where the data base goes

  dir <- dirname(path =WBE_DEFAULT_FN)

  if ( ! dir.exists(dir) ){
    dir.create(dir ,recursive = T)
  }

  return(WBE_DEFAULT_FN)
}

####################################
#' returns a connection to a WBE database
#' creates and empty db if needed
#'
#'
wbe_conn <- function(drv = RSQLite::SQLite(),
                     db_fn = wbe_default_fn(),
                     ...){

  if(! file.exists(db_fn)){
    wbe_create_db_from_script(db_fn = db_fn )
  }

  conn <- dbConnect(drv = drv, db_fn, ...)
  wbe_CONNS <<- c(wbe_CONNS, conn)
  return(conn)
}




wbe_disconnect_all <- function(){
  #'
  #' removes all connections to the db that we know of
  #'

  n_con <- length(wbe_CONNS)

  lapply(wbe_CONNS, function(x){dbDisconnect(x)})
  wbe_CONNS <<- list()

  message(glue("disconnected  {n_con} connections"))
}




wbe_delete_whole_db <- function(db_fn = wbe_default_fn()){
  #'
  #' removes all connections, then deletes the file
  #'
  #'  @param db_fn filename where the database is
  #'
  wbe_disconnect_all()
  file.remove(db_fn)
  message(glue("deleted {db_fn}"))
}
#wbe_delete_whole_db


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


  conn <- dbConnect(drv = drv, db_fn, ...)
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


wbe_excel_datetime_conv <-function(x, sec_in_day = 86400, origin = "1899-12-30", tz = "GMT"){
  as.POSIXct(as.double(x)* sec_in_day, origin = origin, tz = tz)
}

wbe_excel_date_conv <-function(x, origin = "1899-12-30"){
  as.Date(as.integer(x), origin = origin)
}

#dir = file.path("data", "db")
wbe_file_to_df <- function(full_fn,
                           read_func = read_csv,
                           datetime_conv_func = wbe_excel_datetime_conv,
                           date_conv_func = wbe_excel_date_conv,
                           date_time_pattern = "dateTime",
                           date_pattern = "^(?!.*dateTime).*Date.*$",#"analysisDate",
                             ...){
  #' reads in a list for
  #' to will also change the case
  #'
  #' @param dir directory to read in
  #' @param fn_pattern file names to read in
  #' @param read_func function that reads a single file, must take a file name
  #' @param datetime_conv_func converts something to a datetime
  #' @param date_conv_func converts something to a date
  #' @param col_name_cases converts something to a date
  #' @param table_name_cases casing of table names
  #' @param date_time_pattern matches all columns that need conversion to datetime
  #' @param date_pattern matches all columns that need conversion to date
  #' @param ... passed to read_func


  #GET THE df FROM the list of dfs
  df <-
    read_func(full_fn, ...) %>%
    mutate_at(vars(matches(date_time_pattern,  ignore.case = T, perl = T)),datetime_conv_func) %>%
    mutate_at(vars(matches(date_pattern,  ignore.case = T, perl = T)), date_conv_func) %>%
    as_tibble()
}


#dir = file.path("data", "db")
wbe_files_to_dfs <- function(dir,
                             fn_pattern = "*.csv",
                             table_name_cases = "upper_camel",
                            ...){

  #' reads in a list for
  #' to will also change the case
  #'
  #' @param dir directory to read in
  #' @param fn_pattern file names to read in
  #' @param table_name_cases casing of table names
  #' ... passed to wbe_file_to_df

  fns <- list.files(path = dir, pattern = fn_pattern, ignore.case = TRUE, full.names = TRUE)

  to_add <- fns#intersect(tbls, sheets)

  dfs <- list()
  for (adding in to_add) {

    #GET THE df FROM the list of dfs
    df <-
      wbe_file_to_df(full_fn = adding,
                     ... = ...
                     )

    tbl_nm <-
      adding %>%
      file_path_sans_ext() %>%
      basename() %>%
      make_clean_names(case = table_name_cases)

    dfs[[tbl_nm]] <- df
  }

  return(dfs)


}





wbe_xlsx_to_dfs <- function(full_fn,
                            col_name_cases = "lower_camel",
                            table_name_cases = "upper_camel",
                            date_time_pattern = "dateTime",
                            ...
){
  #' reads in an excel file into multiple dataframes
  #' ot will also change the case
  #'
  #' @param full_fn excel file name to read in
  #' @param col_name_cases case to use for the column names
  #' @param table_name_cases case to use for the tables ie the sheet names
  #' @param ... passed to wbe_file_to_df


  to_add <- file.path(full_fn) %>% readxl::excel_sheets()

  dfs <- list()
  for (adding in to_add) {

    #GET THE df FROM the list of dfs
    df <-
      wbe_file_to_df(full_fn = full_fn, read_func = read_xlsx, sheet = adding, col_types = "text",
                     ... = ...
                  )
    tbl_nm <-
      adding %>%
      make_clean_names(case = table_name_cases)

    dfs[[tbl_nm]] <- df
  }

  return(dfs)

}





wbe_append_lookups <- function(df,
                               tbl_nm = "Lookups",
                               conn = wbe_conn(),
                               table_name_cases = "upper_camel",
                               col_name_cases = "lower_camel",
                               value_name_cases = "snake",
                               desc_name_case = "sentence",
                               ...){
  #' fills a data base from from a single table
  #'
  #' @param df dataframe that becomes a table in the db
  #' @param tbl_nm name of the table default is "Lookups"
  #' @param conn connection to the database
  #' @param table_name_cases
  #' @param col_name_cases
  #' @param value_name_cases
  #' @param desc_name_case
  #' @param ... passed to wbe_append_from_df


  # This is what actually goes into the data base
  df2 <- tibble(tmp_index = 1:nrow(df))



  #get formats for the table, so we can match type information
  tbl_format <- wbe_tbl_frmt(tbl_nm = tbl_nm, conn = conn)
  for (col_nm in colnames(tbl_format)){


    #pick the casing for this columns values
    curr_case <- ""
    if( col_nm == "tableName"){curr_case <- table_name_cases}
    else if(col_nm == "columnName"){curr_case <- col_name_cases}
    else if(col_nm == "value"){curr_case <- value_name_cases}
    else{curr_case <- desc_name_case}


    #correct casing in the DB
    df2[[col_nm]] <- df[[col_nm]] %>% snakecase::to_any_case(case = curr_case)

  }

  #remove the index
  df2$tmp_index <- NULL


  #append the df to the table
  wbe_append_from_df(df = df2,
                     tbl_nm = tbl_nm,
                     conn = conn,
                     col_name_cases = col_name_cases,
                     value_name_cases = "",
                     ...)

}




#df <- to_add$Measurement
#tbl_nm <- "Measurement"
#wbe_append_from_df(df = dfs$Lookups, tbl_nm = "Lookups")
wbe_append_from_df <- function(df,
                               tbl_nm,
                               conn = wbe_conn(),
                               col_name_cases = "lower_camel",
                               value_name_cases = "",
                               append = T,
                               ...
){
  #' fills a data base from from a single table
  #'
  #' @param df dataframe that becomes a table in the db
  #' @param tbl_nm name of the table
  #' @param conn connection to the database
  #' @param col_name_cases
  #' @param value_name_cases
  #' @param ... passed to dbWriteTable

  if(nrow(df) == 0){
    message(glue("wrote {nrow(df)} rows to {tbl_nm}"))
    return(TRUE)
  }

  #we do not want to clean names yet
  #df <- df %>% clean_names(case = col_name_cases)

  # Get the columns and the fromat from the DB
  tbl_format <- wbe_tbl_frmt(tbl_nm = tbl_nm, conn = conn)
    #tbl(conn, tbl_nm) %>% head(1) %>% collect() %>% slice(0)


  #init the tibble to append
  df2 <- tibble(tmp_uuid = 1:nrow(df))

  # Make sure we have compatible types and format from our DF
  for (col_nm in colnames(tbl_format)){
    #col_nm <- colnames(tbl_format)[[1]]

    #get the class of the column in the table
    cls <- class(tbl_format[[col_nm]])
    cls <- cls[[1]]

    print(cls)

    #Find matching column in DF list
    df_colNm <- wbe_find_df_col(df = df , col_nm = col_nm)



    if ( length(df_colNm) == 1 && cls != "blob" ){
      #make sure we have the correct type of column to add
      print(cls)
      print(df_colNm)


      if ("Date" %in% class(df[[df_colNm]])){

        df2[[col_nm]] <- as.POSIXct(df[[df_colNm]], origin="1970-01-01")

      }else{
        df2[[col_nm]] <- as(df[[df_colNm]], cls)
      }

    }else if (cls == "blob"){
      message(glue("In {tbl_nm}, I don't know how to deal with 'blob' types yet, skipping and moving on."))
    }else{
      message(glue("In {tbl_nm}, there are {length(df_colNm)} matches to the column {col_nm}, can not use put anything in this column"))
    }

  }

  #delete the tmp ID
  df2$tmp_uuid <- NULL

  #correct casing in the DB
  if (value_name_cases != ""){
    df2 <- df2 %>% mutate_if(is.character, to_any_case, case = value_name_cases)
  }

  #wites the table
  worked <- dbWriteTable(conn = conn,
                         name = tbl_nm,
                         value = df2,
                         append = append,
                         ...)

  message(glue("wrote {nrow(df2)} rows and {ncol(df2)} column to {tbl_nm}, status {worked}"))
  return(worked)
}











wbe_append_from_dfs <- function(dfs,
                                reporter_id = stringi::stri_rand_strings(n = 1, length = 25),
                                conn = wbe_conn(),
                                table_name_cases = "upper_camel",
                                col_name_cases = "lower_camel",
                                value_name_cases = "",
                                append = T,

                                ...
){
  #' fills a data base from from a list of data frames
  #'
  #' @param dfs data frame list that becomes a tables in the db
  #' @param conn connection to the database
  #' @param table_name_cases
  #' @param col_name_cases
  #' @param value_name_cases
  #' @param append
  #' @param ... passed to wbe_append_from_df


  #reporter_id = "NML"

  # get tables in db
  tbl_nms <- dbListTables(conn) %>%
    janitor::make_clean_names(case = table_name_cases)

  # get datafram names
  dfs_nm <- dfs %>%
    names() %>%
    janitor::make_clean_names(case = table_name_cases)

  #which tables and dataframes are the same
  to_add <- intersect(tbl_nms, dfs_nm)





  dbBegin(conn = conn)


  # for every table in the db find a matching dataframe
  for (tbl_nm in tbl_nms){
    #tbl_nm <- tbl_nms[[1]]


    message(glue("looking for df like {tbl_nm}"))
    #######################
    #which df matches this table
    df_nm <- names(dfs) %>%
      grep(pattern = tbl_nm, x = ., ignore.case = T, value = T)




    #only add to the table if there is exactly on matching df
    if ( length(df_nm) == 1 ){
      message(glue("found df for df like {tbl_nm}, {df_nm}"))

      df <- dfs[[df_nm]]



      #append the df
      wbe_append_from_df(df = df,
                         tbl_nm = tbl_nm,
                         conn = conn,
                         col_name_cases = col_name_cases,
                         value_name_cases = value_name_cases,
                         append = append,
                         ...)


    }else{
      df_nm_msg <- paste0(df_nm, collapse = ";")
      message(glue("Not appeding table '{tbl_nm}', because {length(df_nm)} matching dataframes exist,names:{df_nm_msg}"))
    }

  }


  dbCommit(conn)
}




wbe_best_times <-function(df, pattern = "datetime", value_name_cases ="snake"){
  #'
  #' takes a df and returns a vector showing the best times to use for a key
  #'
  #'
  #'
  nms <- df %>%
    select(matches(pattern)) %>% colnames()
  df %>%
    select(matches(pattern)) %>%
    #mutate_all(as.Date)
    mutate(., id = 1:nrow(.)) %>%
    pivot_longer(., 1:ncol(.)- 1) %>%
    unite(value, c(name, value), remove = F) %>%
    pivot_wider(names_from = "name", values_from = "value") %>%
    unite(best, nms) %>%
    arrange(id) %>%
    # mutate(., id = 1:nrow(.)) %>%
    # unite(best)
    # pivot_longer(., 1:ncol(.)- 1) %>%
    # group_by(id) %>%
    # slice(1) %>%
    # unite(best, c("name","value")) %>%
    # mutate(best = make_clean_names(best, case = value_name_cases)) %>%
    pull(best)
}


wbe_find_df_col <- function(df, col_nm = NULL){
  #'
  #' given a data frame and a column name from the DB
  #' Find the best match in the DF to that column
  #' returns a string name if found
  #' otherwise returns null
  #'
  #' @param df dataframe passed in
  #' @param col_nm name of the column we are looking for
  #'
  if (is_null(col_nm)){
    return(NULL)
  }

  df_colNm <-
    colnames(df)  %>%
    grep(pattern = glue("{col_nm}$"), x = ., ignore.case = T, value = T)
  if (length(df_colNm) != 1)
    return(NULL)

  return(df_colNm)
}



wbe_make_ID <-function(id_type, hints){
  #'
  #' Make an ID
  #'

  #TODO:
}


wbe_sampleIDs <-function(...){
  #'
  #' return the sample IDs from the sample table in the DB
  #'
  wbe_sample(...) %>% pull(sampleID)
}


wbe_sample <- function(siteids = NULL,
                       conn = wbe_conn(),
                       ...){
  #'
  #' return the sample table from the DB
  #'
  wbe_tbl("Sample", conn = conn, ... = ...) %>%
    {if(is.null(siteids)) . else filter(., siteID %in% siteids)}
}

wbe_measurementIDs <- function(...){
  #'
  #' return the measurementID from the measurement table in the DB
  #'
  wbe_measurement(...) %>% pull(measurementID)
}



wbe_measurement <- function(sampleids = NULL,
                            labids = NULL,
                            assayids = NULL,
                            siteids = NULL,
                            conn = wbe_conn(),
                            ...){
  #'
  #' return the measurement table in the db filtered by the relevent information
  #'


  #get sample IDs from the site
  sampleids_from_site <- wbe_sampleIDs(siteids, conn = conn)

  wbe_tbl("Measurement", conn = conn, ...) %>%
    {if(is.null(sampleids)) . else filter(., sampleID %in% sampleids)} %>%
    {if(is.null(labids)) . else filter(., labID %in% labids)} %>%
    {if(is.null(assayids)) . else filter(.,  assayID %in% assayids)} %>%
    {if(is.null(sampleids_from_site)) . else filter(.,  sampleID %in% sampleids_from_site)}
}




wbe_tbl <- function(tbl_nm,
                    conn = wbe_conn(),
                    collect_tbl = TRUE,
                    limit = FALSE){
  #' Return the table
  #' maybe collects it
  #'
  #' @param tbl_nm name of the table in the db
  #' @param conn
  #' @param collect_tbl if true calls collect on the dbply table
  #' @param limit if numeric acts as a limit for the number of rows to get

  dplyr::tbl(conn, tbl_nm) %>%
    {if(limit) head(., min(1,limit)) else . } %>%
    {if(collect_tbl) collect(.) else .} %>%
    mutate_at(vars(matches("date")), anytime) # TODO: datetime conversion consistency
  #mutate_at(vars(matches("date"), ignore.case = T), as.integer)
}




wbe_tbl_list <- function(conn = wbe_conn()){
  #' list tables in the db
  #'
  #' @param conn default connection to the db
  #'

  dbListTables(conn)
}




wbe_tbl_col_nms <- function(tbl_nm,
                            conn = wbe_conn()
){
  #' Return the table colum names as a vector
  #'
  #' @param tbl_nm name of the table in the db
  #' @param conn
  #'

  wbe_tbl(tbl_nm = tbl_nm, conn = conn, collect_tbl = TRUE, limit = 1) %>% colnames()
}

#' Return the list of named tibbles  from the Db with the corrcect types, but all the tibbles are length zero
#'
wbe_tbls_db_blank <- function( conn = wbe_conn()){
  wbe_tbl_list() %>%
    lapply(wbe_tbl_frmt) %>% set_names(wbe_tbl_list())
}


wbe_tbl_frmt <- function(tbl_nm,
                         conn = wbe_conn()
){
  #' Return the table format only i.e. zero row tibble
  #'
  #' @param tbl_nm name of the table in the db
  #' @param conn
  #'
  wbe_tbl(tbl_nm = tbl_nm, conn = conn, collect_tbl = TRUE, limit = 1) %>%
    head(0)
}


#'
#' ensures that all dataframes have a primary key
#'
wbe_ensure_primary_keys <- function(dfs, reporter_id){
  dfs_new <-
    lapply(names(dfs), function(tbl_nm){
      #tbl_nm <- names(dfs)[[1]]
      wbe_ensure_primary_key(df = dfs[[tbl_nm]], tbl_nm = tbl_nm, reporter_id = reporter_id)
    }) %>%
    setNames(names(dfs))
  return(dfs_new)
}



###########################################
#'
#' returns df after making sure it has the correctly named primary key with values in it.
#'
wbe_ensure_primary_key <- function(df, tbl_nm, reporter_id){

  pk_nm <- wbe_primary_key(tbl_nm)

  df_pk_nm  <- wbe_find_df_col(df = df, col_nm = pk_nm)
  if(!is.null(df_pk_nm)){
    assertthat::assert_that(df %>% pull(df_pk_nm) %>% is.na() %>% sum() == 0)
    return(df)
  }


  df %>%
    mutate(., pk_nm = wbe_generate_key(., reporter_id = "NML")) %>%
    rename(!!sym(pk_nm) := pk_nm)
}

###########################################
#'
#' Generates a unique key for the dataframe
#'
wbe_generate_key <- function(df, reporter_id){
  # reporter_id = "NML"
  # df <- dfs$AssayMethod
  df %>% format_delim(delim = "_", col_names = F) %>% str_split(pattern = "\n", n = nrow(df)) %>% unlist() %>%
    trimws() %>%
    paste(reporter_id, .,sep = "_") %>%
    digest_vect()
}

wbe_primary_key <-function(tbl_nm,
                           conn = wbe_conn(),
                           intex_of_primary_key = 1){
  #' returns the name of the primary key column from the table
  #' @param tbl_nm name of the table in the db
  #' @param conn
  #' @param intex_of_primary_key TODO: there is a better way to do this


  wbe_tbl(tbl_nm = tbl_nm,
          conn = conn, collect_tbl = T, limit = 0) %>%
    colnames() %>%
    extract2(intex_of_primary_key)
}





wbe_default_Id <- function(known_id,
                           tbl_nm ="Lab",
                           def_col_nm = "assayIDDefault",
                           conn = wbe_conn()){
  #' Finds the default ID,  is also vectorized
  #' So like when a measurement is taken by a given lab, that lab has a default assayId etc...
  #' returns known defaults
  #'
  #'
  #' @param known_id the thing we know
  #' @param tbl_nm name of the table where the default is
  #' @param def_col_nm name of the column where the default we are looking for is.
  #' @param conn
  #' def_col_nm = "assayIDDefault",
  #'


  if(is_null(known_id)){
    return("UnKnown")
  }


  # get primary key name
  pkey <- wbe_primary_key(tbl_nm = tbl_nm,
                          conn = conn
  )

  # make df for the primary keys known_id
  known_id_df <-
    tibble(tmp = known_id) %>%
    rename(!!sym(pkey) := tmp) %>%
    mutate(tmp_uid = 1:nrow(.))


  wbe_tbl(tbl_nm = tbl_nm,
          conn = conn,
          collect_tbl = T) %>%   # Get the full table refered to
    left_join(known_id_df, ., by = pkey) %>% #join with the primary keys
    count(tmp_uid, !!sym(pkey), !!sym(def_col_nm)) %>%
    select(pkey, def_col_nm) %>%
    mutate(tmp = replace_na(!!sym(def_col_nm), "UnKnown")) %>%
    select (-!!sym(def_col_nm)) %>%
    rename(!!sym(def_col_nm)  := tmp) %>%
    pull(!!sym(def_col_nm))
}



wbe_labIDDefault <- function(reporter_id,
                             conn = wbe_conn(),
                             ...){
  #' find the defaul labid for a given reporter
  #'
  #' @param reporter_id id of the reporter
  #' @param conn
  #'

  wbe_default_Id(known_id = reporter_id,
                 tbl_nm =  "Reporter",
                 def_col_nm = "labIDDefault",
                 conn = conn,
                 ...)

}





wbe_narrow_df <-function(df,
                         tbl_nm,
                         conn = wbe_conn()){
  #' return the subset of a df that best matches the tbl, eliminating some columns that don't have a good match
  #'
  #' @param df
  #' @param tbl_nm name of the table
  #' @param conn
  #'



  df2 <- tibble(tmp_uid = 1:nrow(df))


  # removes columns from the dataframe the do not match well with the given table
  for (nm in wbe_tbl_col_nms(tbl_nm = tbl_nm, conn = conn)){
    df_nm <- wbe_find_df_col(df, nm)
    if (! is_null(df_nm))
      df2[[nm]] <- df[[df_nm]]
  }
  df2[["tmp_uid"]] <- NULL

  return(df2)
}





wbe_ensure_measurement_id <- function(measure_df) {
  #' make sure the df have an ID
  #'
  #' @description takes a data frame the represents a measurement table, and makes sure it has an ID, that is unique to each measurement, returns a dataframe
  #'
  #' @param measure_df a dataframe


  #########################
  # Make measurementID if needed
  measurementID_col_nm <- wbe_find_df_col(measure_df, "measurementID")
  if(is_null(measurementID_col_nm)){
    measure_df <-
      measure_df %>%
      unite(measurementID, c("sampleID", "measureCat", "measureUnit", "measureType", "sampleIndex"), remove  = FALSE) %>%
      mutate(measurementID = digest_vect(measurementID))

    measurementID_col_nm <- wbe_find_df_col(measure_df, "measurementID")
  }
  measure_df[["measurementID"]] <- measure_df[[measurementID_col_nm]]
  return(measure_df)

}



wbe_db_2_files <- function(conn = wbe_conn(),
                           dir = dirname(conn@dbname),
                           write_func = write_csv,
                           fn_pattern = "{tbl_nm}.csv",
                           ...){
  #' Writes the db to a series of files, one per table.
  #'
  #' @param conn connection to the db
  #' @param dir directory to save the files to
  #' @param write_func function that does the writng defaults to write_csv
  #' @param fn_pattern pattern for the file name, this should make sense with write_func
  #' @param ... passed to write_func

  tbl_nms <- dbListTables(conn)
  for (tbl_nm in tbl_nms){
    df <- wbe_tbl(tbl_nm = tbl_nm, conn = conn)


    lapply(colnames(df), function(nm){
      cls <- class(df[[nm]] )
      if ("blob" %in% cls){
        message(glue("In {tbl_nm}, I don't know how to deal with 'blob' types yet, skipping and moving on."))
        df[[nm]] <- NULL
        df[[nm]] <<- "blobs are not yet supported, in extract."
      }
    })


    full_fn <- file.path(dir, glue(fn_pattern))


    write_func(df, full_fn, ...)

  }

}



wbe_sample_measurments_long_2_wide <- function(conn = wbe_conn(),
                                               sample_df = wbe_sample(conn = conn),
                                               measurement_df = wbe_measurement(conn = conn)){
  #'
  #' Takes two data frames sample and measurement, and combines them into a wide format then exports them as a single table
  #'
  #'

  sample_df <-
    sample_df %>%
    rename_all(function(nm)(glue("Sample.{nm}")))

  measurement_df_short <-
    measurement_df %>%
    unite(tmp_unified , c(measureCat, measureUnit, measureType, sampleIndex)) %>% #pull(tmp_unified)
    select(-measurementID, -reportedDate) %>%
    pivot_wider(names_from = tmp_unified, values_from = measureValue) %>%
    arrange(sampleID)


  sampleIDs <- measurement_df_short %>% distinct(sampleID, analysisDate) %>% arrange(sampleID, analysisDate)


  f %>% group_by(cat) %>% mutate(id = row_number())


  sampleIDs

  rename_all(function(nm)(glue("Measurement.{nm}"))) %>%
    full_join(sample_df, by = c("Measurement.sampleID" = "Sample.sampleID") ) %>%
    relocate(matches("Sample\\.")) %>%
    relocate(matches("\\.sampleID")) %>%
    relocate(matches("\\.siteID")) %>%
    arrange("Sample.siteID", "Sample.DateTime")
}




wbe_sample_measurments_wide_2_long <- function(df,
                                              parent_reporter_id = NULL,
                                              parent_site_id = NULL,
                                              conn = wbe_conn()){
  #'
  #'   Takes a single dataframe and tries to match it to the sample and measurement tables in the DB
  #'   returns a list of dataframes, does not append the DB
  #'
  #' @param df dataframe to split up
  #' @param parent_reporter_id
  #' @param parent_site_id
  #' @param conn
  #'



  #wbe_delete_whole_db()
  # dfsO <- wbe_xlsx_to_dfs(full_fn = file.path("data", "priv", "ottawa","www_ottawa_v0.1.1.xlsx"))
  # dfs <- wbe_xlsx_to_dfs(full_fn = file.path("data", "priv", "uw","www_uw_v0.1.1.xlsx"))
  # wbe_append_lookups(df = dfsO$Lookups)
  # df <- dfs$SampleMeasurementWide
  # df <- dfs$SampleMeasurementWideUw
  # df <- dfs$SMWideAriveNml



  #########################
  #Make sure we have a siteID
  siteID_col_nm <- wbe_find_df_col(df, "siteID")
  if(is_null(siteID_col_nm)){

    if(is_null(parent_site_id)){
      if(is_null(parent_reporter_id)){
        df[["siteID"]] <- "Unknown_unknown"
      }else{
        df[["siteID"]] <- glue("{parent_reporter_id}_uknown_site")
      }


      df[["siteID"]] <- digest_vect(df[["siteID"]])
    }else{
      df[["siteID"]] <- parent_site_id
    }

    siteID_col_nm <- wbe_find_df_col(df, "siteID")
    df <- df %>% relocate(siteID_col_nm)
  }

  #remove those with no site ID
  df <- df %>% filter(!is.na(!!sym(siteID_col_nm)))


  #########################
  # Make sampleID if needed
  sampleID_col_nm <- wbe_find_df_col(df, "sampleID")
  if(is_null(sampleID_col_nm)){
    df <-
      df %>%
      mutate(best_time = wbe_best_times(.)) %>%
      unite(sampleID, c(siteID_col_nm, best_time), remove  = FALSE) %>%
      mutate(sampleID = digest_vect(sampleID)) #%>% #pull(sampleID)

    sampleID_col_nm <- wbe_find_df_col(df, "sampleID")
    df <- df %>% relocate(sampleID_col_nm)

  }


  df <- df %>% distinct(!!sym(sampleID_col_nm), .keep_all = T)
    #TODO:
  #df %>%  count(!!sym(sampleID_col_nm), sort = T) %>% filter(n > 1) %>%
  #  inner_join(df)



  #########################
  # Make labID if needed
  labID_col_nm <- wbe_find_df_col(df, "labID")

  if(is_null(labID_col_nm )){
    df[["Measurement.labID"]] <- wbe_labIDDefault(reporter_id = parent_reporter_id, conn = conn)
    labID_col_nm <- "Measurement.labID"
    df <- df %>% relocate(labID_col_nm)

  }




  #########################
  # Make assayID if needed
  assayID_col_nm <- wbe_find_df_col(df, "assayID")
  if(is_null(assayID_col_nm)){
    df[["Measurement.assayID"]] <- wbe_default_Id(df[["labID"]],
                                                  tbl_nm ="Lab",
                                                  def_col_nm = "Measurement.assayIDDefault")
    assayID_col_nm <- "Measurement.assayID"
    df <- df %>% relocate(assayID_col_nm)
  }



  #########################
  # Make reportedDate if needed
  reportedDate_col_nm <- wbe_find_df_col(df, "reportedDate")
  if(is_null(reportedDate_col_nm)){
    df[["Measurement.reportedDate"]] <- Sys.Date()
    reportedDate_col_nm <- "Measurement.reportedDate"
    df <- df %>% relocate(reportedDate_col_nm)
  }



  #########################
  # get the measurement columns and values allowed in measurement
  measure_cats <-
    tbl(conn, "Lookups") %>%
    filter(tableName == "Measurement") %>%
    select(columnName, value ) %>%
    distinct() %>%
    collect()


  #wbe_tbl_frmt(tbl_nm = "Measurement", conn = conn)


  df_measurement_all <- df %>% select(matches("^Measurement\\."))
  analysisDate_col_indexs <- df_measurement_all %>%
    colnames() %>%
    grep(pattern = "^Measurement\\..*analysisDate*.", x = ., ignore.case = T)

  df_measurement_common <- df_measurement_all[1:analysisDate_col_indexs[1]-1]
  wbe_find_df_col(df = df_measurement_all, col_nm = "labID")

  #######################
  #
  # Data frame the can be appended to the db for measurements
  measure_df <-
    map_dfr(.x = 1:length(analysisDate_col_indexs), .f = function(i){
      #print(i)
      begin <- analysisDate_col_indexs[i]
      end <- min(analysisDate_col_indexs[i+1]-1, length(df_measurement_all %>% colnames()), na.rm = T)
      #print(begin)
      #print(end)


      pattern4_longing <- "^(?!.*_notes_)Measurement\\..*_.*_(.*)$"

      df_measurement_all[begin:end] %>% #view()
        bind_cols(df_measurement_common, .) %>%
        bind_cols(df[sampleID_col_nm], . ) %>% #view()#select(matches(pattern4_longing, ignore.case = T, perl = T)) %>% mutate_all(as.double)

        mutate_at(vars(matches(pattern4_longing, ignore.case = T, perl = T)), as.double) %>%
        pivot_longer(cols = matches(pattern4_longing, ignore.case = T, perl = T),
                     names_prefix = "Measurement.",
                     values_to = "measureValue") %>%
        separate(name , c("measureCat",
                          "measureUnit",
                          "measureType",
                          "sampleIndex")) %>%
        mutate(sampleIndex = if_else(is.na(sampleIndex) & !is.na(as.integer(measureType)), measureType, sampleIndex)) %>%
        mutate(measureType = if_else(!is.na(as.integer(measureType)), "singlton", measureType)) %>%
        wbe_narrow_df(df = ., tbl_nm = "Measurement", conn = conn) %>%
        wbe_ensure_measurement_id() %>%
        filter( ! is.na(measureValue))

    })



  sample_df <- wbe_narrow_df(df, "Sample", conn)



  return(
    list(
      Sample = sample_df,
      Measurement = measure_df
    )
  )

}





wbe_read_mappers <- function(base_dir = file.path("src", "mappers"),
                             mapper_pattern = "mapper.r"
                             ){
  #'
  #' Reads in all the mapping codes makes a list of mappers and returns the object
  #'
  #' @param base_dir base directory finds all mappers that are sub mappers of this directory
  #' @param mapper_pattern pattern of file to find
  #'


  list.files(path = base_dir, pattern = mapper_pattern, full.names = TRUE, recursive = TRUE) %>%
    map(function(x) {

      e <- parse(x)[[1]]
      mapper <-eval(e)
      mapper$mapcodefn <- basename(x)
      #mapper$mapdir <- dirname(x)
      mapper
    }) %>% set_names(map(., ~.$nm))
}




wbe_read_and_map <- function(nm,
                             mapper = get("mappers")[[nm]],
                             full_fn =  mapper$fn(), #file.path(mapper$mapdir, mapper$fn),
                             read_func = mapper$reader,
                             mapper_func = mapper$mapper
){
  #'
  #'  master function that will call a given submitter  reader and mapper functions to read a raw list
  #'
  #' @param nm name of the submitter being mapped
  #' @param full_fn full file name of the mapper
  #' @param read_func function to read in the tables
  #' @param mapper_func function to read in the tables
  #'

  dfs <- read_func(full_fn)
  mapper_func(dfs)
}

