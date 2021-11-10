"""Testing single table fo removing columns"""
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
    "WWMeasure": [{"uWwMeasureID": "Measure WW100",}],
}

# User requested ORG_NAME:
ORG_NAME = "PHAC"

# For a SINGLE TABLE: `Sample` table is used.
# For single column:

# Rule 1 filters columns based on a single column and all values of the columns.

rule_1 = [
    {
        "ruleID": "rule1",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "ALL",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_1 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule1",
        }
    ],
}


def test_single_table_single_column_all_values():
    """
    Rule 1 filters columns based on a single column and all values of the columns.
    """
    assert create_dataset(rule_1, data=dataset, org=ORG_NAME) == output_1


# Rule 2 filters columns based on a single column and single value being numeric.

rule_2 = [
    {
        "ruleID": "rule2",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": 15.0,
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_2 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule2",
        }
    ],
}


def test_single_table_single_column_single_value_numeric():
    """
    Rule 2 filters columns based on a single column and single value being numeric.
    """
    assert create_dataset(rule_2, data=dataset, org=ORG_NAME) == output_2


# Rule 3 filters columns based on a single column and single value being string.

rule_3 = [
    {
        "ruleID": "rule3",
        "table": "Sample",
        "variable": "type",
        "ruleValue": "swrSed",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_3 = {
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
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "type": [
                            {"sampleID": "Sample S100", "type": "swrSed"},
                            {"sampleID": "Sample S106", "type": "pSludge"},
                            {"sampleID": "Sample S107", "type": "rawWW"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule3",
        }
    ],
}


def test_single_table_single_column_single_value_string():
    """
    Rule 3 filters columns based on a single column and single value being string.
    """
    assert create_dataset(rule_3, data=dataset, org=ORG_NAME) == output_3


# Rule 4 filters columns based on a single column and single value from each column
# or any of the columns being a datetime.

rule_4 = [
    {
        "ruleID": "rule4",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "2021-02-01 21:00:00",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_4 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule4",
        }
    ],
}


def test_single_table_single_column_single_value_datetime():
    """
    Rule 4 filters columns based on a single column and single value
    from each column or any of the columns being a datetime.
    """
    assert create_dataset(rule_4, data=dataset, org=ORG_NAME) == output_4


# Rule 5 filters columns based on a single column and range interval
# for a numeric value with [] interval.

rule_5 = [
    {
        "ruleID": "rule5",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "[15.0,17.0]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_5 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule5",
        }
    ],
}


def test_single_table_single_column_interval_closed_closed_numeric():
    """
    Rule 5 filters columns based on a single column and range interval
    for a numeric value with [] interval.
    """
    assert create_dataset(rule_5, data=dataset, org=ORG_NAME) == output_5


# Rule 6 filters columns based on a single column and range interval
# for a numeric value with () interval.

rule_6 = [
    {
        "ruleID": "rule6",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "(15.0,18.0)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_6 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule6",
        }
    ],
}


def test_single_table_single_column_interval_open_open_numeric():
    """
    Rule 6 filters columns based on a single column and range interval
    for a numeric value with () interval.
    """
    assert create_dataset(rule_6, data=dataset, org=ORG_NAME) == output_6


# Rule 7 filters columns based on a single column and range interval
# for a numeric value with (] interval.

rule_7 = [
    {
        "ruleID": "rule7",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "(15.0,18.0]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_7 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule7",
        }
    ],
}


def test_single_table_single_column_interval_open_closed_numeric():
    """
    Rule 7 filters columns based on a single column and range interval
    for a numeric value with (] interval.
    """
    assert create_dataset(rule_7, data=dataset, org=ORG_NAME) == output_7


# Rule 8 filters columns based on a single column and range interval
# for a numeric value with [) interval.

rule_8 = [
    {
        "ruleID": "rule8",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "[15.0,18.0)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_8 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule8",
        }
    ],
}


def test_single_table_single_column_interval_closed_open_numeric():
    """
    Rule 8 filters columns based on a single column and range interval
    for a numeric value with [) interval.
    """
    assert create_dataset(rule_8, data=dataset, org=ORG_NAME) == output_8


# Rule 9 filters columns based on a single column and range interval
# between datetime value with [] interval.

rule_9 = [
    {
        "ruleID": "rule9",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_9 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule9",
        }
    ],
}


