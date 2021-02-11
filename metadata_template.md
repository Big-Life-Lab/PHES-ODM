# Metadata

There are eight tables that are described below. example data is stored in [data](data).

FOR_REPLACE_LIST_OF_TABLES

## Entity Relationship Diagram

Use Entity Relationship Diagram to identify variable type.

- **BLOB**: The ASCII-encoded string in lower case representing the media type of the Blob. More [details](https://w3c.github.io/FileAPI/#dfn-type)
- **bool**: boolean, TRUE, FALSE
- **char**: ASCII-encoded string
- **cat**: categorical defined using ASCII-encoded string as defined for the variable
- **dateTime**: YYYY-MM-DD HH:mm:ss (24 hour format, in UTC)
- **email**: email address
- **float**: float-point numerical value
- **int**: integer
- **phone**: phone number, either ###-###-#### or #-###-###-####

- **url**: Uniform Resource Identifier

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/invitations/accept/adc1784b-e237-4a2f-947e-4503544d4510)


FOR_REPLACE_LIST_OF_TABLES_DETAILS




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
|----------|------|--------|-----------|-----|
|2021-01-15|covN1 |nPPMoV  |mean       |40   |
|2021-01-15|covN2 |nPPMov  |mean       |42   |

Wide table format

|date      |covN1_nPPMoV_mean|covN2_nPPMoV_mean|
|----------|-----------------|-----------------|
|2021-01-15|40               |42               |


## Order of completion

Because of the multiple relationships between the tables composing the data model, it is important that some tables are completed before others can be. The following order of completion should be respected in order to ensure that the datasets are complete:

- **Step 1**: `Instrument`, `Polygon`

- **Step 2**: `Site`, `AssayMethod`

- **Step 3**: `Lab`

- **Step 4**: `Reporter`

- **Step 5**: `Sample`+`WWMeasure` OR `SiteMeasure` OR `CovidPublicHealthData`



