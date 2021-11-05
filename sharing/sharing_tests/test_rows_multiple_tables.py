"""Testing multiple tables"""
import sys
from pandas import Timestamp

sys.path.append("..")  # Adds higher directory to python modules path.
from create_dataset import create_dataset


# User Data:

dataset = {
    "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
            "index": 160000,
        },
        {
            "analysisDate": Timestamp("2021-01-28 00:00:00"),
            "reportDate": Timestamp("2021-01-25 00:00:00"),
            "type": "covN2",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcMcovN1",
            "value": 16000,
            "index": 170000,
        },
        {
            "analysisDate": Timestamp("2021-02-06 00:00:00"),
            "reportDate": Timestamp("2021-03-06 00:00:00"),
            "type": "nPMMoV",
            "uWwMeasureID": "Measure WW100",
            "unit": "gcMl",
            "unitOther": "gcmnPMMoV",
            "value": 98000,
            "index": 180000,
        },
    ],
}

# User requested ORG_NAME:
ORG_NAME = "PHAC"

# FOR MULTIPLE TABLES: Tables `Sample` and `WWMeasure` are used.
## FOR SINGLE COLUMN FROM EACH TABLE OR ANY OF THE TABLE

# Rule 52 filters rows of each table by a single column and all values.
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

output_52 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule52",
        }
    ],
}


def test_multiple_table_single_column_all_values():
    """
    Rule 52 filters rows of each table by a single column and all values.
    """
    assert create_dataset(rule_52, data=dataset, org=ORG_NAME) == output_52


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

output_53 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule53",
        }
    ],
}


def test_multiple_table_single_column_single_value_numeric():
    """
    Rule 53 filters rows based on a single column from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_53, data=dataset, org=ORG_NAME) == output_53


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

output_54 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule54",
        }
    ],
}


def test_multiple_table_single_column_single_value_string():
    """
    Rule 54 filters rows based on a single column from each table and single
     value from each column or any of the columns being string.
    """
    assert create_dataset(rule_54, data=dataset, org=ORG_NAME) == output_54


# Rule 55 filters rows based on a single column from each table and single
# value from each column or any of the columns being datetime.

rule_55 = [
    {
        "ruleID": "rule55",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "2021-01-28 00:00:00;2021-01-24 08:00:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_55 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule55",
        }
    ],
}


def test_multiple_table_single_column_single_value_datetime():
    """
    Rule 55 filters rows based on a single column from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_55, data=dataset, org=ORG_NAME) == output_55


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

output_56 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
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
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule56",
        }
    ],
}


def test_multiple_table_single_column_interval_closed_closed_numeric():
    """
    Rule 56 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [].
    """
    assert create_dataset(rule_56, data=dataset, org=ORG_NAME) == output_56


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

output_57 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule57",
        }
    ],
}


def test_multiple_table_single_column_interval_open_open_numeric():
    """
    Rule 57 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with ().
    """
    assert create_dataset(rule_57, data=dataset, org=ORG_NAME) == output_57


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


output_58 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule58",
        }
    ],
}


def test_multiple_table_single_column_interval_open_closed_numeric():
    """
    Rule 58 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with (].
    """
    assert create_dataset(rule_58, data=dataset, org=ORG_NAME) == output_58


# Rule 59 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with [).

rule_59 = [
    {
        "ruleID": "rule59",
        "table": "Sample;WWMeasure",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[76000,145000);[15.0,17.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_59 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule59",
        }
    ],
}


def test_multiple_table_single_column_interval_closed_open_numeric():
    """
    Rule 59 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [).
    """
    assert create_dataset(rule_59, data=dataset, org=ORG_NAME) == output_59


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

output_60 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule60",
        }
    ],
}


def test_multiple_table_single_column_interval_closed_closed_datetime():
    """
    Rule 60 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [].
    """
    assert create_dataset(rule_60, data=dataset, org=ORG_NAME) == output_60


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

output_61 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule61",
        }
    ],
}


def test_multiple_table_single_column_interval_open_open_datetime():
    """
    Rule 61 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with ().
    """
    assert create_dataset(rule_61, data=dataset, org=ORG_NAME) == output_61


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

output_62 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule62",
        }
    ],
}


def test_multiple_table_single_column_interval_open_closed_datetime():
    """
    Rule 62 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with (].
    """
    assert create_dataset(rule_62, data=dataset, org=ORG_NAME) == output_62


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

output_63 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule63",
        }
    ],
}


def test_multiple_table_single_column_interval_closed_open_datetime():
    """
    Rule 63 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [).
    """
    assert create_dataset(rule_63, data=dataset, org=ORG_NAME) == output_63


# Rule 64 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with ().