def test_single_table_single_column_interval_closed_closed_datetime():
    """
    Rule 9 filters columns based on a single column and range interval
    between datetime value with [] interval.
    """
    assert create_dataset(rule_9, data=dataset, org=ORG_NAME) == output_9


# Rule 10 filters columns based on a single column and range interval
# between datetime value with () interval.

rule_10 = [
    {
        "ruleID": "rule10",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-02-01 21:00:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_10 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule10",
        }
    ],
}


def test_single_table_single_column_interval_open_open_datetime():
    """
    Rule 10 filters columns based on a single column and range interval
    between datetime value with () interval.
    """
    assert create_dataset(rule_10, data=dataset, org=ORG_NAME) == output_10


# Rule 11 filters columns based on a single column and range interval
# between datetime value with (] interval.

rule_11 = [
    {
        "ruleID": "rule11",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_11 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule11",
        }
    ],
}


def test_single_table_single_column_interval_open_closed_numeric():
    """
    Rule 11 filters columns based on a single column and range interval
    between datetime value with (] interval.
    """
    assert create_dataset(rule_11, data=dataset, org=ORG_NAME) == output_11


# Rule 12 filters columns based on a single column and range interval
# between datetime value with [) interval.

rule_12 = [
    {
        "ruleID": "rule12",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_12 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule12",
        }
    ],
}


def test_single_table_single_column_interval_closed_open_datetime():
    """
    Rule 12 filters columns based on a single column and range interval
    between datetime value with [) interval.
    """
    assert create_dataset(rule_12, data=dataset, org=ORG_NAME) == output_12


# Rule 13 filters columns based on a single column and range interval
# between two value with () interval where lower bound is infinity.

rule_13 = [
    {
        "ruleID": "rule13",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(Inf,2021-01-27 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_13 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule13",
        }
    ],
}


def test_single_table_single_column_interval_open_open_numeric_lower_inf():
    """
    Rule 13 filters columns based on a single column and range interval
    between two value with () interval where lower bound is infinity.
    """
    assert create_dataset(rule_13, data=dataset, org=ORG_NAME) == output_13


# Rule 14 filters columns based on a single column and range interval
# between two value with (] interval where lower bound is infinity.

rule_14 = [
    {
        "ruleID": "rule14",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(Inf,2021-01-27 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_14 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule14",
        }
    ],
}


def test_single_table_single_column_interval_lower_inf():
    """
    Rule 14 filters columns based on a single column and range interval
    between two value with (] interval where lower bound is infinity.
    """
    assert create_dataset(rule_14, data=dataset, org=ORG_NAME) == output_14


# Rule 15 filters columns based on a single column and range interval
# between two value with () interval where upper bound is infinity.

rule_15 = [
    {
        "ruleID": "rule15",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "(2021-01-24 08:00,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_15 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule15",
        }
    ],
}


def test_single_table_single_column_interval_open_open_upper_inf():
    """
    Rule 15 filters columns based on a single column and range interval
    between two value with () interval where upper bound is infinity.
    """
    assert create_dataset(rule_15, data=dataset, org=ORG_NAME) == output_15


# Rule 16 filters columns based on a single column and range interval
# between two value with [) interval where upper bound is infinity.

rule_16 = [
    {
        "ruleID": "rule16",
        "table": "Sample",
        "variable": "dateTimeStart",
        "ruleValue": "[2021-02-01 21:00,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_16 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule16",
        }
    ],
}


def test_single_table_single_column_interval_upper_inf():
    """
    Rule 16 filters columns based on a single column and range interval
    between two value with [) interval where upper bound is infinity.
    """
    assert create_dataset(rule_16, data=dataset, org=ORG_NAME) == output_16


# Rule 17 filters columns based on a single column and multiple values
# to filter by a single value and a range.

rule_17 = [
    {
        "ruleID": "rule17",
        "table": "Sample",
        "variable": "fieldSampleTempC",
        "ruleValue": "15.0;(17.0,18.0]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_17 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
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
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule17",
        }
    ],
}


def test_single_table_single_column_multiple_values():
    """
    Rule 17 filters columns based on a single column and multiple values
    to filter by a single value and a range.
    """
    assert create_dataset(rule_17, data=dataset, org=ORG_NAME) == output_17


# For SINGLE TABLE:
## MULTIPLE COLUMNS:

# Rule 18 filters all columns from more than 1 column from a single table.

rule_18 = [
    {
        "ruleID": "rule18",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "ALL",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]


output_18 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule18",
        }
    ],
}


