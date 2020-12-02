

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

WBE_DB_CONNS <- c()
WBE_DB_CREATE_TABLES_SQL_FN <- file.path("src", "wbe_create_tables.sql")



##############################
# call digest_vect for a vectorized version of digest
digest_vect <- Vectorize(digest)



dbe_db_default_fn <- function(){
  file.path("data", "db" ,"WBE.db")
}


wbe_db_conn <- function(drv = RSQLite::SQLite(),
                        db_fn = dbe_db_default_fn(), 
                        ...){
  #' returns a connection to a WBE database
  #' creates and emply db if needed
  if(!file.exists(db_fn)){
    wbe_db_create_db_from_script(db_fn = db_fn )
  }
  
  conn <- dbConnect(drv = drv, db_fn, ...)
  WBE_DB_CONNS <<- c(WBE_DB_CONNS, conn)
  return(conn)
}




wbe_db_Disconnect_all <- function(){
  #'
  #' removes all connections to the db that we know of
  #' 
  
  n_con <- length(WBE_DB_CONNS)
  
  lapply(WBE_DB_CONNS, function(x){dbDisconnect(x)})
  WBE_DB_CONNS <<- list()
  
  message(glue("disconnected  {n_con} connections"))
}
#wbe_db_Disconnect_all()

wbe_db_delete_whole_DB <- function(db_fn = dbe_db_default_fn()){
  #'
  #' removes all connections, then deletes the file 
  #' 
  wbe_db_Disconnect_all()
  file.remove(db_fn)
  message(glue("deleted {db_fn}"))
}
#wbe_db_delete_whole_DB


wbe_db_create_db_from_script <- function(drv = RSQLite::SQLite(),
                                         full_fn = WBE_DB_CREATE_TABLES_SQL_FN,
                                         db_fn = dbe_db_default_fn(), 
                                         ...
                                         ){
  #' creates a wbe_db from a script
  #' 
  #' 
  conn <- dbConnect(drv = drv, db_fn, ...)
  WBE_DB_CONNS <<- c(WBE_DB_CONNS, conn)

  sql_str <- readChar(con = full_fn, 
                      nchars = file.info(full_fn)$size)
  
  queries1 = str_replace_all(sql_str,'--.*$'," ")  ### remove any commented lines
  queries2 = paste(queries1, collapse = '\n') ### collapse with new lines
  queries3 = unlist(str_split(queries2,"(?<=;)")) ### separate individual queries
  
  
  for (i in 1:length(queries3)) {
    dbExecute(conn, queries3[i])
  }
  
  tbls <- paste0(db_list_tables(conn), collapse = ", ")
  message(glue("database created at:{db_fn}\nWith tables:{tbls}."))
}

#wbe_db_create_db_from_script()
#wbe_db_delete_whole_DB()





wbe_db_xlsx_to_dfs <- function(full_fn,
                               #conn = wbe_db_conn(),
                               col_name_cases = "lower_camel",
                               table_name_cases = "upper_camel"#,
                               #value_name_cases = "snake"
                               ){
  #' reads in an excel file into multiple dataframes
  #' ot will also change the case
  #' 
  
  sheets <- file.path(full_fn) %>% readxl::excel_sheets()
  #tbls <- dbListTables(conn)
  
  to_add <- sheets#intersect(tbls, sheets)
  
  dfs <- list()
  for (sh in to_add) {
    
    #GET THE df FROM the list of dfs
    df <- 
      readxl::read_xlsx(path = full_fn, sheet = sh ) %>% 
      #janitor::clean_names(case = col_name_cases) %>% 
      #mutate_if(is.character, snakecase::to_any_case, case = value_name_cases) %>% 
      as_tibble()
    
    tbl_nm <- make_clean_names(string = sh , case = table_name_cases)
    dfs[[tbl_nm]] <- df
  }

  return(dfs)
}

wbe_db_append_lookups <- function(df,
                                  tbl_nm = "Lookups",
                                  conn = wbe_db_conn(),
                                  table_name_cases = "upper_camel",
                                  col_name_cases = "lower_camel",
                                  value_name_cases = "snake",
                                  desc_name_case = "sentence") {
  #' fills a data base from from a single table
  #'
  #'
  #df <- dfs$Lookups
  
  
  df2 <- tibble(tmp_index = 1:nrow(df))
  
  tbl_format <- wbe_db_tbl_frmt(tbl_nm = tbl_nm, conn = conn)
  for (col_nm in colnames(tbl_format)) {
    curr_case <- ""
    if (col_nm == "tableName") {
      curr_case <- table_name_cases
    }
    else if (col_nm == "columnName") {
      curr_case <- col_name_cases
    }
    else if (col_nm == "value") {
      curr_case <- value_name_cases
    }
    else{
      curr_case <- desc_name_case
    }
    #correct casing in the DB
    df2[[col_nm]] <-
      df[[col_nm]] %>% snakecase::to_any_case(case = curr_case)
    
  }
  df2$tmp_index <- NULL
  wbe_db_append_from_df(
    df = df2,
    tbl_nm = tbl_nm,
    conn = conn,
    col_name_cases = col_name_cases,
    value_name_cases = ""
  )
  
}


