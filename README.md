# Ottawa Wastewater Surveillance Data Model (Ottawa Data Model (ODM))

This repository contains Ottawa Wastewater Surveillance Data Model (Ottawa Data Model (ODM)). Also included are Ottawa wastewater data - other data are welcomed. Plots using this data can be found at: [613covid.ca](https://613covid.ca/wastewater).

See [Metadata](metadata.md) for variable names and definitions.

## Collaborate

The ODM strives to improve wastewater surveillance through the development of a common data structure, including metadata and vocabulary. Also included are templates (under development) to collect and share data. Templates include versions of Excel spreadsheets from different jurisdictions that are based on the ODM. A SQL database structure is available, as well as code to clean data and create tables.

We adhere to the [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) with recognition of benefit from a common data structure, including metadata and vocabulary.

ODM is a collaborative effort from many people within the wastewater surveillance community in Canada and beyond. See [GH issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues) or email [dmanuel\@ohri.ca](mailto:dmanuel@ohri.ca), [howard.swerdfeger\@canada.ca](mailto:howard.swerdfeger@canada.ca).

Follow the [`dev`](https://github.com/Big-Life-Lab/covid-19-wastewater/tree/dev) branch for upcoming changes. Also follow version changes in [issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues), [discussions](https://github.com/Big-Life-Lab/covid-19-wastewater/discussions), and [projects](%3Chttps://github.com/Big-Life-Lab/covid-19-wastewater/projects).

See [contributing](CONTRIBUTING.md) for more information.

## License

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

See [license](LICENSE) for more information.

## Changelog

#### 2021-02-18

**v1.1.0**

- **There are several small breaking changes to correct typos in variable names**

  - `sampleTypeDefault`: Change from `SampleTypeDefault`. Now consistent use of lowercaase first letter.
  - `sampleTypeOtherDefault`: Change from `SampleTypeOtherDefault`.
  - `sampleCollectionDefault`: Change from `SampleCollectionDefault`.
  - `sampleCollectOtherDefault`: Change from `SampleCollectOtherDefault`.
  - `sampleStorageTempCDefault`: Change from `SampleStorageTempCDefault`.
  - `measureFractionAnalyzedDefault`: Change from `MeasureFractionAnalyzedDefault`.

- **New variables**

- [Reporter](metadata.md#reporter) table
  - `organization`: Organziation of reproter. Issue [#97](https://github.com/Big-Life-Lab/covid-19-wastewater/issues/97)

- [Sample](metadata.md#sample) table
  - `reporterID`: Reporter ID. Currently, reporterID is `WWmeasure` table but reporter for samples can be different. Issuse [#93](https://github.com/Big-Life-Lab/covid-19-wastewater/issues/93)
  - `index`: Index number in case the sample was taken multiple times. 

- **New variable categories**

  - Categories added to allow variant reporting. See `WWMeasure` table, `type` variable:

    - `varB117`: Variant B.1.1.7
    - `varB1351`: Variant B.1.351
    - `varP1`: Variant P.1

  - Updated description of `WWMeasure` table, `unit` measure. These descriptions now reference gene or variant copies.
  - New `detected`: Gene copies or variant detected in the sampleGene or variant copies. Detected = 1. Gene or variant copiesNot detected = 0.
  - New `porpVar`: Proportion of variant in sample.
  - `SiteMeasure` table, `type` variable
    - `wwBOD5c`, 5 day biochemical oxygen demand
    - `wwPtot`, Total phosphates
  - New `dailyAvg`: Average value taken over a 24h period, in the `SiteMeasure` table, `aggregation` variable
  - The `SiteMeasure` table now has a categorical `unit` variable with the following options

    - `°C`, Degrees Celcius
    - `mm`, Millimeters
    - `m3/h`, Cubic meters an hour
    - `m3/d`, Cubic meters a day
    - `mg/L`, Milligrams per liter
    - `pH`, pH units
    - `uS/cm`, Micro-siemens per centimeter
  
 
- **Migrate .md files for tables**
  
  - Variable and variable categories to CSV files. Please modify the appropriate CSV file for future updates. `metadata.md` is now automatically generated from the CSV files.

    - `Tables.csv`: list of tables.
    - `Variables.csv`: list of variables.
    - `VariableCategories`: list of categories for variables.

- **Other**

  - SQL template updated to reflect v1.1.0 (and also v1.0.0). These files are now automatically generated from the metadata tables (above). The SQL tables are in SQLite format.
  - Several small grammatical errors corrected in the English variable descriptions.

#### 2021-01-26

**v1.0.0 - Many additions and breaking changes. This version is recommended for widespread use.**

- Naming conventions were further developed. Category names shortened to 7 digits to allow wide variable names up to 31 characters.

- Three NEW tables

  - [SiteMeasure](metadata.md#sitemeasure): The site of wastewater sampling, including several defaults that can be used to populate new samples upon creation. SiteMeasure complements the [WWMeasure](metadata.md#wwmeasure) table. It includes measures that are commonly collected by staff at wastewater treatment facilities and field sample locations. Whereas WWMeasure includes measures that are commonly generated by wastewater testing laboratories.
  - [Inststrument](metadata.md#instrument): Instruments that are used for measurements in SiteMeasure and WWMeasure. Note that the assay method itself for viral measurement is described in [AssayMethod](metadata.md#assaymethod).
  - [Lookup](metadata.md#lookup): Reference for categorical variables.

- Names of variables were updated according to the extended naming conventions. Note that these changes are NOT listed here!

- Examples are provided on how to generate wide and long variables and category names.

- Information on how to collaborate is updated.

- Measurement metadata

  - `aggregation` - Following the existing options, one more option was added to the list `geoMeanNormal`.

- [SiteMeasure](metadata.md#sitemeasure) variables:

  - `ID`: (NEW) Unique identifier for each contextual measurement.
  - `SiteID`: (NEW) Links with the Site table to describe the location of measurement.
  - `dateTime`: (NEW) The date and time the measurement was performed.
  - `type`: (NEW) The type of measurement that was performed.
  - `typeOther`: (NEW) Description of the measurement in case it is not listed in type.
  - `typeDescription`: (NEW) Additional information on the performed measurement.
  - `name`: (NEW) Name of the instrument used to perform the measurement.
  - `type`: (NEW) Type of instrument used to perform the measurement.
  - `typeOther`: (NEW) Description of the instrument in case it is not listed in instrumentType.
  - `aggregation`: (NEW) When reporting an aggregate measurement, this field describes the method used.
  - `aggregationOther`: (NEW) Description for other type of aggregation not listed in aggregation.
  - `aggregationDescription`: (NEW) Information on OR reference to which measurements that were included to calculate the aggregated measurement that is being reported.
  - `value`: (NEW) The actual value that is being reported for this measurement.
  - `unit`: (NEW) The engineering unit of the measurement.
  - `qualityFlag`: (NEW) Does the reporter suspect quality issues with the value of this measurement? (Boolean)
  - `notes`: (NEW) Any additional notes.

- [Sample](metadata.md#sample) variables

  - `samplingTempC`: (NEW) Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples which are either kept at ambient temperature or refrigerated while being sampled.
  - `mailedOnIce`: (NEW) Was the sample kept cool while being sent to the lab? (Boolean)
  - `category` - A distinction is now made between SARS-CoV-2 gene measurements `covid` and the measurement of water quality parameters on the sample `wq`.

- [Site](metadata.md#site) variables

  - `type` - Additional site types were added `airplane`, `correctionalFacility`, `elementarySchool`, `hospital`, `longTermCareFacility`, `sewageTruck`, `universityCampus`, `WWTP`
  - `accessType`: (NEW) Access point of where the sample was collected at the site.
  - `measurement.fractionAnalyzedDefault`: (NEW) Used as default when a new measurement is created for this site. See `fractionAnalyzed` in `Measurement` table.

- [AssayMethod](metadata.md#assaymethod): New variables were introduced to replace `assayDesc`, those are

  - `methodConcentration`: (NEW) Description of the method used to concentrate the sample
  - `methodExtraction`: (NEW) Description of the method used to extract the sample
  - `methodPcr`: (NEW) Description of the PCR method used
  - `qualityAssuranceQC`: (NEW) Description of the quality control steps taken
  - `inhibition`: (NEW) Description of the inhibition parameters.
  - `surrogateRecovery`: (NEW) Description of the surrogate recovery for this method.
  - `description`: (NEW) Description of the assay.
  - `referenceLink`: (NEW) Link to standard operating procedure (assay reference method)

- [CovidPublicHealthData](metadata.md#covidpublichealthdata)

  - `valueType`: (NEW) A categorical variable that replaces the individual variables, instead it provides listed options: `confirmed`, `active`, `tests`, `positiveTests`, `percentPositivityRate`, `hospitalCensus`, `hospitalAdmit`.

#### 2021-01-08

- All variable names were updated according to the name convention.

#### 2020-11-25

- Change date formatting on `wastewater_virus.csv` to YYYY-MM-DD.

#### 2020-11-25

**v0.1.1 - Additions to metadata. No breaking changes.**

- Measurement metadata

  - Add categories `measurementType`:

    - `geoMean`: GeoMean of results
    - `rangeLowestValue`: Lowest value in a range of values
    - `rangeHighestValue`: Highest value in a range of values
    - `singleton`: This value is not an aggregate measurement in any way, and thus is not a `mean`, `median`, `geomean` or other

  - Add `measureValueDetected`: Boolean Value if True then covid-19 was detected.

  - Add `reportDate`: Note use of `reportDate` when historic results are updated for new reporting standards.

- AssayMethod metadata

  - Add `sampleSizeL`: Size of the sample that is analysed in liters
  - Add `loq`: Limit of Quantification for this method if one exists
  - Add `lod`: Limit of detection for this method if one exists
  - Add `inhibition`: Text decription of the inhibition
  - Add `surrogateRecovery`: Text description of the Surrogate Recovery for this method

- Other small corrections to metadata category labels.

- CovidPublicHealthData

  - `dateType`: Type of date used.

- Updated `wastewater_virus.csv` to reflect metadata v0.1.1.

#### 2020-11-17

v0.1.0 - Breaking changes to metadata.

- Assay method database added.
- Change test results to be represented as key:values. Each test result has a measurement type (`measureType`) with a corresponding value (`measureValue`). For example a measureType is `mean` and the corresponding `measureValue` has the mean value.

#### 2020-11-16

- `wastewater_virus.csv` dataset updated to remove adjustment for percent viral recovery from solids. The adjustment allign reporting with other laboratories. The adjustment reduces N1 and N2 values a maginitude of 10 (approximately).

#### 2020-10-29

- Replace invalid values (such as \#DIV/0) with `NA`.

#### 2020-10-27

V0.0.2 - Breaking changes to metadata.

- Change `locationID` to `siteID`.
- Change `locationName` to `siteName`.

#### 2020-10-16

- All Ottawa data points prior to Oct 2nd have been slightly modified to normalize data for a new centrifuge that is being used to collect wastewater samples at the Ottawa site.

#### 2020-10-09

V0.0.1 - Initial variable names and labels.
