import pytest # pylint: disable=import-error
import create_dataset # pylint: disable=import-error
from create_dataset import create_dataset # pylint: disable=import-error
import pandas as pd # pylint: disable=import-error
import numpy as np # pylint: disable=import-error
import json
import csv
import re
import os
from pandas import Timestamp # pylint: disable=import-error
from numpy import nan # pylint: disable=import-error

# User Data:

dataset = {
    "Sample": [
        {
            "collection": "mooreSw",
            "dateTime": Timestamp("2021-02-01 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
            "fieldSampleTempC": 15,
            "notes": "Samples shipped on ice from site to lab by courier",
            "sampleID": "Sample S100",
            "shippedOnce": "Yes",
            "siteID": "Site T113",
            "sizeL": 8,
            "storageTempC": 16,
            "type": "swrSed",
        },
        {
            "collection": "cpTP24h",
            "dateTime": Timestamp("2021-01-25 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
            "fieldSampleTempC": 17,
            "notes": "Samples shipped on ice from site to lab by courier",
            "sampleID": "Sample S106",
            "shippedOnce": "Yes",
            "siteID": "Site T106",
            "sizeL": 2,
            "storageTempC": 18,
            "type": "pSludge",
        },
        {
            "collection": "grb",
            "dateTime": Timestamp("2021-01-28 21:00:00"),
            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
            "fieldSampleTempC": 18,
            "notes": "Samples shipped on ice from site to lab by courier",
            "sampleID": "Sample S107",
            "shippedOnce": "Yes",
            "siteID": "Site T107",
            "sizeL": 10,
            "storageTempC": 22,
            "type": "rawWW",
        },
    ],
    "WWMeasure": [
        {
            "analysisDate": Timestamp("2021-01-25 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 40,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "CovidN2 replicate measures linked by index",
            "reportDate": Timestamp("2021-02-06 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "covN2",
            "typeOther": nan,
            "uWwMeasureID": "Measure WW100",
            "unit": "gcM",
            "unitOther": "gcMcovN2",
            "value": 145000,
        },
        {
            "analysisDate": Timestamp("2021-01-28 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 50,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "CovidN2 replicate measures linked by index",
            "reportDate": Timestamp("2021-01-25 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "covN2",
            "typeOther": nan,
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcMcovN1",
            "value": 16000,
        },
        {
            "analysisDate": Timestamp("2021-02-06 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 60,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "nPMMoV measure linked to CovidN1 by index",
            "reportDate": Timestamp("2021-03-06 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "nPMMoV",
            "typeOther": nan,
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcmnPMMoV",
            "value": 98000,
        },
    ],
}

# User requested organization:
organization = "PHAC"

#FOR ALL TABLES: INCLUDING SAMPLE, WWMEASURE AND ASSAYMETHOD TABLE.
## FOR SINGLE COLUMN FROM EACH TABLE OR ANY OF THE TABLE

# Rule 103 filters rows based on a single column and all values of the rows.

rule_103 = [{
        "ruleID": "rule103",
        "table": "ALL",
        "variable": "fieldSampleTempC;unitOther",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output103 = {
    "filtered_data": {"Sample": [], "WWMeasure": []},
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule103",
        }
    ],
}

def test_method_103():
  assert create_dataset(rule_103, data = dataset, org = organization) == output103

# Rule 104 filters rows based on a single column from each table and single value from each column or any of the columns being numeric.

rule_104 = [{
        "ruleID": "rule104",
        "table": "ALL",
        "variable": "value;fieldSampleTempC",
        "ruleValue": "17.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output104 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule104",
        }
    ],
}

def test_method_104():
  assert create_dataset(rule_104, data = dataset, org = organization) == output104

# Rule 105 filters rows based on a single column from each table and single value from each column or any of the columns being string.

rule_105 = [{
        "ruleID": "rule105",
        "table": "ALL",
        "variable": "unitOther;collection",
        "ruleValue": "mooreSW;gcMcovN2",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output105 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule105",
        }
    ],
}

def test_method_105():
  assert create_dataset(rule_105, data = dataset, org = organization) == output105

# Rule 106 filters rows based on a single column from each table and single value from each column or any of the columns being datetime.

rule_106 = [{
        "ruleID": "rule106",
        "table": "ALL",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "2021-02-06;2021-02-01 21:00",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output106 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule106",
        }
    ],
}

def test_method_106():
  assert create_dataset(rule_106, data = dataset, org = organization) == output106

# Rule 107 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two numeric values with [].

rule_107 = [{
        "ruleID": "rule107",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[16000,98000];[16.0,18.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output107 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule107",
        }
    ],
}

def test_method_107():
  assert create_dataset(rule_107, data = dataset, org = organization) == output107

# Rule 108 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two numeric values with ().

rule_108 = [{
        "ruleID": "rule108",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(89000,145000);(15.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output108 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule108",
        }
    ],
}

def test_method_108():
  assert create_dataset(rule_108, data = dataset, org = organization) == output108

# Rule 109 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two numeric values with (].

rule_109 = [{
        "ruleID": "rule109",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(89000,145000];(15.0,18.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output109 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule109",
        }
    ],
}

def test_method_109():
  assert create_dataset(rule_109, data = dataset, org = organization) == output109

# Rule 110 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two numeric values with [).

rule_110 = [{
        "ruleID": "rule110",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[16000,98000);[16.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output110 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule110",
        }
    ],
}

def test_method_110():
  assert create_dataset(rule_110, data = dataset, org = organization) == output110

# Rule 111 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two datetime values with [].

rule_111 = [{
        "ruleID": "rule111",
        "table": "ALL",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "[2021-01-31,2021-02-06]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output111 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule111",
        }
    ],
}

def test_method_111():
  assert create_dataset(rule_111, data = dataset, org = organization) == output111

# Rule 112 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two datetime values with ().

rule_112 = [{
        "ruleID": "rule112",
        "table": "ALL",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "(2021-01-25 8:00,2021-01-31 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output112 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule112",
        }
    ],
}

def test_method_112():
  assert create_dataset(rule_112, data = dataset, org = organization) == output112

# Rule 113 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two datetime values with (].

rule_113 = [{
        "ruleID": "rule113",
        "table": "ALL",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "(2021-01-29,2021-02-02]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output113 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule113",
        }
    ],
}

def test_method_113():
  assert create_dataset(rule_113, data = dataset, org = organization) == output113

# Rule 114 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two datetime values with [).

rule_114 = [{
        "ruleID": "rule114",
        "table": "ALL",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "[2021-01-25 8:00,2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output114 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule114",
        }
    ],
}

def test_method_114():
  assert create_dataset(rule_114, data = dataset, org = organization) == output114

# Rule 115 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two values where the lower bound limit is infinity with ().

rule_115 = [{
        "ruleID": "rule115",
        "table": "ALL",
        "variable": "storageTempC;analysisDate",
        "ruleValue": "(Inf,17)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output115 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule115",
        }
    ],
}

