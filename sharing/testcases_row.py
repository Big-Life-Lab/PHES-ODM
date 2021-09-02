# For a SINGLE TABLE:
# For single column:

# Rule 1 filters rows based on a single column and all values of the rows.

rule_1 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleID": "rule1"
    }]

# Rule 2 filters rows based on a single column and single value being numeric for Public.

rule_2 = [{
        "description": "null",
        "direction": "row",
        "filterValue": 15000,
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "value",
        "ruleID": "rule2"
    }]

#Rule 3 filters rows based on a single column and single value being numeric for PHAC.

rule_3 = [{
        "description": "null",
        "direction": "row",
        "filterValue": 6,
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "index",
        "ruleID": "rule3"
    }]

#Rule 4 filters rows based on a single column and single value being a string for Public.

rule_4 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "Lab L105",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "LabID",
        "ruleID": "rule4",
    }]

#Rule 5 filters rows based on a single column and single value being a string for PHAC.

rule_5 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "Reporter R3",
        "license": "null",
        "sharedWith": "PHAC",
        "table": "WWMeasure",
        "variable": "reporterID",
        "ruleID": "rule5",
    }]

#Rule 6 filters rows based on a single column and single value being a datetime for Public.

rule_6 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "2021-02-08",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "analysisDate",
        "ruleID": "rule6",
    }]

#Rule 7 filters rows based on a single column and range interval for a numeric value for Public.

rule_7 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "[15000, 20000]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "value",
        "ruleID": "rule7",
    }]

#Rule 8 filters rows based on a single column and range interval for a numeric value for PHAC.

rule_8 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "[72000,92000]",
        "license": "null",
        "sharedWith": "PHAC",
        "table": "WWMeasure", 
        "variable": "value",
        "ruleID": "rule8",
    }]

#Rule 9 filters rows based on a single column and range interval for a datetime value for Public.

rule_9 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-01-25, 2021-01-26]",
        "license": "null",
        "sharedWith": "Public",
        "table": "WWMeasure", 
        "variable": "analysisDate",
        "ruleID": "rule9"
    }]

#Rule 10 filters rows based on a single column and range interval for a datetime value for PHAC.

rule_10 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "(2021-01-26,2021-01-31]",
        "license": "null",
        "sharedWith": "PHAC",
        "table": "WWMeasure", 
        "variable": "analysisDate",
        "ruleID": "rule10"
    }]

#Rule 11 filters rows based on a single column and range interval for a datetime value with upper bound limit being infinity for PHAC.

rule_11 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "(2021-01-31,Inf)",
        "license": "null",
        "sharedWith": "PHAC",
        "table": "WWMeasure", 
        "variable": "analysisDate",
        "ruleID": "rule11"
    }]

#Rule 12 filters rows based on a single column and range interval for a numeric value with lower bound limit being infinity for Public and PHAC.

rule_12 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf, 23000]",
        "license": "null",
        "sharedWith": "Public;PHAC",
        "table": "WWMeasure", 
        "variable": "value",
        "ruleID": "rule12"
    }]

#Rule 13 filters rows based on a single column and multiple values to filter by a single value and a range for Public.

rule_13 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "82000;[10200, Inf)",
        "license": "null",
        "sharedWith": "Public",
        "table": "WWMeasure", 
        "variable": "value",
        "ruleID": "rule13"
    }]

#Rule 14 filters rows based on a single column and multiple values to filter by a single value and a range for Public and PHAC.

rule_14 = [{
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-20; (2021-01-25, 2021-01-28]",
        "license": "null",
        "sharedWith": "Public;PHAC",
        "table": "WWMeasure", 
        "variable": "analysisDate",
        "ruleID": "rule14"
    }]

# For SINGLE TABLE:
## MULTIPLE COLUMNS:

#Rule 15 filters all rows from more than 1 column from a single table.

rule_15 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleID": "rule15_1",
    }, 
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Instrument",
        "variable": "description;name",
        "ruleID": "rule15_2",
    }
]


#Rule 16 filters rows from multiple columns from a single table based on a single value being a number. 

