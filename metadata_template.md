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



## Examples of how to generate wide variable and category names

### 1) Simple viral region report

A long table would represent viral measures of:

``` {.markdown}
date = 2021-01-15
type = covN1
unit = nPMMoV
aggregation = mean
value = 40
```

``` {.markdown}
date = 2021-01-15
type = covN2
unit = nPMMoV
aggregation = mean
value = 42
```

In a long table as:

| date       | type  | unit   | aggregation | value |
|------------|-------|--------|-------------|-------|
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMoV | mean        | 42    |

A wide table would represent the same measurement as:

``` {.markdown}
    covidN1_PPMV_mean = 40
    covidN2_PPMV_mean = 42
```

In a wide table as:

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
|------------|-------------------|-------------------|
| 2021-01-15 | 40                | 42                |

### 2) Derived measure

To report a mean value of existing covidN1 and covidN2 measures:

``` {.markdown}
    date = 2021-01-15
    type = covN1
    unit = ml
    aggregation = mean
    value = 42
```

``` {.markdown}
    date = 2021-01-15
    type = covN2
    unit = ml
    aggregation = mean
    value = 40
```

Represent the derived measure as:

long table format

``` {.markdown}
    date = 2021-01-15
    type = covN1covN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type       | unit | aggregation | value |
|------------|------------|------|-------------|-------|
| 2021-01-15 | covN1covN2 | ml   | mean        | 41    |

or, wide table format

``` {.markdown}
    date = 2021-01-15
    covN1covN2_ml_mean = 41
```

-   Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMoV:

Represent the derived measure as:

long table description

``` {.markdown}
    date = 2021-01-15
    covN1covN2 = 2
    unit = PPMV
    type = meanNr
```

or,

wide table format

``` {.markdown}
    covidN1covidN2_PPMV_meanNr = 2
```
