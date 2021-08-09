# Aim/Objective:

The purpose of the ODM is to support wastewater-based surveillance and epidemiology by facilitating the collection, standardization, and transparency of data by providing a more harmonized ODM data format to share data between different data curators and data repositories. 

The end objective of data sharing is to have a function that can take in the user inputs in the form of a schema with predefined rules and the user data and filter the data based on the rules in the schema and output back the data to the user which is filtered and is ready to be used with specific organizations that user wants to share their data with. This is implement using python code.

# Features

This section will go over the high level features that will need to be implemented

* The data custodian should be able to define all the sharing rules in a CSV file. A standard schema for defining the rules will be developed.
* The schema should allow the data custodians to define the organizations that each rule pertains to. For example, a certain rule may be applicable only to the Public Health Agency of Canada (PHAC) while another rule may be applicable to not only the PHAC but also to Ottawa Public Health.
* The schema should allow data custodians to define rules that applies to rows or to columns. For example, a rule can be made to exclude all the rows from the `Sample` table or to exclude the `type` column from the `Sample` table.
* Rules can be made within the context of an entire table, to a column that may be present in more than one table or to a column specific to a table.
* The rules can be both inclusive or exclusive. For example, a rule can be defined to include all the rows in a table or to exclude rows with certain values for a variable.
* Rules can be combined to form more powerful conditions using logical operators. For example, exclude all rows with `contactEmail` equal to "john.doe@email.com" AND `contactName` equal to "John Doe". Current supported logical operators are `AND` and `OR`.
* The data custodian will be returned a report at the end which will provide details about how many rows were filtered from the data or the individuals and the reasons why they were removed.
* The data custodian will be able to define licenses on how the data can be used by specific users. In many jurisdictions, this is defined in a detailed data-sharing agreement (DSA). The DSA can be short simply referencing a license type, or they can be many pages identifying specifically who can use the data and for what purpose and what will be the data destruction protocols, etc. The license feature or sharing rule will be a free text field and the text field may reference a longer document.
* The implementation should take into account the relationship between the different tables as defined in the ODM. For example, removing a row with siteID 1 from the site table, should also remove all samples with siteID 1 from the samples table. All nested relationships should also be taken care of. The relationships between the tables can be seen [here](https://github.com/Big-Life-Lab/ODM/blob/main/metadata_en.md).
* A python function that implements these rules should be built.