def test_method_115():
  assert create_dataset(rule_115, data = dataset, org = organization) == output115

# Rule 116 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two values where the lower bound limit is infinity with (].

rule_116 = [{
        "ruleID": "rule116",
        "table": "ALL",
        "variable": "fieldSampleTempC;analysisDate",
        "ruleValue": "(Inf,17]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output116 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule116",
        }
    ],
}

def test_method_116():
  assert create_dataset(rule_116, data = dataset, org = organization) == output116

# Rule 117 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two values where the upper bound limit is infinity with ().

rule_117 = [{
        "ruleID": "rule117",
        "table": "ALL",
        "variable": "storageTempC;analysisDate",
        "ruleValue": "(2021-01-30,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output117 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule117",
        }
    ],
}

def test_method_117():
  assert create_dataset(rule_117, data = dataset, org = organization) == output117

# Rule 118 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between 
# two values where the upper bound limit is infinity with [).

rule_118 = [{
        "ruleID": "rule118",
        "table": "ALL",
        "variable": "storageTempC;analysisDate",
        "ruleValue": "[2021-01-28,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output118 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule118",
        }
    ],
}

def test_method_118():
  assert create_dataset(rule_118, data = dataset, org = organization) == output118

# Rule 119 filters rows based on a single column from each table and multiple values from each column or any of the columns where one value could be
# an interval and other a single value.

