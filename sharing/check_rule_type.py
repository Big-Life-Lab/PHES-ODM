"""
This module checks whether the rulevalue is of datetime datatype.
"""
from typing import Union
import re
from regex_patterns import (
    date_pattern_fwd_slash,
    date_pattern_back_slash,
    date_pattern_back_slash_h_m,
    date_pattern_fwd_slash_h_m,
    date_pattern_fwd_slash_h_m_s,
    date_pattern_back_slash_h_m_s,
)


def check_type_of_rule(
    rule_is_datetime: bool,
    lower_limit: str = None,
    upper_limit: str = None,
    filter_val: Union[str, int, float, None] = None,
) -> bool:
    """
    The function checks whether the range interval is of datetime type.

    Parameters:
    lower_limit (str): lower limit of the range interval
    upper_limit (str): upper limit of the range interval
    rule_is_datetime (bool): boolean value to check whether
    the rule is of datetime type
    Returns:
    rule_is_datetime (bool): boolean value returned specifying
    whether rule is of datetime type
    """
    # Checks if there is lower and upper limit for the rule.
    if lower_limit and upper_limit:

        # Define pattern for the datetime type
        # Then ensure if either of the limits is of datetime type:
        if (
            re.fullmatch(date_pattern_fwd_slash, str(lower_limit)) is not None
            or re.fullmatch(date_pattern_back_slash, str(lower_limit)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m, str(lower_limit)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m, str(lower_limit)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m_s, str(lower_limit)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m_s, str(lower_limit)) is not None
        ) or (
            re.fullmatch(date_pattern_fwd_slash, str(upper_limit)) is not None
            or re.fullmatch(date_pattern_back_slash, str(upper_limit)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m, str(upper_limit)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m, str(upper_limit)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m_s, str(upper_limit)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m_s, str(upper_limit)) is not None
        ):
            rule_is_datetime = True
    elif filter_val:
        if (
            re.fullmatch(date_pattern_fwd_slash, str(filter_val)) is not None
            or re.fullmatch(date_pattern_back_slash, str(filter_val)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m, str(filter_val)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m, str(filter_val)) is not None
            or re.fullmatch(date_pattern_back_slash_h_m_s, str(filter_val)) is not None
            or re.fullmatch(date_pattern_fwd_slash_h_m_s, str(filter_val)) is not None
        ):
            rule_is_datetime = True

    return rule_is_datetime
