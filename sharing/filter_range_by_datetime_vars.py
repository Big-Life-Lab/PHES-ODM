"""
This module filters the data by a range between two datetime values.
"""

from typing import Any, Tuple, List, Union  # pylint: disable=import-error
from datetime import datetime, timedelta  # pylint: disable=import-error
import re
import pandas as pd  # pylint: disable=import-error
from pandas.core.frame import DataFrame  # pylint: disable=import-error
from filter_single_value import filter_single_value  # pylint: disable=import-error


def filter_range_by_datetime_vars(
    column: bool,
    bracket: str,
    lower_limit: str,
    upper_limit: str,
    filter_val: Union[str, int, float, None],
    intermediate_filtered_data: DataFrame,
    rule_is_datetime: bool,
    rule_is_numeric: bool,
    rule_is_char: bool,
    datetime_variables: List[Any],
    numeric_variables: List[Any],
    string_variables: List[Any],
) -> Tuple[DataFrame, bool, bool, bool]:
    """The function filters data by the datetime variables in current rule.

    Function checks if the current rule value is of datetime type using
    regular expression. If it is, then filters data by datetime variables
    in current rule.
    Function returns back the dataframe with or without filter operation.

    Parameter:
        column(bool): checks whether the rule direction is column
        bracket(str): type of range bracket
        lower_limit(str): lower limit of the range
        upper_limit(str): upper limit of the range
        filter_val(str): single value to filter
        intermediate_filtered_data(dataframe): data to be filtered
        rule_is_datetime(bool): bool variable checks rule value is datetime type
        rule_is_numeric(bool): bool variable checks rule value is numeric type
        rule_is_char(bool): bool variable checks rule value is string type
        datetime_variables(list): current rule variables of datetime type
        numeric_variables(list): current rule variables of numeric type
        string_variables(list): current rule variables of string type
    Returns:
        dataframe: Dataframe that is filtered if rule value is of datetime type
        bool: bool variable specifies the data type of rule
    """

    # Define pattern for the datetime type
    pat1: str = r"(\d+/\d+/\d+)"
    pat2: str = r"(\d+-\d+-\d+)"
    pat7: str = r"(\d+-\d+-\d+ \d+:\d+)"
    pat8: str = r"(\d+/\d+/\d+ \d+:\d+)"
    pat9: str = r"(\d+-\d+-\d+ \d+:\d+:\d+)"
    pat10: str = r"(\d+/\d+/\d+ \d+:\d+:\d+)"

    # First ensure if either of the limits is of datetime type:

    # Checks if there is lower and upper limit for the rule.
    if lower_limit and upper_limit:
        if (
            re.fullmatch(pat1, str(lower_limit)) is not None
            or re.fullmatch(pat2, str(lower_limit)) is not None
            or re.fullmatch(pat7, str(lower_limit)) is not None
            or re.fullmatch(pat8, str(lower_limit)) is not None
            or re.fullmatch(pat9, str(lower_limit)) is not None
            or re.fullmatch(pat10, str(lower_limit)) is not None
        ) or (
            re.fullmatch(pat1, str(upper_limit)) is not None
            or re.fullmatch(pat2, str(upper_limit)) is not None
            or re.fullmatch(pat7, str(upper_limit)) is not None
            or re.fullmatch(pat8, str(upper_limit)) is not None
            or re.fullmatch(pat9, str(upper_limit)) is not None
            or re.fullmatch(pat10, str(upper_limit)) is not None
        ):
            rule_is_datetime = True
        # If range type and rule is datetime, then loop through all datetime vars
        # and check if there is infinity in either limits
        if rule_is_datetime:
            for datetime_var in datetime_variables:

                # if regular expression in the ruleValue limits matches the datetime
                # pattern then it will set rule_is_datetime variable to True
                if (
                    re.fullmatch(pat1, str(lower_limit)) is not None
                    or re.fullmatch(pat2, str(lower_limit)) is not None
                    or re.fullmatch(pat7, str(lower_limit)) is not None
                    or re.fullmatch(pat8, str(lower_limit)) is not None
                    or re.fullmatch(pat9, str(lower_limit)) is not None
                    or re.fullmatch(pat10, str(lower_limit)) is not None
                ) and (
                    re.fullmatch(pat1, str(upper_limit)) is not None
                    or re.fullmatch(pat2, str(upper_limit)) is not None
                    or re.fullmatch(pat7, str(upper_limit)) is not None
                    or re.fullmatch(pat8, str(upper_limit)) is not None
                    or re.fullmatch(pat9, str(upper_limit)) is not None
                    or re.fullmatch(pat10, str(upper_limit)) is not None
                ):
                    rule_is_datetime = True

                    # Changes the limits to datetime type in pandas to filter
                    low_limit: datetime = pd.to_datetime(lower_limit)
                    up_limit: datetime = pd.to_datetime(upper_limit)
                elif (
                    re.fullmatch(pat1, str(lower_limit)) is not None
                    or re.fullmatch(pat2, str(lower_limit)) is not None
                    or re.fullmatch(pat7, str(lower_limit)) is not None
                    or re.fullmatch(pat8, str(lower_limit)) is not None
                    or re.fullmatch(pat9, str(lower_limit)) is not None
                    or re.fullmatch(pat10, str(lower_limit)) is not None
                ) and str(upper_limit).startswith("inf"):
                    rule_is_datetime = True
                    low_limit = pd.to_datetime(lower_limit)

                    # if upper limit is infinity, add 1 to the max value
                    up_limit = intermediate_filtered_data[
                        datetime_var
                    ].max() + timedelta(days=1)
                elif str(lower_limit).startswith("inf") and (
                    re.fullmatch(pat1, str(upper_limit)) is not None
                    or re.fullmatch(pat2, str(upper_limit)) is not None
                    or re.fullmatch(pat7, str(upper_limit)) is not None
                    or re.fullmatch(pat8, str(upper_limit)) is not None
                    or re.fullmatch(pat9, str(upper_limit)) is not None
                    or re.fullmatch(pat10, str(upper_limit)) is not None
                ):
                    rule_is_datetime = True
                    up_limit = pd.to_datetime(upper_limit)

                    # if lower limit is infinity, then subtract 1 from min value
                    low_limit = intermediate_filtered_data[
                        datetime_var
                    ].min() - timedelta(days=1)

                if not column:
                    # Checks type of bracket to do conditional filtering
                    if bracket == "[]":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[datetime_var] >= low_limit)
                            | ~(intermediate_filtered_data[datetime_var] <= up_limit),
                            :,
                        ]

                    elif bracket == "[)":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[datetime_var] >= low_limit)
                            | ~(intermediate_filtered_data[datetime_var] < up_limit),
                            :,
                        ]

                    elif bracket == "(]":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[datetime_var] > low_limit)
                            | ~(intermediate_filtered_data[datetime_var] <= up_limit),
                            :,
                        ]

                    elif bracket == "()":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[datetime_var] > low_limit)
                            | ~(intermediate_filtered_data[datetime_var] < up_limit),
                            :,
                        ]
                elif column and datetime_var in intermediate_filtered_data.columns:
                    if bracket == "[]":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[datetime_var] >= low_limit)
                            & (intermediate_filtered_data[datetime_var] <= up_limit),
                            datetime_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [datetime_var], axis=1
                            )
                    elif bracket == "[)":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[datetime_var] >= low_limit)
                            & (intermediate_filtered_data[datetime_var] < up_limit),
                            datetime_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [datetime_var], axis=1
                            )
                    elif bracket == "(]":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[datetime_var] > low_limit)
                            & (intermediate_filtered_data[datetime_var] <= up_limit),
                            datetime_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [datetime_var], axis=1
                            )

                    elif bracket == "()":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[datetime_var] > low_limit)
                            & (intermediate_filtered_data[datetime_var] < up_limit),
                            datetime_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [datetime_var], axis=1
                            )

    # if there is no lower and upper limit then filter by single value
    elif filter_val:
        (
            intermediate_filtered_data,
            rule_is_datetime,
            rule_is_numeric,
            rule_is_char,
        ) = filter_single_value(
            column,
            pat1,
            pat2,
            pat7,
            pat8,
            pat9,
            pat10,
            filter_val,
            rule_is_datetime,
            rule_is_numeric,
            rule_is_char,
            intermediate_filtered_data,
            datetime_variables,
            numeric_variables,
            string_variables,
        )
    return intermediate_filtered_data, rule_is_datetime, rule_is_numeric, rule_is_char