def test_single_table_multiple_columns_all_values():
    """
    Rule 18 filters all columns from more than 1 column from a single table.
    """
    assert create_dataset(rule_18, data=dataset, org=ORG_NAME) == output_18


# Rule 19 filters columns from multiple columns from a single table based
# on a single value from each column or any of the columns being a number.

rule_19 = [
    {
        "ruleID": "rule19",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "15;22",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_19 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule19",
        }
    ],
}


def test_single_table_multiple_columns_single_value_numeric():
    """
    Rule 19 filters columns from multiple columns from a single table based
    on a single value from each column or any of the columns being a number.
    """
    assert create_dataset(rule_19, data=dataset, org=ORG_NAME) == output_19


# Rule 20 filters columns from multiple columns from a single table based
# on a single value from each columns or any of the columns being a string.

rule_20 = [
    {
        "ruleID": "rule20",
        "table": "Sample",
        "variable": "type;collection",
        "ruleValue": "grb;pSludge",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_20 = {
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
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "collection": [
                            {"collection": "mooreSw", "sampleID": "Sample S100"},
                            {"collection": "cpTP24h", "sampleID": "Sample S106"},
                            {"collection": "grb", "sampleID": "Sample S107"},
                        ],
                        "type": [
                            {"sampleID": "Sample S100", "type": "swrSed"},
                            {"sampleID": "Sample S106", "type": "pSludge"},
                            {"sampleID": "Sample S107", "type": "rawWW"},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule20",
        }
    ],
}


def test_single_table_multiple_columns_single_value_string():
    """
    Rule 20 filters columns from multiple columns from a single table based
    on a single value from each columns or any of the columns being a string.
    """
    assert create_dataset(rule_20, data=dataset, org=ORG_NAME) == output_20


# Rule 21 filters columns from multiple columns from a single table based on a
# single value from each columns or any of the columns being a datetime.

rule_21 = [
    {
        "ruleID": "rule21",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "2021-01-27 8:00",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_21 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule21",
        }
    ],
}


def test_single_table_multiple_columns_single_value_datetime():
    """
    Rule 21 filters columns from multiple columns from a single table based on a
    single value from each columns or any of the columns being a datetime.
    """
    assert create_dataset(rule_21, data=dataset, org=ORG_NAME) == output_21


# Rule 22 filters columns from multiple columns from a single table
# based on a single value from each column or any of the columns being an
# interval between two numbers with [] interval

rule_22 = [
    {
        "ruleID": "rule22",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "[15.0,25]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_22 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule22",
        }
    ],
}


def test_single_table_multiple_column_interval_closed_closed_numeric():
    """
    Rule 22 filters columns from multiple columns from a single table
    based on a single value from each column or any of the columns being an
    interval between two numbers with [] interval
    """
    assert create_dataset(rule_22, data=dataset, org=ORG_NAME) == output_22


# Rule 23 filters columns from multiple columns from a single table based on a
# single value from each columns or any of the columns
# being an interval between two numbers with () interval

rule_23 = [
    {
        "ruleID": "rule23",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "(16.0,25)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_23 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule23",
        }
    ],
}


def test_single_table_multiple_column_interval_open_open_numeric():
    """
    Rule 23 filters columns from multiple columns from a single table based on a
    single value from each columns or any of the columns
    being an interval between two numbers with () interval
    """
    assert create_dataset(rule_23, data=dataset, org=ORG_NAME) == output_23


# Rule 24 filters columns from multiple columns from a single table based on a
# single value from each columns or any of the columns
# being an interval between two numbers with (] interval


rule_24 = [
    {
        "ruleID": "rule24",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "(15.0,18.0]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_24 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule24",
        }
    ],
}


def test_single_table_multiple_column_interval_open_closed_numeric():
    """
    Rule 24 filters columns from multiple columns from a single table based on a
    single value from each columns or any of the columns
    being an interval between two numbers with (] interval
    """
    assert create_dataset(rule_24, data=dataset, org=ORG_NAME) == output_24


# Rule 25 filters columns from multiple columns from a single table based on a
# single value from each columns or any of the columns
# being an interval between two numbers with [) interval

rule_25 = [
    {
        "ruleID": "rule25",
        "table": "Sample",
        "variable": "fieldSampleTempC;storageTempC",
        "ruleValue": "[16.0,19)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_25 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule25",
        }
    ],
}


