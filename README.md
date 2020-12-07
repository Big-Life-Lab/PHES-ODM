# Ottawa Covid-19 Wastewater Dataset

This respoistory contains Ottawa covid-19 wastewater surveillance data. Plots using this data can be found at: [613covid.ca](https://613covid.ca/wastewater).

Data is stored in [`/data`](data/). See [metadata](metadata.md) for variable names and definitions. See `metadata` branch for proposed changes to data structure and metadata.

## Collaborate to share wastewater data

SARS-CoV-2 Wastewater epidemiology and surveillance is rapidly evolving. We strive to adhere to the [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) and there is benefit from a common data structure, including metadata and vocabulary. We are interested in colloborating to develop covid-19 wastewater data management and stewardship. Let's discussion at [Slack 2019-nCov WBE channel](https://2019-ncovwbe.slack.com), [GH issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues) or contact us directly at <uottawa.sars.cov.2@gmail.com>.

## API

Under discussion and development.

## Licence

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

## Changelog

## 2020-11-19

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

## Acknowledgement

uOttawa -- CHEO SARS-CoV-2 research group: Robert Delatolla, Alex MacKenzie, Patrick D'Aoust, Élisabeth Mercier, Antoine Cantin, Tyson Graber. Contact through GH Issues or <uottawa.sars.cov.2@gmail.com>.
