"""Testing multiple tables"""
import sys
from pandas import Timestamp

sys.path.append("..")  # Adds higher directory to python modules path.
from create_dataset import create_dataset


# User Data:

dataset = {
    "AssayMethod": [
        {
            "assayMethodID": "Assay Y101",
        }
    ],
    "Sample": [
        {
            "dateTime": Timestamp("2021-02-01 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
            "fieldSampleTempC": 15,
            "sizeL": 8,
            "storageTempC": 16,
            "sampleID": "Sample S100",
            "type": "swrSed",
            "collection": "mooreSw",
        },
        {
            "dateTime": Timestamp("2021-01-25 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
            "fieldSampleTempC": 17,
            "sizeL": 2,
            "storageTempC": 18,
            "sampleID": "Sample S106",
            "type": "pSludge",
            "collection": "cpTP24h",
        },
        {
            "dateTime": Timestamp("2021-01-28 21:00:00"),
            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
            "fieldSampleTempC": 18,
            "sizeL": 10,
            "storageTempC": 22,
            "sampleID": "Sample S107",
            "type": "rawWW",
            "collection": "grb",
        },
    ],
    "WWMeasure": [
        {
            "analysisDate": Timestamp("2021-01-25 00:00:00"),
            "reportDate": Timestamp("2021-02-06 00:00:00"),
            "type": "covN2",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcM",
            "unitOther": "gcMcovN2",
            "value": 145000,
        },
        {
            "analysisDate": Timestamp("2021-01-28 00:00:00"),
            "reportDate": Timestamp("2021-01-25 00:00:00"),
            "type": "covN2",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcMcovN1",
            "value": 16000,
        },
        {
            "analysisDate": Timestamp("2021-02-06 00:00:00"),
            "reportDate": Timestamp("2021-03-06 00:00:00"),
            "type": "nPMMoV",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcmnPMMoV",
            "value": 98000,
        },
    ],
}

# User requested ORG_NAME:
ORG_NAME = "PHAC"

# FOR MULTIPLE TABLES: Tables `Sample` and `WWMeasure` are used.
## FOR SINGLE COLUMN FROM EACH TABLE OR ANY OF THE TABLE

#

rule_52 = [
    {
        "ruleID": "rule52",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output52 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [],
        "WWMeasure": [],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule52",
        }
    ],
}


def test_method_52():
    """
    This method tests the function create_dataset against rule_52 with pytest.
    """
    assert create_dataset(rule_52, data=dataset, org=ORG_NAME) == output52


# Rule 53 filters rows based on a single column from each table and single
# value from each column or any of the columns being numeric.

rule_53 = [
    {
        "ruleID": "rule53",
        "table": "Sample;WWMeasure",
        "variable": "value;fieldSampleTempC",
        "ruleValue": "17.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output53 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule53",
        }
    ],
}


def test_method_53():
    """
    Rule 53 filters rows based on a single column from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_53, data=dataset, org=ORG_NAME) == output53


# Rule 54 filters rows based on a single column from each table and single
# value from each column or any of the columns being string.

rule_54 = [
    {
        "ruleID": "rule54",
        "table": "Sample;WWMeasure",
        "variable": "unitOther;type",
        "ruleValue": "gcMcovN1;pSludge",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output54 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule54",
        }
    ],
}


def test_method_54():
    """
    Rule 54 filters rows based on a single column from each table and single
     value from each column or any of the columns being string.
    """
    assert create_dataset(rule_54, data=dataset, org=ORG_NAME) == output54


# Rule 55 filters rows based on a single column from each table and single
# value from each column or any of the columns being datetime.

rule_55 = [
    {
        "ruleID": "rule55",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "2021-01-28 00:00:00;2021-01-28 21:00:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output55 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule55",
        }
    ],
}


def test_method_55():
    """
    Rule 55 filters rows based on a single column from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_55, data=dataset, org=ORG_NAME) == output55


# Rule 56 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with [].

rule_56 = [
    {
        "ruleID": "rule56",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[16000,98000];[16.0,17.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output56 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule56",
        }
    ],
}


def test_method_56():
    """
    Rule 56 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [].
    """
    assert create_dataset(rule_56, data=dataset, org=ORG_NAME) == output56