#wbe_db_append_from_df(df = dfs$Lookups, tbl_nm = "Lookups")
wbe_db_append_from_df <- function(df, 
                                   tbl_nm, 
                                   conn = wbe_db_conn(),
                                   col_name_cases = "lower_camel",
                                   value_name_cases = ""
                                   ){
  #' fills a data base from from a single table
  #' 
  
  
  
  #we do not want to clean names yet
  #df <- df %>% clean_names(case = col_name_cases)
  
  # Get the columns and the fromat from the DB
  tbl_format <- tbl(conn, tbl_nm) %>% head(1) %>% collect() %>% slice(0)
  
  #init the tibble to append
  df2 <- tibble(tmp_uuid = 1:nrow(df))
  
  # Make sure we have compatible types and format from our DF
  for (col_nm in colnames(tbl_format)){
    
    
    #get the class of the column in the table
    cls <- class(tbl_format[[col_nm]])
    cls <- cls[[1]]
    
    print(cls)
    #Find matching column in DF list
    df_colNm <- colnames(df)  %>% grep(pattern = col_nm, x = ., ignore.case = T, value = T) 
    
    if ( length(df_colNm) == 1 && cls != "blob" ){
      #make sure we have the correct type of column to add
      df2[[col_nm]] <- as(df[[df_colNm]], cls)
    }else if (cls == "blob"){
      message(glue("In {tbl_nm}, I don't know how to deal with 'blob' types yet, skipping and moving on."))
    }else{
      message(glue("In {tbl_nm}, there are {length(df_colNm)} matches to the column {col_nm}, can not use put anything in this column"))
    }
    
  }
  
  #delet the tmp ID
  df2$tmp_uuid <- NULL
  
  #correct casing in the DB
  if (value_name_cases != ""){
    df2 <- df2 %>% mutate_if(is.character, snakecase::to_any_case, case = value_name_cases)
  }
  
  
  worked <- dbWriteTable(conn = conn, 
                         name = tbl_nm, 
                         value = df2, 
                         append = T)
  
  message(glue("wrote {nrow(df2)} rows and {ncol(df2)} column to {tbl_nm}, status {worked}"))     
  
}








wbe_db_append_from_dfs <- function(dfs, conn = wbe_db_conn(),
                                   table_name_cases = "upper_camel",
                                   col_name_cases = "lower_camel",
                                   value_name_cases = "snake"){
  #' fills a data base from from a list of data frames
  #' 
  #' 
  
  tbl_nms <- dbListTables(conn)
  dfs_nm <- dfs %>% names() %>% janitor::make_clean_names(case = table_name_cases)
  to_add <- intersect(tbls, dfs_nm)
  
  dbListFields(conn, tbl_nm)
  for (tbl_nm in tbls){
    df_nm <- names(dfs) %>% grep(pattern = tbl_nm, x = ., ignore.case = T, value = T) 
    
    
    #tbl_nm <- df_nm %>% janitor::make_clean_names(case = table_name_cases)

    #if ( db_has_table(conn, tbl_nm)){
    if ( length(df_nm) == 1 ){
    
      df <- dfs[[df_nm]]
      
      
      wbe_db_append_from_df(df = df, tbl_nm = tbl_nm, conn = conn, col_name_cases = col_name_cases, value_name_cases = value_name_cases)
      
         
    }else{
      df_nm_msg <- paste0(df_nm, collapse = ";")
      message(glue("Not appeding table '{tbl_nm}', because {length(df_nm)} matching dataframes exist,names:{df_nm_msg}"))
    }
 
  }
  
}
wbe_db_best_times <-function(df, pattern = "datetime", value_name_cases ="snake"){
  #' takes a df and returns a vector showing the best times to use for a key
  
  df %>% 
    select(matches(pattern)) %>% 
    mutate(., id = 1:nrow(.)) %>% 
    pivot_longer(., 1:ncol(.)- 1) %>%
    group_by(id) %>%
    slice(1) %>%
    unite(best, c("name","value")) %>%
    mutate(best = make_clean_names(best, case = value_name_cases)) %>%
    pull(best)
}


