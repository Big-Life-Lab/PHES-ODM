import pandas as pd # pylint: disable=import-error
from deepdiff import DeepDiff  # For Deep Difference of 2 objects
from deepdiff import grep, DeepSearch  # For finding if item exists in an object
from deepdiff import DeepHash  # For hashing objects based on their contents
import numpy as np # pylint: disable=import-error
import json
import csv
import re
import os
from pandas import Timestamp # pylint: disable=import-error
from numpy import nan # pylint: disable=import-error
import loop_through_tables # pylint: disable=import-error
from loop_through_tables import loop_through_tables # pylint: disable=import-error


def create_dataset(rules: list, data: dict = {}, org: str = '') -> dict:
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
      Dict: Dictionary of two key value pairs of filtered data & shared summary
  """
  
  return {'filtered_data': {}, 'shared_summary': []}