rule_16 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "6;23000",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "index;value",
        "ruleID": "rule16",
    }
]

#Rule 17 filters rows from multiple columns from a single table based on single value being a string.

rule_17 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S101;Site T110",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "sampleID;siteID",
        "ruleID": "rule17_1",
    }, 
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Lab L107;assay Y107",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "LabID;assayID",
        "ruleID": "rule17_2"
    }
]

R#ule 18 filters rows multiple columns from single table based on single value being a datetime value.

rule_18 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-27  8:00:00 AM;2021-01-30  8:00:00 AM",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleID": "rule18",
    }
]

#Rule 19 filters rows from multiple columns from a single table based on an interval value between two numbers.

rule_19 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[12.0,15.0);[8.0,10.0]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "fieldSampleTempC;sizeL",
        "ruleID": "rule19_1",
    }, 
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[5,6);[89000, 98000)",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "index;value",
        "ruleID": "rule19_2"
    }
]

#Rule 20 filters rows from multiple columns from a single table based on an interval value between two datetime values.

rule_20 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-08,2021-03-29];[2021-01-25,2021-01-26)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "analysisDate;reportDate",
        "ruleID": "rule20",
    }
]

#Rule 21 filters rows from multiple columns from a single table based on an interval value between two values where the lower bound limit is infinity.

rule_21 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf, 2021-01-28);(Inf,2021-01-25]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "analysisDate;reportDate",
        "ruleID": "rule21"
    }
]

#Rule 22 filters rows from multiple columns from a single table based on an interval value between two values where the upper bound limit is infinity.

rule_22 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[98000, Inf);[2021-03-29, Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "value;analysisDate",
        "ruleID": "rule22"
    }
]

#Rule 23 filters rows from multiple columns from a single table based on multiple filter values where one may be a single value and other could be a range.

rule_23 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S101;[8.0,1.0]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "sampleID;sizeL",
        "ruleID": "rule23_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "[102000,150000);2021-01-25",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "value;reportDate",
        "ruleID": "rule23",
    }
]

#SINGLE TABLE:
# ALL COLUMNS:

#Rule 25 filters all the rows from all column from a single table.

rule_25 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "ALL",
        "ruleID": "rule25_1",
    }, 
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Instrument",
        "variable": "ALL",
        "ruleID": "rule25_2"
    }
]

#Rule 26 filters rows from all columns from a single table based on a value being a number.

rule_26 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "10.0;13.0",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "ALL",
        "ruleID": "rule26",
    }
]

#Rule 27 filters rows from all columns from a single table based on a value being a string.

rule_27 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Measure WW105;Sample S104;Lab L107;Assay Y102;Instrument IN202;Reporter R5;liquid;nPMMoV1;gcM;nPMMoV measure linked to CovidN2 by index6",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "ALL",
        "ruleID": "rule27",
    }
]

#Rule 28 filters rows from all columns from a single table based on a value being a datetime.

rule_28 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-31  9:00:00 PM;2021-01-28  8:00:00 AM;2021-01-24  8:00:00 AM",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "ALL",
        "ruleID": "rule28",
    }
]

#Rule 29 filters rows from all columns from a single table based on an interval value being a number.

rule_29 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[8.0,10.0]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Sample",
        "variable": "ALL",
        "ruleID": "rule29",
    }
]

#Rule 30 filters rows from all columns from a single table based on an interval value being a datetime value.

rule_30 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-01-25,2021-01-26];(2021-01-25,2021-01-28]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "ALL",
        "ruleID": "rule30",
    }
]

#Rule 31 filters rows from all columns from a single table based on an interval value being where lower limit is infinity. This will apply to all numeric and datetime columns.

rule_31 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-26)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "ALL",
        "ruleID": "rule31",
    }
]

#Rule 32 filters rows from all columns from a single table based on an interval value being where upper limit is infinity. This will apply to all numeric and datetime columns.

rule_32 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(12.0,Inf);[2021-02-01 21:00,Inf);[2021-02-02,Inf);(2021-02-02,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "ALL",
        "ruleID": "rule32",
    }
]

