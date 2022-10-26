# SQL convert
prepare_for_quary <-
  function(string_to_convert,
           db_con,
           sql_connect_symbol,
           lang_code) {
    # Temporary removal of translation code will add when get translations up and running
    string_to_convert <-
      stringr::str_replace_all(string_to_convert, "_%", "")
    
    key_name =
      stringr::str_match_all(string_to_convert, sql_connect_symbol)[[1]][, 2]
    key_pos <-
      stringr::str_locate_all(string_to_convert, sql_connect_symbol)
    
    quary_var <-
      list(db_names = key_name,
           string_pos = key_pos,
           var_base = string_to_convert)
    return(quary_var)
    
  }



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
      if ("/" != stringr::str_sub(key_end_name,-1)) {
        stop("Missing end tag")
      } else{
        # Create translation list item
        trans_start_pos <-
          key_name_pos_list[[key_start_index]][["key_pos"]][[1]][pos_row_start, 1]
        trans_start_line <-
          key_name_pos_list[[key_start_index]][["row_num"]]
        trans_end_pos <-
          key_name_pos_list[[key_end_index]][["key_pos"]][[1]][pos_row_end, 2]
        trans_end_line <-
          key_name_pos_list[[key_end_index]][["row_num"]]
        list_item <-
          list(
            translation_character_reference = c(trans_start_pos, trans_end_pos),
            translation_line_reference = c(trans_start_line, trans_end_line),
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
  function(db_file_name, origin_name, db_name) {
    db_connection <- DBI::dbConnect(RSQLite::SQLite(), db_file_name)
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
    
    return(db_connection)
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
          list(key_pos = key_pos,
               key_name = key_name,
               row_num = line_number)
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
              1,
              1
            )
          translation_list[[length(translation_list) + 1]] <-
            list_item
        }
        # Treat same line translation
      } else
        if (length(tmp_key_name) %% 2 == 0) {
          for (single_key_index in 1:(length(tmp_key_name) - 1)) {
            key_start_name <-
              trimws(key_name_pos_list[[key_number]][["key_name"]][[single_key_index]])
            key_end_name <-
              trimws(key_name_pos_list[[key_number]][["key_name"]][[single_key_index +
                                                                      1]])
            list_item <-
              trans_list_append(
                key_start_name,
                key_end_name,
                key_name_pos_list,
                key_number,
                key_number,
                single_key_index,
                single_key_index + 1
              )
            translation_list[[length(translation_list) + 1]] <-
              list_item
          }
        } else
          stop("Missing key pair")
    }
    
    replace_text <- origin_text
    # Loop over translations
    for (translation_chunk in translation_list) {
      translation_start_line <-
        translation_chunk$translation_line_reference[[1]]
      translation_end_line <-
        translation_chunk$translation_line_reference[[2]]
      translation_start_characer <-
        translation_chunk$translation_character_reference[[1]]
      translation_end_characer <-
        translation_chunk$translation_character_reference[[2]]
      translation_key <- translation_chunk$translation_key
      # Insert single line translation
      if (translation_start_line == translation_end_line) {
        translation_line = translation_start_line
        tmp_line <- replace_text[[translation_line]]
        quary <-
          paste0("SELECT ",
                 lang_code,
                 " FROM localization WHERE key ='",
                 translation_key,
                 "'")
        stringr::str_sub(tmp_line,
                         translation_start_characer,
                         translation_end_characer) <-
          DBI::dbGetQuery(db_con, quary)[[1]]
        
        replace_text[[translation_line]] <- tmp_line
        
        # Insert Multi line translation
      } else{
        # Remove lines from start+1 to end
        replace_text <-
          replace_text[-((translation_start_line + 1):translation_end_line)]
        
        tmp_line <- replace_text[[translation_start_line]]
        quary <-
          paste0("SELECT ",
                 lang_code,
                 " FROM localization WHERE key ='",
                 translation_key,
                 "'")
        stringr::str_sub(tmp_line,
                         translation_start_characer,
                         translation_end_characer) <-
          DBI::dbGetQuery(db_con, quary)[[1]]
        
        replace_text[[translation_start_line]] <- tmp_line
        
      }
    }
    
    return(replace_text)
  }

