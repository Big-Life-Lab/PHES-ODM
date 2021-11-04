"""Testing multiple tables"""
import sys
from pandas import Timestamp

sys.path.append("..")  # Adds higher directory to python modules path.
from create_dataset import create_dataset


# User Data:


dataset = {
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

# Rule 103 filters rows of each table by a single column and all values.

rule_103 = [
    {
        "ruleID": "rule103",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_103 = {
    "filtered_data": {"Sample": [], "WWMeasure": [],},
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
            "rule_id": "rule103",
        }
    ],
}


def test_all_table_single_column_all_values():
    """
    Rule 103 filters rows of each table by a single column and all values.
    """
    assert create_dataset(rule_103, data=dataset, org=ORG_NAME) == output_103


# Rule 104 filters rows based on a single column from each table and single
# value from each column or any of the columns being numeric.

rule_104 = [
    {
        "ruleID": "rule104",
        "table": "ALL",
        "variable": "value;fieldSampleTempC",
        "ruleValue": "17.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_104 = {
    "filtered_data": {
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
            "rule_id": "rule104",
        }
    ],
}


def test_all_table_single_column_single_value_numeric():
    """
    Rule 104 filters rows based on a single column from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_104, data=dataset, org=ORG_NAME) == output_104


# Rule 105 filters rows based on a single column from each table and single
# value from each column or any of the columns being string.

rule_105 = [
    {
        "ruleID": "rule105",
        "table": "ALL",
        "variable": "unitOther;type",
        "ruleValue": "gcMcovN1;pSludge",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_105 = {
    "filtered_data": {
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
            "rule_id": "rule105",
        }
    ],
}


def test_all_table_single_column_single_value_string():
    """
    Rule 105 filters rows based on a single column from each table and single
     value from each column or any of the columns being string.
    """
    assert create_dataset(rule_105, data=dataset, org=ORG_NAME) == output_105


# Rule 106 filters rows based on a single column from each table and single
# value from each column or any of the columns being datetime.

rule_106 = [
    {
        "ruleID": "rule106",
        "table": "ALL",
        "variable": "dateTimeStart;analysisDate",
        "ruleValue": "2021-01-28 00:00:00;2021-01-24 08:00:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_106 = {
    "filtered_data": {
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
            "rule_id": "rule106",
        }
    ],
}


def test_all_table_single_column_single_value_datetime():
    """
    Rule 106 filters rows based on a single column from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_106, data=dataset, org=ORG_NAME) == output_106


# Rule 107 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with [].

