# Aim/Objective

The purpose of the Ottawa Data Model (ODM) is to create an open science structure which can be used as a guideline for future models which promote data sharing.

# Introduction

The validation.csv worksheet contains the details for the variables described in v.1.2 in the Ottawa Data Model (ODM). Information from the validation.csv worksheet is used to auto-generate a set of rules (schema) using the Cerberus package to validate the COVID-19 wastewater data provided from laboratories across Canada. The main objective is to create a human readable, machine-actionable worksheet which can be updated to reflect changes within the data validation process in the ODM. The worksheet is in a wide table format, which allows users to easily insert changes to the validation schema if needed.

# Rows

The rows in validation.csv contain the variables which need to be validated according to guidelines provided by the Ministry of the Environment, Conservation and Parks (MECP). Each individual variable has specific validation criteria which needs to be adhered to in order to be considered “valid”.

# Columns

The columns specify either the name of the function within the Cerberus package or provide description towards for the variable

# Naming Convention

Variables listed in the ODM will follow the pascal case format.

# Allowable Values

The Validate.csv schema supports strings, integers, and floats. It currently does not support the character data-type.

# Formatting

The Validate.csv file is in the wide-table format. The wide table format was selected for the purpose of ensuring the highest degree of human readability.
