# **Aim/ Objective:**

### The purpose of the ODM is to support wastewater-based surveillance and epidemiology by facilitating the collection, standardization, and transparency of data by providing a more harmonized ODM data format to share data between different data curators and data repositories. 

### The end objective of data sharing is to have a function that can take in the user inputs in the form of CSV schema with predefined rules and the user data and filter the data based on the rules in the CSV schema and output back an excel spreadsheet to the user with filtered data that is ready to be used with specific organizations that user wants to share their data with. This is implement using python code.

## **Sharing Specifications:**

## **Milestones**

1. ### **List of features that will be part of the sharing functionality:**

- ### The data custodian can request to share data with only certain groups of people or organizations. Such a feature can be implemented through the use of different access groups defined within the csv schema. There will be a function that selectively allows sharing data with only specific access groups.

- ### The data custodian can also request to share only certain information with certain groups of people or with everyone such as selectively choose to share only certain variables with the certain access groups or with every one in general.  An example of this could be that the data custodian does not wish to share their name, email, and phone information. They will be able to exclude these variables from the final dataframe that will be shared. A function that has that filtration capability will be able to select variables that users chooses to share through the rules defined in csv schema.

- ### The data custodian can request to share only a specific range of values with different organizations or with public. These ranges can be specified for different variables in the table. It is not necessary to specify the range for each and every variable. The data custodian can specify the range in the csv schema file for specific variables only and the python function will be able to filter the data based on the range provided for the particular variable or variables.

- ### The data custodian can also selectively choose only the data from a table where only specific values for a variable are allowed or may not be allowed in the final dataframe. This is also achieved by providing the values for setting the filters in csv sharing schema.

- ### An important part about sharing the data will be to ensure that the primary key and foreign key relationships between certain tables are maintained. The data filtered in one of the tables that has a primary key- foreign key relation with another table should also be filtered in the other tables.

- ### An example of above dependency on primary and foreign key relationship will be Sample table and Waste water measure table (WWmeasure) where the sample id in the sample table must match the sample id in the WWmeasure table. Any sample that is not present in the sample table should not exist in the WWmeasure table as well in the final output data. 

- ### These dependencies can further be nested down to other tables. An example will be sample table and site table. The site id in site table must match site id in sample table. After making an inner join on the site and sample table, a further dependency is matched between sample and WWmeasure table as above based on sample id. This basically helps to filter out results in WWmeasure table that has a site id attached to it. 

- ### The image below defines these relationships.

![table relations](table_relations.jpg)


