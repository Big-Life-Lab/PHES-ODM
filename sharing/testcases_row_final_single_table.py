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
            "collection": "cpTP24h",
            "dateTime": Timestamp("2021-02-01 21:00:00"),
            "dateTimeEnd": Timestamp("2021-02-01 21:00:00"),
            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
            "fieldSampleTempC": 15,
            "notes": "Samples shipped on ice from site to lab by courier",
            "sampleID": "Sample S100",
            "shippedOnce": "Yes",
            "siteID": "Site T100",
            "sizeL": 2,
            "storageTempC": 16,
            "type": "rawWW",
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
            "storageTempC": 16,
            "type": "rawWW",
        },
        {
            "collection": "cpTP24h",
            "dateTime": Timestamp("2021-01-28 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-27 08:00:00"),
            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
            "fieldSampleTempC": 18,
            "notes": "Samples shipped on ice from site to lab by courier",
            "sampleID": "Sample S107",
            "shippedOnce": "Yes",
            "siteID": "Site T107",
            "sizeL": 2,
            "storageTempC": 16,
            "type": "rawWW",
        },
    ],
    "WWMeasure": [
        {
            "analysisDate": Timestamp("2021-02-08 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 1,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "CovidN1 replicate measures linked by index",
            "reportDate": Timestamp("2021-01-25 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "covN1",
            "typeOther": "null",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcM",
            "unitOther": "gcMcovN1",
            "value": 20000,
        },
        {
            "analysisDate": Timestamp("2021-01-28 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 5,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "CovidN2 replicate measures linked by index",
            "reportDate": Timestamp("2021-01-25 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "covN2",
            "typeOther": "null",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcMcovN2",
            "value": 16000,
        },
        {
            "analysisDate": Timestamp("2021-01-27 00:00:00"),
            "assayID": "Assay Y100",
            "fractionAnalyzed": "solid",
            "index": 6,
            "instrumentID": "Instrument IN200",
            "labID": "Lab L100",
            "notes": "CovidN2 replicate measures linked by index",
            "reportDate": Timestamp("2021-01-26 00:00:00"),
            "reporterID": "Reporter R1",
            "sampleID": "Sample S100",
            "type": "covN2",
            "typeOther": "null",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcMcovN2",
            "value": 17000,
        },
    ],
}

# User requested organization:
organization = "PHAC"

# For a SINGLE TABLE: `Sample` table is used.
# For single column:

# Rule 1 filters rows based on a single column and all values of the rows.

rule_1 = [{
        "ruleID": "rule1",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output1 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule1",
        }
    ],
}

def test_method_1():
  assert create_dataset(rule_1, data = dataset, org = organization) == output1

# Rule 2 filters rows based on a single column and single value being numeric.

rule_2 = [{
        "ruleID": "rule2",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": 15.0,
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output2 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule2",
        }
    ],
}

def test_method_2():
  assert create_dataset(rule_2, data = dataset, org = organization) == output2

#Rule 3 filters rows based on a single column and single value being string.

rule_3 = [{
        "ruleID": "rule3",
        "table": "Sample",
        "variable": "type",
        "ruleValue": "swrSed",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output3 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule3",
        }
    ],
}

def test_method_3():
  assert create_dataset(rule_3, data = dataset, org = organization) == output3

#Rule 4 filters rows based on a single column and single value from each column or any of the columns being a datetime.

rule_4 = [{
        "ruleID": "rule4",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "2021-02-01 21:00:00",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output4 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule4",
        }
    ],
}

def test_method_4():
  assert create_dataset(rule_4, data = dataset, org = organization) == output4

#Rule 5 filters rows based on a single column and range interval for a numeric value with [] interval.

rule_5 = [{
        "ruleID": "rule5",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "[15.0,17.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output5 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule5",
        }
    ],
}

def test_method_5():
  assert create_dataset(rule_5, data = dataset, org = organization) == output5