rule_119 = [{
        "ruleID": "rule119",
        "table": "ALL",
        "variable": "analysisDate;fieldSampleTempC",
        "ruleValue": "[2021-01-28,2021-02-06]; 17.0",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output119 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule119",
        }
    ],
}

def test_method_119():
  assert create_dataset(rule_119, data = dataset, org = organization) == output119

# For ALL TABLES:
## MULTIPLE COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 120 filters rows based on multiple columns and all values of the rows.

rule_120 = [{
        "ruleID": "rule120",
        "table": "ALL",
        "variable": "type;dateTimeStart;analysisDate;date;unitOther",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output120 = {
    "filtered_data": {"Sample": [], "WWMeasure": []},
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule120",
        }
    ],
}

def test_method_120():
  assert create_dataset(rule_120, data = dataset, org = organization) == output120

# Rule 121 filters rows based on multiple columns from each table and single value from each column or any of the columns being numeric.

rule_121 = [{
        "ruleID": "rule121",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "16.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output121 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule121",
        }
    ],
}

def test_method_121():
  assert create_dataset(rule_121, data = dataset, org = organization) == output121

# Rule 122 filters rows based on multiple columns from each table and single value from each column or any of the columns being string.

rule_122 = [{
        "ruleID": "rule122",
        "table": "ALL",
        "variable": "unitOther; type; collection",
        "ruleValue": "cpTP24h; gcmnPMMoV; rawWW",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output122 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule122",
        }
    ],
}

def test_method_122():
  assert create_dataset(rule_122, data = dataset, org = organization) == output122

# Rule 123 filters rows based on multiple columns from each table and single value from each column or any of the columns being datetime.

rule_123 = [{
        "ruleID": "rule123",
        "table": "ALL",
        "variable": "analysisDate; reportDate; dateTimeStart;dateTimeEnd",
        "ruleValue": "2021-02-06;2021-02-01 21:00",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output123 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule123",
        }
    ],
}

def test_method_123():
  assert create_dataset(rule_123, data = dataset, org = organization) == output123

# Rule 124 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# numbers with [].

rule_124 = [{
        "ruleID": "rule124",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "[16.0; 17.0]; [98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output124 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule124",
        }
    ],
}

def test_method_124():
  assert create_dataset(rule_124, data = dataset, org = organization) == output124

# Rule 125 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# numbers with ().

rule_125 = [{
        "ruleID": "rule125",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "(15.0, 18.0); (16000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output125 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule125",
        }
    ],
}

def test_method_125():
  assert create_dataset(rule_125, data = dataset, org = organization) == output125

# Rule 126 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# numbers with (].

rule_126 = [{
        "ruleID": "rule126",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "(15.0, 18.0]; (89000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output126 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule126",
        }
    ],
}

def test_method_126():
  assert create_dataset(rule_126, data = dataset, org = organization) == output126

# Rule 127 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# numbers with [).

rule_127 = [{
        "ruleID": "rule127",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "[16.0, 18.0); [89000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output127 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule127",
        }
    ],
}

def test_method_127():
  assert create_dataset(rule_127, data = dataset, org = organization) == output127

# Rule 128 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# datetime values with [].

rule_128 = [{
        "ruleID": "rule128",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "[2021-02-01 21:00, 2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }]

output128 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule128",
        }
    ],
}

def test_method_128():
  assert create_dataset(rule_128, data = dataset, org = organization) == output128

# Rule 129 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# datetime values with ().

rule_129 = [{
        "ruleID": "rule129",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "(2021-01-29,2021-02-06)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }]

output129 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule129",
        }
    ],
}

def test_method_129():
  assert create_dataset(rule_129, data = dataset, org = organization) == output129

# Rule 130 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# datetime values with (].

rule_130 = [{
        "ruleID": "rule130",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "(2021-01-30 8:00, 2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output130 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule130",
        }
    ],
}

def test_method_130():
  assert create_dataset(rule_130, data = dataset, org = organization) == output130

# Rule 131 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
# datetime values with [).

rule_131 = [{
        "ruleID": "rule131",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "[2021-01-30,2021-02-06)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output131 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule131",
        }
    ],
}

def test_method_131():
  assert create_dataset(rule_131, data = dataset, org = organization) == output131


