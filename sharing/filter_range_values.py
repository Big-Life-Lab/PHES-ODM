"""
This module filters the data by a range between two datetime values.
"""

from typing import Tuple, Union  # pylint: disable=import-error
from datetime import datetime, timedelta  # pylint: disable=import-error
import re
import pandas as pd  # pylint: disable=import-error
from pandas.core.frame import DataFrame  # pylint: disable=import-error


def filter_range_value(
    column: bool,
    bracket: str,
    low_limit: str,
    up_limit: str,
    intermediate_filtered_data: DataFrame,
    var: str,
) -> Tuple[DataFrame, bool, bool, bool]:
    """The function filters data based on the type of range interval.

    Function returns back the dataframe with or without filter operation.

    Parameter:
        column(bool): checks whether the rule direction is column
        bracket(str): type of range bracket
        low_limit(str): lower limit of the range
        up_limit(str): upper limit of the range
        intermediate_filtered_data(dataframe): data to be filtered
        var(str): variable to be filtered by from current rule
    Returns:
        dataframe: Dataframe that is filtered if rule value is of datetime type
    """

    if not column:
        # Checks type of bracket to do conditional filtering
        if bracket == "[]":
            intermediate_filtered_data = intermediate_filtered_data.loc[
                ~(intermediate_filtered_data[var] >= low_limit)
                | ~(intermediate_filtered_data[var] <= up_limit),
                :,
            ]

        elif bracket == "[)":
            intermediate_filtered_data = intermediate_filtered_data.loc[
                ~(intermediate_filtered_data[var] >= low_limit)
                | ~(intermediate_filtered_data[var] < up_limit),
                :,
            ]

        elif bracket == "(]":
            intermediate_filtered_data = intermediate_filtered_data.loc[
                ~(intermediate_filtered_data[var] > low_limit)
                | ~(intermediate_filtered_data[var] <= up_limit),
                :,
            ]

        elif bracket == "()":
            intermediate_filtered_data = intermediate_filtered_data.loc[
                ~(intermediate_filtered_data[var] > low_limit)
                | ~(intermediate_filtered_data[var] < up_limit),
                :,
            ]
    elif column and var in intermediate_filtered_data.columns:
        if bracket == "[]":
            if intermediate_filtered_data.loc[
                (intermediate_filtered_data[var] >= low_limit)
                & (intermediate_filtered_data[var] <= up_limit),
                var,
            ].any():
                # Drop the column
                intermediate_filtered_data = intermediate_filtered_data.drop(
                    [var], axis=1
                )
        elif bracket == "[)":
            if intermediate_filtered_data.loc[
                (intermediate_filtered_data[var] >= low_limit)
                & (intermediate_filtered_data[var] < up_limit),
                var,
            ].any():
                # Drop the column
                intermediate_filtered_data = intermediate_filtered_data.drop(
                    [var], axis=1
                )
        elif bracket == "(]":
            if intermediate_filtered_data.loc[
                (intermediate_filtered_data[var] > low_limit)
                & (intermediate_filtered_data[var] <= up_limit),
                var,
            ].any():
                # Drop the column
                intermediate_filtered_data = intermediate_filtered_data.drop(
                    [var], axis=1
                )

        elif bracket == "()":
            if intermediate_filtered_data.loc[
                (intermediate_filtered_data[var] > low_limit)
                & (intermediate_filtered_data[var] < up_limit),
                var,
            ].any():
                # Drop the column
                intermediate_filtered_data = intermediate_filtered_data.drop(
                    [var], axis=1
                )

    return intermediate_filtered_data
