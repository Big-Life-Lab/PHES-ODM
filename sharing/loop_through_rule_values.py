# -*- coding: utf-8 -*-
"""
This module iterates through each rule in the ruleValues.
"""
from typing import List, Sequence, Union
import re
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from classes_for_datatypes import Rule
from filter_range_values import Interval, filter_data_with_interval
from filter_single_value import filter_single_value
from parse_range_limit_as_datetime import parse_range_limit_as_datetime
from parse_range_limit_as_numeric import parse_range_limits_as_numeric
from regex_patterns import (
    left_closed_interval_pattern,
    left_open_interval_pattern,
    right_closed_interval_pattern,
    right_open_interval_pattern,
)


def loop_through_rule_values(
    rule: Rule,
    rule_values: Sequence[Union[str, int, float]],
    table_data: DataFrame,
    list_variables: List[str],
    datetime_variables: List[str],
    numeric_variables: List[str],
    string_variables: List[str],
) -> DataFrame:
    """The function filters data by iterating through each rule value.

    The function filters the current rule data by iterating through each rule.
    The function also checks whether each rule value is of range type and
    defines a bracket type. Determines the limit (lower and upper) for range
    type or the single filter value.
    If the rule is of datetime type, then loops through the datetime variables.
    If the rule value is of numeric type, then loops through the numeric
    variables of current rule.

    The function returns the the filtered data for current table.

    Parameters:
        rule(dict): current organization rule
        rule_values(list): rule in current ruleValue sharing property
        table_data(dataframe): data to be filtered for each table
        list_variables(list): list of variables in current rule
        datetime_variables(list): current rule variables list of type datetime
        numeric_variables(list): current rule variables list of type numeric
        string_variables(list): current rule variables list of type string

    Returns:
        dataframe: filtered data for current rule table

    """

    # Setting patterns for detecting type of brackets

    # ITTERATING THROUGH EACH RULEVALUE
    for rule_value in rule_values:

        # if ruleValue is 'ALL', remove all columns and rows from dataframe
        if isinstance(rule_value, str):
            if rule_value.strip().lower() == "all" and rule["direction"] == "row":
                table_data = table_data.drop(list(table_data.columns), axis=1)
                return table_data

            if rule_value.strip().lower() == "all" and rule["direction"] == "column":
                # Drop all columns in current rule

                table_data = table_data.drop(list_variables, axis=1)
                return table_data
        if isinstance(rule_value, str):
            rule_value = rule_value.strip()

        # Assign a variable for the bracket type, defines lower and upper limit
        # if the particular ruleValue is a range type
        bracket: str = ""
        lower_limit: str = ""
        upper_limit: str = ""

        # Assign a variable for the ruleValue that is not a range type
        filter_val: Union[str, float, int, None] = None

        if isinstance(rule_value, str):

            # Determine the type of bracket present in the ruleValue if it is a range type.
            if (
                re.search(left_closed_interval_pattern, rule_value) is not None
                and re.search(right_closed_interval_pattern, rule_value) is not None
            ):
                bracket = "[]"

            elif (
                re.search(left_open_interval_pattern, rule_value) is not None
                and re.search(right_open_interval_pattern, rule_value) is not None
            ):
                bracket = "()"

            elif (
                re.search(left_open_interval_pattern, rule_value) is not None
                and re.search(right_closed_interval_pattern, rule_value) is not None
            ):
                bracket = "(]"

            elif (
                re.search(left_closed_interval_pattern, rule_value) is not None
                and re.search(right_open_interval_pattern, rule_value) is not None
            ):
                bracket = "[)"

        # Confirm if the ruleValue is range type by checking if bracket exist
        # & create upper_limit and lower_limit value
        if bracket and isinstance(rule_value, str):
            if "," in rule_value:
                lower_limit = rule_value.split(",")[0].strip()
                lower_limit = lower_limit.replace(lower_limit[0], "").strip().lower()
                upper_limit = rule_value.split(",")[-1].strip()
                upper_limit = upper_limit.replace(upper_limit[-1], "").strip().lower()
            else:
                raise Exception(
                    "This is not a range as the numbers have not been separated by comma."
                )

        # if the ruleValue is not a range type then store the single value
        # to filter in variable 'filter_val'
        else:
            if isinstance(rule_value, str):
                filter_val = rule_value.strip()
            else:
                filter_val = rule_value

        # If the direction of the rule is row, remove rows of data based on rule
        if rule["direction"] == "row":
            column: bool = False
        elif rule["direction"] == "column":
            column = True
        # Raise an exception if the rule direction is not row or column
        elif rule["direction"] != "row" or rule["direction"] != "column":
            raise Exception(
                'Sorry this is not a correct direction for a \
                    rule. Please enter either value of "row" or "column".'
            )

        # Itterate through the list of variables in current rule
        for variable in list_variables:

            # Does not proceed to filter if the dataset is already empty
            if not table_data.empty and variable in table_data.columns:
                if variable in datetime_variables:
                    table_data[variable] = pd.to_datetime(table_data[variable])

                    # Parse the ruleValue as datetime if variable is datetime type
                    low_limit, up_limit, filter_val = parse_range_limit_as_datetime(
                        table_data, variable, lower_limit, upper_limit, filter_val
                    )
                elif variable in numeric_variables:

                    # Parse the ruleValue as numeric if variable is numeric type
                    low_limit, up_limit, filter_val = parse_range_limits_as_numeric(
                        lower_limit, upper_limit, filter_val,
                    )

                elif variable in string_variables:
                    low_limit = None
                    up_limit = None

                if low_limit and up_limit:

                    # Filter values based on datetime filter rule
                    interval: Interval = {
                        "left_limit": low_limit,
                        "right_limit": up_limit,
                        "bracket": bracket,
                    }

                    # Check if variable is of datetime type then
                    # change the limits and the column in dataset to np.int
                    # for comparing the datetime values in filter_range_values
                    if variable in datetime_variables:
                        interval["left_limit"] = interval["left_limit"].asm8.astype(
                            np.int64
                        )
                        interval["right_limit"] = interval["right_limit"].asm8.astype(
                            np.int64
                        )
                        table_data[variable] = pd.DataFrame(
                            table_data[variable]
                        ).applymap(lambda x: x.asm8.astype(np.int64))

                    # If column = True then filter by column axis
                    if column:
                        new_data = filter_data_with_interval(
                            interval, pd.DataFrame(table_data[variable]), axis="column",
                        )

                        # If empty dataframe is returned then drop the column
                        # from the original dataset.
                        if new_data.empty:
                            table_data.drop([variable], axis=1, inplace=True)

                    # Handle row filter
                    elif not column:

                        table_data[variable] = filter_data_with_interval(
                            interval, pd.DataFrame(table_data[variable]), axis="row",
                        )

                # if there is no lower and upper limit then filter by single value
                elif filter_val and list(table_data.columns):
                    table_data = filter_single_value(
                        column, filter_val, table_data, variable,
                    )

                # The columns that were filtered in the dataframe will contain
                # nan values in the rows that were filtered.
                # Drop the null values from dataframe from the variables
                # that were filtered.
                if variable in table_data.columns:
                    table_data.dropna(subset=[variable], inplace=True)
                    # If it is a datetime variable make sure to
                    # convert it into datetime type from np.int
                    if variable in datetime_variables:
                        table_data[variable] = pd.to_datetime(table_data[variable])

    return table_data
