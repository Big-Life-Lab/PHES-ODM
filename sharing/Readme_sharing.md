# Aim/ Objective:

The purpose of the ODM is to support wastewater-based surveillance and epidemiology by facilitating the collection, standardization, and transparency of data by providing a more harmonized ODM data format to share data between different data curators and data repositories. 

The end objective of data sharing is to have a function that can take in the user inputs in the form of CSV schema with predefined rules and the user data and filter the data based on the rules in the CSV schema and output back an excel spreadsheet to the user with filtered data that is ready to be used with specific organizations that user wants to share their data with. This is implement using python code.

## Sharing Specifications:

## Milestones

This section will go over the high level features that will need to be implemented

### List of features that will be part of the sharing functionality:

- The data custodian can request to share data with only certain groups of people or organizations. Such a feature can be implemented through the use of different access groups defined within the csv schema. There will be a function that selectively allows sharing data with only specific access groups.

- The data custodian can also request to share only certain information with certain groups of people or with everyone that is they can selectively choose to share only certain variables with the certain access groups or with every one in general.  An example of this could be that the data custodian does not wish to share their name, email, and phone information. They will be able to exclude these variables from the final dataframe that will be shared. A function that has that filtration capability will be able to select variables that users chooses to share through the rules defined in csv schema.

- The data custodian can request to share only a specific range of values with different organizations or with public. These ranges can be specified for different variables in the table. It is not necessary to specify the range for each and every variable. The data custodian can specify the range in the csv schema file for specific variables only and the python function will be able to filter the data based on the range provided for the particular variable or variables.

- The data custodian can also selectively choose only the data from a table where only specific values for a variable are allowed or may not be allowed in the final dataframe. This is also achieved by providing the values for setting the filters in csv sharing schema.

- An important part about sharing the data will be to ensure that the primary key and foreign key relationships between certain tables are maintained. The data filtered in one of the tables that has a primary key- foreign key relation with another table should also be filtered in the other tables.

- An example of above dependency on primary and foreign key relationship will be Sample table and Waste water measure table (WWmeasure) where the sample id in the sample table must match the sample id in the WWmeasure table. Any sample that is not present in the sample table should not exist in the WWmeasure table as well in the final output data. 

- These dependencies can further be nested down to other tables. An example will be sample table and site table. The site id in site table must match site id in sample table. After making an inner join on the site and sample table, a further dependency is matched between sample and WWmeasure table as above based on sample id. This basically helps to filter out results in WWmeasure table that has a site id attached to it.

- The data custodian should be able to define all the sharing rules in a CSV file. A standard schema for defining the rules will be developed.

- The schema should allow the data custodians to define the organizations that each rule pertains to. For example, a certain rule may be applicable only to the Public Health Agency of Canada (PHAC) while another rule may be applicable to not only the PHAC but also to Ottawa Public Health.

- The schema should allow the data custodians to define rules for filtering entire tables. For example, the data custodian may decide that they do not want the data from the Polygon table to be shared. 

- The schema should allow the data custodians to define rules for filtering variables from certain tables. For example, a rule could be defined for removing the `contactName` and `contactEmail` variables from the `Reporter` table.

- The schema should allow the data custodians to define rules for filtering out rows that contains variables values that should not be shared with organizations. For example, a rule could be defined to remove all rows from the `WWMeasure` table whose `analysisData` is older than a defined date. This criteria for filteration will be met by the range sharing property which is part of the schema.

- The data custodian will be able to define the inclusion and exclusion rules.

- The data custodian can filter multiple variables for specific values or multiple values for same variables in the dataset which is same as using 'AND' clause to filter data.

- The data custodian will be returned a report at the end which will provide details about how many rows were filtered from the data or the individuals and the reasons why they were removed.

- The implementation should take into account the relationship between the different tables as defined in the ODM. For example, removing a row with siteID 1 from the site table, should also remove all samples with siteID 1 from the samples table. All nested relationships should also be taken care of. An image showing these relationships is linked below:

![table relations](table_relations.jpg)

### How the features will be implemented?

