# Validation specifications

Data validation ensures consistent and accurate use of the ODM. Data cleaning and transformation alter the data structure or content to a consistent format. Data validation allows users to check whether their data meets the ODM format by providing a report on what variables and entries meet or do not meet the ODM format. The emphasis is on providing guidance and support. There can be warnings and errors in the report; however, where possible, errors should be as few as possible. An example of a warning is when an email does not contain an ‘@’ symbol. An error is when a unique identifier is not repeated (it is not unique). 

Data transformation also merges and creates data in the two ODM formats. “Long” data format with one row in a data table represents each measurement and “wide” data format with one row for each sample day. Users also hold ODM in different formats such as Excel tables, SQL databases and R or Python data frames. Transformations assist in moving data into different, commonly used formats. Data validation can also assess whether the data meets quality assurance metrics, such as applying outlier detection and only reporting values above level of detection. However, quality assessment can be performed at different steps of the data life-cycle.

At the core of data validation and cleaning is a table that lists different rules. Rules include, for example, data types (e.g. integer, string), ranges (e.g. number between 0 and 100), uniqueness (e.g. sample ID is not repeated). The rules are clearly stated, meaning they are easily understood, and they can be added by users and working groups who develop the ODM. 

The rules are also machine-actionable using an open format. Data validation needs to occur for several different uses of the ODM. Laboratories or people who generate ODM-compliant data need to ensure the data is consistent for their uses. Data should be verified before uploading to data repositories. A data analyst needs to verify and clean data before analyses. Different settings can reuse scripts or programs to validate and clean data. See 6.1 for more details.

Context
Data validation must be performed for/by a range of data custodians. Many different data custodians generate wastewater surveillance data, including academic testing labs, national and commercial testing labs, municipal wastewater utilities and public health. These data custodians require different types of support to validate the data they generate in ODM format.

Data validation must be performed on different platforms. Data custodians have many different data systems. Most academic testing labs use Excel. Many data custodians do not use open programming software such as R or Python. ArcGIS and Microsoft 365 are used by key stakeholders. An example of a platform-specific validation is missing data. The ODM format for missing data is to leave the value blank. However, different program platforms specific format for missing data to facilitate analyses. Missing data formats vary considerably between platforms. Missing data can also be coded in different formats within a programming language. The use of platform-specific missing data tokens allows users of the platform to use a consistent missing data format.

Data validation must be performed for ODM users with a range of analytic skills and knowledge. The extent of data validation for most users is limited, and there are considerable inconsistencies in how data is currently recorded. Many data custodians do not have formal data science training or capacity. 

Data validation is required at different stages of the data life cycle, including:
during generation of data within the lab and environments of data custodian;
prior and during transmission from data custodians to data repositories;
within data repositories;
when data is transferred from one data repository to another;
before data analyses by epidemiologists and modellers. 

Validation processes
order - The order of  execution of the validation steps may be important. Validation for some items may need to occur before other items.
items - There are several different items that require validation. Items include: tables, variables, and specific value range for example, validation for a range of dates.
platform - Validation may differ depending on the platform. For example, Excel requires implementation using Excel conditional rules, whereas ArcGIS, Tableau and other platforms allow validation using application-specific applications and also open languages.
role - there may be a specific role(s), purpose or timing of a validation. If so, it may be helpful to define the role. For example, a validation rule may only be meaningful for data entry. In this situation, the role can be identified.
language - The implementation process should support different programming languages if required. For example, the Excel templates will include data validation where possible. However, not all validation steps can be included in Excel, and data validation occurs in multiple steps. Therefore, all validation steps are also able to be executed in Python. 
description - Each validation step should include a clear human-readable description in English and French. 
required - Validation should indicate whether a variable is required.
dependencies - Whether there are dependencies on other variables or validation steps, in addition to the order of validation.
warning - The number and type of warnings should be presented in human-readable form. Warnings should be presented in different formats, platforms, programs, etc.
errors  - The number and type of errors should be presented in human-readable form. Errors should be presented in different formats, platforms, programs, etc.
normalization (transformation) - iI values can be transformed, then this should occur. For example, data submitted with a non-SI unit (e.g., liters/hour) could be converted to its SI equivalent (m3/s)  Variable mapping should be considered during variable mapping and not during validation, despite recognizing that mapping could be performed using normalization methods. 
coercion - If values can be coerced, then this should happen. i.e. integer as text should be coerced to numbers and a warning issued that this occurred.
version-specific - Validation should indicate what version of the ODM the step is applicable for. Provisions for coercion and/or transforming old versions variables, types, and coercion of values to the most recent version. Warnings and errors should be issued, as appropriate. 
wide table - Validation of the  wide table should be supported. Derived variable names should be validated, if possible. 
extensible - Wastewater-based surveillance is rapidly developing. The validation process should be customizable and extensible for new processes not identified in this list of validation processes.

Validation schema and rules
A validation schema is a set of rules or validation dictionaries. The ODM will create the main schema that is updated for each version. However, the schema method can be used by ODM users to extend or develop schemas for their specific applications. ODM will provide a means for sharing schema, similar to the means for sharing input templates.
The list of validation rules below is drawn from the Cerberus Python validation library. Consideration should be given to using the Cerberus package or similar ruleset functions. ODM extends packages such as Cerberus to allow non-data scientists to develop validation sets using simple (CSV) tables. As well, rule sets should be incorporated into Excel where possible.