# Rule 57 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with ().

rule_57 = [
    {
        "ruleID": "rule57",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(85000,145000);(15.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output57 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule57",
        }
    ],
}


def test_method_57():
    """
    Rule 57 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with ().
    """
    assert create_dataset(rule_57, data=dataset, org=ORG_NAME) == output57


# Rule 58 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with (].

rule_58 = [
    {
        "ruleID": "rule58",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(85000,145000];(15.0,17.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]


output58 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule58",
        }
    ],
}


def test_method_58():
    """
    Rule 58 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with (].
    """
    assert create_dataset(rule_58, data=dataset, org=ORG_NAME) == output58


# Rule 59 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with [).

rule_59 = [
    {
        "ruleID": "rule59",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[76000,145000);[16.0,17.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output59 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule59",
        }
    ],
}


def test_method_59():
    """
    Rule 59 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [).
    """
    assert create_dataset(rule_59, data=dataset, org=ORG_NAME) == output59


# Rule 60 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with [].

rule_60 = [
    {
        "ruleID": "rule60",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "[2021-01-24 8:00 , 2021-01-30 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output60 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule60",
        }
    ],
}


def test_method_60():
    """
    Rule 60 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [].
    """
    assert create_dataset(rule_60, data=dataset, org=ORG_NAME) == output60


# Rule 61 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with ().

rule_61 = [
    {
        "ruleID": "rule61",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output61 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule61",
        }
    ],
}


def test_method_61():
    """
    Rule 61 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with ().
    """
    assert create_dataset(rule_61, data=dataset, org=ORG_NAME) == output61


# Rule 62 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with (].

rule_62 = [
    {
        "ruleID": "rule62",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "(2021-01-29 8:00,2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output62 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule62",
        }
    ],
}


def test_method_62():
    """
    Rule 62 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with (].
    """
    assert create_dataset(rule_62, data=dataset, org=ORG_NAME) == output62


# Rule 63 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with [).

rule_63 = [
    {
        "ruleID": "rule63",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "[2021-01-27,2021-02-02)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output63 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule63",
        }
    ],
}


def test_method_63():
    """
    Rule 63 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [).
    """
    assert create_dataset(rule_63, data=dataset, org=ORG_NAME) == output63


# Rule 64 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with ().

rule_64 = [
    {
        "ruleID": "rule64",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,2021-01-28 8:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output64 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {"rows_removed": [], "table": "WWMeasure"},
            ],
            "rule_id": "rule64",
        }
    ],
}


def test_method_64():
    """
    Rule 64 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_64, data=dataset, org=ORG_NAME) == output64


# Rule 65 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with (].

rule_65 = [
    {
        "ruleID": "rule65",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,72000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output65 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule65",
        }
    ],
}


def test_method_65():
    """
    Rule 65 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_65, data=dataset, org=ORG_NAME) == output65


# Rule 66 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with ().

rule_66 = [
    {
        "ruleID": "rule66",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(98000, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output66 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule66",
        }
    ],
}


def test_method_66():
    """
    Rule 66 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_66, data=dataset, org=ORG_NAME) == output66


# Rule 67 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with [).

rule_67 = [
    {
        "ruleID": "rule67",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "[2021-02-01 21:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output67 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {"rows_removed": [], "table": "WWMeasure"},
            ],
            "rule_id": "rule67",
        }
    ],
}


def test_method_67():
    """
    Rule 67 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_67, data=dataset, org=ORG_NAME) == output67


# Rule 68 filters rows based on a single column from each table and multiple
# values from each column or any of the columns where one value could be
# an interval and other a single value.

rule_68 = [
    {
        "ruleID": "rule68",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "[2021-02-01 21:00, 2021-02-06 21:00]; 16000; 2021-01-24 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output68 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule68",
        }
    ],
}


def test_method_68():
    """
    Rule 68 filters rows based on a single column from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and other a single value.
    """
    assert create_dataset(rule_68, data=dataset, org=ORG_NAME) == output68


# For MULTIPLE TABLES:
## MULTIPLE COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 69 filters rows based on multiple columns and all values of the rows.

