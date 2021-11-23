"""
This module filters data by range between two numeric values.
"""

from typing import Tuple, List, Any, Union  # pylint: disable=import-error
from pandas.core.frame import DataFrame  # pylint: disable=import-error


def filter_range_by_numeric_vars(
    column: bool,
    bracket: str,
    lower_limit: str,
    upper_limit: str,
    intermediate_filtered_data: DataFrame,
    rule_is_numeric: bool,
    numeric_variables: List[Any],
) -> Tuple[DataFrame, bool]:
    """The function filters data by the numeric variables in current rule.

    Function checks if the current rule value is of numeric type using
    regular expression. If it is, then filters data by numeric variables
    in current rule.
    Function returns back the dataframe with or without filter operation.

    Parameter:
        column(bool): checks whether rule direction is column
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

    # If lower and upper limit value exist, then filter as per the range rule.
    if lower_limit and upper_limit:
        low_limit: Union[int, float, None] = None
        up_limit: Union[int, float, None] = None

        # HANDLING NUMERIC VALUES

        # iterate through numeric variables
        for numeric_var in numeric_variables:
            if lower_limit.startswith("inf"):
                rule_is_numeric = True

                # if lower limit is infinity subtract 1 from min value of that variable
                low_limit = intermediate_filtered_data[numeric_var].min() - 1
                up_limit = float(upper_limit)

            elif upper_limit.startswith("inf"):
                rule_is_numeric = True

                # if upper limit is infinity add 1 to the max value of that variable
                up_limit = intermediate_filtered_data[numeric_var].max() + 1
                low_limit = float(lower_limit)

            else:
                rule_is_numeric = True
                low_limit = float(lower_limit)
                up_limit = float(upper_limit)

            if rule_is_numeric:
                if not column:
                    # Check for type of bracket and then accordingly filter the range value
                    if bracket == "[]":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[numeric_var] >= low_limit)
                            | ~(intermediate_filtered_data[numeric_var] <= up_limit),
                            :,
                        ]

                    elif bracket == "[)":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[numeric_var] >= low_limit)
                            | ~(intermediate_filtered_data[numeric_var] < up_limit),
                            :,
                        ]

                    elif bracket == "(]":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[numeric_var] > low_limit)
                            | ~(intermediate_filtered_data[numeric_var] <= up_limit),
                            :,
                        ]

                    elif bracket == "()":
                        intermediate_filtered_data = intermediate_filtered_data.loc[
                            ~(intermediate_filtered_data[numeric_var] > low_limit)
                            | ~(intermediate_filtered_data[numeric_var] < up_limit),
                            :,
                        ]

                elif column and numeric_var in intermediate_filtered_data.columns:
                    if bracket == "[]":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[numeric_var] >= low_limit)
                            & (intermediate_filtered_data[numeric_var] <= up_limit),
                            numeric_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [numeric_var], axis=1
                            )
                    elif bracket == "[)":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[numeric_var] >= low_limit)
                            & (intermediate_filtered_data[numeric_var] < up_limit),
                            numeric_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [numeric_var], axis=1
                            )
                    elif bracket == "(]":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[numeric_var] > low_limit)
                            & (intermediate_filtered_data[numeric_var] <= up_limit),
                            numeric_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [numeric_var], axis=1
                            )

                    elif bracket == "()":
                        if intermediate_filtered_data.loc[
                            (intermediate_filtered_data[numeric_var] > low_limit)
                            & (intermediate_filtered_data[numeric_var] < up_limit),
                            numeric_var,
                        ].any():
                            # Drop the column
                            intermediate_filtered_data = intermediate_filtered_data.drop(
                                [numeric_var], axis=1
                            )

    return intermediate_filtered_data, rule_is_numeric
