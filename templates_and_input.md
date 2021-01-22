# Database templates and input forms

Several database templates and input forms are underdevelopment to help labs and other partners enter data.

Templates are in the [template folder](template).

Available templates:

*Database templates*

-   [Ontario_Template_ODM_1.0.xlsx](template/Ontario_Template_ODM_1.0.xlsx) - Ontario Ministry of Environment, Conservation and Parks (MECP). Used in Ontario-funded provincial program. A wide template format with tabs that represent each table.
-   [`covid_wwtp_data_template.xlsx`](template/covid_wwtp_data_template.xlsx) - (do not use - an early example). This template does not adhere to the current version of the ODM. Stay tuned for an updated version.
-   [wbe_create_tables.sql](src/wbe_create_tables.sql) - Code to generate a SQL database.

## Database templates

Database templates are flat file templates (i.e. Excel or CSV file format) that are used to summarize wastewater SARS-CoV-2 measurements. There are two formats - 'wide' and 'long' that are based on the underlying primary databases that are described in Metadata.

-   **'Wide'** format - The 'wide' form of data entry corresponds to how labs commonly hold their own data. This form usually has one *sample* per row. Each sample corresponds to test performed on a wastewater sample taken on a specific day. This means that each row corresponds to a single day. The main variables are from the 'measurement' table, but there are also variables from other tables. Alternatively, variables from other tables can be collected separately.

-   **'Long'** format - This template has one *measurement* per row. The long format follows the ERD and data dictionary.

## Input forms

Input forms correspond to the tables described in metadata. Survey Monkey forms are available for earlier versions of the ODM, but these are current not supported in the most recent version. We are aware of several initiatives to generate Microsoft PowerApp and ArcGIS Survey123. Updates will be provided here as those initiatives develop.

## Example of wide and long variable formats

The [metadata](metadata.md) and [Entity Relationship Diagram](metadata.md#entity-relationship-diagram) are long table formats. 

### Example of reporting two viral regions (N1 and N2) on the same sample

Long table format

|date      |type|unit|aggregation|value|
|----------|--------|----|-----------|-----|
|2021-01-15|covidN1 |vcPPMoV  |mean       |40   |
|2021-01-15|covidN2 |vcPPMov  |mean       |42   |

Wide table format

|date      |WWMeasure__covidN1_vcPPMoV_mean|WWMeasure__covidN2_vcPPMoV_mean|
|----------|------------------------------|------------------------------|
|2021-01-15|40                            |42                            |