The ODM emphasizes open and FAIR data (Findable, Accessible, Interoperable, and Re-usable). 

### Context

- The data sharing takes place between the different data custodians that generates waste water surveilance data and the different organizations or data respositories such as Public health agency, Provincial health authorities, Local health authorities, all organizations, with Quebec site, waste water database and with the general public. The data custodian can share only specific variables with the specific data repositories by providing the rules in shared_data.csv file.

- Data custodians work with their data on different platforms. The goal is to proivde them a tool that can help them share their data based on the platform they use to store their data. Most data custodians use Excel to store data. Some are also using ArcGIS and Tableau. Using a python script that can accept data based on different platforms that data custodians might use to enter the data can provide a tool and common platform to share ODM data. Alternatively, the data custodians may choose to implement the sharing rules in their own data system and not use the ODM method.

- Data will be shared by the data custodian using a web application tool where the data custodian can enter in their data and the CSV schema with their own predefined rules set for different data repositories or access groups. The back end python script will allow them to filter the data based on their provided csv schema and output back the final dataset that is ready to be shared. Pandas library in python is used for the filtration of selective variables and conditional rules that the data custodian provides. The data custodian will have the option to provide the values of tables that they wish to filter data for and receive as an output and the python script will automatically filter data for those tables based on the rules defined for them. The data custodian will also have to provide the names of the access groups in the form which must be part of the sharing property or rule for the particular access group in **shared_data.csv** file. An example will be Public Health Agency (PHAC) has the sharing property **sharing_with_PHAC** in the CSV schema file. The data custodian will need to ensure that the access group name they enter into the form contains the last part of the name of the sharing property. Therefore, in this case they might use **PHAC** as the access group name that they wish to get the data filtered for. The data custodian will have the option to provide multiple access groups in the form to fetch data for if they are fetching the same tables for all of the access groups by filling the form only once. If they want to filter different datasets/ tables for different access groups, then they will need to enter the information separately for each access groups by filling the same form multiple times on the web application tool.

- Data sharing will take place once the data is in the ODM compliant format after it has gone through the validation process and has been cleaned.

### Sharing processes:

- **items -** There are several different items such as tables, variable names that will have different sharing properties or rules applied to them to selectively choose what the custodian might want to share with a particular data repository.

- **range -** The range can be used as a data sharing property or sharing rule that allows data custodian to selectively choose range of data values to share for specific variables in their data. As an example, the data custodian may not want to share their data for the entire time range and will only want to enter a specific timeframe for which the data can be shared. 

- **who -** The sharing property or the rule can identify who the data is intended for. Different data repositories or organizations or public or a person can have different access level to the data as per the requirements of the data custodian. The different access groups will be identified through these rules, **shared_with_access_groups** that will be part of the schema in the **shared_data.csv** file. When the data custodian logs onto the web portal to use ODM tool for data sharing, they will have options to select for the access groups they wish to share the data with.

- **description -** There will be a description for each sharing property or rule that will specify the license or permissions on how the data or specific data elements shared with a specific recipient can or can not be used.

- **extensible -** Since the waste water surveilance is rapidly developing, it will be necessary to make the sharing process more adaptable and extensible for growing changes and processes that allows users to add more variables and rules in the schema for sharing.

### Sharing schema and rules

- The sharing schema defines the rules that will be used to selectively filter the data for the data custodians who want to share only specific part of their data with a specific data repository. The ODM will create the main schema in the **shared_data.csv** file which will be updated in each version. However, the ODM users will be able to extend or develop the schemas for their own specific applications.

- Pandas is a library in python which provides features to do extensive data manipulations including conditional filtration based on different rules. These rules are provided by the data custodian in **shared_data.csv** file which is converted into a json python object which is then used with Pandas library to select variables based on those provided rules. Having the schema for sharing in a CSV format allows non-data scientists to develop their specific data sharing specifications or rules.

- A sharing schema allows ODM users to provide consistent format for sharing data that can be used to filter data based on their specifications.

Following are the rules in the version v1.2 that are part of **shared_data.csv** file:

