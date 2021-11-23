"""
This module returns final filtered dataset and summary of removed data.
"""

from numpy import nan
import pandas as pd
from pandas.core.frame import DataFrame  # pylint: disable=import-error

# import loop_through_tables # pylint: disable=import-error
import loop_through_tables
from typing import Any, Dict, List, TypedDict, Union


class MetaData(TypedDict, total=False):
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


class Rules(TypedDict, total=False):
    ruleID: str
    table: str
    variable: str
    ruleValue: Union[str, int, float]
    direction: str
    sharedWith: str


class CurrentRuleSummary(TypedDict, total=False):
    entities_filtered: List[Dict[str, Any]]
    rule_id: Any


class ReturnedData(TypedDict, total=False):
    filtered_data: Dict[Any, List[Dict[Any, Any]]]
    sharing_summary: List[CurrentRuleSummary]


# from pandas import Timestamp  # pylint: disable=import-error
def create_dataset(rules: List[Rules], data: Dict[Any, Any], org: str) -> ReturnedData:
    """Filters data and returns filtered data and shared summary in dictionary.

    The function will filter only those rules from rules list that correspond
    to the particular organization user has requested and create a list
    org_rules. It will iterate through each rule in org_rule to the filter
    the user data. Return is a list of two dictionaries. One dictionary is
    the filtered data. Other is the current_rule_summary that contains details
    about entities and rows removed.

    Parameters:
        rules(list): list of rule dictionaries
        data(dict): user data to be filtered
        org(str): name of the requested organization

    Returns:
        list: list of two dictionaries with filtered data and entities removed
    """

    # Load the variables.csv file to get the primary key values for each variables in the data
    variables: DataFrame = pd.read_csv("Variables.csv", delimiter=",")

    # Fetch all the names of tables in the ODM
    original_tables: List[Any] = list(variables["tableName"].unique())

    # For each table, create a list of dictionaries that contains the metadata
    # primary, foreign keys, variable type information for each variable
    # Add the metadata for each table as value for the table key in dictionary
    # datatype_dict
    datatype_dict: Dict[str, List[MetaData]] = {}
    for table in original_tables:
        datatype_dict[table] = variables[variables["tableName"] == table].to_dict(
            "records"
        )

    # filtered_data is the copy of the data provided by the user.
    # It is returned to the user after filter.
    filtered_data: Dict[Any, List[Dict[Any, Any]]] = data.copy()

    # Check whether the given organization is part of current rule, then add
    # the rule to a list 'org_rule'. Each rule is a dictionary
    org_rule: List[Rules] = []

    for rule_org in rules:
        if ";" in rule_org["sharedWith"]:
            list_of_organizations: List[str] = rule_org["sharedWith"].split(";")
        else:
            list_of_organizations = [rule_org["sharedWith"]]
        if org in list_of_organizations:
            org_rule.append(rule_org)

    # Create a copy of original dataset dictionary.
    # This is updated for each iteration to detect rows removed.
    updated_data_dict: Dict[Any, List[Dict[Any, Any]]] = data.copy()

    # returned_data is the dictionary with two keys returned to user:
    # one key containing the filtered_data and the other with the removed data
    returned_data: ReturnedData = {}
    sharing_summary: List[CurrentRuleSummary] = []

    # ITTERATE THROUGH EACH RULE
    for rule in org_rule:
        current_rule: Rules = rule
        # Create a dictionary that will contain the entities and data removed.
        current_rule_summary: CurrentRuleSummary = {
            "entities_filtered": [],
            "rule_id": current_rule["ruleID"],
        }

        # Create an empty dataframe only if it does not exist
        # This dataframe is used to detect rows removed in each iteration.
        try:
            original_table_data_copy  # type: ignore
        except NameError:
            original_table_data_copy: DataFrame = pd.DataFrame()

        #'filtered_data' is the dictionary with filtered data
        # calls the function 'loop_through_tables' to iterate through each table
        # and finally returns the 'filtered_data' and the 'current_rule_summary'.
        (
            filtered_data,
            original_table_data_copy,
            current_rule_summary,
        ) = loop_through_tables.loop_through_tables(
            current_rule,
            datatype_dict,
            filtered_data,
            current_rule_summary,
            original_table_data_copy,
            updated_data_dict,
        )
        sharing_summary.append(current_rule_summary)
    for table in filtered_data.keys():
        for row in filtered_data[table]:
            for variable in row.keys():
                if row[variable] == nan:
                    row["variable"] = "null"

    returned_data["filtered_data"] = filtered_data
    returned_data["sharing_summary"] = sharing_summary
    return returned_data