rule_69 = [
    {
        "ruleID": "rule69",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart;analysisDate",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output69 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [],
        "WWMeasure": [],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule69",
        }
    ],
}


def test_method_69():
    """
    Rule 69 filters rows based on multiple columns and all values of the rows.
    """
    assert create_dataset(rule_69, data=dataset, org=ORG_NAME) == output69


# Rule 70 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being numeric.

rule_70 = [
    {
        "ruleID": "rule70",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "16.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output70 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule70",
        }
    ],
}


def test_method_70():
    """
    Rule 70 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_70, data=dataset, org=ORG_NAME) == output70


# Rule 71 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being string.

rule_71 = [
    {
        "ruleID": "rule71",
        "table": "Sample;WWMeasure",
        "variable": "unitOther; type; collection",
        "ruleValue": "rawWW; gcMcovN2",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output71 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule71",
        }
    ],
}


def test_method_71():
    """
    Rule 71 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being string.
    """
    assert create_dataset(rule_71, data=dataset, org=ORG_NAME) == output71


# Rule 72 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being datetime.

rule_72 = [
    {
        "ruleID": "rule72",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate; dateTimeStart; dateTimeEnd",
        "ruleValue": "2021-01-25 ; 2021-01-27 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output72 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule72",
        }
    ],
}


def test_method_72():
    """
    Rule 72 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_72, data=dataset, org=ORG_NAME) == output72


# Rule 73 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [].

rule_73 = [
    {
        "ruleID": "rule73",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "[16.0, 17.0]; [98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output73 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule73",
        }
    ],
}


def test_method_73():
    """
    Rule 73 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [].
    """
    assert create_dataset(rule_73, data=dataset, org=ORG_NAME) == output73


# Rule 74 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with ().

rule_74 = [
    {
        "ruleID": "rule74",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "(15.0, 17.0); (85000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output74 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule74",
        }
    ],
}


def test_method_74():
    """
    Rule 74 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with ().
    """
    assert create_dataset(rule_74, data=dataset, org=ORG_NAME) == output74


# Rule 75 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with (].

rule_75 = [
    {
        "ruleID": "rule75",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "(15.0, 17.0]; (16000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output75 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule75",
        }
    ],
}


def test_method_75():
    """
    Rule 75 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with (].
    """
    assert create_dataset(rule_75, data=dataset, org=ORG_NAME) == output75


# Rule 76 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [).

rule_76 = [
    {
        "ruleID": "rule76",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC",
        "ruleValue": "[16.0, 17.0); [98000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output76 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule76",
        }
    ],
}


def test_method_76():
    """
    Rule 76 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [).
    """
    assert create_dataset(rule_76, data=dataset, org=ORG_NAME) == output76


# Rule 77 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [].

rule_77 = [
    {
        "ruleID": "rule77",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": " [2021-01-27,2021-01-30]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output77 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule77",
        }
    ],
}


def test_method_77():
    """
    Rule 77 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [].
    """
    assert create_dataset(rule_77, data=dataset, org=ORG_NAME) == output77


# Rule 78 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with ().

rule_78 = [
    {
        "ruleID": "rule78",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output78 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule78",
        }
    ],
}


def test_method_78():
    """
    Rule 78 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with ().
    """
    assert create_dataset(rule_78, data=dataset, org=ORG_NAME) == output78


# Rule 79 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with (].

rule_79 = [
    {
        "ruleID": "rule79",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output79 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule79",
        }
    ],
}


def test_method_79():
    """
    Rule 79 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with (].
    """
    assert create_dataset(rule_79, data=dataset, org=ORG_NAME) == output79


# Rule 80 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [).

rule_80 = [
    {
        "ruleID": "rule80",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "[2021-01-29 00:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output80 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule80",
        }
    ],
}


def test_method_80():
    """
    Rule 80 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [).
    """
    assert create_dataset(rule_80, data=dataset, org=ORG_NAME) == output80


# Rule 81 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_81 = [
    {
        "ruleID": "rule81",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "(Inf, 2021-01-31)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output81 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule81",
        }
    ],
}


