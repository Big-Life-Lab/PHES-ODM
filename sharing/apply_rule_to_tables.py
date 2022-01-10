"""
This module loops through each each table within the current rule.
"""
from typing import List, Dict, Any, Tuple, Sequence
from pandas.core.frame import DataFrame
from numpy import nan
import pandas as pd
from classes_for_datatypes import Rule, VariableMetaData, RuleSummary
from create_list_of_datatypes_variables import create_list_of_datatypes_variables
from loop_through_rule_values import loop_through_rule_values
from sharing_csv_helpers import (
    get_tables_for_rule,
    get_variables_for_rule,
    split_cell_value,
)


def apply_rule_to_tables(
    rule: Rule,
    tables_metadata: Dict[str, List[VariableMetaData]],
    filtered_data: Dict[str, List[Dict[str, Any]]],
) -> Tuple[Dict[Any, List[Dict[Any, Any]]], DataFrame, RuleSummary]:
    """This function iterates through each table in the current rule.

    Function iterates through each table in current rule. It creates
    current_table_data which contains data for current table. It creates
    list of variables 'to_keep_vars' that contains variables to keep in
    the current rule.
    The function also creates variables that stores the names of current rule
    variables for different dataypes (datatetime, numeric and string) and filters
    rule values of specific datatypes through the specific variable types
    lists.
    It creates list of rules in the current ruleValue sharing property to loop
    through. Function returns dictionaries and dataframe with filtered data
    and the summary of data removed.

    Parameters:
        rule (dict): current organization rule for current itteration
        datatype_dict (list): list of dictionaries with metadata for each table
        filtered_data (dict): Data to be filtered
        current_rule_summary (dict): will be updated with removed data
        updated_data_dict (dict): updated original dataset dictionary for current rule
    Returns:
        filtered_data(dict): Data filtered for current rule iteration
        updated_data_dict(dict): updated filtered data for current rule
        current_rule_summary(dict): contain removed data
    """

    # Create a dictionary that will contain the entities and data removed.
    current_rule_summary: RuleSummary = {
        "entities_filtered": [],
        "rule_id": rule["ruleID"],
    }
    list_tables: List[str] = get_tables_for_rule(rule, filtered_data.keys())
    # ITTERATE through all the tables in the list of tables in current rule
    for table in list_tables:

        # create a pandas dataframe of the table and store in variable
        # named 'current_table_data'
        current_table_data: DataFrame = pd.DataFrame(filtered_data[table])

        list_variables: List[str] = get_variables_for_rule(
            rule, list(current_table_data.columns)
        )
        # Make sure the variable name has no leading or trailing spaces.\
        list_variables = [
            var.strip() if isinstance(var, str) else var for var in list_variables
        ]

        # Separate the variables of different datatypes in to different list
        # using the function create_list_of_datatypes_variables
        (
            pri_var,
            numeric_variables,
            string_variables,
            datetime_variables,
        ) = create_list_of_datatypes_variables(tables_metadata[table], list_variables)

        rule_values = split_cell_value(rule["ruleValue"])

        # Ensure no leading or trailing spaces present
        rule_values = [rule.strip() for rule in rule_values]  # type: ignore

        # current_table_filtered_data is the dataframe for current table
        # which is filtered by itterating through all the
        # ruleValues for current rule
        current_table_filtered_data = loop_through_rule_values(
            rule,
            rule_values,
            current_table_data,
            list_variables,
            datetime_variables,
            numeric_variables,
            string_variables,
        )

        # create copy of original table that contains starting data for
        # each iteration and store it in variable original_table_data_copy
        # this dataframe is used to filter the rows removed for
        # each iteration it gets updated each iteration with filtered data
        # from last iteration
        original_table_data_copy = pd.DataFrame(filtered_data[table]).copy()

        # Add the values for entities filtered, removed_data, and table name
        # in the current_rule_summary dictionary
        current_rule_summary["entities_filtered"].append({})

        # Add the details of entities and rows removed to 'current_rule_summary'
        # along with the table name. Concatenate the original data with the
        # filtered dataset (which has been filtered for the current rule for given table)
        if rule["direction"] == "row":
            original_filtered_table: DataFrame = pd.concat(
                [original_table_data_copy, current_table_filtered_data], axis=0
            )

            # drop duplicates from original data to get the rows that were removed
            # from the original data from current table
            removed_data: DataFrame = original_filtered_table.drop_duplicates(
                keep=False
            )
            current_rule_summary["entities_filtered"][-1].update(
                {"rows_removed": removed_data.to_dict("records"), "table": table}
            )

        elif rule["direction"] == "column":
            original_filtered_table = pd.concat(
                [original_table_data_copy, current_table_filtered_data], axis=1
            )
            # drop duplicates from original data to get the rows that were removed
            # from the original data from current table
            removed_data = original_filtered_table.loc[
                :, ~original_filtered_table.columns.duplicated(keep=False)
            ]
            removed_data.insert(
                0, pri_var, pd.DataFrame(filtered_data[table])[pri_var], True
            )
            current_rule_summary["entities_filtered"][-1].update(
                {"columns_removed": {}, "table": table}
            )
            removed_columns = list(removed_data.columns)
            removed_columns.remove(pri_var)

            for col in removed_columns:

                temp_df = removed_data[[pri_var, col]]
                current_rule_summary["entities_filtered"][-1]["columns_removed"][
                    col
                ] = temp_df.to_dict("records")

        # Append current_rule_summary to the returned_data list
        filtered_data[table] = current_table_filtered_data.to_dict("records")

    # After all tables are filtered in the loop then return the filtered_data
    # and current_rule_summary. Also return updated dictionary updated_data_dict
    return filtered_data, current_rule_summary