rule_64 = [
    {
        "ruleID": "rule64",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,2021-01-28 8:00);(Inf, 17000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_64 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule64",
        }
    ],
}


def test_multiple_table_single_column_interval_open_open_lower_inf():
    """
    Rule 64 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_64, data=dataset, org=ORG_NAME) == output_64


# Rule 65 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with (].

rule_65 = [
    {
        "ruleID": "rule65",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,72000]; (Inf, 2021-01-24 08:00:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_65 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule65",
        }
    ],
}


def test_multiple_table_single_column_interval_open_closed_lower_inf():
    """
    Rule 65 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_65, data=dataset, org=ORG_NAME) == output_65


# Rule 66 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with ().

rule_66 = [
    {
        "ruleID": "rule66",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "(98000, Inf);(2021-01-27 08:00:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_66 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                            "index": 160000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule66",
        }
    ],
}


def test_multiple_table_single_column_interval_open_open_upper_inf():
    """
    Rule 66 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_66, data=dataset, org=ORG_NAME) == output_66


# Rule 67 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with [).

rule_67 = [
    {
        "ruleID": "rule67",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart",
        "ruleValue": "[2021-02-01 21:00, Inf);[145000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_67 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                            "index": 160000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule67",
        }
    ],
}


def test_multiple_table_single_column_interval_closed_open_upper_inf():
    """
    Rule 67 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_67, data=dataset, org=ORG_NAME) == output_67


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

output_68 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule68",
        }
    ],
}


def test_multiple_table_single_column_multiple_values():
    """
    Rule 68 filters rows based on a single column from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and other a single value.
    """
    assert create_dataset(rule_68, data=dataset, org=ORG_NAME) == output_68


# For MULTIPLE TABLES:
## MULTIPLE COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 69 filters rows based on multiple columns and all values of the rows.

rule_69 = [
    {
        "ruleID": "rule69",
        "table": "Sample;WWMeasure",
        "variable": "value;dateTimeStart;analysisDate;dateTimeEnd",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_69 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule69",
        }
    ],
}


def test_multiple_table_multiple_column_all_values():
    """
    Rule 69 filters rows based on multiple columns and all values of the rows.
    """
    assert create_dataset(rule_69, data=dataset, org=ORG_NAME) == output_69


# Rule 70 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being numeric.

rule_70 = [
    {
        "ruleID": "rule70",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC;index",
        "ruleValue": "16.0;98000;170000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_70 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
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
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule70",
        }
    ],
}


def test_multiple_table_multiple_column_single_value_numeric():
    """
    Rule 70 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_70, data=dataset, org=ORG_NAME) == output_70


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

output_71 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 160000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule71",
        }
    ],
}


def test_multiple_table_multiple_column_single_value_string():
    """
    Rule 71 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being string.
    """
    assert create_dataset(rule_71, data=dataset, org=ORG_NAME) == output_71


# Rule 72 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being datetime.

rule_72 = [
    {
        "ruleID": "rule72",
        "table": "Sample;WWMeasure",
        "variable": "analysisDate; dateTimeStart; dateTimeEnd; reportDate",
        "ruleValue": "2021-01-25 ; 2021-01-27 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_72 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule72",
        }
    ],
}


def test_multiple_table_multiple_column_single_value_datetime():
    """
    Rule 72 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_72, data=dataset, org=ORG_NAME) == output_72


# Rule 73 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [].

rule_73 = [
    {
        "ruleID": "rule73",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "[16.0, 17.0]; [98000,145000]; [175000, 180000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_73 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule73",
        }
    ],
}


def test_multiple_table_multiple_column_interval_closed_closed_numeric():
    """
    Rule 73 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [].
    """
    assert create_dataset(rule_73, data=dataset, org=ORG_NAME) == output_73


# Rule 74 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with ().