#Rule 6 filters rows based on a single column and range interval for a numeric value with () interval.

rule_6 = [{
        "ruleID": "rule6",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "(15.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output6 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule6",
        }
    ],
}

def test_method_6():
  assert create_dataset(rule_6, data = dataset, org = organization) == output6

#Rule 7 filters rows based on a single column and range interval for a numeric value with (] interval.

rule_7 = [{
        "ruleID": "rule7",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "(15.0,18.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output7 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule7",
        }
    ],
}

def test_method_7():
  assert create_dataset(rule_7, data = dataset, org = organization) == output7

#Rule 8 filters rows based on a single column and range interval for a numeric value with [) interval.

rule_8 = [{
        "ruleID": "rule8",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "[15.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output8 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule8",
        }
    ],
}

def test_method_8():
  assert create_dataset(rule_8, data = dataset, org = organization) == output8

#Rule 9 filters rows based on a single column and range interval between datetime value with [] interval.

rule_9 = [{
        "ruleID": "rule9",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output9 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule9",
        }
    ],
}

def test_method_9():
  assert create_dataset(rule_9, data = dataset, org = organization) == output9

#Rule 10 filters rows based on a single column and range interval between datetime value with () interval.

rule_10 = [{
        "ruleID": "rule10",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-02-01 21:00:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]
  
output10 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule10",
        }
    ],
}

def test_method_10():
  assert create_dataset(rule_10, data = dataset, org = organization) == output10

#Rule 11 filters rows based on a single column and range interval between datetime value with (] interval.

rule_11 = [{
        "ruleID": "rule11",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output11 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule11",
        }
    ],
}

def test_method_11():
  assert create_dataset(rule_11, data = dataset, org = organization) == output11

#Rule 12 filters rows based on a single column and range interval between datetime value with [) interval.

rule_12 = [{
        "ruleID": "rule12",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output12 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule12",
        }
    ],
}

def test_method_12():
  assert create_dataset(rule_12, data = dataset, org = organization) == output12

#Rule 13 filters rows based on a single column and range interval between two value with () interval where lower bound is infinity.

rule_13 = [{
        "ruleID": "rule13",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(Inf,2021-01-27 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output13 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule13",
        }
    ],
}

def test_method_13():
  assert create_dataset(rule_13, data = dataset, org = organization) == output13

#Rule 14 filters rows based on a single column and range interval between two value with (] interval where lower bound is infinity.

rule_14 = [{
        "ruleID": "rule14",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(Inf,2021-01-27 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output14 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule14",
        }
    ],
}

def test_method_14():
  assert create_dataset(rule_14, data = dataset, org = organization) == output14

#Rule 15 filters rows based on a single column and range interval between two value with () interval where upper bound is infinity.

rule_15 = [{
        "ruleID": "rule15",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 08:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output15 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule15",
        }
    ],
}

def test_method_15():
  assert create_dataset(rule_15, data = dataset, org = organization) == output15

#Rule 16 filters rows based on a single column and range interval between two value with [) interval where upper bound is infinity.

rule_16 = [{
        "ruleID": "rule16",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-02-01 21:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output16 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule16",
        }
    ],
}

def test_method_16():
  assert create_dataset(rule_16, data = dataset, org = organization) == output16

#Rule 17 filters rows based on a single column and multiple values to filter by a single value and a range.

rule_17 = [{
        "ruleID": "rule17",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "15.0;(17.0,18.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output17 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule17",
        }
    ],
}

def test_method_17():
  assert create_dataset(rule_17, data = dataset, org = organization) == output17

# For SINGLE TABLE:
## MULTIPLE COLUMNS:

#Rule 18 filters all rows from more than 1 column from a single table.

rule_18 = [{
        "ruleID": "rule18",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]


output1 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule18",
        }
    ],
}

def test_method_18():
  assert create_dataset(rule_18, data = dataset, org = organization) == output18

#Rule 19 filters rows from multiple columns from a single table based on a single value from each column or any of the columns being a number. 

