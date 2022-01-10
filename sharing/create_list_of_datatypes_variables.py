"""
This module creates lists of variables of differnt datatypes.
"""

from typing import Any, List, Tuple
from classes_for_datatypes import VariableMetaData


def create_list_of_datatypes_variables(
    current_table_metadata: List[VariableMetaData], to_keep_vars: List[str],
) -> Tuple[str, List[Any], List[Any], List[Any]]:
    """The function creates lists of variables of different datatypes.

    The functions uses the metadata from variables.csv file to create three
    different lists of different datatype. One of datetime type, other of
    numeric type and third of string type.

    Parameters:
        temp_datatype_dict(dict): dictionaries of variable metadata
        table(str): current table being itterated
        to_keep_vars(list): list of variables to keep in current rule
    Returns:
        pri_var: the primary key variable
        dict: dictionary of variables metadata
        list: list of variables with different datatype
    """

    # For each table in current rule, create a list of variables of different
    # datatypes (datetime, numeric, or string type)
    datetime_variables: List[Any] = []
    string_variables: List[Any] = []
    numeric_variables: List[Any] = []

    # temp_datatype_dict[table] is a list of dictionaries where each dictionary
    # contains the metadata for each variables in that table such as primary,
    # foreign key, and variable datatype
    for key in current_table_metadata:

        columns_to_check = [key.lower() for key in to_keep_vars]

        # checks if the variable exist in the current rule
        if key["variableName"].lower() in columns_to_check:

            # If variables are not part of current rule columns, continue
            if key["variableType"] == "integer" or key["variableType"] == "float":

                # Add float variables to list numeric_variables
                numeric_variables.append(key["variableName"])
            elif (
                key["variableType"] == "string"
                or key["variableType"] == "category"
                or key["variableType"] == "boolean"
            ):

                # Add character variables to list string_variables
                string_variables.append(key["variableName"])
            elif key["variableType"] == "datetime" or key["variableType"] == "date":

                # Add character variables to list string_variables
                datetime_variables.append(key["variableName"])
        if key["key"] == "Primary Key":
            pri_var: str = key["variableName"]
    return (
        pri_var,
        numeric_variables,
        string_variables,
        datetime_variables,
    )
