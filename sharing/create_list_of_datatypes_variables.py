"""
This module creates lists of variables of differnt datatypes.
"""

from typing import Tuple


def create_list_of_datatypes_variables(
    temp_datatype_dict: dict, table: str, to_keep_vars: list
) -> Tuple[str, dict, list, list, list]:
    """The function creates lists of variables of different datatypes.

    The functions uses the metadata from variables.csv file to create three
    different lists of different datatype. One of datetime type, other of
    numeric type and third of string type.

    Parameters:
        temp_datatype_dict(dict): dictionaries of variable metadata
        to_keep_vars(list): list of variables to keep in current rule
    Returns:
        pri_var: the primary key variable
        dict: dictionary of variables metadata
        list: list of variables with different datatype
    """

    # For each table in current rule, create a list of variables of different
    # datatypes (datetime, numeric, or string type)
    datetime_variables = []
    string_variables = []
    numeric_variables = []

    # temp_datatype_dict[table] is a list of dictionaries where each dictionary
    # contains the metadata for each variables in that table such as primary,
    # foreign key, and variable datatype
    for var in temp_datatype_dict[table]:
        columns_to_check = [var.lower() for var in to_keep_vars]

        # checks if the variable exist in the current rule
        if var["variableName"].lower() in columns_to_check:

            # If variables are not part of current rule columns, continue
            if var["variableType"] == "integer" or var["variableType"] == "float":

                # Add float variables to list numeric_variables
                numeric_variables.append(var["variableName"])
            elif (
                var["variableType"] == "string"
                or var["variableType"] == "category"
                or var["variableType"] == "boolean"
            ):

                # Add character variables to list string_variables
                string_variables.append(var["variableName"])
            elif var["variableType"] == "datetime" or var["variableType"] == "date":

                # Add character variables to list string_variables
                datetime_variables.append(var["variableName"])
        if var["key"] == "Primary Key":
            pri_var = var["variableName"]
    return (
        pri_var,
        temp_datatype_dict,
        numeric_variables,
        string_variables,
        datetime_variables,
    )