def test_single_table_multiple_column_interval_closed_open_numeric():
    """
    Rule 25 filters columns from multiple columns from a single table based on a
    single value from each columns or any of the columns
    being an interval between two numbers with [) interval
    """
    assert create_dataset(rule_25, data=dataset, org=ORG_NAME) == output_25


# Rule 26 filters columns from multiple columns from a single table based on a
# single value from each columns or any of the columns
# being an interval between two datetime values with [] interval

rule_26 = [
    {
        "ruleID": "rule26",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-01-24 8:00,2021-01-27 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_26 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule26",
        }
    ],
}


def test_single_table_multiple_column_interval_closed_closed_datetime():
    """
    Rule 26 filters columns from multiple columns from a single table based on a
    single value from each columns or any of the columns
    being an interval between two datetime values with [] interval
    """
    assert create_dataset(rule_26, data=dataset, org=ORG_NAME) == output_26


# Rule 27 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns
# being an interval between two datetime values with () interval

rule_27 = [
    {
        "ruleID": "rule27",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-27 8:00,2021-01-30 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_27 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
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
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule27",
        }
    ],
}


def test_single_table_multiple_column_interval_open_open_datetime():
    """
    Rule 27 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns
    being an interval between two datetime values with () interval
    """
    assert create_dataset(rule_27, data=dataset, org=ORG_NAME) == output_27


# Rule 28 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns
# being an interval between two datetime values with (] interval

rule_28 = [
    {
        "ruleID": "rule28",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-27 8:00,2021-02-01 21:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_28 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule28",
        }
    ],
}


def test_single_table_multiple_column_interval_open_closed_datetime():
    """
    Rule 28 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns
    being an interval between two datetime values with (] interval
    """
    assert create_dataset(rule_28, data=dataset, org=ORG_NAME) == output_28


# Rule 29 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns
# being an interval between two datetime values with [) interval

rule_29 = [
    {
        "ruleID": "rule29",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-01-27 8:00,2021-01-30 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_29 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule29",
        }
    ],
}


def test_single_table_multiple_column_interval_closed_open_datetime():
    """
    Rule 29 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns
    being an interval between two datetime values with [) interval
    """
    assert create_dataset(rule_29, data=dataset, org=ORG_NAME) == output_29


# Rule 30 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns being interval between
# two values where the lower bound limit is infinity and with () interval

rule_30 = [
    {
        "ruleID": "rule30",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(Inf,2021-01-30 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_30 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule30",
        }
    ],
}


def test_single_table_multiple_column_interval_open_open_lower_inf():
    """
    Rule 30 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns being interval between
    two values where the lower bound limit is infinity and with () interva
    """
    assert create_dataset(rule_30, data=dataset, org=ORG_NAME) == output_30


# Rule 31 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns being interval between
# two values where the lower bound limit is infinity and with (] interval

rule_31 = [
    {
        "ruleID": "rule31",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(Inf,2021-01-28 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_31 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule31",
        }
    ],
}


def test_single_table_multiple_column_interval_open_closed_lower_inf():
    """
    Rule 31 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns being interval between
    two values where the lower bound limit is infinity and with (] interval
    """
    assert create_dataset(rule_31, data=dataset, org=ORG_NAME) == output_31


# Rule 32 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns being interval between
# two values where the upper bound limit is infinity and with () interval

rule_32 = [
    {
        "ruleID": "rule32",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "(2021-01-29 08:00,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_32 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule32",
        }
    ],
}


def test_single_table_multiple_column_interval_open_open_upper_inf():
    """
    Rule 32 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns being interval between
    two values where the upper bound limit is infinity and with () interval
    """
    assert create_dataset(rule_32, data=dataset, org=ORG_NAME) == output_32


# Rule 33 filters columns from multiple columns from a single table based on a
# single value from each column or any of the columns being interval between
# two values where the upper bound limit is infinity and with [) interval

rule_33 = [
    {
        "ruleID": "rule33",
        "table": "Sample",
        "variable": "dateTimeStart;dateTimeEnd",
        "ruleValue": "[2021-02-01 21:00,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_33 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
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
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule33",
        }
    ],
}


def test_single_table_multiple_column_interval_closed_open_upper_inf():
    """
    Rule 33 filters columns from multiple columns from a single table based on a
    single value from each column or any of the columns being interval between
    two values where the upper bound limit is infinity and with [) interval
    """
    assert create_dataset(rule_33, data=dataset, org=ORG_NAME) == output_33


