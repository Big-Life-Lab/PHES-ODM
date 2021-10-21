"""
This module loops through each each table within the current rule.
"""

from typing import Tuple
from pandas.core.frame import DataFrame
from numpy import nan
import pandas as pd
from create_list_of_datatypes_variables import (
    create_list_of_datatypes_variables,
)
from loop_through_rules import loop_through_rules


def loop_through_tables(
    rule: dict,
    datatype_dict: dict,
    filtered_data: dict,
    current_rule_summary: dict,
    original_table_data_copy: DataFrame,
    updated_data_dict,
) -> Tuple[dict, DataFrame, dict]:
    """This function iterates through each table in the current rule.

    Function iterates through each table in current rule. It creates
    current_rule_data which contains data for current table. It creates
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
        rule (dict): current organization rule
        datatype_dict (list): list of dictionaries with metadata for each table
        filtered_data (dict): Data to be filtered
        current_rule_summary (dict): will be updated with removed data
        original_table_data_copy (dataframe): updated filtered data from each rule iteration
        updated_data_dict (dict): original dataset dictionary updated each iteration
    Returns:
        filtered_data(dict): Data filtered for current rule iteration
        original_data_copy(dataframe): updated filtered data for current rule
        current_rule_summary(dict): contain removed data
    """

    # tables present in current rule
    existing_tables = rule["table"]

    # list_tables is the list of all tables that exist in the current rule
    existing_variables = rule["variable"]
    if ";" in existing_tables:
        list_tables = existing_tables.split(";")
    elif existing_tables == "ALL":
        list_tables = list(filtered_data.keys())
    else:
        list_tables = [existing_tables]

    # Use a temporary dictionary that contains metadata for each table
    # such as variable type, primary and foreign key information
    temp_datatype_dict = {}

    # ITTERATE through all the tables in the list of tables in current rule

    # create a temporary variable to store table name for each rule.
    # set it to None initially

    for table in list_tables:

        # datatype_dict[table] is a list of dictionaries where each dictionary
        # contains all the primary, foreign keys and variable type for each
        # variable in current table
        temp_datatype_dict[table] = datatype_dict[table]

        # ITTERATE THROUGH EACH TABLE IN THE RULE
        if table in filtered_data.keys():
            # if table in current itteration is part of 'filtered_data' provided
            # by user, create  a pandas dataframe of it and store it in variable
            # named 'current_rule_data'
            current_rule_data = pd.DataFrame(filtered_data[table])
            if ";" in existing_variables:
                list_variables = existing_variables.split(";")
            elif existing_variables == "ALL":
                list_variables = list(current_rule_data.columns)
            else:
                list_variables = [existing_variables]

            # Make sure the variable name has no leading or trailing spaces.\
            list_variables = [
                var.strip() if isinstance(var, str) else var for var in list_variables
            ]

            # checks if the list of variables in current rule are also present in
            # the data provided by the user if present then create a list of
            # current variables named 'to_keep_vars'
            columns_to_check = [var.lower() for var in list_variables]
            to_keep_vars = [
                vars
                for vars in list(current_rule_data.columns)
                if vars.lower() in columns_to_check
            ]

            # Separate the variables of different datatypes in to different list
            # using the function create_list_of_datatypes_variables
            (
                temp_datatype_dict,
                numeric_variables,
                string_variables,
                datetime_variables,
            ) = create_list_of_datatypes_variables(
                temp_datatype_dict, table, to_keep_vars
            )

            rule_values = rule["ruleValue"]

            # Create list of all the RuleValues in current org_rule list_of_rules
            if isinstance(rule_values, (float, int)):
                list_of_rules = [rule_values]
            elif ";" in rule_values:
                list_of_rules = rule_values.split(";")
            else:
                list_of_rules = [rule_values]

            # Ensure no leading or trailing spaces present
            list_of_rules = [
                rule.strip() if isinstance(rule, str) else rule
                for rule in list_of_rules
            ]  # type: ignore

            # current_filtered_data is the dataframe for current table which is
            # filtered by itterating through all the ruleValues for current org_rule
            current_filtered_data = loop_through_rules(
                rule,
                list_of_rules,
                current_rule_data,
                datetime_variables,
                numeric_variables,
                string_variables,
            )

            # create copy of original table that contains starting data for each iteration
            # and store it in variable original_table_data_copy
            # this dataframe is used to filter the rows removed for each iteration
            # it gets updated each iteration with filtered data from last iteration

            original_table_data_copy = pd.DataFrame(updated_data_dict[table]).copy()

            # Add the details of entities and rows removed to 'current_rule_summary'
            # along with the table name. Concatenate the original data with the
            # filtered dataset (which has been filtered for the current rule for given table)
            original_filtered_table = pd.concat(
                [original_table_data_copy, current_filtered_data], axis=0
            )

            # drop duplicates from original data to get the rows that were removed
            # from the original data from current table
            removed_data = original_filtered_table.drop_duplicates(keep=False)

            # Add the values for entities filtered, removed_data, and table name
            # in the current_rule_summary dictionary
            current_rule_summary["entities_filtered"].append({})
            for num, entity_removed in enumerate(
                current_rule_summary["entities_filtered"]
            ):
                if entity_removed == {}:

                    # If the direction is row, add row_removed to the entities filtered
                    if rule["direction"] == "row":
                        current_rule_summary["entities_filtered"][num][
                            "rows_removed"
                        ] = removed_data.to_dict("records")
                        current_rule_summary["entities_filtered"][num]["table"] = table
                        for row in current_rule_summary["entities_filtered"][num][
                            "rows_removed"
                        ]:
                            for key in row.keys():
                                if row[key] == nan:
                                    row[key] = "null"

            # Append current_rule_summary to the returned_data list
            filtered_data[table] = current_filtered_data.to_dict("records")

            # update original_table_data_copy with current_filtered_data for next rule
            # update updated_data_dict dictionary after removing rows from the data.
            original_table_data_copy = current_filtered_data.copy()
            updated_data_dict[table] = original_table_data_copy.to_dict("records")
        else:
            print("Table in the rule does not exist in the data provided.")

    # After all tables are filtered in the loop then return the filtered_data
    # and current_rule_summary. Also return updated original_table_data_copy
    return filtered_data, original_table_data_copy, current_rule_summary