def test_method_81():
    """
    Rule 81 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_81, data=dataset, org=ORG_NAME) == output81


# Rule 82 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_82 = [
    {
        "ruleID": "rule82",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "(Inf , 2021-01-28 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output82 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule82",
        }
    ],
}


def test_method_82():
    """
    Rule 82 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_82, data=dataset, org=ORG_NAME) == output82


# Rule 83 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_83 = [
    {
        "ruleID": "rule83",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "(2021-01-25, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output83 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule83",
        }
    ],
}


def test_method_83():
    """
    Rule 83 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_83, data=dataset, org=ORG_NAME) == output83


# Rule 84 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_84 = [
    {
        "ruleID": "rule84",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "[2021-02-01 21:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output84 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule84",
        }
    ],
}


def test_method_84():
    """
    Rule 84 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_84, data=dataset, org=ORG_NAME) == output84


# Rule 85 filters rows based on multiple columns from each table and multiple
# values from each column or any of the columns where one value could be an
# interval and the other could be a single value.

rule_85 = [
    {
        "ruleID": "rule85",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;value;analysisDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00] ; 145000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output85 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule85",
        }
    ],
}


def test_method_85():
    """
    Rule 85 filters rows based on multiple columns from each table and multiple
    values from each column or any of the columns where one value could be an
    interval and the other could be a single value.
    """
    assert create_dataset(rule_85, data=dataset, org=ORG_NAME) == output85


# For MULTIPLE TABLES:
## ALL COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 86 filters rows based on all columns from each table and all values of
# the rows.

rule_86 = [
    {
        "ruleID": "rule86",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output86 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [],
        "WWMeasure": [],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "rows_removed": [
                        {
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule86",
        }
    ],
}


def test_method_86():
    """
    Rule 86 filters rows based on all columns from each table and all values
    of the rows.
    """
    assert create_dataset(rule_86, data=dataset, org=ORG_NAME) == output86


# Rule 87 filters rows based on all columns from each table and single value
# from each column or any of the columns being numeric.

rule_87 = [
    {
        "ruleID": "rule87",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "17.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output87 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule87",
        }
    ],
}


def test_method_87():
    """
    Rule 87 filters rows based on all columns from each table and single value
    from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_87, data=dataset, org=ORG_NAME) == output87


# Rule 88 filters rows based on all columns from each table and single value
# from each column or any of the columns being string.

rule_88 = [
    {
        "ruleID": "rule88",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "gcmnPMMoV; pSludge; grb;gcM",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output88 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule88",
        }
    ],
}


def test_method_88():
    """
    Rule 88 filters rows based on all columns from each table and single value
    from each column or any of the columns being string.
    """
    assert create_dataset(rule_88, data=dataset, org=ORG_NAME) == output88


# Rule 89 filters rows based on all columns from each table and single value
# from each column or any of the columns being datetime.

rule_89 = [
    {
        "ruleID": "rule89",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "2021-02-01 21:00; 2021-01-25",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output89 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule89",
        }
    ],
}


def test_method_89():
    """
    Rule 89 filters rows based on all columns from each table and single value
    from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_89, data=dataset, org=ORG_NAME) == output89


# Rule 90 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with [].

rule_90 = [
    {
        "ruleID": "rule90",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0];[16.0,17.0];[98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output90 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule90",
        }
    ],
}


def test_method_90():
    """
    Rule 90 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [].
    """
    assert create_dataset(rule_90, data=dataset, org=ORG_NAME) == output90


# Rule 91 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with ().

rule_91 = [
    {
        "ruleID": "rule91",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0);(15.0,17.0);(16000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output91 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        }
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule91",
        }
    ],
}


def test_method_91():
    """
    Rule 91 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with ().
    """
    assert create_dataset(rule_91, data=dataset, org=ORG_NAME) == output91


# Rule 92 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with (].

rule_92 = [
    {
        "ruleID": "rule92",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0];(98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output92 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule92",
        }
    ],
}


def test_method_92():
    """
    Rule 92 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with (].
    """
    assert create_dataset(rule_92, data=dataset, org=ORG_NAME) == output92


# Rule 93 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with [).

rule_93 = [
    {
        "ruleID": "rule93",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0);[16.0,18.0);[98000,102000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output93 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule93",
        }
    ],
}


