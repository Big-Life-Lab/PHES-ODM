



#
trans_list_append <-
  function(key_start_name,
           key_end_name,
           key_name_pos_list,
           key_start_index,
           key_end_index,
           pos_row_start,
           pos_row_end) {
    if (grepl(key_start_name , key_end_name, fixed = TRUE)) {
      # Verify end tag
      if ("/" != stringr::str_sub(key_end_name, -1)) {
        stop("Missing end tag")
      } else{
        # Create translation list item
        trans_start_pos <-
          key_name_pos_list[[key_start_index]][["key_pos"]][[1]][pos_row_start,1]
        trans_start_line <- 
          key_name_pos_list[[key_start_index]][["row_num"]]
        trans_end_pos <-
          key_name_pos_list[[key_end_index]][["key_pos"]][[1]][pos_row_end,2]
        trans_end_line <-
          key_name_pos_list[[key_end_index]][["row_num"]]
        list_item <-
          list(
            translation_character_reference = c(trans_start_pos, trans_end_pos),
            translation_line_reference = c(trans_start_line,trans_end_line),
            translation_key = key_start_name
          )
      }
    } else{
      stop("Missing translation key pair")
    }
    return(list_item)
  }


# Read in csv into sql db

create_db_from_csv <-
  function(db_connection, origin_name, db_name) {
    # direct read not working when commas present inside of text
    tmp_table <- readr::read_csv(origin_name)
    # Write csv to db
    RSQLite::dbWriteTable(
      conn = db_connection,
      name = db_name,
      value = tmp_table,
      row.names = FALSE,
      header = TRUE
    )
    
    
  }



# Read in template file

read_in_template <- function(template_path) {
  con = file(template_path)
  return(readLines(con))
}


# Insert translation where posible

insert_translation <-
  function(origin_text, lang_code, db_con) {
    chunk_symbol <- "<!--`\\s*(.*?)\\s*-->"
    key_name_pos_list <- list()
    translation_list <- list()
    
    # Get positions and keys of chunks for translation
    for (line_number in 1:length(origin_text)) {
      key_name =
        stringr::str_match_all(origin_text[[line_number]], chunk_symbol)[[1]][, 2]
      key_pos <-
        stringr::str_locate_all(origin_text[[line_number]], chunk_symbol)
      
      if (length(key_name) > 0) {
        key_name_pos_list[[length(key_name_pos_list) + 1]] <-
          list(key_pos = key_pos, key_name = key_name, row_num = line_number)
      }
    }
    
    for (key_number in length(key_name_pos_list):1) {
      # Check for chunk key pair
      tmp_key_name <- key_name_pos_list[[key_number]][["key_name"]]
      key_end_symbol <- "/"
      
      # Check for early exit through invalid ending key
      
      if (length(tmp_key_name) < 2) {
        if (grepl(key_end_symbol, tmp_key_name, fixed = TRUE)) {
          key_end_index <- key_number
          key_start_index <- key_number - 1
          
          # Verify key match
          key_end_name <-
            trimws(key_name_pos_list[[key_end_index]][["key_name"]])
          key_start_name <-
            trimws(key_name_pos_list[[key_start_index]][["key_name"]])
          list_item <-
            trans_list_append(
              key_start_name,
              key_end_name,
              key_name_pos_list,
              key_start_index,
              key_end_index,
              1,1
            )
          translation_list[[length(translation_list)+1]] <- list_item
        }
        # Treat same line translation
      } else
        if (length(tmp_key_name) %% 2 == 0) {
          for (single_key_index in 1:(length(tmp_key_name)-1)) {
            key_start_name <-
              trimws(key_name_pos_list[[key_number]][["key_name"]][[single_key_index]])
            key_end_name <-
              trimws(key_name_pos_list[[key_number]][["key_name"]][[single_key_index+1]])
            list_item <-
              trans_list_append(
                key_start_name,
                key_end_name,
                key_name_pos_list,
                key_number,
                key_number,
                single_key_index,
                single_key_index+1
              )
            translation_list[[length(translation_list)+1]] <- list_item
          }
        } else
          stop("Missing key pair")
    }
    
    replace_text <- origin_text
    # Loop over translations
    for (translation_chunk in translation_list) {
      translation_start_line <- translation_chunk$translation_line_reference[[1]]
      translation_end_line <- translation_chunk$translation_line_reference[[2]]
      translation_start_characer <- translation_chunk$translation_character_reference[[1]]
      translation_end_characer <- translation_chunk$translation_character_reference[[2]]
      translation_key <- translation_chunk$translation_key
      # Insert single line translation
      if(translation_start_line == translation_end_line){
        translation_line = translation_start_line
        tmp_line <- replace_text[[translation_line]]
        quary <- paste0("SELECT ", lang_code, " FROM localization WHERE key ='", translation_key,"'")
        stringr::str_sub(tmp_line, translation_start_characer, translation_end_characer) <- dbGetQuery(db_con, quary)[[1]]
        
        replace_text[[translation_line]]<- tmp_line
      
      # Insert Multi line translation
      }else{
        
        # Remove lines from start+1 to end
        replace_text <- replace_text[-((translation_start_line+1):translation_end_line)]
        
        tmp_line <- replace_text[[translation_start_line]]
        quary <- paste0("SELECT ", lang_code, " FROM localization WHERE key ='", translation_key,"'")
        stringr::str_sub(tmp_line, translation_start_characer, translation_end_characer) <- dbGetQuery(db_con, quary)[[1]]
        
        replace_text[[translation_start_line]]<- tmp_line
       
      }
    }
    
    return(replace_text)
  }

# Import RVML
insert_content <- function(origin_text, lang_code, db_con) {
  chunk_symbol <- "```\\{rvml\\s*(.*?)\\s*\\}```"
  pos_list <- list()
  insertion_list <- list()
  
  # Get positions and keys of chunks for translation
  for (line_number in 1:length(origin_text)) { 
    if (length(stringr::str_match_all(origin_text[[line_number]], chunk_symbol)[[1]][, 2]) > 0) {
      pos_list[[length(pos_list) + 1]] <-line_number
    }
  }
  for (pos_index in seq(1,length(pos_list), by=2)) {
    insertion_list[[length(insertion_list)+1]] <- list(start_line <- pos_list[[pos_index]], end_line <- pos_list[[pos_index+1]])
  }
  
  # Retrive code line
  for (variable in vector) {
    
  }
  
}

#
run_translations <- function(db_con, template_origin){
  valid_translations <- c("en","fr")
  template_text <- read_in_template(template_origin)
  #insert_translation(tmp_line, lang_code = "fr", db_con = db)
  dir.create(file.path(getwd(), "content"), showWarnings = FALSE)
  for (translation_code in valid_translations) {
    dir.create(file.path(getwd(), paste0("content/",translation_code)), showWarnings = FALSE)
    translated_text <- insert_translation(template_text, lang_code = translation_code, db_con = db_con)
    
    #Write output
    fileConn<-file(paste0("content/",translation_code,"/",template_origin))
    writeLines(translated_text, fileConn)
    close(fileConn)
  }
}