rule_19 = [{
        "ruleID": "rule19",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "15;22",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output17 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule19",
        }
    ],
}

def test_method_19():
  assert create_dataset(rule_19, data = dataset, org = organization) == output19

#Rule 20 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns being a string. 

rule_20 = [{
        "ruleID": "rule20",
        "table": "Sample",
        "variable": "type;collection",
        "ruleValue": "grb;pSludge",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output20 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule20",
        }
    ],
}

def test_method_20():
  assert create_dataset(rule_20, data = dataset, org = organization) == output20

#Rule 21 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns being a datetime. 

rule_21 = [{
        "ruleID": "rule21",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "2021-01-27 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output21 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule21",
        }
    ],
}

def test_method_21():
  assert create_dataset(rule_21, data = dataset, org = organization) == output21

#Rule 22 filters rows from multiple columns from a single table based on a single value from each column or any of the columns being an 
# interval between two numbers with [] interval 

rule_22 = [{
        "ruleID": "rule22",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "[15.0,17.0];[18,25]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output1 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule22",
        }
    ],
}

def test_method_22():
  assert create_dataset(rule_22, data = dataset, org = organization) == output22

#Rule 23 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns 
# being an interval between two numbers with () interval 

rule_23 = [{
        "ruleID": "rule23",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "(16.0,18.0);(17,25)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output23 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule23",
        }
    ],
}

def test_method_23():
  assert create_dataset(rule_23, data = dataset, org = organization) == output23   

#Rule 24 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns 
# being an interval between two numbers with (] interval 
 

rule_24 = [{
        "ruleID": "rule24",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "(15.0,18.0];(17,19]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output24 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule24",
        }
    ],
}

def test_method_24():
  assert create_dataset(rule_24, data = dataset, org = organization) == output24

#Rule 25 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns
# being an interval between two numbers with [) interval 

rule_25 = [{
        "ruleID": "rule25",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "[16.0,18.0);[17,19)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output25 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule25",
        }
    ],
}

def test_method_25():
  assert create_dataset(rule_25, data = dataset, org = organization) == output25

#Rule 26 filters rows from multiple columns from a single table based on a single value from each columns or any of the columns 
# being an interval between two datetime values with [] interval 

rule_26 = [{
        "ruleID": "rule26",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output26 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule26",
        }
    ],
}

def test_method_26():
  assert create_dataset(rule_26, data = dataset, org = organization) == output26

#Rule 27 filters rows from multiple columns from a single table based on a single value from each column or any of the columns
# being an interval between two datetime values with () interval 

rule_27 = [{
        "ruleID": "rule27",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-27 8:00,2021-01-30 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output27 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule27",
        }
    ],
}

def test_method_27():
  assert create_dataset(rule_27, data = dataset, org = organization) == output27

#Rule 28 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two datetime values with (] interval 

rule_28 = [{
        "ruleID": "rule28",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-27 8:00,2021-02-01 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output28 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule28",
        }
    ],
}

def test_method_28():
  assert create_dataset(rule_28, data = dataset, org = organization) == output28

#Rule 29 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two datetime values with [) interval 

rule_29 = [{
        "ruleID": "rule29",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-01-27 8:00,2021-01-30 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output29 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule29",
        }
    ],
}

def test_method_29():
  assert create_dataset(rule_29, data = dataset, org = organization) == output29

#Rule 30 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two values where the lower bound limit is infinity and with () interval

rule_30 = [{
        "ruleID": "rule30",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(Inf,2021-01-30 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output30 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule30",
        }
    ],
}

def test_method_30():
  assert create_dataset(rule_30, data = dataset, org = organization) == output30

#Rule 31 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two values where the lower bound limit is infinity and with (] interval

rule_31 = [{
        "ruleID": "rule31",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(Inf,2021-01-28 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output31 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule31",
        }
    ],
}

