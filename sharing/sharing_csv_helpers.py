"""
This module will return a list of table names or variable names in current
rule.
"""
from typing import List, Dict, Any
from pandas.core.frame import DataFrame
import pandas as pd
from classes_for_datatypes import Rule, RuleSummary


def split_value_in_rule_dict(
    rule: Rule,
    filtered_data: Dict[Any, List[Dict[Any, Any]]],
    value="all",
    to_split="table",
    current_rule_data: DataFrame = pd.DataFrame(),
) -> List[str]:
    """
    Function returns list of table names or variable names in current rule.

    Parameters:
    rule (dict): current organization rule
    filtered_data (dict): User data to be filtered
    value (str): value for table or variable key in current rule
    to_split (str): key of the rule passed in as parameter (table or variable)
    current_rule_data (DataFrame): current user table being itterated
    Returns:
    list_values (List): list of table names or variable names in current rule
    """
    if rule[to_split].strip().lower() == value and to_split == "table":
        list_values: List[str] = list(filtered_data.keys())
    elif rule[to_split].strip().lower() == value and to_split == "variable":
        list_values: List[str] = list(current_rule_data.columns)
    else:
        list_values = rule[to_split].split(";")

    return list_values