#Rule 33 filters rows from all columns from a single table based on multiple values where one can be a single value and other an interval.

rule_33 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "98000;(15000,23000];2021-01-31;[2021-02-01 21:00,Inf);[2021-02-02,Inf);(2021-02-02,Inf);Lab L105",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure",
        "variable": "ALL",
        "ruleID": "rule33",
    }
]

#For MULTIPLE TABLES:

# SINGLE COLUMNS:

#Rule 34 filters all rows from a single column from multiple tables.

rule_34 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Instrument",
        "variable": "notes;referenceLink",
        "ruleID": "rule34",
    }
]

#Rule 35 filters selected rows from a single column from multiple tables where value of the column is a number.

rule_35 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "85000;10.0",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;sizeL",
        "ruleID": "rule35",
    }
]

#Rule 36 filters selected rows from a single column from multiple tables where value of the column is a string.

rule_36 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Measure WW106;Sample S101",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "uWwMeasureID;sampleID",
        "ruleID": "rule36_1",
    },
   {
        "description": "null",
        "direction": "row",
        "filterValue": "Assay Y108;Sample S112",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "assayID;siteID",
        "ruleID": "rule36_2",
    }
]

#Rule 37 filters selected rows from a single column from multiple tables where value of the column is a datetime type.

rule_37 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-26;2021-01-26",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;dateTime",
        "ruleID": "rule37_1",
    },
   {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-31;2021-01-30",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "reportDate;dateTimeStart",
        "ruleID": "rule37_2",
    }
]

#Rule 38 filters selected rows from a single column from multiple tables where value of the column is an interval with numeric type.


rule_38 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[15000,23000);(8.0,10.0]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;sizeL",
        "ruleID": "rule38_1",
    },
   {
        "description": "null",
        "direction": "row",
        "filterValue": "[98000,102000];[12.0,13.0]",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;fieldSampleTempC",
        "ruleID": "rule38_2",
    }
]

#Rule 39 filters selected rows from a single column from multiple tables where value of the column is an interval with datetime type.


rule_39 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-08,2021-03-31);(2021-01-25,2021-01-26]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;dateTimeStart",
        "ruleID": "rule39",
    },
]

#Rule 40 filters selected rows from a single column from multiple tables where value of the column is an interval with lower bound limit as infinity.


rule_40 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,17000);(Inf,10.0]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;sizeL",
        "ruleID": "rule40_1",
    },
   {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-26];[12.0,13.0]",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;fieldSampleTempC",
        "ruleID": "rule40_2",
    }
]

#Rule 41 filters selected rows from a single column from multiple tables where value of the column is an interval with upper bound limit as infinity.


rule_41 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[102000,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;sizeL",
        "ruleID": "rule41",
    }
]


#Rule 42 filters selected rows from a single column from multiple tables based on multiple values of the column where one could be a value and other a range.


rule_42 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "16000;[102000,Inf);[2021-02-26  9:00:00 PM, 2021-02-01  9:00:00 PM];2021-01-25",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;dateTime",
        "ruleID": "rule42"
    }
]

# MULTIPLE TABLES
## MULTIPLE COLUMNS

#Rule 43 filters all rows from multiple columns from multiple tables.


rule_43 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "index;notes;dateTimeStart;collection",
        "ruleID": "rule43",
    }
]

#Rule 44 filters selected rows from multiple columns from multiple tables where value of the columns is a number.


rule_44 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "15000;5;8.0",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;index;sizeL;fieldSampleTempC",
        "ruleID": "rule44",
    }
]

#Rule 45 filters selected rows from multiple columns from multiple tables where value of the columns is a string.


rule_45 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S101;Lab L106",
        "license": "null",
        "sharedWith": "Public;PHAC",
        "table": "WWMeasure;Lab",
        "variable": "sampleID;labID;name",
        "ruleID": "rule45",
    }
]

#Rule 46 filters selected rows from multiple columns from multiple tables where value of the columns is a datetime.