rule_107 = [
    {
        "ruleID": "rule107",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[16000,98000];[16.0,17.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_107 = {
    "filtered_data": {
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
            "rule_id": "rule107",
        }
    ],
}


def test_all_table_single_column_interval_closed_closed_numeric():
    """
    Rule 107 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [].
    """
    assert create_dataset(rule_107, data=dataset, org=ORG_NAME) == output_107


# Rule 108 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with ().

rule_108 = [
    {
        "ruleID": "rule108",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(85000,145000);(15.0,18.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_108 = {
    "filtered_data": {
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
            "rule_id": "rule108",
        }
    ],
}


def test_all_table_single_column_interval_open_open_numeric():
    """
    Rule 108 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with ().
    """
    assert create_dataset(rule_108, data=dataset, org=ORG_NAME) == output_108


# Rule 109 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with (].

rule_109 = [
    {
        "ruleID": "rule109",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "(85000,145000];(15.0,17.0]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]


output_109 = {
    "filtered_data": {
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
            "rule_id": "rule109",
        }
    ],
}


def test_all_table_single_column_interval_open_closed_numeric():
    """
    Rule 109 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with (].
    """
    assert create_dataset(rule_109, data=dataset, org=ORG_NAME) == output_109


# Rule 110 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two numeric values with [).

rule_110 = [
    {
        "ruleID": "rule110",
        "table": "ALL",
        "variable": "fieldSampleTempC;value",
        "ruleValue": "[76000,145000);[15.0,17.0)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_110 = {
    "filtered_data": {
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
            "rule_id": "rule110",
        }
    ],
}


def test_all_table_single_column_interval_closed_open_numeric():
    """
    Rule 110 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two numeric values with [).
    """
    assert create_dataset(rule_110, data=dataset, org=ORG_NAME) == output_110


# Rule 111 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with [].

rule_111 = [
    {
        "ruleID": "rule111",
        "table": "ALL",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "[2021-01-24 8:00 , 2021-01-30 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_111 = {
    "filtered_data": {
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
            "rule_id": "rule111",
        }
    ],
}


def test_all_table_single_column_interval_closed_closed_datetime():
    """
    Rule 111 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [].
    """
    assert create_dataset(rule_111, data=dataset, org=ORG_NAME) == output_111


# Rule 112 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with ().

rule_112 = [
    {
        "ruleID": "rule112",
        "table": "ALL",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_112 = {
    "filtered_data": {
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
            "rule_id": "rule112",
        }
    ],
}


def test_all_table_single_column_interval_open_open_datetime():
    """
    Rule 112 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with ().
    """
    assert create_dataset(rule_112, data=dataset, org=ORG_NAME) == output_112


# Rule 113 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with (].

rule_113 = [
    {
        "ruleID": "rule113",
        "table": "ALL",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "(2021-01-29 8:00,2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_113 = {
    "filtered_data": {
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
            "rule_id": "rule113",
        }
    ],
}


def test_all_table_single_column_interval_open_closed_datetime():
    """
    Rule 113 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with (].
    """
    assert create_dataset(rule_113, data=dataset, org=ORG_NAME) == output_113


# Rule 114 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two datetime values with [).

rule_114 = [
    {
        "ruleID": "rule114",
        "table": "ALL",
        "variable": "analysisDate;dateTimeStart",
        "ruleValue": "[2021-01-27,2021-02-02)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_114 = {
    "filtered_data": {
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
            "rule_id": "rule114",
        }
    ],
}


def test_all_table_single_column_interval_closed_open_datetime():
    """
    Rule 114 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two datetime values with [).
    """
    assert create_dataset(rule_114, data=dataset, org=ORG_NAME) == output_114


# Rule 115 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with ().

rule_115 = [
    {
        "ruleID": "rule115",
        "table": "ALL",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,2021-01-28 8:00);(Inf, 17000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_115 = {
    "filtered_data": {
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
            "rule_id": "rule115",
        }
    ],
}


def test_all_table_single_column_interval_open_open_lower_inf():
    """
    Rule 115 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_115, data=dataset, org=ORG_NAME) == output_115


# Rule 116 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the lower bound limit is infinity with (].

rule_116 = [
    {
        "ruleID": "rule116",
        "table": "ALL",
        "variable": "value;dateTimeStart",
        "ruleValue": "(Inf,72000]; (Inf, 2021-01-24 08:00:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_116 = {
    "filtered_data": {
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
            "rule_id": "rule116",
        }
    ],
}


def test_all_table_single_column_interval_open_closed_lower_inf():
    """
    Rule 116 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_116, data=dataset, org=ORG_NAME) == output_116


# Rule 117 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with ().

rule_117 = [
    {
        "ruleID": "rule117",
        "table": "ALL",
        "variable": "value;dateTimeStart",
        "ruleValue": "(98000, Inf);(2021-01-27 08:00:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_117 = {
    "filtered_data": {
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
            "rule_id": "rule117",
        }
    ],
}


def test_all_table_single_column_interval_open_open_upper_inf():
    """
    Rule 119 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_117, data=dataset, org=ORG_NAME) == output_117


# Rule 118 filters rows based on a single column from each table and single
# value from each column or any of the columns being an interval between
# two values where the upper bound limit is infinity with [).

rule_118 = [
    {
        "ruleID": "rule118",
        "table": "ALL",
        "variable": "value;dateTimeStart",
        "ruleValue": "[2021-02-01 21:00, Inf);[145000,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_118 = {
    "filtered_data": {
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
            "rule_id": "rule118",
        }
    ],
}


def test_all_table_single_column_interval_closed_open_upper_inf():
    """
    Rule 118 filters rows based on a single column from each table and single
    value from each column or any of the columns being an interval between
    two values where the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_118, data=dataset, org=ORG_NAME) == output_118


# Rule 119 filters rows based on a single column from each table and multiple
# values from each column or any of the columns where one value could be
# an interval and other a single value.

rule_119 = [
    {
        "ruleID": "rule119",
        "table": "ALL",
        "variable": "value;dateTimeStart",
        "ruleValue": "[2021-02-01 21:00, 2021-02-06 21:00]; 16000; 2021-01-24 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_119 = {
    "filtered_data": {
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
            "rule_id": "rule119",
        }
    ],
}


def test_all_table_single_column_multiple_values():
    """
    Rule 119 filters rows based on a single column from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and other a single value.
    """
    assert create_dataset(rule_119, data=dataset, org=ORG_NAME) == output_119


# For MULTIPLE TABLES:
## MULTIPLE COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 120 filters rows based on multiple columns and all values of the rows.

rule_120 = [
    {
        "ruleID": "rule120",
        "table": "ALL",
        "variable": "value;dateTimeStart;analysisDate;dateTimeEnd",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_120 = {
    "filtered_data": {"Sample": [], "WWMeasure": [],},
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
            "rule_id": "rule120",
        }
    ],
}


def test_all_table_multiple_column_all_values():
    """
    Rule 120 filters rows based on multiple columns and all values of the rows.
    """
    assert create_dataset(rule_120, data=dataset, org=ORG_NAME) == output_120


# Rule 121 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being numeric.

rule_121 = [
    {
        "ruleID": "rule121",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC;index",
        "ruleValue": "16.0;98000;170000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_121 = {
    "filtered_data": {
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
            "rule_id": "rule121",
        }
    ],
}


def test_all_table_multiple_column_single_value_numeric():
    """
    Rule 121 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_121, data=dataset, org=ORG_NAME) == output_121


# Rule 122 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being string.

rule_122 = [
    {
        "ruleID": "rule122",
        "table": "ALL",
        "variable": "unitOther; type; collection",
        "ruleValue": "rawWW; gcMcovN2",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_122 = {
    "filtered_data": {
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
            "rule_id": "rule122",
        }
    ],
}


def test_all_table_multiple_column_single_value_string():
    """
    Rule 122 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being string.
    """
    assert create_dataset(rule_122, data=dataset, org=ORG_NAME) == output_122


# Rule 123 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being datetime.

rule_123 = [
    {
        "ruleID": "rule123",
        "table": "ALL",
        "variable": "analysisDate; dateTimeStart; dateTimeEnd; reportDate",
        "ruleValue": "2021-01-25 ; 2021-01-27 8:00",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_123 = {
    "filtered_data": {
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
            "rule_id": "rule123",
        }
    ],
}


def test_all_table_multiple_column_single_value_datetime():
    """
    Rule 123 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_123, data=dataset, org=ORG_NAME) == output_123


# Rule 124 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [].

rule_124 = [
    {
        "ruleID": "rule124",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "[16.0, 17.0]; [98000,145000]; [175000, 180000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_124 = {
    "filtered_data": {
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
            "rule_id": "rule124",
        }
    ],
}


def test_all_table_multiple_column_interval_closed_closed_numeric():
    """
    Rule 124 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [].
    """
    assert create_dataset(rule_124, data=dataset, org=ORG_NAME) == output_124


# Rule 125 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with ().

rule_125 = [
    {
        "ruleID": "rule125",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "(15.0, 17.0); (85000,145000); (170000,190000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_125 = {
    "filtered_data": {
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
            "rule_id": "rule125",
        }
    ],
}


def test_all_table_multiple_column_interval_open_open_numeric():
    """
    Rule 125 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with ().
    """
    assert create_dataset(rule_125, data=dataset, org=ORG_NAME) == output_125


# Rule 126 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with (].

rule_126 = [
    {
        "ruleID": "rule126",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "(15.0, 17.0]; (16000,145000]; (170000,180000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_126 = {
    "filtered_data": {
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
            "rule_id": "rule126",
        }
    ],
}


def test_all_table_multiple_column_interval_open_closed_numeric():
    """
    Rule 126 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with (].
    """
    assert create_dataset(rule_126, data=dataset, org=ORG_NAME) == output_126


# Rule 127 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# numbers with [).

rule_127 = [
    {
        "ruleID": "rule127",
        "table": "ALL",
        "variable": "value;storageTempC;fieldSampleTempC; index",
        "ruleValue": "[16.0, 17.0); [98000,145000); [170000,180000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_127 = {
    "filtered_data": {
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
            "rule_id": "rule127",
        }
    ],
}


def test_all_table_multiple_column_interval_closed_open_numeric():
    """
    Rule 127 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    numbers with [).
    """
    assert create_dataset(rule_127, data=dataset, org=ORG_NAME) == output_127


# Rule 128 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [].

rule_128 = [
    {
        "ruleID": "rule128",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": " [2021-01-27,2021-01-30]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_128 = {
    "filtered_data": {
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
            "rule_id": "rule128",
        }
    ],
}


def test_all_table_multiple_column_interval_closed_closed_datetime():
    """
    Rule 128 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [].
    """
    assert create_dataset(rule_128, data=dataset, org=ORG_NAME) == output_128


# Rule 129 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with ().

rule_129 = [
    {
        "ruleID": "rule129",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_129 = {
    "filtered_data": {
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
            "rule_id": "rule129",
        }
    ],
}


def test_all_table_multiple_column_interval_open_open_datetime():
    """
    Rule 129 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with ().
    """
    assert create_dataset(rule_129, data=dataset, org=ORG_NAME) == output_129


# Rule 130 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with (].

rule_130 = [
    {
        "ruleID": "rule130",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_130 = {
    "filtered_data": {
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
            "rule_id": "rule130",
        }
    ],
}


def test_all_table_multiple_column_interval_open_closed_datetime():
    """
    Rule 130 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with (].
    """
    assert create_dataset(rule_130, data=dataset, org=ORG_NAME) == output_130


# Rule 131 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval between two
# datetime values with [).

rule_131 = [
    {
        "ruleID": "rule131",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate",
        "ruleValue": "[2021-01-29 00:00 , 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_131 = {
    "filtered_data": {
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
            "rule_id": "rule131",
        }
    ],
}


def test_all_table_multiple_column_interval_closed_open_datetime():
    """
    Rule 131 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval between two
    datetime values with [).
    """
    assert create_dataset(rule_131, data=dataset, org=ORG_NAME) == output_131


# Rule 132 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_132 = [
    {
        "ruleID": "rule132",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "(Inf, 2021-01-31)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_132 = {
    "filtered_data": {
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
            "rule_id": "rule132",
        }
    ],
}


def test_all_table_multiple_column_interval_open_open_lower_inf():
    """
    Rule 132 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_132, data=dataset, org=ORG_NAME) == output_132


# Rule 133 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_133 = [
    {
        "ruleID": "rule133",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate; reportDate",
        "ruleValue": "(Inf , 2021-01-28 8:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_133 = {
    "filtered_data": {
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
            "rule_id": "rule133",
        }
    ],
}


def test_all_table_multiple_column_interval_open_closed_lower_inf():
    """
    Rule 133 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_133, data=dataset, org=ORG_NAME) == output_133


# Rule 134 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_134 = [
    {
        "ruleID": "rule134",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "(2021-01-25, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_134 = {
    "filtered_data": {
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
            "rule_id": "rule134",
        }
    ],
}


def test_all_table_multiple_column_interval_open_open_upper_inf():
    """
    Rule 134 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_134, data=dataset, org=ORG_NAME) == output_134


# Rule 135 filters rows based on multiple columns from each table and single
# value from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_135 = [
    {
        "ruleID": "rule135",
        "table": "ALL",
        "variable": "dateTimeStart;dateTimeEnd;analysisDate;reportDate",
        "ruleValue": "[2021-02-01 21:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_135 = {
    "filtered_data": {
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
            "rule_id": "rule135",
        }
    ],
}


def test_all_table_multiple_column_interval_closed_open_upper_inf():
    """
    Rule 135 filters rows based on multiple columns from each table and single
    value from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_135, data=dataset, org=ORG_NAME) == output_135


# Rule 136 filters rows based on multiple columns from each table and multiple
# values from each column or any of the columns where one value could be an
# interval and the other could be a single value.

rule_136 = [
    {
        "ruleID": "rule136",
        "table": "ALL",
        "variable": "dateTimeStart;value;analysisDate;fieldSampleTempC",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00] ; 145000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_136 = {
    "filtered_data": {
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
            "rule_id": "rule136",
        }
    ],
}


def test_all_table_multiple_column_multiple_values():
    """
    Rule 136 filters rows based on multiple columns from each table and multiple
    values from each column or any of the columns where one value could be an
    interval and the other could be a single value.
    """
    assert create_dataset(rule_136, data=dataset, org=ORG_NAME) == output_136


# For MULTIPLE TABLES:
## ALL COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 137 filters rows based on all columns from each table and all values of
# the rows.

rule_137 = [
    {
        "ruleID": "rule137",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "ALL",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_137 = {
    "filtered_data": {"Sample": [], "WWMeasure": [],},
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
            "rule_id": "rule137",
        }
    ],
}


def test_all_table_all_columns_all_values():
    """
    Rule 137 filters rows based on all columns from each table and all values
    of the rows.
    """
    assert create_dataset(rule_137, data=dataset, org=ORG_NAME) == output_137


# Rule 138 filters rows based on all columns from each table and single value
# from each column or any of the columns being numeric.

rule_138 = [
    {
        "ruleID": "rule138",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "17.0;98000",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_138 = {
    "filtered_data": {
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
            "rule_id": "rule138",
        }
    ],
}


def test_all_table_all_columns_single_value_numeric():
    """
    Rule 138 filters rows based on all columns from each table and single value
    from each column or any of the columns being numeric.
    """
    assert create_dataset(rule_138, data=dataset, org=ORG_NAME) == output_138


# Rule 139 filters rows based on all columns from each table and single value
# from each column or any of the columns being string.

rule_139 = [
    {
        "ruleID": "rule139",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "gcmnPMMoV; pSludge; grb;gcM",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_139 = {
    "filtered_data": {
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
            "rule_id": "rule139",
        }
    ],
}


def test_all_table_all_columns_single_value_string():
    """
    Rule 139 filters rows based on all columns from each table and single value
    from each column or any of the columns being string.
    """
    assert create_dataset(rule_139, data=dataset, org=ORG_NAME) == output_139


# Rule 140 filters rows based on all columns from each table and single value
# from each column or any of the columns being datetime.

rule_140 = [
    {
        "ruleID": "rule140",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "2021-02-01 21:00; 2021-01-25",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_140 = {
    "filtered_data": {
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
            "rule_id": "rule140",
        }
    ],
}


def test_all_table_all_columns_single_value_datetime():
    """
    Rule 140 filters rows based on all columns from each table and single value
    from each column or any of the columns being datetime.
    """
    assert create_dataset(rule_140, data=dataset, org=ORG_NAME) == output_140


# Rule 141 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with [].

rule_141 = [
    {
        "ruleID": "rule141",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0];[16.0,17.0];[98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_141 = {
    "filtered_data": {
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
            "rule_id": "rule141",
        }
    ],
}


def test_all_table_all_columns_interval_closed_closed_numeric():
    """
    Rule 141 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [].
    """
    assert create_dataset(rule_141, data=dataset, org=ORG_NAME) == output_141


# Rule 142 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with ().

rule_142 = [
    {
        "ruleID": "rule142",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0);(15.0,17.0);(16000,145000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_142 = {
    "filtered_data": {
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
            "rule_id": "rule142",
        }
    ],
}


def test_all_table_all_columns_interval_open_open_numeric():
    """
    Rule 142 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with ().
    """
    assert create_dataset(rule_142, data=dataset, org=ORG_NAME) == output_142


# Rule 143 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with (].

rule_143 = [
    {
        "ruleID": "rule143",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0];(98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_143 = {
    "filtered_data": {
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
            "rule_id": "rule143",
        }
    ],
}


def test_all_table_all_columns_interval_open_closed_numeric():
    """
    Rule 143 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with (].
    """
    assert create_dataset(rule_143, data=dataset, org=ORG_NAME) == output_143


# Rule 144 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two numbers
# with [).

rule_144 = [
    {
        "ruleID": "rule144",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0);[16.0,18.0);[98000,102000)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_144 = {
    "filtered_data": {
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
            "rule_id": "rule144",
        }
    ],
}


def test_all_table_all_columns_interval_closed_open_numeric():
    """
    Rule 144 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two numbers
    with [).
    """
    assert create_dataset(rule_144, data=dataset, org=ORG_NAME) == output_144


# Rule 145 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with [].

rule_145 = [
    {
        "ruleID": "rule145",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[2021-01-27,2021-01-31]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_145 = {
    "filtered_data": {
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
            "rule_id": "rule145",
        }
    ],
}


def test_all_table_all_columns_interval_closed_closed_datetime():
    """
    Rule 145 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [].
    """
    assert create_dataset(rule_145, data=dataset, org=ORG_NAME) == output_145


# Rule 146 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with ().

rule_146 = [
    {
        "ruleID": "rule146",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2021-01-29 8:00, 2021-02-06 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_146 = {
    "filtered_data": {
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
            "rule_id": "rule146",
        }
    ],
}


def test_all_table_all_columns_interval_open_open_datetime():
    """
    Rule 146 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with ().
    """
    assert create_dataset(rule_146, data=dataset, org=ORG_NAME) == output_146


# Rule 147 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with [).

rule_147 = [
    {
        "ruleID": "rule147",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[2021-01-27 8:00, 2021-02-01 21:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_147 = {
    "filtered_data": {
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
            "rule_id": "rule147",
        }
    ],
}


def test_all_table_all_columns_interval_closed_open_datetime():
    """
    Rule 147 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with [).
    """
    assert create_dataset(rule_147, data=dataset, org=ORG_NAME) == output_147


# Rule 148 filters rows based on all columns from each table and single value
# from each column or any of the columns being interval between two datetime
# with (].

rule_148 = [
    {
        "ruleID": "rule148",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(2021-01-26,2021-02-02];",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_148 = {
    "filtered_data": {
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
            "rule_id": "rule148",
        }
    ],
}


def test_all_table_all_columns_interval_open_closed_datetime():
    """
    Rule 148 filters rows based on all columns from each table and single value
    from each column or any of the columns being interval between two datetime
    with (].
    """
    assert create_dataset(rule_148, data=dataset, org=ORG_NAME) == output_148


# Rule 149 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with ().

rule_149 = [
    {
        "ruleID": "rule149",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(Inf , 8.0);(Inf,2021-01-26 00:00:00)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_149 = {
    "filtered_data": {
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
            "rule_id": "rule149",
        }
    ],
}


def test_all_table_all_columns_interval_open_open_lower_inf():
    """
    Rule 149 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with ().
    """
    assert create_dataset(rule_149, data=dataset, org=ORG_NAME) == output_149


# Rule 150 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the lower bound limit is infinity with (].

rule_150 = [
    {
        "ruleID": "rule150",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(Inf , 4.0];(Inf,2021-01-26 08:00:00]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_150 = {
    "filtered_data": {
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
            "rule_id": "rule150",
        }
    ],
}


def test_all_table_all_columns_interval_open_closed_lower_inf():
    """
    Rule 150 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the lower bound limit is infinity with (].
    """
    assert create_dataset(rule_150, data=dataset, org=ORG_NAME) == output_150


# Rule 151 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with ().

rule_151 = [
    {
        "ruleID": "rule151",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "(92000,Inf);(2021-02-01 08:00:00, Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_151 = {
    "filtered_data": {
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
            "rule_id": "rule151",
        }
    ],
}


def test_all_table_all_columns_interval_open_open_upper_inf():
    """
    Rule 151 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with ().
    """
    assert create_dataset(rule_151, data=dataset, org=ORG_NAME) == output_151


# Rule 152 filters rows based on all columns from each table and single value
# from each column or any of the columns being an interval where the
# the upper bound limit is infinity with [).

rule_152 = [
    {
        "ruleID": "rule152",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "[98000,Inf);[2021-02-01 21:00:00,Inf)",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_152 = {
    "filtered_data": {
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
            "rule_id": "rule152",
        }
    ],
}


def test_all_table_all_columns_interval_closed_open_upper_inf():
    """
    Rule 152 filters rows based on all columns from each table and single value
    from each column or any of the columns being an interval where the
    the upper bound limit is infinity with [).
    """
    assert create_dataset(rule_152, data=dataset, org=ORG_NAME) == output_152


# Rule 153 filters rows based on all columns from each table and multiple
# values from each column or any of the columns where one value could be
# an interval and the other could be a single value.

rule_153 = [
    {
        "ruleID": "rule153",
        "table": "ALL",
        "variable": "ALL",
        "ruleValue": "( 2021-01-30 8:00 , 2021-02-06 21:00] ; 145000;[98000,145000]",
        "direction": "row",
        "sharedWith": "Public;PHAC",
    }
]

output_153 = {
    "filtered_data": {
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
            "rule_id": "rule153",
        }
    ],
}


def test_all_table_all_columns_multiple_values():
    """
    Rule 153 filters rows based on all columns from each table and multiple
    values from each column or any of the columns where one value could be
    an interval and the other could be a single value.
    """
    assert create_dataset(rule_153, data=dataset, org=ORG_NAME) == output_153

