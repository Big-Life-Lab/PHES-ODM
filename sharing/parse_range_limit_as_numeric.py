"""
This module parses range interval values as numeric datatypes.
"""
from typing import Tuple
import re
import numpy as np


def parse_range_limits_as_numeric(
    lower_limit: str = None, upper_limit: str = None, filter_val: str = None,
) -> Tuple[float, float]:
    """
    This function will parse the lower and upper limit values as float datatype.

    Parameters:
    lower_limit (str): lower limit of the range rule value
    upper_limit (str): upper limit of the range rule value
    filter_val (str): single filter value
    Returns:
    low_limit (float): lower limit value parsed as float datatype
    up_limit (float): upper limit value parsed as float datatype
    filter_val (float): single filter value parsed as float datatype
    """
    low_limit = None
    up_limit = None
    if lower_limit or upper_limit:
        # HANDLING NUMERIC VALUES
        try:
            if lower_limit.lower().startswith("inf"):
                low_limit = -np.inf
                up_limit = float(upper_limit)

            elif upper_limit.lower().startswith("inf"):
                low_limit = float(lower_limit)
                up_limit = np.inf
            else:
                low_limit = float(lower_limit)
                up_limit = float(upper_limit)

        except:
            print("Error: The value provided could not be coerced to numeric")

    elif filter_val:

        # use regular expression to check if it is of numeric type
        # print(filter_val.isnumeric())
        if re.fullmatch(r"\d+\.*\d*", str(filter_val)):
            filter_val = float(str(filter_val))
        else:
            print("Error: The value provided could not be coerced to numeric")

    return low_limit, up_limit, filter_val