rule_46 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-26;2021-01-31;2021-02-27  9:00:00 PM",
        "license": "null",
        "sharedWith": "Public;PHAC",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;reportDate;dateTime;dateTimeStart",
        "ruleID": "rule46",
    }
]

#Rule 47 filters selected rows from multiple columns from multiple tables where value of the columns is an interval between two numbers.

rule_47 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[15000,18000);[8.0,10.0];(12.0,13.0]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;index;sizeL;fieldSampleTempC",
        "ruleID": "rule47",
    }
]


#Rule 48 filters selected rows from multiple columns from multiple tables where value of the columns is an interval between two datetime values.

rule_48 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-01-25,2021-01-31);[2021-02-26  9:00:00 PM,2021-02-01  9:00:00 PM]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;reportDate;dateTime;dateTimeEnd",
        "ruleID": "rule48"
    }
]

#Rule 49 filters selected rows from multiple columns from multiple tables where value of the columns is an interval between two values where the lower bound limit is infinity.

rule_49 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-31)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "analysisDate;reportDate;dateTime;dateTimeStart",
        "ruleID": "rule49"
    }
]

#Rule 50 filters selected rows from multiple columns from multiple tables where value of the columns is an interval between two values where the lower bound limit is infinity.

rule_50 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(2.0,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "sizeL;analysisDate;reporterID;notes",
        "ruleID": "rule50"
    }
]

#Rule 51 filters selected rows from multiple columns from multiple tables based on multiple values from the column where one of the values could be a single value and other could be range intervals.

rule_51 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "85000;[16000,20000);(2.0,Inf);Sample S105",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "value;sizeL;reporterID;sampleID",
        "ruleID": "rule51"
    }
]

# MULTIPLE TABLES
## ALL COLUMNS

#Rule 52 filters all rows from multiple tables from all the columns.

rule_52 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "Instrument;Sample",
        "variable": "ALL",
        "ruleID": "rule52"
    }
]

#Rule 53 filters selected rows from multiple tables from all the columns based on the value of column being a number.

rule_53 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2.0;102000;5",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample",
        "variable": "ALL",
        "ruleID": "rule53"
    }
]

#Rule 54 filters selected rows from multiple tables from all the columns based on the value of column being a string.

rule_54 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Site T113;Sample S112;Instrument IN204",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule54_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "Assay Y107;Lab L102",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Lab",
        "variable": "ALL",
        "ruleID": "rule54_2"
    }
]

#Rule 55 filters selected rows from multiple tables from all the columns based on the value of column being a datetime.

rule_55 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-26  9:00:00 PM;2021-01-31",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule55"
    }
]

#Rule 56 filters selected rows from multiple tables from all columns based on the value of column being an interval between two numbers.

rule_56 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(72000,145000);(8,10]",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Lab",
        "variable": "ALL",
        "ruleID": "rule56_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "(92000,145000);(8,10]",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule56_2"
    }
]

#Rule 57 filters selected rows from multiple tables from all columns based on the value of column being an interval between two datetime values.

rule_57 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-07,2021-02-08];[2021-01-31,2021-02-08]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Lab",
        "variable": "ALL",
        "ruleID": "rule57"
    }
]

#Rule 58 filters selected rows from multiple tables from all columns based on the value of column being an interval between two values where lower bound limit is infinity.

rule_58 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-26]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule58"
    }
]

#Rule 59 filters selected rows from multiple tables from all columns on the value of the column being an interval between two values where upper bound limit is infinity.

rule_59 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(89000,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule59_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "(8.0,Inf)",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule59_2"
    }
]


#Rule 60 filters selected rows from multiple tables from all columns based on multiple values where one value can be a single value and other an interval.

rule_60 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-26];145000;Sample S105;[2021-01-25  8:00:00 AM,2021-01-27  8:00:00 AM],No,Instrument IN206",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "WWMeasure;Sample;Instrument",
        "variable": "ALL",
        "ruleID": "rule60"
    }
]

# All TABLES
## SINGLE COLUMN

#Rule 61 removes all rows from all tables from a single column from different tables in each table.

rule_61 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "notes;name",
        "ruleID": "rule61"
    }
]

