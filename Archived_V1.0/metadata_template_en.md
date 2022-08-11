<!-- metadata.md is generated from metadata_template.md Please edit metadata_template.md file -->
<!-- create metadata.md with wbe_metadata_write() in generate_db_generation_sql.R -->

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

FOR_REPLACE_LIST_OF_TABLES_DETAILS

# Database templates and input forms

Several database templates and input forms are underdevelopment to help labs and other partners enter data.

Templates are in the [template folder](template).

Available templates:

_Database templates_

- [`covid_wwtp_data_template.xlsx`](template/covid_wwtp_data_template.xlsx) - (do not use - an early example). This template does not adhere to the current version of the ODM. Stay tuned for an updated version.
- [wbe_create_tables.sql](src/wbe_create_tables.sql) - Code to generate a SQL database.

## Database templates

Database templates are flat file templates (i.e. Excel or CSV file format) that are used to summarize wastewater SARS-CoV-2 measurements. There are two formats - 'wide' and 'long' that are based on the underlying primary databases that are described in Metadata.

- **'Wide'** format - The 'wide' form of data entry corresponds to how labs commonly hold their own data. This form usually has one _sample_ per row. Each sample corresponds to test performed on a wastewater sample taken on a specific day. This means that each row corresponds to a single day. The main variables are from the 'measurement' table, but there are also variables from other tables. Alternatively, variables from other tables can be collected separately.

- **'Long'** format - This template has one _measurement_ per row. The long format follows the ERD and data dictionary.

## Input forms

Input forms correspond to the tables described in metadata. Survey Monkey forms are available for earlier versions of the ODM, but these are current not supported in the most recent version. We are aware of several initiatives to generate Microsoft PowerApp and ArcGIS Survey123. Updates will be provided here as those initiatives develop.

## Example of wide and long variable formats

The [metadata](metadata.md) and [Entity Relationship Diagram](metadata.md#entity-relationship-diagram) are long table formats.

### Example of reporting two viral regions (N1 and N2) on the same sample

Long table format

| date       | type  | unit   | aggregation | value |
| ---------- | ----- | ------ | ----------- | ----- |
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMov | mean        | 42    |

Wide table format

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
| ---------- | ----------------- | ----------------- |
| 2021-01-15 | 40                | 42                |

## Order of completion

Because of the multiple relationships between the tables composing the data model, it is important that some tables are completed before others can be. The following order of completion should be respected in order to ensure that the datasets are complete:

- **Step 1**: `Instrument`, `Polygon`

- **Step 2**: `Site`, `AssayMethod`

- **Step 3**: `Lab`

- **Step 4**: `Reporter`

- **Step 5**: `Sample`+`WWMeasure` OR `SiteMeasure` OR `CovidPublicHealthData`

## Naming conventions

- **Table names**: Table names use UpperCamelCase.

- **Variable and category names**: Both variables and variable categories use lowerCamelCase. Do not use special characters (only uppercase, lowercase letters and numbers). Reason: variable and category names can be combined to generate derived variables. Using special characters will generate non-allowable characters - see below. Category names a maximum of 7 characters to allow concatenation of four categories into a single variaable to comply with ArcGIS 31 character maximum for variable names.

- **Variables in wide tables**: Wide tables use `_` to concatenate variables from long tables.

- **Variable order** If a multiple measurement take place on different dates this has a natural form in the long table format, however in the pivot wider format this can be ambiguous. In this case, show a `reportDate` followed by a series of measurements taken on that date (e.g. `covN1_PPMV_mean`) followed by more measurements (e.g. `covN2_PPMV_mean`)

- **Merging tables** : Merging tables into a wide table requires additional steps when a variable does not have an unique name (when the variable name appears in more than one table). For example, variables such as `dateTime`, `notes`, `description`, `type`, `version` and `ID` variables such as `sampleID` are used in several tables. Use the following approach:

  - Variable that are not unique (they are in more than one table): add the table name to the variable by concatenate column names with `_`. e.g. `dateTime` from the `Sample` table becomes `Sample_dateTime`.
  - Variable that are unique (they are in only one table in the entire OMD). No variable name changes are needed.

- **Derived, summary or transformed measure**: These measures are generated to summarize or transform one or more variables. Naming convention follows the same approach as naming variable and category names, except use a `_` when concatenating variable or category names. Examples of a derived measure is the calculation of a mean value of one or more SARS-CoV-2 regions. Normalization and standardization are other examples of a transformed measure. Typically derived, summary or transformed measures are not reported, rather the preferred reporting approach is reporting the underlying individual measures.

- **Date time**: YYYY-MM-DD HH:mm:ss (24 hour format, in UTC)

- **Location**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) for polygon.

- **Version**: [Semantic versioning](https://semver.org)

## Examples of how to generate wide variable and category names

### 1) Simple viral region report

A long table would represent viral measures of:

```{.markdown}
date = 2021-01-15
type = covN1
unit = nPMMoV
aggregation = mean
value = 40
```

```{.markdown}
date = 2021-01-15
type = covN2
unit = nPMMoV
aggregation = mean
value = 42
```

In a long table as:

| date       | type  | unit   | aggregation | value |
| ---------- | ----- | ------ | ----------- | ----- |
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMoV | mean        | 42    |

A wide table would represent the same measurement as:

```{.markdown}
    covidN1_PPMV_mean = 40
    covidN2_PPMV_mean = 42
```

In a wide table as:

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
| ---------- | ----------------- | ----------------- |
| 2021-01-15 | 40                | 42                |

### 2) Derived measure

To report a mean value of existing covidN1 and covidN2 measures:

```{.markdown}
    date = 2021-01-15
    type = covN1
    unit = ml
    aggregation = mean
    value = 42
```

```{.markdown}
    date = 2021-01-15
    type = covN2
    unit = ml
    aggregation = mean
    value = 40
```

Represent the derived measure as:

long table format

```{.markdown}
    date = 2021-01-15
    type = covN1covN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type       | unit | aggregation | value |
| ---------- | ---------- | ---- | ----------- | ----- |
| 2021-01-15 | covN1covN2 | ml   | mean        | 41    |

or, wide table format

```{.markdown}
    date = 2021-01-15
    covN1covN2_ml_mean = 41
```

- Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMoV:

Represent the derived measure as:

long table description

```{.markdown}
    date = 2021-01-15
    covN1covN2 = 2
    unit = PPMV
    type = meanNr
```

or,

wide table format

```{.markdown}
    covN1covN2_PPMV_meanNr = 2
```
