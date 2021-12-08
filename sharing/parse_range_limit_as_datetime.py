"""
This module parses range interval values as datetime datatypes.
"""
from typing import List, Tuple
import re
from datetime import datetime, timedelta  # pylint: disable=import-error
import pandas as pd
from pandas.core.frame import DataFrame
from regex_patterns import (
    date_pattern_fwd_slash,
    date_pattern_back_slash,
    date_pattern_back_slash_h_m,
    date_pattern_fwd_slash_h_m,
    date_pattern_fwd_slash_h_m_s,
    date_pattern_back_slash_h_m_s,
)


def parse_range_limit_as_datetime(
    lower_limit: str, upper_limit: str, table_data: DataFrame, datetime_var: List[str],
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

    # Checking pattern of bracket to determine if infinity is present
    if (
        re.fullmatch(date_pattern_fwd_slash, str(lower_limit)) is not None
        or re.fullmatch(date_pattern_back_slash, str(lower_limit)) is not None
        or re.fullmatch(date_pattern_back_slash_h_m, str(lower_limit)) is not None
        or re.fullmatch(date_pattern_fwd_slash_h_m, str(lower_limit)) is not None
        or re.fullmatch(date_pattern_back_slash_h_m_s, str(lower_limit)) is not None
        or re.fullmatch(date_pattern_fwd_slash_h_m_s, str(lower_limit)) is not None
    ) and str(upper_limit).startswith("inf"):
        low_limit = pd.to_datetime(lower_limit)

        # if upper limit is infinity, add 1 to the max value
        up_limit = table_data[datetime_var].max() + timedelta(days=1)

    elif str(lower_limit).startswith("inf") and (
        re.fullmatch(date_pattern_fwd_slash, str(upper_limit)) is not None
        or re.fullmatch(date_pattern_back_slash, str(upper_limit)) is not None
        or re.fullmatch(date_pattern_back_slash_h_m, str(upper_limit)) is not None
        or re.fullmatch(date_pattern_fwd_slash_h_m, str(upper_limit)) is not None
        or re.fullmatch(date_pattern_back_slash_h_m_s, str(upper_limit)) is not None
        or re.fullmatch(date_pattern_fwd_slash_h_m_s, str(upper_limit)) is not None
    ):
        up_limit = pd.to_datetime(upper_limit)

        # if lower limit is infinity, then subtract 1 from min value
        low_limit = table_data[datetime_var].min() - timedelta(days=1)

    else:
        low_limit: datetime = pd.to_datetime(lower_limit)
        up_limit: datetime = pd.to_datetime(upper_limit)

    return low_limit, up_limit