#Rule 62 removes selected rows from all tables from a single column from different tables where the column value is a number.

rule_62 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "10.0;102000;0.002;17.0",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sizeL;value;SampleSizeL",
        "ruleID": "rule62_1"
    },
    {
        "description": "null",
        "direction": "row",
        "filterValue": "8.0;145000;0.002;22.0",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sizeL;value;SampleSizeL",
        "ruleID": "rule62_2"
    }
]


#Rule 63 removes selected rows from all tables from a single column from different tables where value of the column is a string.

rule_63 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S105;Instrument IN205;Assay Y111;wwPH1;wwtpMuC",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sampleID;type;assayMethodIDDefault;instrumentID",
        "ruleID": "rule63_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S103;University L101 Lab;wwPH1;wwtpMuC;offline",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sampleID;type;name",
        "ruleID": "rule63_2"
    }
]

#Rule 64 removes selected rows from all tables from a single column from different tables where value of the column is a datetime value.

rule_64 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-27 12:00;2021-02-08;2021-02-25",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;dateTime;updateDate",
        "ruleID": "rule64"
    }
]

#Rule 65 removes selected rows from all tables from a single column from different tables where value of the column is a datetime value.

rule_65 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-27 12:00;2021-02-08;2021-01-28 21:00;2021-01-31",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;dateTime;updateDate;date",
        "ruleID": "rule65"
    }
]

#Rule 66 removes selected rows from all tables from a single column from different tables where value of the column is an interval between two numbers.

rule_66 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(98000,150000);[8.0,1.0];(43.766829;44.766829];(0.001,0.002]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;sizeL;geoLat;sampleSizeL",
        "ruleID": "rule66"
    }
]

#Rule 67 removes selected rows from all tables from a single from different tables where value of the column is an interval between two datetime values.

rule_67 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-02 12:00,2021-02-03 12:00];[2021-02-27 21:00,2021-02-29 21:00);[2021-03-29,2021-03-31];[2021-02-07,2021-02-08]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "dateTime;analysisDate;updateDate",
        "ruleID": "rule67"
    }
]

#Rule 68 removes selected rows from all tables from a single column from different tables where value of the column is an interval between two values where the lower bound limit is infinity.

rule_68 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-25 21:00]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "dateTime;analysisDate;value;updateDate",
        "ruleID": "rule68"
    }
]

#Rule 69 removes selected rows from all tables from a single column from different tables where value of the column is an interval between two values where the upper bound limit is infinity.

rule_69 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[92000,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;sizeL;fieldSampleTempC",
        "ruleID": "rule69"
    }
]

#Rule 70 removes selected rows from all tables from a single column from different tables based on multiple values where one could be a value and other a range interval.

rule_70 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-25 21:00];2021-01-31 21:00;(89000,98000],17000,Instrument IN207,Instrument IN208",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;dateTime;instrumentID",
        "ruleID": "rule70"
    }
]

# ALL Tables
## MULTIPLE COLUMNS

#Rule 71 removes all rows from multiple columns from all the tables.

rule_71 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-01-25 21:00];2021-01-31 21:00;(89000,98000],17000,Instrument IN207,Instrument IN208",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "typeOther;notes;type;name",
        "ruleID": "rule71"
    }
]

#Rule 72 removes selected rows from multiple columns from all the tables based on a value of the column being a number.

rule_72 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "92000;6;8.0;13.0",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;index;sizeL;fileSampleTempC",
        "ruleID": "rule72_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "89000;6;10.0;12.0",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;index;sizeL;fileSampleTempC",
        "ruleID": "rule72_2"
    }
]

#Rule 73 removes selected rows from multiple columns from all the tables based on a value of the column being a string.

rule_73 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S105; Site T112;liquid",
        "license": "null",
        "sharedWith": "Public;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sampleID;siteID;fractionAnalyzed",
        "ruleID": "rule73_1"
    },
        {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S106;Site T111;offline",
        "license": "null",
        "sharedWith": "PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "sampleID;siteID;instrumentID;type",
        "ruleID": "rule73_2"
    }
]