wbe_db_find_df_col <- function(df, col_nm = NULL){
  #'
  #' given a data frame and a column name from the DB
  #' Find the best match in the DF to that column
  #' returns a string name if found
  #' otherwise returns null
  #'
  if (is_null(col_nm)){
    return(NULL)
  }
  
  df_colNm <- colnames(df)  %>% grep(pattern = glue("{col_nm}$"), x = ., ignore.case = T, value = T)
  if (length(df_colNm) != 1)
    return(NULL)
  
  return(df_colNm)
}



wbe_db_make_ID <-function(id_type, hints){
  #'
  #' Make an ID
  #'
  
  
}




wbe_db_tbl <- function(tbl_nm,
                       conn = wbe_db_conn(), 
                       collect_tbl = TRUE,
                       limit = FALSE){
  #' Return the table
  #' maybe collects it
  #' 
  
  dplyr::tbl(conn, tbl_nm) %>% 
    {if(limit) head(., min(1,limit)) else . } %>%
    {if(collect_tbl) collect(.) else .}
  

}

wbe_db_tbl_col_nms <- function(tbl_nm,
                            conn = wbe_db_conn() 
){
  #' Return the table format only i.e. zero row tibble
  #' 
  #' 
  #dbListFields(conn = conn, tbl_nm = tbl_nm)
  wbe_db_tbl(tbl_nm = tbl_nm, conn = conn, collect_tbl = TRUE, limit = 1) %>% colnames()
}


wbe_db_tbl_frmt <- function(tbl_nm,
                            conn = wbe_db_conn() 
                       ){
  #' Return the table format only i.e. zero row tibble
  #' 
  #' 
  wbe_db_tbl(tbl_nm = tbl_nm, conn = conn, collect_tbl = TRUE, limit = 1) %>% 
    head(0)
}

wbe_db_primary_key <-function(tbl_nm,
                              conn = wbe_db_conn(),
                              intex_of_primary_key = 1){
  #` primary key
  
  
  wbe_db_tbl(tbl_nm = tbl_nm,
             conn = conn, collect_tbl = T, limit = 0) %>%
    colnames() %>%
    extract2(intex_of_primary_key)
}





wbe_db_default_Id <- function(known_id,
                  tbl_nm ="Lab",
                  def_col_nm = "assayIDDefault",
                  conn = wbe_db_conn()){
  #` finds the default ID,  is also vectorized
  
  if(is_null(known_id)){
    return("UnKnown")
  }
  
  # get primary key name
  pkey <- wbe_db_primary_key(tbl_nm = tbl_nm, conn = conn)
  
  
  known_id_df <-
    tibble(tmp = known_id) %>%
    rename(!!sym(pkey) := tmp) %>% 
    mutate(tmp_uid = 1:nrow(.))
  
  
  wbe_db_tbl(tbl_nm = tbl_nm,
             conn = conn, collect_tbl = T) %>% 
    left_join(known_id_df, ., by = pkey) %>%
    count(tmp_uid, !!sym(pkey), !!sym(def_col_nm)) %>%
    select(pkey, def_col_nm) %>%
    mutate(tmp = replace_na(!!sym(def_col_nm), "UnKnown")) %>%
    select (-!!sym(def_col_nm)) %>% 
    rename(!!sym(def_col_nm)  := tmp) %>%
    pull(!!sym(def_col_nm))
}


wbe_db_labIDDefault <- function(reporter_id,
                                conn = wbe_db_conn()){
  #` unkown lab id
  
  
  
  wbe_db_default_Id(known_id = reporter_id, tbl_nm =  "Reporter", def_col_nm = "labIDDefault", conn = conn)
  # if(is_null(reporter_id)){
  #   return("UnKnown")
  # }
  # 
  # lab_id <- 
  #   wbe_db_tbl(tbl_nm = "Reporter",
  #            conn = conn, collect_tbl = T) %>% 
  #   filter(reporterID == reporter_id) %>%
  #   pull(labIDDefault) 
  # 
  # if(length(lab_id) != 1){
  #   message(glue("Tried to lookup labIDDefault by reporterID={reporter_id}, got back {length(lab_id)} responses, using UnKnown."))
  #   return("UnKnown")    
  # }
  # 
  # return(lab_id)
}


wbe_db_narrow_df <-function(df, tbl_nm, conn = wbe_db_conn()){
  #` return the subset of a df that best matches the tbl
  df2 <- tibble(tmp_uid = 1:nrow(df))
  for (nm in wbe_db_tbl_col_nms(tbl_nm = tbl_nm, conn = conn)){
    df_nm <- wbe_db_find_df_col(df, nm)
    if (! is_null(df_nm))
      df2[[nm]] <- df[[df_nm]]
  }
  df2[["tmp_uid"]] <- NULL
  return(df2)
}