rule_74 = [
    {
        "ruleID": "rule74",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "(15.0, 17.0); (85000,145000); (170000,190000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_74 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule74",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_open_numeric():
    """
    Rule 74 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with ().
    """
    assert create_dataset(rule_74, data=dataset, org=ORG_NAME) == output_74


# Rule 75 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with (].

rule_75 = [
    {
        "ruleID": "rule75",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "(15.0, 17.0]; (16000,145000]; (170000,180000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_75 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule75",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_closed_numeric():
    """
    Rule 75 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with (].
    """
    assert create_dataset(rule_75, data=dataset, org=ORG_NAME) == output_75


# Rule 76 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [).

rule_76 = [
    {
        "ruleID": "rule76",
        "table": "Sample;WWMeasure",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "[16.0, 17.0); [98000,145000); [170000,180000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_76 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
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
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule76",
        }
    ],
}


def test_multiple_table_multiple_column_interval_closed_open_numeric():
    """
    Rule 76 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [).
    """
    assert create_dataset(rule_76, data=dataset, org=ORG_NAME) == output_76


# Rule 77 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [].

rule_77 = [
    {
        "ruleID": "rule77",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": " [2021-01-27,2021-01-30]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_77 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule77",
        }
    ],
}


def test_multiple_table_multiple_column_interval_closed_closed_datetime():
    """
    Rule 77 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [].
    """
    assert create_dataset(rule_77, data=dataset, org=ORG_NAME) == output_77


# Rule 78 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with ().

rule_78 = [
    {
        "ruleID": "rule78",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_78 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule78",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_open_datetime():
    """
    Rule 78 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with ().
    """
    assert create_dataset(rule_78, data=dataset, org=ORG_NAME) == output_78


# Rule 79 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with (].

rule_79 = [
    {
        "ruleID": "rule79",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_79 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule79",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_closed_datetime():
    """
    Rule 79 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with (].
    """
    assert create_dataset(rule_79, data=dataset, org=ORG_NAME) == output_79


# Rule 80 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [).

rule_80 = [
    {
        "ruleID": "rule80",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "[2021-01-29 00:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_80 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule80",
        }
    ],
}


def test_multiple_table_multiple_column_interval_closed_open_datetime():
    """
    Rule 80 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [).
    """
    assert create_dataset(rule_80, data=dataset, org=ORG_NAME) == output_80


# Rule 81 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_81 = [
    {
        "ruleID": "rule81",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "(Inf, 2021-01-31)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_81 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule81",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_open_lower_inf():
    """
    Rule 81 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_81, data=dataset, org=ORG_NAME) == output_81


# Rule 82 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_82 = [
    {
        "ruleID": "rule82",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "(Inf , 2021-01-28 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_82 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule82",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_closed_lower_inf():
    """
    Rule 82 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_82, data=dataset, org=ORG_NAME) == output_82


# Rule 83 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_83 = [
    {
        "ruleID": "rule83",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "(2021-01-25, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_83 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule83",
        }
    ],
}


def test_multiple_table_multiple_column_interval_open_open_upper_inf():
    """
    Rule 83 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_83, data=dataset, org=ORG_NAME) == output_83


# Rule 84 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_84 = [
    {
        "ruleID": "rule84",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "[2021-02-01 21:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_84 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule84",
        }
    ],
}


def test_multiple_table_multiple_column_interval_closed_open_upper_inf():
    """
    Rule 84 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_84, data=dataset, org=ORG_NAME) == output_84


# Rule 85 filters rows based on multiple columns from each table and multiple
# values from each column or any of the columns where one value could be an
# interval and the other could be a single value.

rule_85 = [
    {
        "ruleID": "rule85",
        "table": "Sample;WWMeasure",
        "variable": "dateTimeStart;value;analysisDate;fieldSampleTempC",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00] ; 145000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_85 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule85",
        }
    ],
}


def test_multiple_table_multiple_column_multiple_values():
    """
    Rule 85 filters rows based on multiple columns from each table and multiple
    values from each column or any of the columns where one value could be an
    interval and the other could be a single value.
    """
    assert create_dataset(rule_85, data=dataset, org=ORG_NAME) == output_85


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

output_86 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule86",
        }
    ],
}


def test_multiple_table_all_columns_all_values():
    """
    Rule 86 filters rows based on all columns from each table and all values
    of the rows.
    """
    assert create_dataset(rule_86, data=dataset, org=ORG_NAME) == output_86


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

output_87 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule87",
        }
    ],
}


def test_multiple_table_all_columns_single_value_numeric():
    """
    Rule 87 filters rows based on all columns from each table and single value
    from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_87, data=dataset, org=ORG_NAME) == output_87


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

output_88 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule88",
        }
    ],
}


def test_multiple_table_all_columns_single_value_string():
    """
    Rule 88 filters rows based on all columns from each table and single value
    from each column or any of the columns being string.
    """
    assert create_dataset(rule_88, data=dataset, org=ORG_NAME) == output_88


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

output_89 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 180000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule89",
        }
    ],
}


def test_multiple_table_all_columns_single_value_datetime():
    """
    Rule 89 filters rows based on all columns from each table and single value
    from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_89, data=dataset, org=ORG_NAME) == output_89


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

output_90 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule90",
        }
    ],
}


def test_multiple_table_all_columns_interval_closed_closed_numeric():
    """
    Rule 90 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [].
    """
    assert create_dataset(rule_90, data=dataset, org=ORG_NAME) == output_90


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

output_91 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule91",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_open_numeric():
    """
    Rule 91 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with ().
    """
    assert create_dataset(rule_91, data=dataset, org=ORG_NAME) == output_91


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