# Rule 132 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the 
# the lower bound limit is infinity with ().

rule_132 = [{
        "ruleID": "rule132",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "(Inf, 2021-01-26)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output132 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule132",
        }
    ],
}

def test_method_132():
  assert create_dataset(rule_132, data = dataset, org = organization) == output132

# Rule 133 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the 
# the lower bound limit is infinity with (].

rule_133 = [{
        "ruleID": "rule133",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "(Inf, 2021-01-27]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output133 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule133",
        }
    ],
}

def test_method_133():
  assert create_dataset(rule_133, data = dataset, org = organization) == output133

# Rule 134 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the 
# the upper bound limit is infinity with ().

rule_134 = [{
        "ruleID": "rule134",
        "table": "ALL",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "(16.0,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output134 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule134",
        }
    ],
}

def test_method_134():
  assert create_dataset(rule_134, data = dataset, org = organization) == output134

# Rule 135 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the 
# the upper bound limit is infinity with [).

rule_135 = [{
        "ruleID": "rule135",
        "table": "ALL",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "[17.0,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output135 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
            ],
            "rule_id": "rule135",
        }
    ],
}

def test_method_135():
  assert create_dataset(rule_135, data = dataset, org = organization) == output135

# Rule 136 filters rows based on multiple columns from each table and multiple values from each column or any of the columns where one value could be an interval
# and the other could be a single value.

rule_136 = [{
        "ruleID": "rule136",
        "table": "ALL",
        "variable": "dateTimeStart;value;analysisDate",
        "ruleValue": "( 2021-01-27 8:00 , 2021-02-01 21:00] ; 145000;(2021-01-29, 2021-02-06]; [98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC" 
    }]

output136 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule136",
        }
    ],
}

def test_method_136():
  assert create_dataset(rule_136, data = dataset, org = organization) == output136

# For ALL TABLES:
## ALL COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 137 filters rows based on all columns from each table and all values of the rows.

rule_137 = [{
        "ruleID": "rule137",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output137 = {
    "filtered_data": {"Sample": [], "WWMeasure": []},
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule137",
        }
    ],
}

def test_method_137():
  assert create_dataset(rule_137, data = dataset, org = organization) == output137

# Rule 138 filters rows based on all columns from each table and single value from each column or any of the columns being numeric.

rule_138 = [{
        "ruleID": "rule138",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "17.0;16000",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output138 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule138",
        }
    ],
}

def test_method_138():
  assert create_dataset(rule_138, data = dataset, org = organization) == output138

# Rule 139 filters rows based on all columns from each table and single value from each column or any of the columns being string.

rule_139 = [{
        "ruleID": "rule139",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "mooreSw;gcMcovN2",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output139 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule139",
        }
    ],
}

def test_method_139():
  assert create_dataset(rule_139, data = dataset, org = organization) == output139

# Rule 140 filters rows based on all columns from each table and single value from each column or any of the columns being datetime.

rule_140 = [{
        "ruleID": "rule140",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "2021-01-27 8:00;2021-02-06",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output140 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule140",
        }
    ],
}

def test_method_140():
  assert create_dataset(rule_140, data = dataset, org = organization) == output140

# Rule 141 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two numbers with [].

rule_141 = [{
        "ruleID": "rule141",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0];[16.0,17.0],[76000,102000]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output141 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule141",
        }
    ],
}

def test_method_141():
  assert create_dataset(rule_141,data = dataset, org = organization) == output141    

# Rule 142 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two numbers with ().

rule_142 = [{
        "ruleID": "rule142",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0);(15.0,18.0),(92000,102000)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output142 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule142",
        }
    ],
}

def test_method_142():
  assert create_dataset(rule_142, data = dataset, org = organization) == output142

# Rule 143 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two numbers with (].

rule_143 = [{
        "ruleID": "rule143",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0];(16.0,18.0],(92000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output143 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule143",
        }
    ],
}

def test_method_143():
  assert create_dataset(rule_143, data = dataset, org = organization) == output143

# Rule 144 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two numbers with [).

rule_144 = [{
        "ruleID": "rule144",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[2.0,10.0);[19.0,22.0),[92000,102000)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output144 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule144",
        }
    ],
}

