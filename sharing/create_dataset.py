"""
This module returns final filtered dataset and summary of removed data.
"""
from typing import List, Dict, Any
from numpy import nan
import pandas as pd
from pandas.core.frame import DataFrame
from classes_for_datatypes import Rule, VariableMetaData, RuleSummary, ReturnedData
from apply_rule_to_tables import apply_rule_to_tables


def create_dataset(
    rules: List[Rule], data: Dict[str, List[Dict[str, Any]]], org: str
) -> ReturnedData:
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
    original_tables: List[str] = list(variables["tableName"].unique())

    # For each table, create a list of dictionaries that contains the metadata
    # primary, foreign keys, variable type information for each variable
    # Add the metadata for each table as value for the table key in dictionary
    # datatype_dict
    tables_metadata: Dict[str, List[VariableMetaData]] = {}
    for table in original_tables:
        tables_metadata[table] = variables[variables["tableName"] == table].to_dict(
            "records"
        )

    # filtered_data is the copy of the data provided by the user.
    # It is returned to the user after filter.
    filtered_data: Dict[str, List[Dict[str, Any]]] = data.copy()

    # Check whether the given organization is part of current rule, then add
    # the rule to a list 'org_rule'. Each rule is a dictionary
    org_rules: List[Rule] = []

    for rule in rules:
        list_of_organizations: List[str] = rule["sharedWith"].split(";")
        if org in list_of_organizations:
            org_rules.append(rule)

    sharing_summary: List[RuleSummary] = []

    # ITTERATE THROUGH EACH RULE
    for org_rule in org_rules:

        #'filtered_data' is the dictionary with filtered data
        # calls the function 'apply_rule_to_tables' to iterate through each table
        # and finally returns the 'filtered_data' and the 'current_rule_summary'.
        (filtered_data, current_rule_summary,) = apply_rule_to_tables(
            org_rule, tables_metadata, filtered_data,
        )
        for data_removed in current_rule_summary["entities_filtered"]:
            if "rows_removed" in data_removed.keys():
                for row in data_removed["rows_removed"]:
                    for key in row.keys():
                        if row[key] == nan:
                            row[key] = "null"

        sharing_summary.append(current_rule_summary)
    # If the value for any variable in the data is nan, the
    # for loop below replaces it with "null" value as the code
    # fails to compare nan values when testing the code with test cases
    for table in filtered_data.keys():
        for row in filtered_data[table]:
            for variable in row.keys():
                if row[variable] == nan:
                    row["variable"] = "null"

    # returned_data is the dictionary with two keys returned to user:
    # one key containing the filtered_data and the other with the removed data
    returned_data: ReturnedData = {}
    returned_data["filtered_data"] = filtered_data
    returned_data["sharing_summary"] = sharing_summary
    return returned_data