wbe_db_sample_measurments_wide_2_long<- function(df, 
                                                 parent_reporter_id = NULL, 
                                                 parent_site_id = NULL, 
                                                 conn = wbe_db_conn()){
  #' 
  #'   Takes a single dataframe and tries to match it to the sample and measurement tables in the DB
  #'     
  
  
  
  #wbe_db_delete_whole_DB()
  dfsO <- wbe_db_xlsx_to_dfs(full_fn = file.path("data", "priv", "ottawa","www_ottawa_v0.1.1.xlsx"))
  dfs <- wbe_db_xlsx_to_dfs(full_fn = file.path("data", "priv", "uw","www_uw_v0.1.1.xlsx"))
  wbe_db_append_lookups(df = dfsO$Lookups)
  #df <- dfs$SampleMeasurementWide
  df <- dfs$SampleMeasurementWideUw
  
  
  
  #########################
  #Make sure we have a siteID
  siteID_col_nm <- wbe_db_find_df_col(df, "siteID")
  if(is_null(siteID_col_nm)){
    
    if(is_null(parent_site_id)){
      if(is_null(parent_reporter_id)){
        df[["siteID"]] <- "Unknown_unknown"
      }else{
        df[["siteID"]] <- glue("{parent_reporter_id}_uknown_site")
      }      
    }else{
      df[["siteID"]] <- parent_site_id
    }
    library(digest)
    df[["siteID"]] <- digest_vect(df[["siteID"]])
    siteID_col_nm <- wbe_db_find_df_col(df, "siteID")
  }
  
  
  
  
  #########################
  # Make sampleID if needed
  sampleID_col_nm <- wbe_db_find_df_col(df, "sampleID")
  if(is_null(sampleID_col_nm)){
    df <- 
      df %>% 
      mutate(best_time = wbe_db_best_times(.)) %>% 
      unite(sampleID, c(siteID_col_nm, best_time), remove  = FALSE) %>%
      mutate(sampleID = digest_vect(sampleID))
    
    sampleID_col_nm <- wbe_db_find_df_col(df, "sampleID")
  }
  
  labID_col_nm <- wbe_db_find_df_col(df, "labID")
  if(is_null(labID_col_nm )){
    df[["labID"]] <- wbe_db_labIDDefault(reporter_id = parent_reporter_id, conn = conn)
    labID_col_nm <- "labID"
  }
  
  
  assayID_col_nm <- wbe_db_find_df_col(df, "assayID")
  if(is_null(assayID_col_nm)){
    df[["assayID"]] <- wbe_db_default_Id(df[["labID"]],
                                       tbl_nm ="Lab",
                                       def_col_nm = "assayIDDefault")
    assayID_col_nm <- "labID"
  }
  
  reportedDate_col_nm <- wbe_db_find_df_col(df, "reportedDate")
  if(is_null(reportedDate_col_nm)){
    df[["reportedDate"]] <- Sys.Date()
    assayID_col_nm <- "reportedDate"
  }  
  
  measure_cats <- 
    tbl(conn, "Lookups") %>%
    filter(tableName == "Measurement") %>% 
    select(columnName, value ) %>%
    distinct() %>% 
    collect()
    
  
  #wbe_db_tbl_frmt(tbl_nm = "Measurement", conn = conn)
  
  
  
  measure_df <-
    df %>% #select(sampleID_col_nm, matches("^Measurement\\..*_.*_.*$", ignore.case = T))%>% 
    mutate_at(vars(matches("^Measurement\\..*_.*_.*$", ignore.case = T)), as.double) %>% 
    pivot_longer(cols = matches("^Measurement\\..*_.*_.*$", ignore.case = T), names_prefix = "Measurement.", values_to = "measureValue") %>% 
    separate(name , c("measureCat", "measureUnit", "measureType", "sampleIndex")) %>%
    wbe_db_narrow_df(df = ., tbl_nm = "Measurement", conn = conn)
  
  
  #########################
  # Make measurementID if needed
  measurementID_col_nm <- wbe_db_find_df_col(measure_df, "measurementID")
  if(is_null(measurementID_col_nm)){
    measure_df <- 
      measure_df %>% 
      unite(measurementID, c("sampleID", "measureCat", "measureUnit", "measureType", "sampleIndex"), remove  = FALSE) %>%
      mutate(measurementID = digest_vect(measurementID))

    measurementID_col_nm <- wbe_db_find_df_col(measure_df, "measurementID")
  }
  

  sample_df <- wbe_db_narrow_df(df, "Sample", conn)
  
  
  dbBegin(conn = conn)
  wbe_db_append_from_df(df = measure_df, tbl_nm = "Measurement", conn = conn )
  wbe_db_append_from_df(df = sample_df, tbl_nm = "Sample", conn = conn ) 
  dbCommit(conn)
  
  
  wbe_db_tbl("Measurement") %>% view()
}


