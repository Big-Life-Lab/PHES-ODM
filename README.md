# Ottawa wastewater surveillance data model (Ottawa Data Model (ODM))

This repository contains Ottawa wastewater surveillance data model. Also included are Ottawa wastewater data - other data are welcomed. Plots using this data can be found at: [613covid.ca](https://613covid.ca/wastewater).

See [Metadata](metadata.md) for variable names and definitions.

## Collaborate

The ODM strives to improve wastewater surveillance through the development of a common data structure, including metadata and vocabulary. Also included are templates (under development) to collect and share data. Templates include versions of Excel spreadsheets from different jurisdictions that are based on the ODM. A SQL database structure is available, as well as code to clean data and create tables.

We adhere to the [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) with recognition of benefit from a common data structure, including metadata and vocabulary.

ODM is a collaborative effort from many people within the wastewater surveillance community in Canada and beyond. See [GH issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues) or email [dmanuel\@ohri.ca](mailto:dmanuel@ohri.ca), [howard.swerdfeger\@canada.ca](mailto:howard.swerdfeger@canada.ca).

Follow the [`dev`](https://github.com/Big-Life-Lab/covid-19-wastewater/tree/dev) branch for upcoming changes. Also follow version changes in [issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues), [discussions](https://github.com/Big-Life-Lab/covid-19-wastewater/discussions), and [projects](%3Chttps://github.com/Big-Life-Lab/covid-19-wastewater/projects).

See [Collaborate](collaborate.md) for more information.

## License

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

## Changelog

#### 2021-01-08

-   All variable names were updated according to the name convention. 

#### 2020-11-25

-   Change date formatting on `wastewater_virus.csv` to YYYY-MM-DD.

#### 2020-11-25

v0.1.1 - Additions to metadata. No breaking changes.

-   Measurement metadata

    -   Add categories `measurementType`:

        -   `geoMean`: GeoMean of results
        -   `rangeLowestValue`: Lowest value in a range of values
        -   `rangeHighestValue`: Highest value in a range of values
        -   `singleton`: This value is not an aggregate measurement in any way, and thus is not a `mean`, `median`, `geomean` or other

    -   Add `measureValueDetected`: Boolean Value if True then covid-19 was detected.

    -   Add `reportDate`: Note use of `reportDate` when historic results are updated for new reporting standards.

-   AssayMethod metadata

    -   Add `sampleSizeL`: Size of the sample that is analysed in liters
    -   Add `loq`: Limit of Quantification for this method if one exists
    -   Add `lod`: Limit of detection for this method if one exists
    -   Add `inhibition`: Text decription of the inhibition
    -   Add `surrogateRecovery`: Text description of the Surrogate Recovery for this method

-   Other small corrections to metadata category labels.

-   CovidPublicHealthData

    -   `dateType`: Type of date used.

-   Updated `wastewater_virus.csv` to reflect metadata v0.1.1.

#### 2020-11-17

v0.1.0 - Breaking changes to metadata.

-   Assay method database added.
-   Change test results to be represented as key:values. Each test result has a measurement type (`measureType`) with a corresponding value (`measureValue`). For example a measureType is `mean` and the corresponding `measureValue` has the mean value.

#### 2020-11-16

-   `wastewater_virus.csv` dataset updated to remove adjustment for percent viral recovery from solids. The adjustment allign reporting with other laboratories. The adjustment reduces N1 and N2 values a maginitude of 10 (approximately).

#### 2020-10-29

-   Replace invalid values (such as \#DIV/0) with `NA`.

#### 2020-10-27

V0.0.2 - Breaking changes to metadata.

-   Change `locationID` to `siteID`.
-   Change `locationName` to `siteName`.

#### 2020-10-16

-   All Ottawa data points prior to Oct 2nd have been slightly modified to normalize data for a new centrifuge that is being used to collect wastewater samples at the Ottawa site.

#### 2020-10-09

V0.0.1 - Initial variable names and labels.