def test_method_31():
  assert create_dataset(rule_31, data = dataset, org = organization) == output31

#Rule 32 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two values where the upper bound limit is infinity and with () interval

rule_32 = [{
        "ruleID": "rule32",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-29 08:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output32 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule32",
        }
    ],
}

def test_method_32():
  assert create_dataset(rule_32, data = dataset, org = organization) == output32

#Rule 33 filters rows from multiple columns from a single table based on a single value from each column or any of the columns 
# being an interval between two values where the upper bound limit is infinity and with [) interval

rule_33 = [{
        "ruleID": "rule33",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-02-01 21:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output33 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule33",
        }
    ],
}

def test_method_33():
  assert create_dataset(rule_33, data = dataset, org = organization) == output33

#Rule 34 filters rows from multiple columns from a single table based on multiple values where one can be a single value 
# and other being an interval. 

rule_34 = [{
        "ruleID": "rule34",
        "table": "Sample",
        "variable": "type;dateTimeStart;dateTimeEnd;storageTempC",
        "ruleValue": "swrSed;[2021-01-25 8:00,2021-01-27 8:00);[16,17]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output34 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule34",
        }
    ],
}

def test_method_34():
  assert create_dataset(rule_34, data = dataset, org = organization) == output34

#SINGLE TABLE:
# ALL COLUMNS:

#Rule 35 filters all the rows from all column from a single table.

rule_35 = [{
        "ruleID": "rule35",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output35 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule35",
        }
    ],
}

def test_method_35():
  assert create_dataset(rule_35, data = dataset, org = organization) == output35

#Rule 36 filters rows from all columns from a single table based on a single value from each column or any of the columns being a number.

rule_36 = [{
        "ruleID": "rule36",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "10;22",
        "direction": "row",
        "sharedWith": "PHAC"
    }]

output36 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule36",
        }
    ],
}

def test_method_36():
  assert create_dataset(rule_36, data = dataset, org = organization) == output36

#Rule 37 filters rows from all columns from a single table based on a single value from each column or any of the columns being a string.

rule_37 = [{
        "ruleID": "rule37",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "Site T113;mooreSw;pSludge;",
        "direction": "row",
        "sharedWith": "PHAC"
    }]

output37 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule37",
        }
    ],
}

def test_method_37():
  assert create_dataset(rule_37, data = dataset, org = organization) == output37

#Rule 38 filters rows from all columns from a single table based on a single value from each column or any of the columns being a datetime.

rule_38 = [{
        "ruleID": "rule38",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "2021-02-28 21:00;2021-01-24 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output38 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule38",
        }
    ],
}

def test_method_38():
  assert create_dataset(rule_38, data = dataset, org = organization) == output38

#Rule 39 filters rows from all columns from a single table based on a single value from each column or any of the columns being an 
# interval between two numbers with [] interval.

rule_39 = [{
        "ruleID": "rule39_1",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0]",
        "direction": "row",
        "sharedWith": "PHAC"
    },{
        "ruleID": "rule39_2",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[16.0,18.0]",
        "direction": "row",
        "sharedWith": "PHAC"}
]

output39 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule39_1",
        },
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
            ],
            "rule_id": "rule39_2",
        },
    ],
}

def test_method_39():
  assert create_dataset(rule_39, data = dataset, org = organization) == output39

#Rule 40 filters rows from all columns from a single table based on a single value from each column or any of the columns 
# being an interval between two numbers with () interval.

rule_40 = [{
        "ruleID": "rule40",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0);(17,22)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output40 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule40",
        }
    ],
}

def test_method_40():
  assert create_dataset(rule_40, data = dataset, org = organization) == output40

#Rule 41 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two numbers with (] interval.

rule_41 = [{
        "ruleID": "rule41",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(8.0,10.0];(16,25]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output41 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule41",
        }
    ],
}

def test_method_41():
  assert create_dataset(rule_41, data = dataset, org = organization) == output41

