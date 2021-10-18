import csv
import json
import os
import re

import numpy as np  # pylint: disable=import-error
import pandas as pd  # pylint: disable=import-error
import pytest  # pylint: disable=import-error
from numpy import nan  # pylint: disable=import-error
from pandas import Timestamp  # pylint: disable=import-error

# import create_dataset  # pylint: disable=import-error
from create_dataset import create_dataset  # pylint: disable=import-error

# User Data:

dataset = {
    "AssayMethod": [
        {
            "assayMethodID": "Assay Y101",
        }
    ],
    "Sample": [
        {
            "collection": "mooreSw",
            "dateTime": Timestamp("2021-02-01 21:00:00"),
            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
            "fieldSampleTempC": 15,
            "sampleID": "Sample S100",
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
            "sampleID": "Sample S106",
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
            "sampleID": "Sample S107",
            "sizeL": 10,
            "storageTempC": 22,
            "type": "rawWW",
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

# User requested organization:
organization = "PHAC"

# FOR MULTIPLE TABLES: Tables `Sample` and `WWMeasure` are used.
## FOR SINGLE COLUMN FROM EACH TABLE OR ANY OF THE TABLE

# Rule 52 filters rows based on a single column and all values of the rows.

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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    assert create_dataset(rule_52, data=dataset, org=organization) == output52


# Rule 53 filters rows based on a single column from each table and single value from each column or any of the columns being numeric.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_53 with pytest.
    """
    assert create_dataset(rule_53, data=dataset, org=organization) == output53


# Rule 54 filters rows based on a single column from each table and single value from each column or any of the columns being string.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_54 with pytest.
    """
    assert create_dataset(rule_54, data=dataset, org=organization) == output54


# Rule 55 filters rows based on a single column from each table and single value from each column or any of the columns being datetime.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_55 with pytest.
    """
    assert create_dataset(rule_55, data=dataset, org=organization) == output55


# Rule 56 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_56 with pytest.
    """
    assert create_dataset(rule_56, data=dataset, org=organization) == output56


# Rule 57 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_57 with pytest.
    """
    assert create_dataset(rule_57, data=dataset, org=organization) == output57


# Rule 58 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_58 with pytest.
    """
    assert create_dataset(rule_58, data=dataset, org=organization) == output58


# Rule 59 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_59 with pytest.
    """
    assert create_dataset(rule_59, data=dataset, org=organization) == output59


# Rule 60 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_60 with pytest.
    """
    assert create_dataset(rule_60, data=dataset, org=organization) == output60


# Rule 61 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_61 with pytest.
    """
    assert create_dataset(rule_61, data=dataset, org=organization) == output61


# Rule 62 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
    This method tests the function create_dataset against rule_62 with pytest.
    """
    assert create_dataset(rule_62, data=dataset, org=organization) == output62


# Rule 63 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_63 with pytest.
    """
    assert create_dataset(rule_63, data=dataset, org=organization) == output63


# Rule 64 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
                            "sizeL": 10,
                            "storageTempC": 22,
                            "type": "rawWW",
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
    This method tests the function create_dataset against rule_64 with pytest.
    """
    assert create_dataset(rule_64, data=dataset, org=organization) == output64


# Rule 65 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_65 with pytest.
    """
    assert create_dataset(rule_65, data=dataset, org=organization) == output65


# Rule 66 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_66 with pytest.
    """
    assert create_dataset(rule_66, data=dataset, org=organization) == output66


# Rule 67 filters rows based on a single column from each table and single value from each column or any of the columns being an interval between
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
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
    This method tests the function create_dataset against rule_67 with pytest.
    """
    assert create_dataset(rule_67, data=dataset, org=organization) == output67


# Rule 68 filters rows based on a single column from each table and multiple values from each column or any of the columns where one value could be
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
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_68 with pytest.
    """
    assert create_dataset(rule_68, data=dataset, org=organization) == output68


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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_69 with pytest.
    """
    assert create_dataset(rule_69, data=dataset, org=organization) == output69


# Rule 70 filters rows based on multiple columns from each table and single value from each column or any of the columns being numeric.

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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
    This method tests the function create_dataset against rule_70 with pytest.
    """
    assert create_dataset(rule_70, data=dataset, org=organization) == output70


# Rule 71 filters rows based on multiple columns from each table and single value from each column or any of the columns being string.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_71 with pytest.
    """
    assert create_dataset(rule_71, data=dataset, org=organization) == output71


# Rule 72 filters rows based on multiple columns from each table and single value from each column or any of the columns being datetime.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "grb",
                            "dateTime": Timestamp("2021-01-28 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                            "fieldSampleTempC": 18,
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_72 with pytest.
    """
    assert create_dataset(rule_72, data=dataset, org=organization) == output72


# Rule 73 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_73 with pytest.
    """
    assert create_dataset(rule_73, data=dataset, org=organization) == output73


# Rule 74 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
    This method tests the function create_dataset against rule_74 with pytest.
    """
    assert create_dataset(rule_74, data=dataset, org=organization) == output74


# Rule 75 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_75 with pytest.
    """
    assert create_dataset(rule_75, data=dataset, org=organization) == output75


# Rule 76 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
    This method tests the function create_dataset against rule_76 with pytest.
    """
    assert create_dataset(rule_76, data=dataset, org=organization) == output76


# Rule 77 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_77 with pytest.
    """
    assert create_dataset(rule_77, data=dataset, org=organization) == output77


# Rule 78 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_78 with pytest.
    """
    assert create_dataset(rule_78, data=dataset, org=organization) == output78


# Rule 79 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_79 with pytest.
    """
    assert create_dataset(rule_79, data=dataset, org=organization) == output79


# Rule 80 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval between two
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_80 with pytest.
    """
    assert create_dataset(rule_80, data=dataset, org=organization) == output80


# Rule 81 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_81 with pytest.
    """
    assert create_dataset(rule_81, data=dataset, org=organization) == output81


# Rule 82 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_82 with pytest.
    """
    assert create_dataset(rule_82, data=dataset, org=organization) == output82


# Rule 83 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_83 with pytest.
    """
    assert create_dataset(rule_83, data=dataset, org=organization) == output83


# Rule 84 filters rows based on multiple columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
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
    This method tests the function create_dataset against rule_84 with pytest.
    """
    assert create_dataset(rule_84, data=dataset, org=organization) == output84


# Rule 85 filters rows based on multiple columns from each table and multiple values from each column or any of the columns where one value could be an interval
# and the other could be a single value.

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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
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
    This method tests the function create_dataset against rule_85 with pytest.
    """
    assert create_dataset(rule_85, data=dataset, org=organization) == output85


# For MULTIPLE TABLES:
## ALL COLUMNS FROM EACH TABLE OR ANY OF THE TABLES

# Rule 86 filters rows based on all columns from each table and all values of the rows.

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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_86 with pytest.
    """
    assert create_dataset(rule_86, data=dataset, org=organization) == output86


# Rule 87 filters rows based on all columns from each table and single value from each column or any of the columns being numeric.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_87 with pytest.
    """
    assert create_dataset(rule_87, data=dataset, org=organization) == output87


# Rule 88 filters rows based on all columns from each table and single value from each column or any of the columns being string.

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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
                "sizeL": 8,
                "storageTempC": 16,
                "type": "swrSed",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_88 with pytest.
    """
    assert create_dataset(rule_88, data=dataset, org=organization) == output88


# Rule 89 filters rows based on all columns from each table and single value from each column or any of the columns being datetime.

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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
                            "sizeL": 8,
                            "storageTempC": 16,
                            "type": "swrSed",
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
    This method tests the function create_dataset against rule_89 with pytest.
    """
    assert create_dataset(rule_89, data=dataset, org=organization) == output89


# Rule 90 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two numbers
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_90 with pytest.
    """
    assert create_dataset(rule_90, data=dataset, org=organization) == output90


# Rule 91 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two numbers
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
    This method tests the function create_dataset against rule_91 with pytest.
    """
    assert create_dataset(rule_91, data=dataset, org=organization) == output91


# Rule 92 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two numbers
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_92 with pytest.
    """
    assert create_dataset(rule_92, data=dataset, org=organization) == output92


# Rule 93 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two numbers
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
                "collection": "grb",
                "dateTime": Timestamp("2021-01-28 21:00:00"),
                "dateTimeEnd": Timestamp("2021-02-01 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-27 08:00:00"),
                "fieldSampleTempC": 18,
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S106",
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
    This method tests the function create_dataset against rule_93 with pytest.
    """
    assert create_dataset(rule_93, data=dataset, org=organization) == output93


# Rule 94 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two datetime
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_94 with pytest.
    """
    assert create_dataset(rule_94, data=dataset, org=organization) == output94


# Rule 95 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two datetime
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_95 with pytest.
    """
    assert create_dataset(rule_95, data=dataset, org=organization) == output95


# Rule 96 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two datetime
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_96 with pytest.
    """
    assert create_dataset(rule_96, data=dataset, org=organization) == output96


# Rule 97 filters rows based on all columns from each table and single value from each column or any of the columns being an interval between two datetime
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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_97 with pytest.
    """
    assert create_dataset(rule_97, data=dataset, org=organization) == output97


# Rule 98 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
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
    This method tests the function create_dataset against rule_98 with pytest.
    """
    assert create_dataset(rule_98, data=dataset, org=organization) == output98


# Rule 99 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
                            "collection": "cpTP24h",
                            "dateTime": Timestamp("2021-01-25 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                            "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                            "fieldSampleTempC": 17,
                            "sampleID": "Sample S106",
                            "sizeL": 2,
                            "storageTempC": 18,
                            "type": "pSludge",
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
    This method tests the function create_dataset against rule_99 with pytest.
    """
    assert create_dataset(rule_99, data=dataset, org=organization) == output99


# Rule 100 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_100 with pytest.
    """
    assert create_dataset(rule_100, data=dataset, org=organization) == output100


# Rule 101 filters rows based on all columns from each table and single value from each column or any of the columns being an interval where the
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
                "collection": "mooreSw",
                "dateTime": Timestamp("2021-02-01 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                "fieldSampleTempC": 15,
                "sampleID": "Sample S100",
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
                "sampleID": "Sample S106",
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
                "sampleID": "Sample S107",
                "sizeL": 10,
                "storageTempC": 22,
                "type": "rawWW",
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
    This method tests the function create_dataset against rule_101 with pytest.
    """
    assert create_dataset(rule_101, data=dataset, org=organization) == output101


# Rule 102 filters rows based on all columns from each table and multiple values from each column or any of the columns where one value could be an interval
# and the other could be a single value.

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
                "collection": "cpTP24h",
                "dateTime": Timestamp("2021-01-25 21:00:00"),
                "dateTimeEnd": Timestamp("2021-01-24 08:00:00"),
                "dateTimeStart": Timestamp("2021-01-24 08:00:00"),
                "fieldSampleTempC": 17,
                "sampleID": "Sample S106",
                "sizeL": 2,
                "storageTempC": 18,
                "type": "pSludge",
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
                            "collection": "mooreSw",
                            "dateTime": Timestamp("2021-02-01 21:00:00"),
                            "dateTimeEnd": Timestamp("2021-01-29 21:00:00"),
                            "dateTimeStart": Timestamp("2021-02-01 21:00:00"),
                            "fieldSampleTempC": 15,
                            "sampleID": "Sample S100",
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
                            "sampleID": "Sample S107",
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
    This method tests the function create_dataset against rule_102 with pytest.
    """
    assert create_dataset(rule_102, data=dataset, org=organization) == output102
