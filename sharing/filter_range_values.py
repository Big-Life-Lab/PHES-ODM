"""
This module filters rows and columns of data based on a range interval.
"""

from typing import TypedDict, List, Any
from pandas.core.frame import DataFrame
import pandas as pd


class Interval(TypedDict):
    """
    This classs defines the lower and upper limit of the range.
    """

    left_limit: Any
    right_limit: Any
    bracket: str


def is_within_interval(interval: Interval, data: DataFrame):
    """
    Function checks whether interval exist within the dataset based on bracket

    Parameter:
    interval (Interval): the interval with lower and upper limit of the range
    data (Dataframe): The dataset to be filtered

    Returns:
    data (Dataframe): Filtered dataset
    """
    if interval["bracket"] == "[]":
        return data.applymap(
            lambda x: x >= interval["left_limit"] and x <= interval["right_limit"]
        )
    elif interval["bracket"] == "[)":
        return data.applymap(
            lambda x: x >= interval["left_limit"] and x < interval["right_limit"]
        )
    elif interval["bracket"] == "(]":
        return data.applymap(
            lambda x: x > interval["left_limit"] and x <= interval["right_limit"]
        )
    elif interval["bracket"] == "()":

        return data.applymap(
            lambda x: x > interval["left_limit"] and x < interval["right_limit"]
        )
    else:
        raise f"Invalid bracket for interval {interval.bracket}"


def filter_data_with_interval(
    interval: Interval, data_frame: DataFrame, axis: str
) -> DataFrame:
    """
    Function will remove rows or columns from the data based on range interval

    Parameters:
    interval (Interval): lower and upper limit of range interval to check
    df (Dataframe): Dataframe to be filtered

    Returns:
    df (Dataframe): Filtered dataset
    """
    df_boolean = is_within_interval(interval, data_frame)

    if axis == "row":
        rows_to_remove: List[bool] = []
        for index, row in df_boolean.iterrows():
            if False in row.values:
                rows_to_remove.append(True)
            else:
                rows_to_remove.append(False)

        return data_frame.loc[rows_to_remove, :]
    elif axis == "column":
        for index, row in df_boolean.iterrows():
            # If the range exist within the variable
            # then return empty dataframe for that variable
            if True in row.values:
                return pd.DataFrame()
            else:
                continue
        return data_frame