# Import RVML
insert_content <- function(origin_text, lang_code, db_con) {
  chunk_symbol <- "```\\{rvml\\s*(.*?)\\s*\\}```"
  var_keyword <- "var"
  sql_connect_symbol <- "\\{\\{\\s*(.*?)\\s*\\}\\}"
  pos_list <- list()
  insertion_list <- list()
  content_to_insert <- list()
  
  
  # Get positions and keys of chunks for translation
  for (line_number in 1:length(origin_text)) {
    if (length(stringr::str_match_all(origin_text[[line_number]], chunk_symbol)[[1]][, 2]) > 0) {
      pos_list[[length(pos_list) + 1]] <- line_number
    }
  }
  for (pos_index in seq(1, length(pos_list), by = 2)) {
    insertion_list[[length(insertion_list) + 1]] <-
      list(start_line <-
             pos_list[[pos_index]], end_line <-
             pos_list[[pos_index + 1]])
  }
  
  # Retrive code line
  for (single_chunk in insertion_list) {
    start_pos <- single_chunk[[1]]
    end_pos <- single_chunk[[2]]
    var_list <- list()
    var_names <- ""
    
    for (line_number in start_pos:end_pos) {
      if (grepl(var_keyword, origin_text[[line_number]])) {
        var_value <- sub(".*= ", "", origin_text[[line_number]])
        var_name <- sub("=.*", "", origin_text[[line_number]])
        var_name <- trimws(sub(var_keyword, "", var_name))
        var_names <- paste(names(var_list), collapse = "|")
        
        # Check for presense of variables inside var_value
        if (grepl(var_names, var_value)) {
          for (insert_var_name in names(var_list)) {
            if (grepl(insert_var_name, var_value)) {
              var_value <-
                stringr::str_replace_all(var_value, insert_var_name, var_list[[insert_var_name]][["var_value"]])
            }
          }
        }
        
        if (grepl(sql_connect_symbol, var_value)) {
          prepared_quary_list <-
            prepare_for_quary(var_value, db_con, sql_connect_symbol, lang_code)
          var_list[[var_name]] <-
            list(line_number = line_number,
                 quary_info = prepared_quary_list)
        } else{
          var_list[[var_name]] <-
            list(line_number = line_number,
                 var_value = var_value)
        }
        
      } else if (grepl(sql_connect_symbol, origin_text[[line_number]])) {
        # SQL keywords
        sql_where <- "filter"
        sql_order <- "order"
        sql_select <- "format"
        # Create content to insert
        sql_select_blob <- ""
        sql_order_blob <- ""
        sql_where_blob <- ""
        
        quary_line <- origin_text[[line_number]]
        quary_line <-
          stringr::str_remove_all(quary_line, "\\{\\{|\\}\\}")
        quary_commands <- unlist(strsplit(quary_line, ","))
        
        valid_columns <- DBI::dbListFields(db_con, "parts")
        quary_columns <- list()
        for (SQL_command in quary_commands) {
          if (grepl(sql_select, SQL_command)) {
            name_of_var <-
              stringr::str_remove_all(SQL_command, "format|\\(|\\)")
            vars_to_pull <-
              var_list[[name_of_var]][["quary_info"]][["db_names"]]
            
            # Verify existance of vars
            for (db_var_name in vars_to_pull) {
              # Check for var presense
              if (db_var_name %in% valid_columns) {
                quary_columns[length(quary_columns) + 1] <- db_var_name
              }
            }
            quary_columns <-
              paste(unique(unlist(quary_columns)), collapse = ", ")
            sql_select_blob <- paste("SELECT", quary_columns)
          } else if (grepl(sql_select, sql_where)) {
            
          } else if (grepl(sql_select, sql_order)) {
            
          }
        }
        # Create content object
        quary <- paste("SELECT", quary_columns, "FROM parts")
        content_to_insert[[length(content_to_insert) + 1]] <-
          list(
            chunk_location = single_chunk,
            line_number = line_number,
            quary = quary,
            template = var_list[[name_of_var]][["quary_info"]][["var_base"]]
          )
      }
      #
      #val_table <- DBI::dbGetQuery(db_con, quary)
    }
  }
  # Create output
  return_content <- list("")
  for (content_index in 1:length(content_to_insert)) {
    sql_table <-
      DBI::dbGetQuery(db_con, content_to_insert[[content_index]]$quary)
    template <- content_to_insert[[content_index]]$template
    template <- gsub('^.|.$', '', template)
    vars_in_template <-
      unique(stringr::str_match_all(template, sql_connect_symbol)[[1]][, 2])
    
    # @RUSTY Figure out way to do with apply
    for (current_row in 1:nrow(sql_table)) {
      running_content <- template
      for (running_var in vars_in_template) {
        tmp_insert <- as.character(sql_table[current_row, running_var])
        # For now while i get translations in place
        if (length(tmp_insert) < 1) {
          tmp_insert <- "missing till i get translation"
        }
        if (is.na(tmp_insert)) {
          tmp_insert <- "NA(maybe bug)"
        }
        running_content <-
          stringr::str_replace_all(running_content,
                                   paste0("\\{\\{", running_var, "\\}\\}"),
                                   tmp_insert)
      }
      return_content[[content_index]] <-
        append(return_content[[content_index]], running_content)
      
      # Create empty line for clarity
      
      return_content[[content_index]] <-
        append(return_content[[content_index]], "")
    }
  }
  # Create output
  new_file <- c()
  previous_chunk_end <- 1
  for (content_index in 1:length(content_to_insert)) {
    chunk_start <-
      content_to_insert[[content_index]]$chunk_location[[1]]
    chunk_end <-
      content_to_insert[[content_index]]$chunk_location[[2]]
    
    new_file <-
      append(new_file, origin_text[previous_chunk_end:chunk_start - 1])
    
    previous_chunk_end <- chunk_end
    
    new_file <- append(new_file, return_content[[content_index]])
  }
  if (previous_chunk_end + 1 < length(origin_text)) {
    new_file <-
      append(new_file, origin_text[previous_chunk_end + 1:length(origin_text)])
  }
  return(new_file)
}