**is_excluded:** This rule will allow the user to exclude any variable from their data that they do not wish to share with any data repository or organizations at all. The rule will accept values as True/ False based on whether the variable can be shared or not shared.

**shared_with_Public:** This rule will allow the user to exclude any variable that the data custodian may not wish to share with the general public based on True/ False values specified for that rule in the sharing schema.

**shared_with_PHAC:** This rule will allow the user to exclude any variable or table that the user does not want to share with the Public health agency by specifying True/ False values in the sharing schema.

**shared_with_Local:** This rule will allow the user to exclude any variable or table that the user does not want to share with all the Local health authorities which will be specified using the True/ False conditions in the sharing schema.

**shared_with_Prov:** This rule will allow the user to exclude any variable or table that the user does not intend to share with the Provincial health authorities based on True/ False values that the user provides in the sharing schema.

**shared_with_Quebec:** This rule will filter data or select variables that data custodian wants to share with the Quebec site based on True/ False values.

**shared_with_OntarioWSI:** This rule will allow the user to filter data and select variables or tables that they wish to share with Ontario waste water system. Again, they will need to provide True/ False values in the sharing CSV schema for each variable for that rule.

**shared_with_CanadianWasteWaterDatabase:** This rule allows the user to filter the variables or tales that they do not wish to share with the Canadian Waste water database. True/ False values will be provided by the user in the sharing schema for each variable.

**lower_range_Public:** This rule allows the user to limit the range of data shared for specific variables that user may not want to share with the general public. The lower range values specifies the lower value of the range of data that user wants to share with specific data repository or in this case it will be public. An example will be range of dates that user wants to share. The lower bound of the range for the date variable is provided in this rule. Anything below this value will be filtered unless an upper bound is also specified. The values for the lower bound limit is provided in a list as the data custodian can choose several ranges of data to filter from the table such as 'analysisDate' values in the 'WWMeasure' table. An example will be to filter values between '2021-05-21 and 2021-07-21' and values between '2021-09-13 and 2021-12-31'. In such a case, there will be two lower bound limits and they will given in a list such as ['2021-05-21', '2021-09-13']. Any datetime values or character values must be provided in quotes whereas integer values should not be written in quotes. An example will be the 'value' variables for table 'WWMeasure'. The data custodian may choose to filter values between '2 and 4' and between '10' and '15'. They will provide that in range sharing property for the lower limit as a list again such as [2,10]. For integer values, quotes should not be used. If there is only a single lower bound limit, it should still be specified inside the list as a single entity. More than 1 lower bound limits should be separated by a comma as shown in example above. This property filters the rows of the data instead of removing the entire variable.

**upper_range_Public:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the general public. Anything above this value will be filtered unless a lower bound is also specified. The values for the upper bound limit is provided in a list as the data custodian can choose several ranges of data to filter from the table such as 'analysisDate' values in the 'WWMeasure' table. An example will be to filter values between '2021-05-21 and 2021-07-21' and values between '2021-09-13 and 2021-12-31'. In such a case, there will be two upper bound limits and they will given in a list such as ['2021-07-21', '2021-12-31']. Any datetime values or character values must be provided in quotes whereas integer values should not be written in quotes. An example will be the 'value' variables for table 'WWMeasure'. The data custodian may choose to filter values between '2 and 4' and between '10' and '15'. They will provide that in range sharing property as a list again such as [4,15]. For integer or numeric values, quotes should not be used. If there is only a single upper bound limit, it should still be specified inside the list as a single entity. More than 1 upper bound limits should be separated by a comma as shown in example above. This property filters the rows of the data instead of removing the entire variable.