# Rule 34 filters columns from multiple columns from a single table based on
# multiple values where one can be a single value and other being interval.

rule_34 = [
    {
        "ruleID": "rule34",
        "table": "Sample",
        "variable": "type;dateTimeStart;dateTimeEnd;storageTempC",
        "ruleValue": "swrSed;[2021-01-25 8:00,2021-01-27 8:00);[16,17]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_34 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "sampleID": "Sample S100",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "sampleID": "Sample S106",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "sampleID": "Sample S107",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                        "type": [
                            {"sampleID": "Sample S100", "type": "swrSed"},
                            {"sampleID": "Sample S106", "type": "pSludge"},
                            {"sampleID": "Sample S107", "type": "rawWW"},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule34",
        }
    ],
}


def test_single_table_multiple_column_multiple_values():
    """
    Rule 34 filters columns from multiple columns from a single table based on
    multiple values where one can be a single value and other being interval.
    """
    assert create_dataset(rule_34, data=dataset, org=ORG_NAME) == output_34


# SINGLE TABLE:
# ALL COLUMNS:

# Rule 35 filters all the columns from all column from a single table.

rule_35 = [
    {
        "ruleID": "rule35",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "ALL",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_35 = {
    "filtered_data": {"Sample": [], "WWMeasure": [{"uWwMeasureID": "Measure WW100"}]},
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "collection": [
                            {"collection": "mooreSw", "sampleID": "Sample S100"},
                            {"collection": "cpTP24h", "sampleID": "Sample S106"},
                            {"collection": "grb", "sampleID": "Sample S107"},
                        ],
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "sampleID": [
                            {"sampleID": "Sample S100"},
                            {"sampleID": "Sample S106"},
                            {"sampleID": "Sample S107"},
                        ],
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                        "type": [
                            {"sampleID": "Sample S100", "type": "swrSed"},
                            {"sampleID": "Sample S106", "type": "pSludge"},
                            {"sampleID": "Sample S107", "type": "rawWW"},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule35",
        }
    ],
}


def test_single_table_all_columns_all_values():
    """
    Rule 35 filters all the columns from all column from a single table.
    """
    assert create_dataset(rule_35, data=dataset, org=ORG_NAME) == output_35


# Rule 36 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being a number.

rule_36 = [
    {
        "ruleID": "rule36",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "10;22",
        "direction": "column",
        "sharedWith": "PHAC",
    }
]

output_36 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule36",
        }
    ],
}


def test_single_table_all_columns_single_value_numeric():
    """
    Rule 36 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being a number.
    """
    assert create_dataset(rule_36, data=dataset, org=ORG_NAME) == output_36


# Rule 37 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being a string.

rule_37 = [
    {
        "ruleID": "rule37",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "Site T113;mooreSw;pSludge;",
        "direction": "column",
        "sharedWith": "PHAC",
    }
]

output_37 = {
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
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "collection": [
                            {"collection": "mooreSw", "sampleID": "Sample S100"},
                            {"collection": "cpTP24h", "sampleID": "Sample S106"},
                            {"collection": "grb", "sampleID": "Sample S107"},
                        ],
                        "type": [
                            {"sampleID": "Sample S100", "type": "swrSed"},
                            {"sampleID": "Sample S106", "type": "pSludge"},
                            {"sampleID": "Sample S107", "type": "rawWW"},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule37",
        }
    ],
}


def test_single_table_all_columns_single_value_string():
    """
    Rule 37 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being a string.
    """
    assert create_dataset(rule_37, data=dataset, org=ORG_NAME) == output_37


# Rule 38 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being a datetime.

rule_38 = [
    {
        "ruleID": "rule38",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "2021-01-28 21:00;2021-01-24 8:00",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_38 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule38",
        }
    ],
}


def test_single_table_all_columns_single_value_datetime():
    """
    Rule 38 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being a datetime.
    """
    assert create_dataset(rule_38, data=dataset, org=ORG_NAME) == output_38


# Rule 39 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two numbers with [] interval.

# As we can get several rules in a list from one schema, therefore,
# in the below list of rules, we have added 2 rules to ensure function works
# for multiple rules in one schema.
rule_39 = [
    {
        "ruleID": "rule39_1",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0]",
        "direction": "column",
        "sharedWith": "PHAC",
    },
    {
        "ruleID": "rule39_2",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[16.0,18.0]",
        "direction": "column",
        "sharedWith": "PHAC",
    },
]

