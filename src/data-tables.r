library(here)
library(osfr)
library(dplyr)
library(knitr)
library(readxl)

osf_project_url <- 'https://osf.io/49z2b/'
osf_project <- '49z2b'
data_folder <- file.path(here(),'dictionary-tables')

# get the OSF project information
odm_osf <- osf_retrieve_node(osf_project)

# get OSF.io components, ODM versions.
components <- osf_ls_nodes(odm_osf)
versions <- filter(components, grepl('^Version', name))

# order by version number
versions <- versions[order(versions$name), ]
version_names <- versions[c('name')]

# use the last version, or change the default version
default_version <- tail(versions, n=1)
default_version_name <- tail(version_names, n=1)
# default_version <- "Version 2.0 Release Candidate 2 - Dictionary & Templates"

files <- osf_ls_files(default_version)
file_names <- files[c('name')]

#download and save the Excel dictionary and templates in ../data/raw
dictionary <- filter(files, grepl('^Dict', name))
dictionary <- osf_retrieve_file(as.character(dictionary['id']))
dictionary <- osf_download(dictionary, path = data_folder, conflicts = "overwrite")
templates <- filter(files, grepl('^Templates', name))
templates <- osf_retrieve_file(as.character(templates['id']))
templates <- osf_download(templates, path = data_folder, conflicts = "overwrite")

parts <- read_excel(as.character(dictionary['local_path']), sheet = 'parts')
write.csv(parts, file.path(data_folder, "parts.csv"))

sets <- read_excel(as.character(dictionary['local_path']), sheet = 'sets')
write.csv(parts, file.path(data_folder, "parts.csv"))