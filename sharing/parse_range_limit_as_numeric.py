"""
This module parses range interval values as numeric datatypes.
"""
from typing import List, Tuple

from pandas.core.frame import DataFrame


def parse_range_limits_as_numeric(
    lower_limit: str, upper_limit: str, table_data: DataFrame, numeric_var: List[str]
) -> Tuple[float, float]:
    """
    This function will parse the lower and upper limit values as float datatype.

    Parameters:
    lower_limit (str): lower limit of the range rule value
    upper_limit (str): upper limit of the range rule value
    table_data (DataFrame): Dataframe from the current table being itterated
    numeric_var (List): list of numeric variables in the current rule.
    Returns:
    low_limit (float): lower limit value parsed as float datatype
    up_limit (float): upper limit value parsed as float datatype
    """

    # HANDLING NUMERIC VALUES
    if lower_limit.startswith("inf"):

        # if lower limit is infinity subtract 1 from min value of that variable
        low_limit = table_data[numeric_var].min() - 1
        up_limit = float(upper_limit)
    elif upper_limit.startswith("inf"):

        # if upper limit is infinity add 1 to the max value of that variable
        up_limit = table_data[numeric_var].max() + 1
        low_limit = float(lower_limit)
    else:
        low_limit = float(lower_limit)
        up_limit = float(upper_limit)

    return low_limit, up_limit
