# -*- coding: utf-8 -*-
"""
This module iterates through each rule in the ruleValues.
"""
from typing import List, Any, Sequence, Union
import re
from pandas.core.frame import DataFrame  # pylint: disable=import-error
from classes_for_datatypes import Rule
from check_rule_type import check_type_of_rule  # pylint: disable=import-error
from filter_range_values import filter_range_value
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
        datetime_variables(list): current rule variables list of type datetime
        numeric_variables(list): current rule variables list of type numeric
        string_variables(list): current rule variables list of type string

    Returns:
        dataframe: filtered data for current rule table

    """

    # Setting patterns for detecting type of brackets

    # ITTERATING THROUGH EACH RULEVALUE
    for rule_value in rule_values:

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

        # Create boolean variables that checks if the current filter value
        # is a datetime or numeric or character value
        rule_is_datetime: bool = False
        rule_is_numeric: bool = False
        rule_is_char: bool = False

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

        # if ruleValue is 'ALL', remove all columns and rows from dataframe
        if isinstance(rule_value, str):
            if rule_value.strip().lower() == "all" and rule["direction"] == "row":
                table_data = table_data.drop(list(table_data.columns), axis=1)
                return table_data

            if rule_value.strip().lower() == "all" and rule["direction"] == "column":
                # Drop all columns in current rule
                variables_in_rule: List[Any] = (
                    numeric_variables + datetime_variables + string_variables
                )
                table_data = table_data.drop(variables_in_rule, axis=1)
                return table_data

        # Check whether there is a lower or upper limit value
        if lower_limit and upper_limit:

            # function check_type_of_rule will check whether
            # string is of datetime type, then only calls
            # other functions to filter by datetime
            rule_is_datetime = check_type_of_rule(
                rule_is_datetime, lower_limit, upper_limit, filter_val
            )

            # If the rule_is_datetime, then parse values as datetime objects
            if rule_is_datetime:
                for datetime_var in datetime_variables:
                    low_limit, up_limit = parse_range_limit_as_datetime(
                        lower_limit, upper_limit, table_data, datetime_var,
                    )

                    # Filter values based on datetime filter rule
                    table_data = filter_range_value(
                        column, bracket, low_limit, up_limit, table_data, datetime_var,
                    )

            elif not rule_is_datetime:

                # If rule is not datetime and lower and upper limit exist
                # Then set rule as numeric.
                rule_is_numeric = True

                # Parse values as integer or float values
                for numeric_var in numeric_variables:
                    low_limit, up_limit = parse_range_limits_as_numeric(
                        lower_limit, upper_limit, table_data, numeric_var
                    )

                    # Filter based on numeric filter rule
                    table_data = filter_range_value(
                        column, bracket, low_limit, up_limit, table_data, numeric_var,
                    )

        # if there is no lower and upper limit then filter by single value
        elif filter_val and list(table_data.columns):
            (
                table_data,
                rule_is_datetime,
                rule_is_numeric,
                rule_is_char,
            ) = filter_single_value(
                column,
                filter_val,
                rule_is_datetime,
                rule_is_numeric,
                rule_is_char,
                table_data,
                datetime_variables,
                numeric_variables,
                string_variables,
            )
    return table_data
