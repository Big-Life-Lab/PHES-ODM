
rm(list=ls())
gc()

source("src/wbe_db_func.r")
#wbe_delete_whole_db()



mappers <- wbe_read_mappers()


mapper <- mappers$NML
dfs <- mapper$reader(mapper$fn())

names(dfs)
dfs <- mapper$mapper(dfs)
dfs <- wbe_ensure_primary_keys(dfs = dfs ,reporter_id = "NML" )


#wbe_append_from_df(df = dfs$Sample, tbl_nm = "Sample")
wbe_append_from_dfs(dfs = dfs)

dfs

dfs_NML <- wbe_read_and_map(nm = "NML")


dfs$Sample$SampleID


mapper <- mappers$NML

do_mapping = function(mapper){
    mapper$fn()
    mapper$validate()
    dfs <- mapper$reader(full_fn = mapper$fn())
    new_dfs <- mapper$mapper(dfs)
}




mappers$NML$fn()

dfs <- mappers$NML$reader(file.path(mappers$NML$mapdir, mappers$NML$fn))

dfs_UW <- wbe_read_and_map(nm = "UW")
dfs_NML <- wbe_read_and_map(nm = "NML")
dfs_Ottawa <- wbe_read_and_map(nm = "Ottawa")


wbe_append_from_dfs(dfs_UW)
wbe_append_from_dfs(dfs_NML)
wbe_append_from_dfs(dfs_Ottawa)