#Rule 42 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two numbers with [) interval.

rule_42 = [{
        "ruleID": "rule42",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0);[19,25)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]


output42 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule42",
        }
    ],
}

def test_method_42():
  assert create_dataset(rule_42, data = dataset, org = organization) == output42

#Rule 43 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two datetime values with [] interval.

rule_43 = [{
        "ruleID": "rule43",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[2021-01-25 8:00,2021-01-29 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output43 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule43",
        }
    ],
}

def test_method_43():
  assert create_dataset(rule_43, data = dataset, org = organization) == output43

#Rule 44 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two datetime values with () interval.

rule_44 = [{
        "ruleID": "rule44",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2021-01-25 8:00,2021-01-30 8:00);(2021-01-29 21:00,2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "PHAC"
    }]

output44 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule44",
        }
    ],
}

def test_method_44():
  assert create_dataset(rule_44, data = dataset, org = organization) == output44

#Rule 45 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two datetime values with (] interval.

rule_45 = [{
        "ruleID": "rule45",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2021-01-25 8:00,2021-01-30 8:00];(2021-01-29 21:00,2021-02-01 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output45 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule45",
        }
    ],
}

def test_method_45():
  assert create_dataset(rule_45, data = dataset, org = organization) == output45

#Rule 46 filters rows from all columns from a single table based on a single value from each column or any of the columns
# being an interval between two datetime values with [) interval.

rule_46 = [{
        "ruleID": "rule46",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[2021-02-01 21:00,2021-02-04 21:00);[2021-01-28 08:00,2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output46 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule46",
        }
    ],
}

def test_method_46():
  assert create_dataset(rule_46, data = dataset, org = organization) == output46

#Rule 47 filters rows from all columns from a single table based on a single value 
# being an interval where the lower bound limit is infinity with (] interval

rule_47 = [{
        "ruleID": "rule47",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(Inf,2021-01-27 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output47 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule47",
        }
    ],
}

def test_method_47():
  assert create_dataset(rule_47, data = dataset, org = organization) == output47

#Rule 48 filters rows from all columns from a single table based on a single value
# being an interval where the lower bound limit is infinity with () interval

rule_48 = [{
        "ruleID": "rule48",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(Inf,2021-01-28 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output48 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule48",
        }
    ],
}

def test_method_48():
  assert create_dataset(rule_48, data = dataset, org = organization) == output48

#Rule 49 filters rows from all columns from a single table based on a single value 
# being an interval where the upper bound limit is infinity with () interval

rule_49 = [{
        "ruleID": "rule49",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(18,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output49 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule49",
        }
    ],
}

def test_method_49():
  assert create_dataset(rule_49, data = dataset, org = organization) == output49

#Rule 50 filters rows from all columns from a single table based on a single value being an interval 
# where the upper bound limit is infinity with [) interval

rule_50 = [{
        "ruleID": "rule50",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[19,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output50 = {
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
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule50",
        }
    ],
}

def test_method_50():
  assert create_dataset(rule_50, data = dataset, org = organization) == output50

#Rule 51 filters rows from all columns from a single table based on a multiple values where one can be an interval and other a value.

rule_51 = [{
        "ruleID": "rule51",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[19,25];(18,22);(2021-01-24 21:00,2021-02-01 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC"
    }]

output51 = {
    "filtered_data": {
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-08 00:00:00"),
                "assayID": "Assay Y100",
                "fractionAnalyzed": "solid",
                "index": 1,
                "instrumentID": "Instrument IN200",
                "labID": "Lab L100",
                "notes": "CovidN1 replicate measures linked by index",
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "reporterID": "Reporter R1",
                "sampleID": "Sample S100",
                "type": "covN1",
                "typeOther": nan,
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN1",
                "value": 20000,
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
            ],
            "rule_id": "rule51",
        }
    ],
}

def test_method_51():
  assert create_dataset(rule_51, data = dataset, org = organization) == output51