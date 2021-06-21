# Aim/Objective
 
The purpose of the Ottawa Data Model (ODM) is to create an open science structure which can be used as a guideline for future models which promote data sharing. 
 
 
# Introduction
 
The validation.csv worksheet contains the details for the variables described in v.1.2 in the Ottawa Data Model (ODM). Information from the validation.csv worksheet is used to auto-generate a set of rules (schema) using the Cerberus package to validate the COVID-19 wastewater data provided from laboratories across Canada. The main objective is to create a human readable, machine-actionable worksheet which can be updated to reflect changes within the data validation process in the ODM. The worksheet is in a wide table format, which allows users to easily insert changes to the validation schema if needed. 
 
# Structure of Validate.csv
 
_Rows_
 
The rows in validation.csv contain the variables which need to be validated according to guidelines provided by the Ministry of the Environment, Conservation and Parks (MECP). Each individual variable has specific validation criteria which needs to be adhered to in order to be considered “valid”.


_Columns_
 
The following columns are listed in validation.csv. The columns specify either the name of the function within the Cerberus package or provide description towards for the variable
- `item:` determines what type of entity is being manipulated
- `versionStart:` the starting version number of the Ottawa Data Model
- `versionEnd:` the current version number of the Ottawa Data Model
- `tableName:` the table where the variable resides in
- `variableName:` the name of the variable which is being validated
- `description_en:` description of the variable in the English
- `allow_unknown:` allow variables that are not defined in the ODM dictionary. The ODM default validation schema will allow user-generated variables and types that are not in the ODM dictionary. A count of unknown variables will be returned to the user as a warning. Implementations of the ODM may wish to restrict variables to the ODM schema, in which case users can extend or modify the validation schema for their purposes. The extension should be clearly identified as not part of the ODM schema.
- `allowed:` define a set of items within the validation schema which will allow the user to pre-approve a specific list of items. If the input exists within the allowable list, then no errors should arise after entering the data. If an entry is not within the predefined list, an error will be thrown, showing the user the `unallowed` value. Instances of this function could be applied to all categories in `variableCategory.csv`. Examples include WWMeasure `type` such as `covN1`, `conN2` etc.
- `allof:` if an entry has dependencies that need to be met, this will verify all its conditions prior to output whether it is acceptable. If all conditions have not been fulfilled, the user will be notified where the error is located, and then can be changed appropriately. Examples include: applied to specifying character limits for the 'notes' in the ODM.
- `anyof:`  if an entry has some conditions which need to be met, then the entry can be validated. If a certain number of conditions have not been verified, the user will be shown where the error lies, and can be amended if necessary. Examples of this implementation would be if the user has correctly inputted the site where wastewater sample has been 
- `check_with:` validates the entry by its ability to call other functions. If the data is not valid under the criteria of the external function, then the user will receive an error message specifying the issue. An example of this function applied to the ODM would be to determine if an email address is valid.
- `contains:`  is used to verify if there are any missing entries within the document. Compare the schema and the file to determine if the entries contain all the necessary items. If the document does not contain the necessary items, then a user will be prompted with an error to ensure all entries are filled/contain the correct inputs. This could be applied to scanning whether the inputted email address contains the “@” character. 
- `dependencies:` if adequate mapping is provided in the schema, dependencies are extremely useful when trying to ensure that entries/inputs are in the correct format/and are within the bounds in the prespecified rules. If the input does not satisfy all the parameters, an error will be reflected to the user indicating that the field depends on other values, meaning that they may need to be modified. Within the ODM, several variables within the WWMeasure table contain dependencies, such as the assayMethodID (sourced from the AssayMethod table).
- `empty:` used to specify whether an entry is mandatory. If set to false, then the parameter must be filled. An error detailed that this variable is not allowed to be empty will be thrown to the user. Examples of this implementation within the ODM can be seen through variables such as “typeOther” where if “type” has an input, typeOther can remain empty.
- `forbidden:` allows specific criteria defined within the schema to be excluded from the data. If an input is within the pre-defined forbidden list for a certain variable, the user will receive an error specifying that the item is forbidden. As the model is evolving, this could be used to filter out dated inputs, such as inputting a date prior to 2020-01-01.
- `items:` creates a list of items whose size depends on the amount of allowed predefined entries. Each index within the list has a pre-specified data-type which must match the input. When a list is inputted, each entry within the list is cross-referenced to determine if all data types are in the appropriate format. If a list of only “characters” is desired, this implementation could be used. 
- `keysrules:` takes a list of key,value pairs with their desired data type. The input must match the definitions within the schema. If the correct data types are not inputted, then the user will receive error warnings to change the datatype. 
- `min:` specifies the minimum and maximum range of values for an input. This function is designed for floats, doubles or integers, and can be used to set boundaries for variables within the ODM (eg: geoLong/geoLat). 
- `max:` specifies the minimum and maximum range of values for an input. This function is designed for floats, doubles or integers, and can be used to set boundaries for variables within the ODM (eg: geoLong/geoLat). 
- `minlength:` specifies the minimum and maximum values for lists. 
- `noneof:` returns an error if all entries do not meet any of the criteria. 
- `nullable:` specifies whether an entry is allowed to be blank. This would be implemented for variables such as “typeOther” which can be blank under the correct circumstances. 
- `noneof:` if the entries fulfills exactly one of the specifications in the schema, then the input will be validated.
- `regex:` this function validates only string values which match the pre-specified format in the schema. This can be extremely useful when trying to validate email addresses, and ensure they are in the correct format
- `required:`  used to specify whether a variable requires an entry. Can be applied to all variables within the ODM.
- `type:` type the data types allowed for the key values.
- `coerce:` ensuring the variables are in the same type 
- `error:` error value associated if data is not entered correctly
 
# Naming Convention
 
Variables listed in the ODM will follow the pascal case format. 
 
 
# Allowable Values
 
The Validate.csv schema supports strings, integers, and floats. It currently does not support the character data-type.
 
# Formatting
 
The Validate.csv file is in the wide-table format. The wide table format was selected for the purpose of ensuring the highest degree of human readability. 
