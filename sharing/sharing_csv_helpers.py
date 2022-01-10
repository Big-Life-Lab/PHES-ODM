"""
This module returns the list of all values for variables and tables
present in current rule.
"""
from typing import List, Callable
from classes_for_datatypes import Rule


def split_cell_value(cell_value: str) -> List[str]:
    """
    Function splits the values of table and variable values of sharing rule
    into a list

    Parameters:
    cell_value (str): the variable or table string from current rule

    Returns:
    List[str]: List of all the values for variable and table in current rule
    """
    return cell_value.split(";")


def construct_parse_entity_cell_value(
    field_name: str,
) -> Callable[[str, List[str]], List[str]]:

    """

    Constructs and returns a function to be used when parsing out the entities
    (table, variables etc.) to filter in a rule

    Parameters:

    field_name (str): The name of the field in the rule that contains the

    entity values

    """

    def parse_entity_cell_value(rule: Rule, entity_names: List[str]) -> List[str]:

        """

        Parses the entity value for a rule and returns the one which apply

        to the rule



        Parameters:

        rule (Rule): The rule from where we need to extract the entity values

        entity_names (List[str]): The names of all the entities to filter from

        """

        entity_values = split_cell_value(rule[field_name])

        if entity_values[0].strip().lower() == "all":

            return entity_names

        else:
            print("ENTITY VALUES", entity_values)
            print("ENTITY NAMES", entity_names)
            entity_values = [
                e_v
                for e_v in entity_values
                if e_v.strip().lower()
                in list(map(lambda var: var.strip().lower(), entity_names))
            ]
            print("FINAL ENTITY VALUES", entity_values)
            return entity_values

    return parse_entity_cell_value


"""

Returns the tables which applies to a rule



Parameters

:param rule (Rule) -- The rule from where we need to extract the tables to work on

:param tables (List[str]) -- All the tables that the user wants to filter

"""

get_tables_for_rule = construct_parse_entity_cell_value("table")


"""

Returns the variables which applies to a rule



Parameters

:param rule (Rule) -- The rule from where we need to extract the tables to work on

:param variables (List[str]) -- The full list of variables to filter from.

"""

get_variables_for_rule = construct_parse_entity_cell_value("variable")