#
run_translations <- function(db_con, template_origin) {
  valid_translations <- c("en", "fr")
  template_text <- read_in_template(template_origin)
  #insert_translation(tmp_line, lang_code = "fr", db_con = db)
  dir.create(file.path(getwd(), "content"), showWarnings = FALSE)
  for (translation_code in valid_translations) {
    dir.create(file.path(getwd(), paste0("content/", translation_code)), showWarnings = FALSE)
    translated_text <-
      insert_translation(template_text, lang_code = translation_code, db_con = db_con)
    
    #Write output
    fileConn <-
      file(paste0("content/", translation_code, "/", template_origin))
    writeLines(translated_text, fileConn)
    close(fileConn)
  }
}

run_content_insert <- function(db_con, content_location) {
  valid_translations <- c("en", "fr")
  for (translation_code in valid_translations) {
    files <-
      list.files(
        path = paste0(content_location, "/", translation_code),
        pattern = "*.md",
        full.names = TRUE,
        recursive = FALSE
      )
    lapply(files, function(x) {
      template_text <- read_in_template(x)
      content_text <-
        insert_content(template_text, lang_code = translation_code, db_con = db_con)
      fileConn <-
        file(x)
      # Replace br tag with actual new line
      content_text <- unlist(stringr::str_split(content_text, "<br />"))
      writeLines(content_text, fileConn)
      close(fileConn)
    })
  }
}