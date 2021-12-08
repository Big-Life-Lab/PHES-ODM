"""
This module defines classes that assigns datatypes for different
variables or parameters used in the function.
"""
from typing import Any, Dict, List, TypedDict, Union


class VariableMetaData(TypedDict):
    """
    This is a child class of TypeDict. It defines the data types of
    each variable in the variables.csv file.
    """

    tableName: str
    variableName: str
    variableLabel_en: str
    variableLabel_fr: str
    key: str
    foreignKeyTable: str
    foreignKeyVariable: str
    variableType: str
    variableDesc_en: str
    variableDesc_fr: str


class Rule(TypedDict, total=False):
    """
    Rules is a child class of TypeDict. It defines the data types of
    the values of each of the keys in rules dictionary provided by the user.
    """

    ruleID: str
    table: str
    variable: str
    ruleValue: Union[str, int, float]
    direction: str
    sharedWith: str


class RuleSummary(TypedDict, total=False):
    """
    CurrentRuleSummary is a child class of TypeDict. It provides
    the datatypes of the values for each key inside current_rule_summary
    dictionary that contains the information about data removed.
    """

    entities_filtered: List[Dict[str, Any]]
    rule_id: str


class ReturnedData(TypedDict, total=False):
    """
    ReturnedData is the child class of TypeDict. It provides the datatypes of
    of the values for each key in the returned_data dictionary that is
    returned to the user.
    """

    filtered_data: Dict[Any, List[Dict[Any, Any]]]
    sharing_summary: List[RuleSummary]