output_39 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule39_1",
        },
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule39_2",
        },
    ],
}


def test_single_table_all_columns_interval_closed_closed_numeric():
    """
    Rule 39 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two numbers with [] interval.
    """
    assert create_dataset(rule_39, data=dataset, org=ORG_NAME) == output_39


# Rule 40 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two numbers with () interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_40 = [
    {
        "ruleID": "rule40",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2.0,10.0);(17,22)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_40 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule40",
        }
    ],
}


def test_single_table_all_columns_interval_open_open_numeric():
    """
    Rule 40 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two numbers with () interval.
    """
    assert create_dataset(rule_40, data=dataset, org=ORG_NAME) == output_40


# Rule 41 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two numbers with (] interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_41 = [
    {
        "ruleID": "rule41",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(8.0,10.0];(16,25]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_41 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "fieldSampleTempC": [
                            {"fieldSampleTempC": 15, "sampleID": "Sample S100"},
                            {"fieldSampleTempC": 17, "sampleID": "Sample S106"},
                            {"fieldSampleTempC": 18, "sampleID": "Sample S107"},
                        ],
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule41",
        }
    ],
}


def test_single_table_all_columns_interval_open_closed_numeric():
    """
    Rule 41 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two numbers with (] interval.
    """
    assert create_dataset(rule_41, data=dataset, org=ORG_NAME) == output_41


# Rule 42 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two numbers with [) interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_42 = [
    {
        "ruleID": "rule42",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[8.0,10.0);[19,25)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_42 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "sizeL": [
                            {"sampleID": "Sample S100", "sizeL": 8},
                            {"sampleID": "Sample S106", "sizeL": 2},
                            {"sampleID": "Sample S107", "sizeL": 10},
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule42",
        }
    ],
}


def test_single_table_all_columns_interval_closed_open_numeric():
    """
    Rule 42 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two numbers with [) interval.
    """
    assert create_dataset(rule_42, data=dataset, org=ORG_NAME) == output_42


# Rule 43 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two datetime values with [] interval.

rule_43 = [
    {
        "ruleID": "rule43",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[2021-01-25 8:00,2021-01-29 21:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_43 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule43",
        }
    ],
}


def test_single_table_all_columns_interval_closed_closed_datetime():
    """
    Rule 43 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two datetime values with [] interval.
    """
    assert create_dataset(rule_43, data=dataset, org=ORG_NAME) == output_43


# Rule 44 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two datetime values with () interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_44 = [
    {
        "ruleID": "rule44",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2021-01-25 8:00,2021-01-30 8:00);(2021-01-29 21:00,2021-02-01 21:00)",
        "direction": "column",
        "sharedWith": "PHAC",
    }
]

output_44 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule44",
        }
    ],
}


def test_single_table_all_columns_interval_open_open_datetime():
    """
    Rule 44 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two datetime values with () interval.
    """
    assert create_dataset(rule_44, data=dataset, org=ORG_NAME) == output_44


# Rule 45 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two datetime values with (] interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_45 = [
    {
        "ruleID": "rule45",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(2021-01-25 8:00,2021-01-30 8:00];(2021-01-29 21:00,2021-02-01 21:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_45 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule45",
        }
    ],
}


def test_single_table_all_columns_interval_open_closed_datetime():
    """
    Rule 45 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two datetime values with (] interval.
    """
    assert create_dataset(rule_45, data=dataset, org=ORG_NAME) == output_45


# Rule 46 filters columns from all columns from a single table based on a
# single value from each column or any of the columns being an interval
# between two datetime values with [) interval.

# multiple values in ruleValue ensure atleast 1 rule applies to each column
rule_46 = [
    {
        "ruleID": "rule46",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[2021-02-01 21:00,2021-02-04 21:00);[2021-01-28 08:00,2021-02-01 21:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_46 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule46",
        }
    ],
}


def test_single_table_all_columns_interval_closed_open_datetime():
    """
    Rule 46 filters columns from all columns from a single table based on a
    single value from each column or any of the columns being an interval
    between two datetime values with [) interval.
    """
    assert create_dataset(rule_46, data=dataset, org=ORG_NAME) == output_46


# Rule 47 filters columns from all columns from a single table based on a single
# value being interval where lower bound limit is infinity with (] interval

