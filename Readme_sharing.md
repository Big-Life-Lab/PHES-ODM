# **Aim/ Objective:**

### The purpose of the ODM is to support wastewater-based surveillance and epidemiology by facilitating the collection, standardization, and transparency of data by providing a more harmonized ODM data format to share data between different data curators and data repositories.

## **Sharing Specifications:**

### The ODM emphasizes open and FAIR data (Findable, Accessible, Interoperable, and Re-usable). 
### Data sharing allows the different data curators to selectively share their data with different data repositories based on different selection rules. This allows them to share only those variables in their data that they intend to share with a specific person or organization or a data repository. A shared_data.csv file is created that specifies these rules that allows selective data sharing. An example of a data sharing rule would be what variables within each table the data custodian wishes to share with a specific access group or a data repository. One of the access groups that the data custodian may wish to share the data with is the Public health agency (PHAC). 

### Data custodian will provide the data and the csv schema with predefined rules set by data custodian. A Python script will run at the back end that will take in both the data and the csv schema and convert the csv schema into a json object which will be used to filter the data in a Pandas dataframe using the features of Pandas library in python for data manipulation.

## **Context**

### The data sharing takes place between the different data custodians that generates waste water surveilance data and the different organizations or data respositories such as Public health agency, Provincial health authorities, Local health authorities, all organizations, with Quebec site, waste water database and with the general public. The data custodian can share only specific variables with the specific data repositories by providing the rules in shared_data.csv file.

### Data custodians work with their on different platforms. The goal is to proivde them a tool that can help them share their data based on the platform they use to store their data. Most data custodians use Excel to store data. Some are also using ArcGIS and Tableau. Using a python script that can accept data based on different platforms that data custodians might use to enter the data can provide a tool and common platform to share ODM data.

### Data will be shared by the data custodian using a web application tool where the data custodian can enter in their data and the CSV schema with their own predefined rules set for different data repositories. The back end python script will allow them to filter the data based on their provided csv schema and output back the final dataset that is ready to be shared. Pandas library in python is used for the filtration of selective variables and conditional rules that the data custodian provides.

### Data sharing will take place once the data is in the ODM compliant format after it has gone through the validation process and has been cleaned.

## **Sharing processes:**

### **items -** There are several different items such as tables, variable names that will have different sharing properties or rules applied to them to selectively choose what the custodian might want to share with a particular data repository.

### **range -** The range can be used as a data sharing property or sharing rule that allows data custodian to selectively choose range of data values to share for specific variables in their data. As an example, the data custodian may not want to share their data for the entire time range and will only want to enter a specific timeframe for which the data can be shared. 

### **who -** The sharing property or the rule can identify who the data is intended for. Different data repositories or organizations or public or a person can have different access level to the data as per the requirements of the data custodian. The different access groups will be identified through these rules, **shared_with_access_groups** that will be part of the schema in the **shared_data.csv** file. When the data custodian logs onto the web portal to use ODM tool for data sharing, they will have options to select for the access groups they wish to share the data with.

### **description -** There will be a description for each sharing property or rule that will specify the license or details how the data or specific data elements shared with a specific recipient can or can not be used.

### **extensible -** Since the waste water surveilance is rapidly developing, it will be necessary to make the sharing process more adaptable and extensible for growing changes and processes that allows users to add more variables and rules in the schema for sharing.

## **Sharing schema and rules**

### The sharing schema defines the rules that will be used to selectively filter the data for the data custodians who want to share only specific part of their data with a specific data repository. The ODM will create the main schema in the **shared_data.csv** file which will be updated in each version. However, the ODM users will be able to extend or develop the schemas for their own specific applications.

### Pandas is a library in python which provides features to do extensive data manipulations including conditional filtration based on different rules. These rules are provided by the data custodian in **shared_data.csv** file which is converted into a json python object which is then used with Pandas library to select variables based on those provided rules. Having the schema for sharing in a CSV format allows non-data scientists to develop their specific data sharing specifications or rules.

### A sharing schema allows ODM users to provide consistent format for sharing data that can be used to filter data based on their specifications.

### Following are the rules in the version v1.2 that are part of **shared_data.csv** file:

### **is_excluded:** This rule will allow the user to exclude any variable from their data that they do not wish to share with any data repository or organizations at all. The rule will accept values as True/ False based on whether the variable can be shared or not shared.

### **shared_with_Public:** This rule will allow the user to exclude any variable that the data custodian may not wish to share with the general public based on True/ False values specified for that rule in the sharing schema.

### **shared_with_PHAC:** This rule will allow the user to exclude any variable or table that the user does not want to share with the Public health agency by specifying True/ False values in the sharing schema.

### **shared_with_Local_HA:** This rule will allow the user to exclude any variable or table that the user does not want to share with all the Local health authorities which will be specified using the True/ False conditions in the sharing schema.

### **shared_with_Prov_HA:** This rule will allow the user to exclude any variable or table that the user does not intend to share with the Provincial health authorities based on True/ False values that the user provides in the sharing schema.

### **shared_with_Quebec_site:** This rule will filter data or select variables that data custodian wants to share with the Quebec site based on True/ False values.

### **shared_with_Ontario_WSI:** This rule will allow the user to filter data and select variables or tables that they wish to share with Ontario waste water system. Again, they will need to provide True/ False values in the sharing CSV schema for each variable for that rule.

### **shared_with_Canadian_WWS_database:** This rule allows the user to filter the variables or tales that they do not wish to share with the Canadian Waste water database. True/ False values will be provided by the user in the sharing schema for each variable.

### **lower_range_Public:** This rule allows the user to limit the range of data shared for specific variables that user may not want to share with the general public. The lower range values specifies the lower value of the range of data that user wants to share with specific data repository or in this case it will be public. An example will be range of dates that user wants to share. The lower bound of the range for the date variable is provided in this rule.

### **upper_range_Public:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the general public.

### **lower_range_PHAC:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Public health agency.

### **upper_range_PHAC:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Public health agency.

### **lower_range_Local:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Local health authorities.

### **upper_range_Local:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Local health authorities.

### **lower_range_Prov:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Provincial health authorities.

### **upper_range_Prov:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Provincial health authorities.

### **lower_range_Ontario_WSI:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Ontario waste water system.

### **upper_range_Ontario_WSI:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Ontario waste water system.

### **lower_range_Can_WWDB:** This rules provides the lower bound of the range of values that the data custodian wants to share for the specific variables with the Canadian waste water database sytem.

### **upper_range_Can_WWDB:** This rules provides the upper bound of the range of values that the data custodian wants to share for the specific variables with the Canadian waste water database system.

### **description_Public:** This rule specifies the permissions and licenses for the specific variables regarding how the public that have access to the data can use it.

### **description_PHAC:** This rule specifies the permissions and licenses for the specific variables regarding how the public health agency that have access to the data can use it.

### **description_Local:** This rule specifies the permissions and licenses for the specific variables regarding how the Local health authorities that have access to the data can use it.

### **description_WSI:** This rule specifies the permissions and licenses for the specific variables regarding how the Waste water surveilance systems that have access to the data can use it.

### **description_Can_WWDB:** This rule specifies the permissions and licenses for the specific variables regarding how the Canadian waste water surveilance database that have access to the data can use it.

### The data, filtered out using the above schema rules and the python script in back end that runs the Pandas package, is returned back to the user in an Excel spreadsheet. 