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

### The ODM emphasizes open and FAIR data (Findable, Accessible, Interoperable, and Re-usable). 
### Data sharing allows the different data curators to selectively share their data with different data repositories based on different selection rules. This allows them to share only those variables in their data that they intend to share with a specific person or organization or a data repository. A shared_data.csv file is created that specifies these rules that allows selective data sharing. An example of a data sharing rule would be what variables within each table the data custodian wishes to share with a specific access group or a data repository. One of the access groups that the data custodian may wish to share the data with is the Public health agency (PHAC). 

### Data custodian will provide the data and the csv schema with predefined rules set by data custodian. A Python script will run at the back end that will take in both the data and the csv schema and convert the csv schema into a json object which will be used to filter the data in a Pandas dataframe using the features of Pandas library in python for data manipulation.

## **Context**

### The data sharing takes place between the different data custodians that generates waste water surveilance data and the different organizations or data respositories such as Public health agency, Provincial health authorities, Local health authorities, all organizations, with Quebec site, waste water database and with the general public. The data custodian can share only specific variables with the specific data repositories by providing the rules in shared_data.csv file.

### Data custodians work with their data on different platforms. The goal is to proivde them a tool that can help them share their data based on the platform they use to store their data. Most data custodians use Excel to store data. Some are also using ArcGIS and Tableau. Using a python script that can accept data based on different platforms that data custodians might use to enter the data can provide a tool and common platform to share ODM data.

### Data will be shared by the data custodian using a web application tool where the data custodian can enter in their data and the CSV schema with their own predefined rules set for different data repositories. The back end python script will allow them to filter the data based on their provided csv schema and output back the final dataset that is ready to be shared. Pandas library in python is used for the filtration of selective variables and conditional rules that the data custodian provides.

### Data sharing will take place once the data is in the ODM compliant format after it has gone through the validation process and has been cleaned.

## **Sharing processes:**

### **items -** There are several different items such as tables, variable names that will have different sharing properties or rules applied to them to selectively choose what the custodian might want to share with a particular data repository.

### **range -** The range can be used as a data sharing property or sharing rule that allows data custodian to selectively choose range of data values to share for specific variables in their data. As an example, the data custodian may not want to share their data for the entire time range and will only want to enter a specific timeframe for which the data can be shared. 

### **who -** The sharing property or the rule can identify who the data is intended for. Different data repositories or organizations or public or a person can have different access level to the data as per the requirements of the data custodian. The different access groups will be identified through these rules, **shared_with_access_groups** that will be part of the schema in the **shared_data.csv** file. When the data custodian logs onto the web portal to use ODM tool for data sharing, they will have options to select for the access groups they wish to share the data with.

### **description -** There will be a description for each sharing property or rule that will specify the license or details how the data or specific data elements shared with a specific recipient can or can not be used.

### **extensible -** Since the waste water surveilance is rapidly developing, it will be necessary to make the sharing process more adaptable and extensible for growing changes and processes that allows users to add more variables and rules in the schema for sharing.