rule_47 = [
    {
        "ruleID": "rule47",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(Inf,2021-01-27 8:00]",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_47 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule47",
        }
    ],
}


def test_single_table_all_columns_interval_open_closed_lower_inf():
    """
    Rule 47 filters columns from all columns from a single table based on a single
    value being interval where lower bound limit is infinity with (] interval
    """
    assert create_dataset(rule_47, data=dataset, org=ORG_NAME) == output_47


# Rule 48 filters columns from all columns from a single table based on a single
# value being interval where lower bound limit is infinity with () interval

rule_48 = [
    {
        "ruleID": "rule48",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(Inf,2021-01-28 8:00)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_48 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "storageTempC": 16,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "storageTempC": 18,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "storageTempC": 22,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule48",
        }
    ],
}


def test_single_table_all_columns_interval_open_open_lower_inf():
    """
    Rule 48 filters columns from all columns from a single table based on a single
    value being interval where lower bound limit is infinity with () interval
    """
    assert create_dataset(rule_48, data=dataset, org=ORG_NAME) == output_48


# Rule 49 filters columns from all columns from a single table based on a single
# value being interval where upper bound limit is infinity with () interval

rule_49 = [
    {
        "ruleID": "rule49",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "(18,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_49 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
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
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule49",
        }
    ],
}


def test_single_table_all_columns_interval_open_open_upper_inf():
    """
    Rule 49 filters columns from all columns from a single table based on a single
    value being interval where upper bound limit is infinity with () interval
    """
    assert create_dataset(rule_49, data=dataset, org=ORG_NAME) == output_49


# Rule 50 filters columns from all columns from a single table based on single
# value being interval where upper bound limit is infinity with [) interval

rule_50 = [
    {
        "ruleID": "rule50",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[19,Inf)",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_50 = {
    "filtered_data": {
        "Sample": [
            {
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sizeL": 8,
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
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ]
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule50",
        }
    ],
}


def test_single_table_all_columns_interval_closed_open_upper_inf():
    """
    Rule 50 filters columns from all columns from a single table based on single
    value being interval where upper bound limit is infinity with [) interval
    """
    assert create_dataset(rule_50, data=dataset, org=ORG_NAME) == output_50


# Rule 51 filters columns from all columns from a single table based on a
# multiple values where one can be an interval and other a value.

rule_51 = [
    {
        "ruleID": "rule51",
        "table": "Sample",
        "variable": "ALL",
        "ruleValue": "[19,25];(18,22);(2021-01-24 21:00,2021-02-01 21:00];16.0",
        "direction": "column",
        "sharedWith": "Public;PHAC",
    }
]

output_51 = {
    "filtered_data": {
        "Sample": [
            {
                "fieldSampleTempC": 15,
                "sizeL": 8,
                "sampleID": "Sample S100",
                "type": "swrSed",
                "collection": "mooreSw",
            },
            {
                "fieldSampleTempC": 17,
                "sizeL": 2,
                "sampleID": "Sample S106",
                "type": "pSludge",
                "collection": "cpTP24h",
            },
            {
                "fieldSampleTempC": 18,
                "sizeL": 10,
                "sampleID": "Sample S107",
                "type": "rawWW",
                "collection": "grb",
            },
        ],
        "WWMeasure": [{"uWwMeasureID": "Measure WW100"}],
    },
    "sharing_summary": [
        {
            "entities_filtered": [
                {
                    "columns_removed": {
                        "dateTime": [
                            {
                                "dateTime": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTime": Timestamp("2021-01-25 21:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTime": Timestamp("2021-01-28 21:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeEnd": [
                            {
                                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "dateTimeStart": [
                            {
                                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                                "sampleID": "Sample S100",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                                "sampleID": "Sample S106",
                            },
                            {
                                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                                "sampleID": "Sample S107",
                            },
                        ],
                        "storageTempC": [
                            {"sampleID": "Sample S100", "storageTempC": 16},
                            {"sampleID": "Sample S106", "storageTempC": 18},
                            {"sampleID": "Sample S107", "storageTempC": 22},
                        ],
                    },
                    "table": "Sample",
                },
            ],
            "rule_id": "rule51",
        }
    ],
}


def test_single_table_all_columns_multiple_values():
    """
    Rule 51 filters columns from all columns from a single table based on a
    multiple values where one can be an interval and other a value.
    """
    assert create_dataset(rule_51, data=dataset, org=ORG_NAME) == output_51