#Rule 74 removes selected rows from multiple columns from all the tables based on a value of the column being a datetime value. 

rule_74 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-02-08;2021-01-25;2021-01-26 8:00;2021-01-28  8:00:00 AM",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;reportDate;dateTimeStart;dateTimeEnd;updateDate",
        "ruleID": "rule74"
    }
]


#Rule 75 removes selected rows from multiple columns from all the tables based on a value of the column being an interval between two numerical values. 

rule_75 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[89000,102000);(12.0,13.0]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "value;index;sizeL;fieldSampleTempC",
        "ruleID": "rule75"
    }
]


#Rule 76 removes selected rows from multiple columns from all the tables based on a value of the column being an interval between two datetime values.

rule_76 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-07,2021-02-08];(2021-01-25,2021-01-26];[2021-01-25 8:00,2021-01-26 8:00);[2021-01-28  8:00:00 AM,2021-01-30 8:00);(2021-02-07, 2021-02-08]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;reportDate;dateTimeStart;dateTimeEnd;updateDate",
        "ruleID": "rule76"
    }
]

#Rule 77 removes selected rows from multiple columns from all the tables based on an interval where the upper bound limit is infinity.

rule_77 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,2021-02-09]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;reportDate;value;dateTimeStart;sizeL;updateDate;labID",
        "ruleID": "rule77"
    }
]

#Rule 78 removes selected rows from multiple columns from all the tables based on an interval where the upper bound limit is infinity.

rule_78 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-07,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;value;dateTimeStart;sizeL;updateDate;labID",
        "ruleID": "rule78"
    }
]


#Rule 79 removes selected rows from multiple columns from all the tables based on multiple values where one value can be a single value and other can be an interval.

rule_79 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-01-26;(102000,145000];[2021-01-27 8:00,2021-01-28 8:00];Lab L110""2021-01-26;(102000,145000];[2021-01-27 8:00,2021-01-28 8:00];Lab L110",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "analysisDate;value;dateTimeStart;sizeL;updateDate;labID",
        "ruleID": "rule79"
    }
]

# ALL TABLES
## ALL COLUMNS
#Rule 80 removes all rows from all columns from all tables. Basically all rows are null values for all tables.

rule_80 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "ALL",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule80"
    }
]

#Rule 81 removes selected rows from all columns from all tables based on a value being a number.

rule_81 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "98000;5;12.0",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule80"
    }
]

#Rule 82 removes selected rows from all columns from all tables based on a value being a string.

rule_82 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "Sample S104; Site T108;No;nPMMoV1;Lab L104; Assay Y106",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule80"
    }
]

#Rule 83 removes selected rows from all columns from all tables based on a value being a datetime value.

rule_83 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "2021-02-04 21:00;2021-02-27 21:00;2021-01-31;2021-02-08",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule83"
    }
]

#Rule 84 removes selected rows from all columns from all tables based on a value being an interval between two numbers.

rule_84 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[15000,17000];(12.0,13.0]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule84"
    }
]

#Rule 85 removes selected rows from all columns from all tables based on a value being an interval between two datetime values.

rule_85 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-07,2021-02-08];(2021-01-25,2021-01-26]",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule85"
    }
]

#Rule 86 removes selected rows from all columns from all tables based on an interval where the lower bound limit is infinity.

rule_86 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "(Inf,17000)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule86"
    }
]


#Rule 87 removes selected rows from all columns from all tables based on an interval where the upper bound limit is infinity.

rule_87 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[102000,Inf)",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule87"
    }
]


#Rule 88 removes selected rows from all columns from all tables based on multiple values where one value can be a single value and the other could be a range interval.

rule_88 = [
    {
        "description": "null",
        "direction": "row",
        "filterValue": "[2021-02-07,2021-02-08];(2021-01-25,2021-01-27);89000;13.0",
        "license": "null",
        "sharedWith": "Public;PHAC;Local;Provincial;Quebec;OntarioWSI;CanadianWasteWaterDatabase",
        "table": "ALL",
        "variable": "ALL",
        "ruleID": "rule88"
    }
]
