# Roadmap

The [ODM Steering Group](https://github.com/Big-Life-Lab/covid-19-wastewater/wiki#canadian-wastewater-based-epidemiology-data-steering-group) or Working Groups have identified the following features and tools for development.

See the [Roadmap](https://github.com/Big-Life-Lab/covid-19-wastewater/projects/3?add_cards_query=is%3Aopen) project for progress on the roadmap. Add new items or discuss on the discussion [thread](https://github.com/Big-Life-Lab/covid-19-wastewater/discussions/108). Issues with "future" tag are discussed for addition to the roadmap.

There are two scoping documents that support the development of the roadmap. Feel free to made suggestions to these documents.
- [Project Scope Statement for the ODM](https://docs.google.com/document/d/1QPSTi3zdY5eUQ62eOxSDMVyJBiKa2HEzKHEAnBzpRYA/edit)
- [Project Scope Statement for the COWSD](https://docs.google.com/document/d/1O9qUaF8bEp-ME2_RV7Qqpvt4SmGGP99VIgCoL3HnFvM/edit) - a proposed open database with funding support from [CoVaRRNet](https://covarrnet.ca).


## Requirements

Requirements for future tools and features:

- **Support for English and French** - initially for the data model and then other documentation.
- **Open and cross platform** - Tools to support the data model will be generated using or support open software. The objective is to create pseudo-code that can form the basis to program code in R or Python. Rules as pseudo-code allow development teams to generate consistent data applications in other program platforms (i.e. MS 365 or ArcGIS).

## Tools

1. **Automatic updating tools** - scripts that can be used to automatically push the most recent updates of the data model to the necessary depending files (template, ERD, ...)
1. **Data mapping methods** - a collection of methods to:
   Read in data from templates into a database (SQLite supported).
   Conversion from "long" format to "wide" format needed for data analysis/ML. 
1. **Data validation tool** - can validate a datafile in terms of formatting and context, and provides feedback of needed changes
1. **Data linking tools** - tools that will help ensure consistan summarization of public health data into summary results relevent for the WWTP catchment area.
1. **Data cleaning methods** - rules for cleaning raw ODM data. 
1. **Visualization tools** - basic plots to visualize relevant signals. Simple visualization tools can be part of vignettes to show how to analyze wastewater data.
1. **Transformation functions** - functions to create derived variables and aggreagations. i.e. moving averages, normalisation,...
1. **Open, public data examples within the repository** - Example data to build
and test common tools and demonstrate ODM compliant data format.


## Documentation

Documentation that including tutorials, how-to guides, technical references and explanations. See [Divio documentation approach](https://documentation.divio.com).

1. Tutorials - learning-oriented.
1. How-to guides - problem-oriented.
1. Explanation - understanding-oriented.
1. Reference - information-oriented.

- Several presentations have introduced the ODM. Let's make the recordings available as a first step. Next, create additional visual documentation for specific functionalities.
- Peer-review description with a permalink/DOI reference which would facilitate sharing and referencing within the scientific community.
- Consider a website that organizes documentation for a wider audience of users that not necessarily know how to work with GitHub. 

## Process

- Ensure Steering Committee and Working Groups have representation from a range discplines and regions.
- Add a code of conduct.
