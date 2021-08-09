# Aim/Objective:

The purpose of the ODM is to support wastewater-based surveillance and epidemiology by facilitating the collection, standardization, and transparency of data by providing a more harmonized ODM data format to share data between different data curators and data repositories. 

The end objective of data sharing is to have a function that can take in the user inputs in the form of a schema with predefined rules and the user data and filter the data based on the rules in the schema and output back the data to the user which is filtered and is ready to be used with specific organizations that user wants to share their data with. This is implement using python code.

# Features

This section will go over the high level features that will need to be implemented

* The data custodian should be able to define all the sharing rules in a CSV file. A standard schema for defining the rules will be developed.
* The schema should allow the data custodians to define the organizations that each rule pertains to. For example, a certain rule may be applicable only to the Public Health Agency of Canada (PHAC) while another rule may be applicable to not only the PHAC but also to Ottawa Public Health.
* The schema should allow the data custodians to define rules for filtering entire tables. For example, the data custodian may decide that they do not want the data from the Polygon table to be shared.
* The schema should allow the data custodians to define rules for filtering variables from certain tables. For example, a rule could be defined for removing the `contactName` and `contactEmail` variables from the `Reporter` table.
* The schema should allow the data custodians to define rules for filtering out rows that contains variables values that should not be shared with organizations. For example, a rule could be defined to remove all rows from the `WWMeasure` table whose `analysisData` is older than a defined date.
* The data custodian will be able to define the inclusion and exclusion rules.
* The data custodian can filter multiple variables for specific values or multiple values for same variables in the dataset which is same as using 'AND' clause to filter data.
* The data custodian will be returned a report at the end which will provide details about how many rows were filtered from the data or the individuals and the reasons why they were removed.
* The data custodian will be able to define licenses on how the data can be used by specific users. In many jurisdictions, this is defined in a detailed data-sharing agreement (DSA). DSA can be short simply referencing a license type, or they can be many pages identifying specifically who can use the data and for what purpose and what will be the data destruction protocols, etc. The license feature or sharing rule will be a free text field and the text field may reference a longer document.
* The implementation should take into account the relationship between the different tables as defined in the ODM. For example, removing a row with siteID 1 from the site table, should also remove all samples with siteID 1 from the samples table. All nested relationships should also be taken care of. An image showing these relationships is linked below:
![table relations](table_relations.jpg)
* A python function that implements these rules should be built.




