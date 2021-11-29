"""
This module filters data by a single rule value of any datatype.
"""

from typing import Any, Tuple, List, Union  # pylint: disable=import-error
import re
import pandas as pd  # pylint: disable=import-error
from pandas.core.frame import DataFrame  # pylint: disable=import-error


def filter_single_value(
    column: bool,
    pat1: str,
    pat2: str,
    pat7: str,
    pat8: str,
    pat9: str,
    pat10: str,
    filter_val: Union[str, int, float, None],
    rule_is_datetime: bool,
    rule_is_numeric: bool,
    rule_is_char: bool,
    intermediate_filtered_data: DataFrame,
    datetime_variables: List[Any],
    numeric_variables: List[Any],
    string_variables: List[Any],
) -> Tuple[DataFrame, bool, bool, bool]:

    """The function will filter dataframe based on a single rule value.

    The function will check if the current rule value is of string type.
    If so, will check if it is datetime type, numeric type of character type
    and accordingly filter from respective types of variables in current rule.
    The function returns the filtered dataframe.


    Parameters:
        column(bool): checks whether the rule direction is column or not
        pat1(str): the datetime pattern to check with refular expression
        pat2(str): the datetime pattern to check with refular expression
        pat7(str): the datetime pattern to check with refular expression
        pat8(str): the datetime pattern to check with refular expression
        pat9(str): the datetime pattern to check with refular expression
        pat10(str): the datetime pattern to check with refular expression
        filter_val(str): current single rule value
        rule_is_datetime(bool): bool variable checks rule value is datetime type
        rule_is_numeric(bool): bool variable checks rule value is numeric type
        rule_is_char(bool): bool variable checks rule value is string type
        datetime_variables(list): current rule variables of datetime type
        numeric_variables(list): current rule variables of numeric type
        string_variables(list): current rule variables of string type
    Returns:
        dataframe: filtered data
        bool: bool variable specifies if rule is datetime, numeric or character
    """

    # First check if the single ruleValue if of string type, then check if it is
    # of datetime type, numeric type or character type
    if isinstance(filter_val, str):
        for datetime_var in datetime_variables:

            # Check whether the ruleValue is of datetime type
            if (
                re.fullmatch(pat1, str(filter_val)) is not None
                or re.fullmatch(pat2, str(filter_val)) is not None
                or re.fullmatch(pat7, str(filter_val)) is not None
                or re.fullmatch(pat8, str(filter_val)) is not None
                or re.fullmatch(pat9, str(filter_val)) is not None
                or re.fullmatch(pat10, str(filter_val)) is not None
            ):
                rule_is_datetime = True
                filter_val = pd.to_datetime(filter_val)

                if not column and rule_is_datetime:
                    intermediate_filtered_data = intermediate_filtered_data.loc[
                        (intermediate_filtered_data[datetime_var] != filter_val), :
                    ]
                elif (
                    column
                    and rule_is_datetime
                    and datetime_var in intermediate_filtered_data.columns
                ):
                    if filter_val in intermediate_filtered_data[datetime_var].to_list():
                        intermediate_filtered_data = intermediate_filtered_data.drop(
                            [datetime_var], axis=1
                        )
            else:
                print("DATETIME MATCH NOT FOUND")

        # if rule_is_datetime is not set to True, check if it is numeric type
        if not rule_is_datetime:
            for numeric_var in numeric_variables:

                # use regular expression to check if it is of numeric type
                if re.fullmatch(r"(\d+)", str(filter_val)) or re.fullmatch(
                    r"(\d+\.\d+)", str(filter_val)
                ):
                    rule_is_numeric = True
                    filter_val = float(str(filter_val))

                    if not column and rule_is_numeric:
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            (intermediate_filtered_data[numeric_var] != filter_val)
                        ]
                    elif (
                        column
                        and rule_is_numeric
                        and numeric_var in intermediate_filtered_data.columns
                    ):
                        if (
                            filter_val
                            in intermediate_filtered_data[numeric_var].to_list()
                        ):
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [numeric_var], axis=1
                            )

        # If rule is neither datetime nor numeric
        if not rule_is_datetime and not rule_is_numeric:
            for char_var in string_variables:
                if not rule_is_datetime:
                    rule_is_char = True

                    if not column and rule_is_char:
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            (intermediate_filtered_data[char_var] != filter_val), :
                        ]
                    elif (
                        column
                        and rule_is_char
                        and char_var in intermediate_filtered_data.columns
                    ):
                        if filter_val in intermediate_filtered_data[char_var].to_list():
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [char_var], axis=1
                            )
    else:

        # if ruleValue is not of string type, filter it as a numeric type
        for numeric_var in numeric_variables:
            if not rule_is_datetime and (isinstance(filter_val, (float, int))):
                rule_is_numeric = True
                if not column and rule_is_numeric:
                    intermediate_filtered_data = intermediate_filtered_data.loc[
                        (intermediate_filtered_data[numeric_var] != filter_val), :
                    ]
                elif (
                    column
                    and rule_is_numeric
                    and numeric_var in intermediate_filtered_data.columns
                ):
                    if filter_val in intermediate_filtered_data[numeric_var].to_list():
                        intermediate_filtered_data = intermediate_filtered_data.drop(
                            [numeric_var], axis=1
                        )

    return intermediate_filtered_data, rule_is_datetime, rule_is_numeric, rule_is_char
