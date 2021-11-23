# -*- coding: utf-8 -*-
"""
This module iterates through each rule in the ruleValues.
"""
from typing import List, Any, Sequence, TypedDict, Union
import re
from pandas.core.frame import DataFrame  # pylint: disable=import-error
import pandas as pd  # pylint: disable=import-error
from filter_range_by_datetime_vars import (
    filter_range_by_datetime_vars,
)  # pylint: disable=import-error
from filter_range_by_numeric_vars import (
    filter_range_by_numeric_vars,
)  # pylint: disable=import-error


class Rules(TypedDict, total=False):
    ruleID: str
    table: str
    variable: str
    ruleValue: Union[str, int, float]
    direction: str
    sharedWith: str


def loop_through_rules(
    rule: Rules,
    list_of_rules: Sequence[Union[str, int, float]],
    intermediate_filtered_data: DataFrame,
    datetime_variables: List[Any],
    numeric_variables: List[Any],
    string_variables: List[Any],
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
        list_of_rules(list): rule in current ruleValue sharing property
        intermediate_filtered_data(dataframe): data to be filtered for each table
        datetime_variables(list): current rule variables list of type datetime
        numeric_variables(list): current rule variables list of type numeric
        string_variables(list): current rule variables list of type string

    Returns:
        dataframe: filtered data for current rule table

    """

    # Setting patterns for detecting type of brackets
    pat3: str = r"^\["
    pat4: str = r"\]$"
    pat5: str = r"^\("
    pat6: str = r"\)$"

    # ITTERATING THROUGH EACH RULEVALUE
    for filter_rule in list_of_rules:

        filter_by: Union[str, int, float] = filter_rule
        if isinstance(filter_rule, str):
            filter_by = filter_rule.strip()

        # Assign a variable for the bracket type, defines lower and upper limit
        # if the particular ruleValue is a range type
        bracket: str = ""
        lower_limit: str = ""
        upper_limit: str = ""

        # Assign a variable for the ruleValue that is not a range type
        filter_val: Union[str, float, int, None] = None

        if isinstance(filter_by, str):

            # Determine the type of bracket present in the ruleValue if it is a range type.
            if (
                re.search(pat3, filter_by) is not None
                and re.search(pat4, filter_by) is not None
            ):
                bracket = "[]"
                print("BRACKET PRESENT []")
            if (
                re.search(pat5, filter_by) is not None
                and re.search(pat6, filter_by) is not None
            ):
                bracket = "()"
                print("BRACKET PRESENT ()")
            if (
                re.search(pat5, filter_by) is not None
                and re.search(pat4, filter_by) is not None
            ):
                bracket = "(]"
                print("BRACKET PRESENT (]")
            if (
                re.search(pat3, filter_by) is not None
                and re.search(pat6, filter_by) is not None
            ):
                bracket = "[)"
                print("BRACKET PRESENT [)")

        # Confirm if the ruleValue is range type by checking if bracket exist
        # & create upper_limit and lower_limit value
        if bracket and isinstance(filter_by, str):
            if "," in filter_by:
                filter_list = filter_by.split(",")
                lower_limit = filter_list[0].strip()
                lower_limit = lower_limit.replace(lower_limit[0], "")
                lower_limit = lower_limit.strip()
                lower_limit = lower_limit.lower()
                upper_limit = filter_list[-1].strip()
                upper_limit = upper_limit.replace(upper_limit[-1], "")
                upper_limit = upper_limit.strip()
                upper_limit = upper_limit.lower()
            else:
                filter_val = filter_by[0].strip()
                filter_val = filter_val[1:-1]

        # if the ruleValue is not a range type then store the single value
        # to filter in variable 'filter_val'
        else:
            if isinstance(filter_by, str):
                filter_val = filter_by.strip()
            else:
                filter_val = filter_by

        # Create boolean variables that checks if the current filter value
        # is a datetime or numeric or character value
        rule_is_datetime: bool = False
        rule_is_numeric: bool = False
        rule_is_char: bool = False

        # If the direction of the rule is row, remove rows of data based on rule
        if rule["direction"] == "row":
            column: bool = False
            # if ruleValue is 'ALL', remove all columns and rows from dataframe
            if filter_by == "ALL":
                intermediate_filtered_data = pd.DataFrame()
            else:

                # filter rows of data by datetime variables
                (
                    intermediate_filtered_data,
                    rule_is_datetime,
                    rule_is_numeric,
                    rule_is_char,
                ) = filter_range_by_datetime_vars(
                    column,
                    bracket,
                    lower_limit,
                    upper_limit,
                    filter_val,
                    intermediate_filtered_data,
                    rule_is_datetime,
                    rule_is_numeric,
                    rule_is_char,
                    datetime_variables,
                    numeric_variables,
                    string_variables,
                )

                # filters rows of data by numeric variables
                if not rule_is_datetime:
                    (
                        intermediate_filtered_data,
                        rule_is_numeric,
                    ) = filter_range_by_numeric_vars(
                        column,
                        bracket,
                        lower_limit,
                        upper_limit,
                        intermediate_filtered_data,
                        rule_is_numeric,
                        numeric_variables,
                    )
        elif rule["direction"] == "column":
            column = True
            if filter_by == "ALL":
                # Drop all columns in current rule
                variables_in_rule: List[Any] = (
                    numeric_variables + datetime_variables + string_variables
                )
                intermediate_filtered_data = intermediate_filtered_data.drop(
                    variables_in_rule, axis=1
                )
            else:
                # filter rows of data by datetime variables
                (
                    intermediate_filtered_data,
                    rule_is_datetime,
                    rule_is_numeric,
                    rule_is_char,
                ) = filter_range_by_datetime_vars(
                    column,
                    bracket,
                    lower_limit,
                    upper_limit,
                    filter_val,
                    intermediate_filtered_data,
                    rule_is_datetime,
                    rule_is_numeric,
                    rule_is_char,
                    datetime_variables,
                    numeric_variables,
                    string_variables,
                )

                # filters rows of data by numeric variables
                if not rule_is_datetime:
                    (
                        intermediate_filtered_data,
                        rule_is_numeric,
                    ) = filter_range_by_numeric_vars(
                        column,
                        bracket,
                        lower_limit,
                        upper_limit,
                        intermediate_filtered_data,
                        rule_is_numeric,
                        numeric_variables,
                    )

        # Raise an exception if the rule direction is not row or column
        elif rule["direction"] != "row" or rule["direction"] != "column":
            raise Exception(
                'Sorry this is not a correct direction for a \
                    rule. Please enter either value of "row" or "column".'
            )

    return intermediate_filtered_data
