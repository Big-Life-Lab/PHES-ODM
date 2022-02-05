# -*- coding: utf-8 -*-
pip install cerberus

#importing necessary packages

from cerberus import Validator
import pandas as pd
import yaml

#load the csv file
from google.colab import files
uploaded = files.upload()

#%%

import yaml
import json

import pandas as pd
df = pd.read_csv("validate.csv")

data_types = {
    "empty" : bool,
    "required" : bool,
    "minlength" : int,
    "maxlength" : int,
    "allowed" : "array",
}

def _convert(x, field_name):
    dtype = data_types.get(field_name)
    if dtype is None:
        return x
    if isinstance(dtype, str):
        if dtype == "array" and isinstance(x, str):
            return yaml.safe_load(x)
        return x
    try:
        return dtype(x)
    except:
        return None

# Delete all not required columns
del_columns = ["item", "versionStart", "versionEnd", "tableName", "variableName", "description_en", 'empty']
df = df.drop(del_columns, axis=1)

# Convert to dictionary
d = { row["tableVariableName"] : {f:_convert(row[f], f) for f in row.dropna().index if not pd.isna(row[f])} for _, row in df.iterrows()}
for item in d.values():
    del item["tableVariableName"]

# Dump to file
#with open("out.json", "w") as f:
    #json.dump(d, f, indent=4)

#loading into cerberus

schema = d 

print(schema)

#testing for schema error
v = Validator(schema)
#document = {'siteID': 'Ottawa-1'}
#v = Validator(document, schema)
#v = Validator(schema)
#v.validate()
#print(document)
#v.validate(document, schema)

#loading a test document 

document = {'siteSiteID': 'Ottawa-1'}

#validating the document

#v = Validator(document, schema)
#v.validate(document, schema)
#v.validate()

#checking/return errors to the user 

#v.errors()
