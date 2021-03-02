



library(stringr)
library(DiagrammeR)
library(DiagrammeRsvg)
library(datamodelr)
library(htmltools)

wbe_generate_erd <- function(
                            lang = "fr",
                            encoding = "UTF-8",
                            tbls = read_csv(file.path(curr_wd, "Tables.csv")),
                            variables = read_csv(file.path(curr_wd, "Variables.csv")),
                            tableLabel_nm = paste0("tableLabel_", lang),
                            erd_fn = file.path("IMG", "ERD.svg")
                            ){

    #Create blank tables
    blank_tbls <-
    tbls %>%
        pull(tableName) %>%
        unique() %>%
        lapply(
            function(curr_tbl){
                cols <-
                    variables %>%
                    filter(tableName == curr_tbl) %>%
                    pull(variableName) %>%
                    unique()

                new_tbl <- tibble()
                lapply(cols, function(curr_col){

                    colType <-
                        variables %>%
                        filter(tableName == curr_tbl) %>%
                        filter(variableName == curr_col) %>%
                        pull(variableType) %>%
                        wbe_sql_dataType_2_ERD_type()
                    new_tbl[curr_col] <<- colType
                })
                new_tbl
            })

    #put names on the tables
    names(blank_tbls) <- tbls %>%
        #mutate(tmp = paste0(tableName, " (" , !!sym(tableLabel_nm), ")")) %>%
        mutate(tmp = tableName) %>%
        pull(tmp) %>%
        unique()



    #create the data model
    dm_f <- dm_from_data_frames(blank_tbls)



    fk <-
        variables %>%
        filter(key == "Foreign key")

    pk <-
        variables %>%
        filter(key == "Primary Key")

    #make primary keys
    walk(1:nrow(pk), function(i_row){
        curr_pk <- pk %>% slice(i_row) #%>%
        dm_f <<- dm_set_key(dm_f, curr_pk$tableName    , curr_pk$variableName)
    })



    #make links
    walk(1:nrow(fk), function(i_row){

        curr_fk <- fk %>% slice(i_row) #%>%
            #mutate(tableName = stringr::str_to_title(tableName)) %>%
            #mutate(foreignKeyTable = stringr::str_to_title(foreignKeyTable))
        dm_f <<- dm_add_reference_(
            dm_f,
            curr_fk$tableName,
            curr_fk$variableName,
            curr_fk$foreignKeyTable,
            curr_fk$foreignKeyVariable
            #blank_tbls[[curr_fk$tableName]][[curr_fk$variableName]] == blank_tbls[[curr_fk$foreignKeyTable]][[curr_fk$foreignKeyVariable]]
        )
    })

    graph <- dm_create_graph(dm_f, rankdir = "LR", col_attr = c("column", "type"), view_type = "all")
    g <- dm_render_graph(graph)
    g
    svg_str <- export_svg(g)



    fileConn<-file(erd_fn,  encoding = encoding)
    writeLines(text = c(svg_str), con = fileConn)
    close(fileConn)
    svg_str
}