def test_method_93():
    """
    Rule 93 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [).
    """
    assert create_dataset(rule_93, data=dataset, org=ORG_NAME) == output93


# Rule 94 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with [].

rule_94 = [
    {
        "ruleID": "rule94",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[2021-01-27,2021-01-31]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output94 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule94",
        }
    ],
}


def test_method_94():
    """
    Rule 94 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [].
    """
    assert create_dataset(rule_94, data=dataset, org=ORG_NAME) == output94


# Rule 95 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with ().

rule_95 = [
    {
        "ruleID": "rule95",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(2021-01-29 8:00, 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output95 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule95",
        }
    ],
}


def test_method_95():
    """
    Rule 95 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with ().
    """
    assert create_dataset(rule_95, data=dataset, org=ORG_NAME) == output95


# Rule 96 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with [).

rule_96 = [
    {
        "ruleID": "rule96",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[2021-01-27 8:00, 2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output96 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule96",
        }
    ],
}


def test_method_96():
    """
    Rule 96 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [).
    """
    assert create_dataset(rule_96, data=dataset, org=ORG_NAME) == output96


# Rule 97 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with (].

rule_97 = [
    {
        "ruleID": "rule97",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(2021-01-26,2021-02-02];",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output97 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule97",
        }
    ],
}


def test_method_97():
    """
    Rule 97 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with (].
    """
    assert create_dataset(rule_97, data=dataset, org=ORG_NAME) == output97


# Rule 98 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_98 = [
    {
        "ruleID": "rule98",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(Inf , 8.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output98 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {"rows_removed": [], "table": "WWMeasure"},
            ],
            "rule_id": "rule98",
        }
    ],
}


def test_method_98():
    """
    Rule 98 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_98, data=dataset, org=ORG_NAME) == output98


# Rule 99 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_99 = [
    {
        "ruleID": "rule99",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(Inf , 4.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output99 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-25 00:00:00"),
                "reportDate": Timestamp("2021-02-06 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcM",
                "unitOther": "gcMcovN2",
                "value": 145000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
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
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sizeL": 2,
                            "storageTempC": 18,
                            "sampleID": "Sample S106",
                            "type": "pSludge",
                            "collection": "cpTP24h",
                        }
                    ],
                    "table": "Sample",
                },
                {"rows_removed": [], "table": "WWMeasure"},
            ],
            "rule_id": "rule99",
        }
    ],
}


def test_method_99():
    """
    Rule 99 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_99, data=dataset, org=ORG_NAME) == output99


# Rule 100 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_100 = [
    {
        "ruleID": "rule100",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(92000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output100 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule100",
        }
    ],
}


def test_method_100():
    """
    Rule 100 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_100, data=dataset, org=ORG_NAME) == output100


# Rule 101 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_101 = [
    {
        "ruleID": "rule101",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[98000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output101 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                {"rows_removed": [], "table": "Sample"},
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule101",
        }
    ],
}


def test_method_101():
    """
    Rule 101 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_101, data=dataset, org=ORG_NAME) == output101


# Rule 102 filters rows based on all columns from each table and multiple
# values from each column or any of the columns where one value could be
# an interval and the other could be a single value.

rule_102 = [
    {
        "ruleID": "rule102",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00] ; 145000;[98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output102 = {
    "filtered_data": {
        "AssayMethod": [
            {
                "assayMethodID": "Assay Y101",
            }
        ],
        "Sample": [
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            }
        ],
        "WWMeasure": [
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
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
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sizeL": 8,
                            "storageTempC": 16,
                            "sampleID": "Sample S100",
                            "type": "swrSed",
                            "collection": "mooreSw",
                        },
                        {
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sizeL": 10,
                            "storageTempC": 22,
                            "sampleID": "Sample S107",
                            "type": "rawWW",
                            "collection": "grb",
                        },
                    ],
                    "table": "Sample",
                },
                {
                    "rows_removed": [
                        {
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule102",
        }
    ],
}


def test_method_102():
    """
    Rule 102 filters rows based on all columns from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and the other could be a single value.
    """
    assert create_dataset(rule_102, data=dataset, org=ORG_NAME) == output102
