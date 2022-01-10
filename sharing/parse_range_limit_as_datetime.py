"""
This module parses range interval values as datetime datatypes.
"""
from typing import List, Tuple
import re
from datetime import datetime, timedelta
import pandas as pd
from pandas.core.frame import DataFrame
from regex_patterns import date_time_pattern_iso_8601


def parse_range_limit_as_datetime(
    table_data: DataFrame,
    datetime_var: List[str],
    lower_limit: str = None,
    upper_limit: str = None,
    filter_val: str = None,
) -> Tuple[datetime, datetime]:
    """
    This function will parse the lower and upper limit values as datetime
    datatype.

    Parameters:
    lower_limit (str): lower limit of the range rule value
    upper_limit (str): upper limit of the range rule value
    table_data (DataFrame): Dataframe from the current table being itterated
    numeric_var (List): list of numeric variables in the current rule.
    Returns:
    low_limit (float): lower limit value parsed as datetime datatype
    up_limit (float): upper limit value parsed as datetime datatype
    """
    low_limit = None
    up_limit = None

    if lower_limit or upper_limit:
        # Checking pattern of bracket to determine if infinity is present
        try:
            if (
                re.fullmatch(date_time_pattern_iso_8601, str(lower_limit)) is not None
            ) and str(upper_limit).lower().startswith("inf"):
                low_limit = pd.to_datetime(lower_limit)
                up_limit = table_data[datetime_var].max() + timedelta(days=1)

            elif str(lower_limit).lower().startswith("inf") and (
                re.fullmatch(date_time_pattern_iso_8601, str(upper_limit)) is not None
            ):
                low_limit = table_data[datetime_var].min() - timedelta(days=1)
                up_limit = pd.to_datetime(upper_limit)

            else:
                low_limit: datetime = pd.to_datetime(lower_limit)
                up_limit: datetime = pd.to_datetime(upper_limit)
        except:
            print("Error: The value provided could not be coerced to datetime")

    elif filter_val:
        try:
            filter_val = pd.to_datetime(filter_val)
        except:
            print("Error: The value provided could not be coerced to datetime")

    return low_limit, up_limit, filter_val