output_92 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 160000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule92",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_closed_numeric():
    """
    Rule 92 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with (].
    """
    assert create_dataset(rule_92, data=dataset, org=ORG_NAME) == output_92


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

output_93 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-01-28 00:00:00"),
                "reportDate": Timestamp("2021-01-25 00:00:00"),
                "type": "covN2",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcMcovN1",
                "value": 16000,
                "index": 170000,
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
                            "index": 180000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule93",
        }
    ],
}


def test_multiple_table_all_columns_interval_closed_open_numeric():
    """
    Rule 93 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [).
    """
    assert create_dataset(rule_93, data=dataset, org=ORG_NAME) == output_93


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

output_94 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule94",
        }
    ],
}


def test_multiple_table_all_columns_interval_closed_closed_datetime():
    """
    Rule 94 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [].
    """
    assert create_dataset(rule_94, data=dataset, org=ORG_NAME) == output_94


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

output_95 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule95",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_open_datetime():
    """
    Rule 95 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with ().
    """
    assert create_dataset(rule_95, data=dataset, org=ORG_NAME) == output_95


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

output_96 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule96",
        }
    ],
}


def test_multiple_table_all_columns_interval_closed_open_datetime():
    """
    Rule 96 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [).
    """
    assert create_dataset(rule_96, data=dataset, org=ORG_NAME) == output_96


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

output_97 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 160000,
            },
            {
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "index": 170000,
                        }
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule97",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_closed_datetime():
    """
    Rule 97 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with (].
    """
    assert create_dataset(rule_97, data=dataset, org=ORG_NAME) == output_97


# Rule 98 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_98 = [
    {
        "ruleID": "rule98",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(Inf , 8.0);(Inf,2021-01-26 00:00:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_98 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule98",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_open_lower_inf():
    """
    Rule 98 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_98, data=dataset, org=ORG_NAME) == output_98


# Rule 99 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_99 = [
    {
        "ruleID": "rule99",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(Inf , 4.0];(Inf,2021-01-26 08:00:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_99 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "analysisDate": Timestamp("2021-02-06 00:00:00"),
                "reportDate": Timestamp("2021-03-06 00:00:00"),
                "type": "nPMMoV",
                "uWwMeasureID": "Measure WW100",
                "unit": "gcMl",
                "unitOther": "gcmnPMMoV",
                "value": 98000,
                "index": 180000,
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
                            "analysisDate": Timestamp("2021-01-25 00:00:00"),
                            "reportDate": Timestamp("2021-02-06 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcM",
                            "unitOther": "gcMcovN2",
                            "value": 145000,
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule99",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_closed_lower_inf():
    """
    Rule 99 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_99, data=dataset, org=ORG_NAME) == output_99


# Rule 100 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_100 = [
    {
        "ruleID": "rule100",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "(92000,Inf);(2021-02-01 08:00:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_100 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule100",
        }
    ],
}


def test_multiple_table_all_columns_interval_open_open_upper_inf():
    """
    Rule 100 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_100, data=dataset, org=ORG_NAME) == output_100


# Rule 101 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_101 = [
    {
        "ruleID": "rule101",
        "table": "Sample;WWMeasure",
        "variable": "ALL",
        "ruleValue": "[98000,Inf);[2021-02-01 21:00:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_101 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-01-28 00:00:00"),
                            "reportDate": Timestamp("2021-01-25 00:00:00"),
                            "type": "covN2",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcMcovN1",
                            "value": 16000,
                            "index": 170000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule101",
        }
    ],
}


def test_multiple_table_all_columns_interval_closed_open_upper_inf():
    """
    Rule 101 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_101, data=dataset, org=ORG_NAME) == output_101


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

output_102 = {
    "filtered_data": {
        "AssayMethod": [{"assayMethodID": "Assay Y101",}],
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
                "index": 170000,
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
                            "index": 160000,
                        },
                        {
                            "analysisDate": Timestamp("2021-02-06 00:00:00"),
                            "reportDate": Timestamp("2021-03-06 00:00:00"),
                            "type": "nPMMoV",
                            "uWwMeasureID": "Measure WW100",
                            "unit": "gcMl",
                            "unitOther": "gcmnPMMoV",
                            "value": 98000,
                            "index": 180000,
                        },
                    ],
                    "table": "WWMeasure",
                },
            ],
            "rule_id": "rule102",
        }
    ],
}


def test_multiple_table_all_columns_multiple_values():
    """
    Rule 102 filters rows based on all columns from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and the other could be a single value.
    """
    assert create_dataset(rule_102, data=dataset, org=ORG_NAME) == output_102

