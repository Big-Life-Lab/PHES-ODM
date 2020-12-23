
rm(list=ls())
gc()

source("src/wbe_db_func.r")
#wbe_delete_whole_db()


mappers <- wbe_read_mappers()

dfs <- mappers$NML$reader(file.path(mappers$NML$mapdir, mappers$NML$fn))

dfs_UW <- wbe_read_and_map(nm = "UW")
dfs_NML <- wbe_read_and_map(nm = "NML")
dfs_Ottawa <- wbe_read_and_map(nm = "Ottawa")


wbe_append_from_dfs(dfs_UW)
wbe_append_from_dfs(dfs_NML)
wbe_append_from_dfs(dfs_Ottawa)

