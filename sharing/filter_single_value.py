"""
This module filters data by a single rule value of any datatype.
"""

from typing import Tuple, List, Union
import re
import pandas as pd
from pandas.core.frame import DataFrame


def filter_single_value(
    column: bool,
    filter_val: Union[str, int, float, None],
    intermediate_filtered_data: DataFrame,
    variable: str,
) -> Tuple[
    DataFrame,
]:

    """The function will filter dataframe based on a single rule value.

    Parameters:
        column(bool): checks whether the rule direction is column or not
        filter_val(str): current single rule value
        variable(list): current rule variables of string type
    Returns:
        dataframe: filtered data
    """

    if not column:
        intermediate_filtered_data = intermediate_filtered_data.loc[
            (intermediate_filtered_data[variable] != filter_val), :
        ]
    elif column and variable in intermediate_filtered_data.columns:
        # Checks if the filter_val value exist in the
        # current variable
        if filter_val in intermediate_filtered_data[variable].to_list():
            intermediate_filtered_data = intermediate_filtered_data.drop(
                [variable], axis=1
            )

    return intermediate_filtered_data
