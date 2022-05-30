# Implementation

## filter
Allows the filtering of a column by values must follow format of filter: column = value.

In case of multiple values needed for filtering values must be enclosed in []
In case of multiple columns the [] must be present after filter: and wrap any column = value sets

## content/value
I reccomend renaming the value tag to a content tag.

Usage example "content = column_name".

In case of multiple values a [] can be used to specify a list of columns to pull content from.

## order
Order once again follows the "order:keyword(column)" format

keyword is representing different types of order ex: ascending alphanumerical or descending alphanumerical.

following the keyword tag the brackets contain the columns that the sorting is performed on in case of multiple columns the [] notation is used and ordering is done in order of left to right.

## format 
format could support differnt types of display currently I suggest the usage of table or list

An example of format usage: "format:type(label)"

Each queary statement will only support one format statement.

The format type is where you specify the table or list option

The label should represent a template of data visualization(its the name of the template)

### label templates

Label templates contain elements for queary population

The template name/label should be wrapped in {{}} followed by : and {}
the {} wrap around a quary-esque statement. This statement however cannot contain any filtering or ordering options.

It is simply a list of columns and their option parameters.
Example of template filetering: "{{label}}:{column:option, column:option.....}

### option

Options(I am not set on the name and open to suggestions) contain options for that section of the template this can include: font type, font size, bolding, color, etc.

# Potential suggestions that might be overkill

Allowing creation of option templates in case we want to reuse a particular style.



# Notes
Add && and || support

Focus on format template/variable declaration for md snippets