By defining a validation schema for the ODM, we will be able to create and maintain a consistent universal data entry format.

allow_unknown - allow variables that are not defined in the ODM dictionary. The ODM default validation schema will allow user-generated variables and types that are not in the ODM dictionary. A count of unknown variables will be returned to the user as a warning. Implementations of the ODM may wish to restrict variables to the ODM schema, in which case users can extend or modify the validation schema for their purposes. The extension should be clearly identified as not part of the ODM schema.

allowed - define a set of items within the validation schema which will allow the user to pre-approve a specific list of items. If the input exists within the allowable list, then no errors should arise after entering the data. If an entry is not within the predefined list, an error will be thrown, showing the user the “unallowed” value. Instances of this function could be applied to all categories in `variableCategory.csv`. Examples include WWMeasure `type` such as `covN1`, `conN2` etc.

allof - if an entry has dependencies that need to be met, this would verify all it’s conditions prior to output whether it is acceptable. If all conditions have not been fulfilled, the user will be notified where the error is located, and then can be changed appropriately. Examples include:applied to specifying character limits for the “notes” in the ODM.

anyof -  if an entry has some conditions which need to be met, then the entry can be validated. If a certain number of conditions have not been verified, the user will be shown where the error lies, and can be amended if necessary. Examples of this implementation would be if the user has correctly inputted the site where wastewater sample has been collected (type-variable) and is able to leave the “typeOther” variable empty for this table. 

check_with - validates the entry by its ability to call other functions. If the data is not valid under the criteria of the external function, then the user will receive an error message specifying the issue. An example of this function applied to the ODM would be to determine if an email address is valid. 

contains - is used to verify if there are any missing entries within the document. Compare the schema and the file to determine if the entries contain all the necessary items. If the document does not contain the necessary items, then a user will be prompted with an error to ensure all entries are filled/contain the correct inputs. This could be applied to scanning whether the inputted email address contains the “@” character.

dependencies - if adequate mapping is provided in the schema, dependencies are extremely useful when trying to ensure that entries/inputs are in the correct format/and are within the bounds in the prespecified rules. If the input does not satisfy all the parameters, an error will be reflected to the user indicating that the field depends on other values, meaning that they may need to be modified. Within the ODM, several variables within the WWMeasure table contain dependencies, such as the assayMethodID (sourced from the AssayMethod table).

empty - used to specify whether an entry is mandatory. If set to false, then the parameter must be filled. An error detailed that this variable is not allowed to be empty will be thrown to the user. Examples of this implementation within the ODM can be seen through variables such as “typeOther” where if “type” has an input, typeOther can remain empty. 

excludes - allows for specific variables when defined in the schema to ignore other fields. A use case would arise if variables overlapped within the ODM.

forbidden - allows specific criteria defined within the schema to be excluded from the data. If an input is within the pre-defined forbidden list for a certain variable, the user will receive an error specifying that the item is forbidden. As the model is evolving, this could be used to filter out dated inputs, such as inputting a date prior to 2020-01-01.

items - creates a list of items whose size depends on the amount of allowed predefined entries. Each index within the list has a pre-specified data-type which must match the input. When a list is inputted, each entry within the list is cross-referenced to determine if all data types are in the appropriate format. If a list of only “characters” is desired, this implementation could be used. 
 
keysrules - takes a list of key,value pairs with their desired data type. The input must match the definitions within the schema. If the correct data types are not inputted, then the user will receive error warnings to change the datatype.  

min, max - specifies the minimum and maximum range of values for an input. This function is designed for floats, doubles or integers, and can be used to set boundaries for variables within the ODM (eg: geoLong/geoLat). 

minlength, maxlength - specifies the minimum and maximum values for lists. 

noneof - returns an error if all entries do not meet any of the criteria. 

nullable - specifies whether an entry is allowed to be blank. This would be implemented for variables such as “typeOther” which can be blank under the correct circumstances. 

oneof - if the entries fulfills exactly one of the specifications in the schema, then the input will be validated. 

regex - this function validates only string values which match the pre-specified format in the schema. This can be extremely useful when trying to validate email addresses, and ensure they are in the correct format

required - used to specify whether a variable requires an entry. Can be applied to all variables within the ODM.

schema (dict) - defining the validation rules in a key-value format.

schema (list) - defining the validation rules in a list format.

type - the data types allowed for the key values.

valuesrules - validates the key.

Validation warnings and errors

Warnings are returned to a user when the data does not conform to a validation rule but the data can either be coerced or normalized to the specified rule or the deviation is not a requirement for ODM compliant data. Whenever possible, warnings will be used instead of errors. For example, a warning is issued when:
the variable type is an integer, but the value is a text that can be coerced to an integer. i.e. “1” → 1.
The text length exceeds maximum allowable, in which case it will be truncated to the maximum length.

Errors are returned to a user when the data does not conform to a validation rule and the data cannot be coerced or normalized to the specified rule. An example is required data that is missing. 

Both warnings and errors will include a message that includes:
Why the warning or error occurred.
How to correct the warning or error.

Normalization or transformation

Normalization is the process of modifying data to ODM format. 
If the dataset is not in the desired “long” format, a transformation function will be applied to reformat the table which can then be validated using the appropriate rules/specifications. If data types are not in the correct format, then data-types will be converted into the correct data types, as reflected in the validation schema. If there is any missing data, then warnings will be sent to the user, to rectify this issue. 