def test_method_144():
  assert create_dataset(rule_144, data = dataset, org = organization) == output144

# Rule 145 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two datetime
# with [].

rule_145 = [{
        "ruleID": "rule145",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[2021-01-29,2021-02-06]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output145 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule145",
        }
    ],
}

def test_method_145():
  assert create_dataset(rule_145, data = dataset, org = organization) == output145

# Rule 146 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two datetime with ().

rule_146 = [{
        "ruleID": "rule146",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2021-01-27 8:00, 2021-01-30 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output146 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 40,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule146",
        }
    ],
}

def test_method_146():
  assert create_dataset(rule_146, data = dataset, org = organization) == output146

# Rule 147 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two datetime with (].

rule_147 = [{
        "ruleID": "rule147",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2021-01-31,2021-02-09]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output147 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule147",
        }
    ],
}

def test_method_147():
  assert create_dataset(rule_147, data = dataset, org = organization) == output147

# Rule 148 filters rows based on all columns from each table and single value from each column or any of the columns being an interval 
# between two datetime with [).

rule_148 = [{
        "ruleID": "rule148",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[2021-01-29,2021-02-09)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output148 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule148",
        }
    ],
}

def test_method_148():
  assert create_dataset(rule_148, data = dataset, org = organization) == output148

# Rule 149 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the 
# the lower bound limit is infinity with ().

rule_149 = [{
        "ruleID": "rule149",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(Inf, 2021-01-27)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output149 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule149",
        }
    ],
}

def test_method_149():
  assert create_dataset(rule_149, data = dataset, org = organization) == output149

# Rule 150 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the 
# the lower bound limit is infinity with (].

rule_150 = [{
        "ruleID": "rule150",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(Inf, 2021-01-27]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output150 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S106",
                            "shippedOnce": "Yes",
                            "siteID": "Site T106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 50,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule150",
        }
    ],
}

def test_method_150():
  assert create_dataset(rule_150, data = dataset, org = organization) == output150

# Rule 151 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the 
# the upper bound limit is infinity with ().

rule_151 = [{
        "ruleID": "rule151",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(98000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output151 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 60,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "nPMMoV measure linked to CovidN1 by index",
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "nPMMoV",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
            },
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule151",
        }
    ],
}

def test_method_151():
  assert create_dataset(rule_151, data = dataset, org = organization) == output151

# Rule 152 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the 
# the upper bound limit is infinity with [).

rule_152 = [{
        "ruleID": "rule152",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[98000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output152 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S100",
                "shippedOnce": "Yes",
                "siteID": "Site T113",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
            },
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            },
            {
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S107",
                "shippedOnce": "Yes",
                "siteID": "Site T107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule152",
        }
    ],
}

def test_method_152():
  assert create_dataset(rule_152, data = dataset, org = organization) == output152

# Rule 153 filters rows based on all columns from each table and multiple values from each column or any of the columns where one value could be an interval
# and the other could be a single value.

rule_153 = [{
        "ruleID": "rule153",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-03 21:00] ; 145000; [98000,145000]; 2021-03-06;swrSed",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output153 = {
    "filtered_data": {
        "Sample": [
            {
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "notes": "Samples shipped on ice from site to lab by courier",
                "sampleID": "Sample S106",
                "shippedOnce": "Yes",
                "siteID": "Site T106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 50,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN2 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN2",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            }
        ],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S100",
                            "shippedOnce": "Yes",
                            "siteID": "Site T113",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
                        },
                        {
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "notes": "Samples shipped on ice from site to lab by courier",
                            "sampleID": "Sample S107",
                            "shippedOnce": "Yes",
                            "siteID": "Site T107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 40,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "CovidN2 replicate measures linked by index",
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "covN2",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "assayID": "Assay Y100",
                            "fractionAnalyzed": "solid",
                            "index": 60,
                            "instrumentID": "Instrument IN200",
                            "labID": "Lab L100",
                            "notes": "nPMMoV measure linked to CovidN1 by index",
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "reporterID": "Reporter R1",
                            "sampleID": "Sample S100",
                            "type": "nPMMoV",
                            "typeOther": nan,
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule153",
        }
    ],
}

def test_method_153():
  assert create_dataset(rule_153, data = dataset, org = organization) == output153