**lower_range_PHAC:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Public health agency. Anything below this value will be filtered unless an upper bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**upper_range_PHAC:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Public health agency. Anything above this value will be filtered unless a lower bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**lower_range_Local:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Local health authorities. Anything below this value will be filtered unless an upper bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**upper_range_Local:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Local health authorities. Anything above this value will be filtered unless a lower bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**lower_range_Prov:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Provincial health authorities. Anything below this value will be filtered unless an upper bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**upper_range_Prov:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Provincial health authorities. Anything above this value will be filtered unless a lower bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**lower_range_OntarioWSI:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Ontario waste water system. Anything below this value will be filtered unless an upper bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**upper_range_OntarioWSI:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Ontario waste water system. Anything above this value will be filtered unless a lower bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**lower_range_CanadianWasteWaterDatabase:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Canadian waste water database sytem. Anything below this value will be filtered unless an upper bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**upper_range_CanadianWasteWaterDatabase:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Canadian waste water database system. Anything above this value will be filtered unless a lower bound is also specified. These limits must be specified inside a list just as explained above for range sharing property for public. Datetime and character values must be written inside quotes but not the integer or numeric variables.

**filter_value_Public:** This rule filters the data shared with Public based on the values that may not be allowed to share for specific variables. An example will be for site table, the site1 and site2 values for SiteID variable may not be shared with the general public. Such a rule allows for data to be filtered based on specific values of the variable. The values for this property must also go within a list. Even if there is only one single value to filter still it must be inside a list. An example will be to filter the 'Site' data on 'siteID' variable. If the data custodian does not want to share the data that has siteID value equal to 'siteT101' then they will enter it into the schema as a list ['siteT101']. All datetime and character variables will be specified in quotes whereas integer values will not be specified in quotes. A data custodian can give multiple values to filter the particular variable in the data such as ['siteT101', 'siteT102']. The multiple values are separated with a comma. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**filter_value_PHAC:** This rule filters the data shared with Public health agency on the values that may not be shared for specific variables. Just as in the filter property defined for the general public above, this filter property will also take values in a list with the same rules. Datetime and character values must be written inside quotes but not the integer or numeric variables.This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables. 

**filter_value_Local:** This rule filters the data shared with Local health authorities on the values that the data custodian may not wish to share for specific variables in their data. Just as in the filter property defined for the general public above, this filter property will also take values in a list. Datetime and character values must be written inside quotes but not the integer or numeric variables. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**filter_value_Prov:** This rule filters the data shared with Provincial health authorities on the values that the data custodian may not wish to share for specific variables in their data. Just as in the filter property defined for the general public above, this filter property will also take values in a list with the same rules. Datetime and character values must be written inside quotes but not the integer or numeric variables. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**filter_value_Quebec:** This rule filters the data shared with Quebec site on those values that the data custodian may not want to share for specific variables in their data. Just as in the filter property defined for the general public above, this filter property will also take values in a list with the same rules. Datetime and character values must be written inside quotes but not the integer or numeric variables. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**filter_value_OntarioWSI:** This rule filters the data shared with Ontario waste water surveilance system on the values that the data custodian may not wish to share for specific variables in their data. Just as in the filter property defined for the general public above, this filter property will also take values in a list with the same rules. Datetime and character values must be written inside quotes but not the integer or numeric variables. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**filter_value_CanadianWasteWaterDatabase:** This rule filters the data shared with Canadian waste water database on those values that the data custodian may not want to share for specific variables in their data. Just as in the filter property defined for the general public above, this filter property will also take values in a list with the same rules. Datetime and character values must be written inside quotes but not the integer or numeric variables. This rule instead of filtering out the whole variable or a column in the dataset filters out specific rows in the dataset based on the values of certain variables.

**description_Public:** This rule specifies the permissions and licenses for the specific variables regarding how the public that have access to the data can use it.

**description_PHAC:** This rule specifies the permissions and licenses for the specific variables regarding how the public health agency that have access to the data can use it.

**description_Local:** This rule specifies the permissions and licenses for the specific variables regarding how the Local health authorities that have access to the data can use it.

**description_OntarioWSI:** This rule specifies the permissions and licenses for the specific variables regarding how the Waste water surveilance systems that have access to the data can use it.

**description_CanadianWasteWaterDatabase:** This rule specifies the permissions and licenses for the specific variables regarding how the Canadian waste water surveilance database that have access to the data can use it.

The data, filtered out using the above schema rules and the python script in back end that runs the Pandas package, is returned back to the user in an Excel spreadsheet along with the report that list the number of rows removed, variables removed from each table and the reason for that.
