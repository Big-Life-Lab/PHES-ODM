# Vocabulary and tools

Meeting: 2021-03-29

## Attendees

Doug Manuel - OHRI
Howard Swerdfeger - PHAC
Jean-David Therriern - uLaval
Niels Nicolaï - uLaval

# Discussion

## 1. Architecture and support code

- Create an archicture diagram
- Create SQL data model
- Create data frame from different input templates or data model (SQL)

### 1.1. Test data

### 1.2. Site that holds and uses the data

## 2 Collaboration with other data models

Including NORMAN SCORE, CDC

## 3. V1.2.

# Working group on data validation and analyses tools

Meeting: 2021-04-01

Jean-David and Howard:

- working on transformation for Québec, NML/Statscan labs. This will be a Python package to take different starting data from labs as Excel spreadsheets and recode/transform them into OMD compliant data base.
- Also to be developed are visulazation tools, data analyses and mapping tools. Likely platform is Plotly Dash/Python.

MECP:

- continuing development of rules with warnings and errors when submitting data.

  - Warnings and errors are in human readible form in an excel spreadsheet that is then implemented in two approaches:data validation rules in Excel; within ARCgis (?).

- ante - creating guide for how to use MECP data templates. Consider sharing to have common elements added to a how to on the ODM.

Doug:

- creating Ottawa data available in ODM format for public use on the OMD repo. This is both long and wide formats. Will allow data a testing environment for data validaation and other code.

- international meeting planned for after Easter to discuss potential collaboration between other data models including CDC and NORMAN SCORE.

## Discussion

1. MECP's warnings and error spreadsheet is well formatted and can serve purposes for both MECP and the broader ODM users, including Québec. Ante will share when possible for further discussion to implement into ODM.

- Jean-David is interested in reviewing the document to assess implementation in his current QC work.

2. The instructions for using MECP template appears to have elements that are common to general ODM. Ante will share when possible for further discussion whether to include/inform the documentation for ODM.
3. Data visualization that Jean-David is developing is a common elememt that is being developed by different groups, including Ryerson. Suggestion to invite Ryerson to future meetings.

4. There is interest in continuing meetings on a weekly basis for the next 4 to 8 weeks.

# Working group on data validation and analyses tools

Meeting: 2021-04-22

1. Roundtable.

   - A scope document for the Canadian Wastewater Surveillance Database has been created. In addition a scope document for further development of the Ottawa Wastewater Data Model is under development.
     > Action: These documents will be incorporated into the website text.
   - A discussion with PHAC epis about common tools to support epidemiology and modelling. Folks from the ODM will work with PHAC epi to develop these.
   - Mappers from existing lab spreadsheets continues.
     - Mapping from NML will likely begin.
     - A general tool that combines recodeflow and Jean-David's work was discussed.
     - Mapping Ottawa data wasa discussed.
   - MECP folks gave an update to their work to launch dashboards in the next weeks which will include:
     - dashboards
     - data download in different aggregate forms.
     - Terms of use, with data access privledges.
     - Mapping.

2. Discussion:
   - different "wide" table formats were discussed with the concern that wide table formats could be interpretated different because the description and examples are brief. Jean-David and Howard created transformation tools to move from long to wide tables.

- > Action: Monday's meeting will compare Québec, Ottawa and MECP wide tables to identify any differences and to improve documentation.

Meeting: 2021-04-29
