
rm(list=ls())
gc()

source("src/wbe_db_func.r")
#wbe_delete_whole_db()


map_from <- "UW"


mappers <- wbe_read_mappers()

dfs <- mappers$NML$reader(file.path(mappers$NML$mapdir, mappers$NML$fn))

dfs_UW <- wbe_read_and_map(nm = "UW")
dfs_NML <- wbe_read_and_map(nm = "NML")
dfs_O <- wbe_read_and_map(nm = "Ottawa")

dfs_O %>% names()
dfs_O$Measurement
