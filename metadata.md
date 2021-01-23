# Metadata

There are eight tables that are described below. example data is stored in [data](data).

-   [Sample](#sample)
-   [WWMeasure](#wwmeasure)
-   [Site](#Site)
-   [SiteMeasure](#sitemeasure)
-   [Reporter](#reporter)
-   [Lab](#lab)
-   [AssayMethod](#assaymethod)
-   [Instrument](#instrument)
-   [Polygon](#polygon)
-   [CovidPublicHealthData](#covidpublicHealthdata)
-   [Lookups](#lookups)

Entity Relationship Diagram [here](#entity-relationship-diagram).

## Entity Relationship Diagram {#entity-relationship-diagram}

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/invitations/accept/adc1784b-e237-4a2f-947e-4503544d4510)

## Sample {#sample}

The sample is a representative volume of wastewater taken from a site which is then analysed by a lab.

-   **ID**: (Primary Key) Unique identification for sample. Suggestions: *siteID-date-index*.

-   **site.ID**: (Foreign key) Links with the Site table to describe the location of sampling.

-   **dateTime**: For grab samples this is the *date, time and timezone* the sample was taken.

-   **dateTimeStart**: For integrated time averaged samples this is the *date, time and timezone* the sample was started being taken.

-   **dateTimeEnd**: For integrated time average samples this is the *date, time and timezone* the sample was finished being taken.

-   **type**: Type of sample.

    -   `primarySludge`: Sludge produced by primary clarifiers
    -   `rawCollector`: Raw wastewater (in collector system)
    -   `rawPostGrit`: Raw wastewater after the treatment plant's headworks (post-grit)
    -   `other`: Other type of site. Add description to `typeOther`.

-   **typeOther**: Description for other type of sample not listed in `type`.

-   **collection**: Method used to collect the data.

    -   `grab sample`: Sample was a simple grab sample
    -   `contFlowProp`: Continuous flow proportional
    -   `contConstant`: Continuous constant
    -   `contOther`: Continuous other
    -   `discTimeProp`: Discrete time proportional
    -   `discTimeProp24hq1h`: Discrete time proportional 24-hour composite, every 1 hr
    -   `discTimeProp24hq4h`: Discrete time proportional 24-hour composite, every 4 hr
    -   `discTimeProp24hq6h`: Discrete time proportional 24-hour composite, every 6 hr
    -   `discFlowProp`: Discrete flow proportional
    -   `discVolumeProp`: Discrete volume proportional
    -   `moreSwab`: Moore swab passive sampler
    -   `discOther`: Discrete other
    -   `other`: Other type of collection method. Add description to `collectionOther`.

-   **collectionOther**: Description for other type of method not listed in `collection`.

-   **collectionTriggerTime** Time between sub-samples for `discTimeProp` numeric value given in minutes.

-   **preTreatment**: Was the sample chemically treated in anyway with the addition of stabilizers or other? (Boolean)

-   **preTreatmentDescription**: If `preTreatment` then describe the treatment that was performed.

-   **childID**: If this is a sample with many smaller samples either because of pooling or sub-sampling this indicates *a coma separated list of child sampleIDs*.

-   **parentID** : If this sample has been pooled into one big sample for analysis this indicates the *sampleID of the larger pooled sample*.

-   **sizeL**: Total volume of water or sludge sampled.

-   **samplingTempC**: Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples which are either kept at ambient temperature or refrigerated while being sampled.

-   **mailedOnIce**: Was the sample kept cool while being sent to the lab? (Boolean)

-   **storageTempC**: Temperature that the sample is stored at in Celsius.

-   **qualityFlag**: Does the reporter suspect the sample having some quality issues? (Boolean)

-   **notes**: Any additional notes.

## WWMeasure {#wwmeasure}

Measurement result (ie. single variable) obtained by analyzing a potentially positive SARS-CoV-2 wastewater sample.

-   **uID**: (Primary key) Unique identifier within the measurement table.

-   **ID**: Unique identifier for a given analysis, where analysis means you performed all steps needed to get the measurement, but measurements are not independent.

-   **Sample\_\_ID**: (Foreign key) Links with the identified Sample.

-   **Lab\_\_ID**: (Foreign key) Links with the identified Lab that performed the analysis.

-   **Assay\_\_ID**: (Foreign key) Links with the `AssayMethod` used to perform the analysis. Use `instrument.ID` for measures that are not viral measures.

-   **Instrument\_\_ID**: (Foreign key) Links with the `Instrument` used to perform the analysis. Use `assay.ID` for viral measures.

-   **Reporter\_\_ID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **analysisDate**: Date the measurement was performed in the lab.

-   **reportDate**: Date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original `sampleID` but updated `MeasureID`, `reportDate` and `assayID` (if needed).

-   **fractionAnalyzed**: Faction of the sample that is analyzed.

    -   `liquid`: Liquid fraction
    -   `solid`: Solid fraction
    -   `mixed`: Mixed/homogenized sample

-   **type**: The variable that is being measured on the sample, e.g. gene target region (`covid`) or water quality parameter (`wq`).

    -   `covidUnspecified (default)`:
    -   `covidN1`: SARS-CoV-2 gene region N1
    -   `covidN2`: SARS-CoV-2 gene region N2
    -   `covidN3`: SARS-CoV-2 gene region N3
    -   `covidE`: SARS-CoV-2 gene region E
    -   `covidRdRp`: SARS-CoV-2 gene region RdRp
    -   `covidN1N2avg`: SARS-CoV-2 gene region average of N1 and N2
    -   `PMMoV`: Pepper mild mottle virus
    -   `crA`: cross-assembly phage
    -   `wqTS`: Total solids concentration.
    -   `wqTSS`: Total suspended solids concentration.
    -   `wqVSS`: Volatile suspended solids concentration.
    -   `wqCOD`: Chemical oxygen demand.
    -   `wqOrthoP`: Ortho-phosphate concentration.
    -   `wqNH4N`: Ammonium nitrogen concentration.
    -   `wqTN`: Total nitrogen concentration.
    -   `other`: Other measurement category. Add description to `categoryOther`.

-   **typeOther**: Description for an other variable not listed in `category`.

-   **unit**: Unit of the measurement.

    -   `vcPMMoV`: Viral copies/copies PMMoV
    -   `vcMl`: Viral copies/millilitres
    -   `vcGms`: Viral copies/grams solids
    -   `vcL`: Viral copies/L
    -   `vcCrA`: Viral copies/copies crAssphage
    -   `Ct`: Cycle threshold
    -   `mgl`: milligrams per liter
    -   `mgOl`: milligrams of oxygen per liter
    -   `ph`: pH units (unitless)
    -   `pps`: percent primary sludge - for estimate of `wqTS`.
    -   `bool`: unit is a pass fail value like if covid is detected or not, or sample is frozen or not.
    -   `other`: Other measurement of viral copies or wastewater treatment plant parameter. Add description to `UnitOther`.

-   **unitOther**: Description for other measurement unit not listed in `unit`.

-   **aggregation**: Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each aggregation has a corresponding value.

    -   `single`: This value is not an aggregate measurement in any way (ie. not a `mean`, `median`, `geoMean` or any other).
    -   `mean`: Arithmetic mean
    -   `meanNormal`: Arithmetic mean, normalized
    -   `geoMean`: Geometric mean
    -   `geoMeanNormal`: Geometric mean, normalized
    -   `median`: Median
    -   `rangeLowestValue`: Lowest value in a range of values
    -   `rangeHighestValue`: Highest value in a range of values
    -   `sd`: Standard deviation
    -   `sdNormal`: Standard deviation, normalized
    -   `other`: Other aggregation method. Add description to `aggregationOther`

-   **aggregationOther**: Description for other type of aggregation not listed in `aggregation`.

-   **index**: Index number in case the measurement was taken multiple times.

-   **value**: The actual measurement value that was obtained through analysis.

-   **qualityFlag**: Does the reporter suspect the measurement having some quality issues? (Boolean)

-   **denyAccessToPublic**: If this is True, this data will not be available to the public. (Boolean)

-   **denyAccessToAllOrganizations**: If this is True, this data will not be available to any partner organization. (Boolean)

-   **denyAccessToSelf**: If this is True, this data will not be shown on the portal when this reporter logs in. (Boolean)

-   **denyAccessToFederalPublicHealthAuthorities**: If this is True, the data will not be available to employees of the Public Health Agency of Canada - PHAC. (Boolean)

-   **denyAccessToLocalPublicHealthAuthorities**: If this is True the, data will not be available to local health authorities. (Boolean)

-   **denyAccessToProvincialPublicHealthAuthorities**: If this is True, this data will not be available to provincial health authorities. (Boolean)

-   **denyAccessToOtherDataProviders**: If this is True, this data will not be available to other data providers not listed before. (Boolean)

-   **denyAccessToDetails**: More details on the existing confidentiality requirements of this measurement.

-   **notes**: Any additional notes.

## Site {#site}

The site of wastewater sampling, including several *defaults* that can be used to populate new samples upon creation.

-   **ID**: (Primary Key) Unique identifier for the location where wastewater sample was taken.

-   **name**: Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.

-   **description**: Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.

-   **type**: Type of site or institution where sample was taken.

    -   `airplane`: Airplane
    -   `correctionalFacility`: Federal or provincial correctional facility or jail
    -   `elementarySchool`: Elementary school
    -   `hospital`: Hospital
    -   `lagoon`: Lagoon
    -   `longTermCareFacility`: Long-term care facility
    -   `sewageTruck`: Sewage truck
    -   `universityCampus`: University campus or resident
    -   `WWTP`: Wastewater treatment plant
    -   `other`: Other

-   **typeOther**: Description of site where the site is other. See `siteType`. If `institution` consider placing things like `meat plant' or description of institute, etc, If`airplane consider identifying the flight number.

-   **accessType**: Access point or where the sample was collected at the site.

    -   `SAPFlowWater`: Sewer access point flowing water
    -   `SAPStandingWater`: Sewer access point standing water
    -   `treatPlantInfluent`: Treatment plant influent
    -   `treatPlantPrimarySludge`: Primary treatment sludge
    -   `treatPlantEffluent`: Treatment plant effluent
    -   `buildingCleanout`: Building clean out
    -   `propertyLineCleanout`: Property line clean out
    -   `lagoonInfluent`: Wastewater treatment lagoon influent
    -   `lagoonEffluent`: Wastewater treatment lagoon effluent
    -   `other`: An other type of access point. Add description to `accessTypeOther`.

-   **accessTypeOther**: Description of an access point not listed in `accessType`.

-   **sample.typeDefault**: Used as default when a new sample is created for this site. See `type` in `Sample` table.

-   **sample.typeOtherDefault**: Used as default when a new sample is created for this site. See `typeOther` in `Sample` table.

-   **sample.collectionDefault**: Used as default when a new sample is created for this site. See `collection` in `Sample` table.

-   **sample.collectOtherDefault**: Used as default when a new sample is created for this site. See `collectionOther` in `Sample` table.

-   **sample.storageTempCDefault**: Used as default when a new sample is created for this site. See `storageTempC` in `Sample` table.

-   **measurement.fractionAnalyzedDefault**: Used as default when a new measurement is created for this site. See `fractionAnalyzed` in `Measurement` table.

-   **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)

-   **geoLong**: Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)

-   **notes**: Any additional notes.

-   **Polygon.ID**: (Foreign key) Links with the Polygon table, this should encompass the area that typically drains into this site.

-   **sewerNetworkFileLink**: Link to a file that has any detailed information about the sewer network associated with the site (any format).

-   **sewerNetworkFileBLOB**: A file BLOB that has any detailed information about the sewer network associated with the site (any format).

## SiteMeasure {#sitemeasure}

Measures that are not performed on the wastewater sample but provide additional context necessary for the interpretation of the results.

-   **ID**: (Primary Key) Unique identifier for each contextual measurement.

-   **Site\_\_ID**: (Foreign Key) Links with the Site table to describe the location of measurement.

-   **Instrument\_\_ID**: (Foreign Key) Links with the `Instrument` table to describe instrument used for the measurement.

-   **Reporter\_\_ID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **dateTime**: The date and time the measurement was performed.

-   **type**: The type of measurement that was performed

    -   `envTemperature`: Environmental temperature.
    -   `envRainfall`: Amount of precipitation in the form of rain.
    -   `envSnowFall`: Amount of precipitation in the form of snow.
    -   `envSnowDepth`: Total depth of snow on the ground.
    -   `wwFlow`: Flow of wastewater.
    -   `wwTemp`: Temperature of the wastewater.
    -   `wwpH`: pH of the wastewater.
    -   `wwConductivity`: Conductivity of the wastewater.
    -   `wwTurbidity`: Turbidity of the wastewater.
    -   `wwTSS`: Total suspended solids concentration of the wastewater.
    -   `wwCOD`: Chemical oxygen demand of the wastewater.
    -   `other`: An other type of measurement. Add description to `typeOther`.

-   **typeOther**: Description of the measurement in case it is not listed in `type`.

-   **typeDescription**: Additional information on the performed measurement.

-   **aggregation**: When reporting an aggregate measurement, this field describes the method used.

    -   `single`: This value is not an aggregate measurement in any way (i.e. not a `mean`, `median`, `geoMean` or any other).
    -   `mean`: Arithmetic mean
    -   `meanNormal`: Arithmetic mean, normalized
    -   `geoMean`: Geometric mean
    -   `geoMeanNormal`: Geometric mean, normalized
    -   `median`: Median
    -   `rangeLowestValue`: Lowest value in a range of values
    -   `rangeHighestValue`: Highest value in a range of values
    -   `sd`: Standard deviation
    -   `sdNormal`: Standard deviation, normalized
    -   `other`: Other aggregation method. Add description to `aggregationOther`

-   **aggregationOther**: Description for other type of aggregation not listed in `aggregation`.

-   **aggregationDescription**: Information on OR reference to which measurements that were included to calculate the aggregated measurement that is being reported.

-   **value**: The actual value that is being reported for this measurement.

-   **unit**: The engineering unit of the measurement.

-   **qualityFlag**: Does the reporter suspect quality issues with the value of this measurement? (Boolean)

-   **denyAccessToPublic**: If this is True, this data will not be available to the public. (Boolean)

-   **denyAccessToAllOrganizations**: If this is True, this data will not be available to any partner organization. (Boolean)

-   **denyAccessToSelf**: If this is True, this data will not be shown on the portal when this reporter logs in. (Boolean)

-   **denyAccessToFederalPublicHealthAuthorities**: If this is True, the data will not be available to employees of the Public Health Agency of Canada - PHAC. (Boolean)

-   **denyAccessToLocalPublicHealthAuthorities**: If this is True the, data will not be available to local health authorities. (Boolean)

-   **denyAccessToProvincialPublicHealthAuthorities**: If this is True, this data will not be available to provincial health authorities. (Boolean)

-   **denyAccessToOtherDataProviders**: If this is True, this data will not be available to other data providers not listed before. (Boolean)

-   **denyAccessToDetails**: More details on the existing confidentiality requirements of this measurement.

-   **notes**: Any additional notes.

## Reporter {#reporter}

The individual or organization that is reporting and responsible for the quality of the data.

-   **ID**: (Primary Key) Unique identifier for the person or organization that is reporting the data.

-   **Site\_\_IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Site` table.

-   **Lab\_\_IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Lab` table.

-   **contactName**: Full Name of the reporter, either an organization or individual.

-   **contactEmail**: Contact e-mail address.

-   **contactPhone**: Contact phone number.

-   **notes**: Any additional notes.

## Lab {#lab}

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

-   **ID**: (Primary key) Unique identifier for the laboratory.

-   **assay.IDDefault**: (Foreign key) Used as default when a new measurement is created for this lab. See `ID` in `AssayMethod` table.

-   **name**: Name corresponding to lab.

-   **contactName**: Contact person or group, for the lab.

-   **contactEmail**: Contact e-mail address, for the lab.

-   **contactPhone**: Contact phone number, for the lab.

-   **updateDate**: Date information was provided or updated.

## AssayMethod {#assaymethod}

The assay method that was used to perform testing. Create a new record if there are changes (improvements) to an existing assay method. Keep the same `ID` and use an updated `version`. A new record for a new version can include only the fields that changed, however, we recommend duplicating existing fields to allow each record to clearly describe all steps. Add a current `date` when recording a new version to an assay.

-   **ID**: (Primary key) Unique identifier for the assay method.

-   **Instrument_ID**: (Foreign Key) Links with the `Instrument` table to describe instruments used for the measurement.

-   **name**: Name of the assay method.

-   **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended.

-   **description**: Description of the assay.

-   **date**: Date on which the assayMethod was created or updated (for version update).

-   **referenceLink**: Link to standard operating procedure (assay reference method).

-   **aliasID**: ID of an assay that is the same or similar. *a coma separated list*.

-   **sampleSizeL**: Size of the sample that is analyzed in liters.

-   **loq**: Limit of quantification (LOQ) for this method if one exists.

-   **lod**: Limit of detection (LOD) for this method if one exists.

-   **unit**: Unit used by this method, that are applicable to the LOD and LOQ.

    -   `vcPMMoV`: Viral copies/copies PMMoV
    -   `vcMl`: Viral copies/millilitres
    -   `vcGms`: Viral copies/grams solids
    -   `vcL`: Viral copies/L
    -   `vcCrA`: Viral copies/copies crAssphage
    -   `m3s`: meters cubed per second
    -   `mgl`: milligrams per liter
    -   `mgOl`: milligrams of oxygen per liter
    -   `other`: Other measurement of viral copies or wastewater treatment plant parameter. Add description to `unitOther`.

-   **unitOther**: Unit used by this method, that are applicable to the LOD and LOQ.

-   **methodConcentration**: Description of the method used to concentrate the sample

-   **methodExtraction**: Description of the method used to extract the sample

-   **methodPcr**: Description of the PCR method used

-   **qualityAssuranceQC**: Description of the quality control steps taken

-   **inhibition**: Description of the inhibition parameters.

-   **surrogateRecovery**: Description of the surrogate recovery for this method.

## Instrument {#instrument}

Instruments that are used for measures in `WWMeaure` and `SiteMeasure`. The assay method for viral measurement are described in `AssayMethod`.

-   **ID**: (Primary key) Unique identifier for the assay method.

-   **name**: Name of the instrument used to perform the measurement.

-   **version** Version or model nummber of the instrument.

-   **description** Description of the instrument.

-   **aliasID**: ID of an assay that is the same or similar. A coma separated list.

-   **referenceLink**: Link to reference for the instrutment.

-   **type**: Type of instrument used to perform the measurement.

    -   `online`: An online sensor
    -   `lab`: Offline laboratory analysis
    -   `handheld`: A handheld measurement analyzer.
    -   `atlineAnalyzer`: An atline analyzer with sampler.
    -   `other:` An other type of measurement instrument. Add description to instrumentTypeOther.

-   **typeOther**: Description of the instrument in case it is not listed in instrumentType.

## Polygon {#polygon}

A simple polygon that encloses an area on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area.

-   **ID**: (Primary key) Unique identifier for the polygon.

-   **name**: Descriptive name of the polygon.

-   **pop**: Approximate population size of people living inside the polygon.

-   **type**: Type of polygon.

    -   `sewerNetwork`: Sewer network
    -   `healthRegion`: Health region served by the sewer network

-   **wkt**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) of the polygon

-   **file**: File containing the geometry of the polygon, BLOB format.

-   **link**: Link to an external reference that describes the geometry of the polygon.

## CovidPublicHealthData {#covidpublichealthdata}

Covid-19 patient data for a specified polygon.

-   **ID**: (Primary key) Unique identifier for the table.

-   \*\*Reporter\_\_ID\*\*: (Foreign key) ID of the reporter who gave this data.

-   \*\*Polygon\_\_ID\*\*: (Foreign key) Links with the `Polygon` table.

-   **date**: Date of reporting for covid-19 measure.

-   **type**: Type of covid-19 patient data.

    -   `confirmed`: Number of confirmed cases. This measure should be accompanied by `dateTyep`.
    -   `active`: Number of active cases.
    -   `tests`: Number of tests performed.
    -   `positiveTests`: Number of positive tests.
    -   `percentPositivityRate`: Percent positivity rate.
    -   `hospitalCensus`: Hospital census or the number of people admitted with covid-19.
    -   `hospitalAdmit`: Hospital admissions or patients newly admitted to hospital.

-   **dateType**: Type of date used for `confirmed` cases. Typically `reported` or `episode` are reported. `onset` and `test` date is not usually reported within aggregate data.

    -   `episode` : Episode date is the earliest of onset, test or reported date.
    -   `onset`: Earliest that symptoms were reported for this case. This data is often not known and reported. In lieu, `episode` is used.
    -   `reported`: Date that the numbers were reported publicly. Typically, `reported` data and this measure is most commonly reported and used.
    -   `test`: Date that the covid-19 test was performed.

-   **value**: The numeric value that is being reported.

-   **notes**: Any additional notes.

## Lookups {#lookups}

Used for lookup values of all category based columns

-   **tableName**: Name of the Table

-   **columnName**: Name for the column

-   **value**: Name of the value

-   **description**: Name of the description

## Naming conventions

-   **table names**: Table names use UpperCamelCase.
-   **variable and category names**: Both variables and variable categories use lowerCamelCase. Do not use special characters (only uppercase, lowercase letters and numbers). Reason: variable and category names can be combined to generate derived variables. Using special characters will generate non-allowable characters - see below.
-   **variables in Wide tables**: Wide tables use `_` to concatenate variables from long tables.
-   **variable order** if a multiple measurement take place on different dates this has a natural form in the long table format, however in the pivot wider format this can be ambiguous. In this case, show a `analysisDate` followed by a series of measurements taken on that date ex(`temp_c_singleton`) then another `covidN1_PPMV_mean` followed by more measurements ex(`covidN1_PPMV_mean`)
-   **merging Tables** : when you merge tables concatenate column names with`__`. So `dateTime` from the `Sample` table becomes `Sample__dateTime`.
-   **Derived, summary or transformed measures**: Follows the same approach as naming variable and category names, except use a `_` when concatenating variable or category names. These three types measures are generated to summarize or transform one or more variables. An example is calculating the mean value of one or more SARS-CoV-2 regions. Normalization and standardization are other examples of a transformed measure.
-   **date**: YYYY-MM-DD HH:mm:ss (24 hour format, in UTC)
-   **location**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) for polygon.
-   **versions**: [Semantic versioning](https://semver.org)

## Examples of how to generate wide variable and category names

### 1) Simple viral region report

A long table would represent viral measures of:

``` {.markdown}
date = 2021-01-15
type = covidN1
unit = vcPMMoV
aggregation = mean
value = 40
```

``` {.markdown}
date = 2021-01-15
type = covidN2
unit = vcPMMoV
aggregation = mean
value = 42
```

In a long table as:

| date       | type    | unit    | aggregation | value |
|------------|---------|---------|-------------|-------|
| 2021-01-15 | covidN1 | vcPPMoV | mean        | 40    |
| 2021-01-15 | covidN2 | vcPPMoV | mean        | 42    |

A wide table would represent the same measurement as:

``` {.markdown}
    WWMeasure__covidN1_PPMV_mean = 40
    WWMeasure__covidN2_PPMV_mean = 42
```

In a wide table as:

| date       | WWMeasure\_\_covidN1_vcPPMoV_mean | WWMeasure\_\_covidN2_vcPPMoV_mean |
|------------|-----------------------------------|-----------------------------------|
| 2021-01-15 | 40                                | 42                                |

### 2) Derived measure

To report a mean value of existing covidN1 and covidN2 measures:

``` {.markdown}
    date = 2021-01-15
    type = covidN1
    unit = ml
    aggregation = mean
    value = 42
```

``` {.markdown}
    date = 2021-01-15
    type = covidN2
    unit = ml
    aggregation = mean
    value = 40
```

Represent the derived measure as:

long table format

``` {.markdown}
    date = 2021-01-15
    type = covidN1covidN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type           | unit | aggregation | value |
|------------|----------------|------|-------------|-------|
| 2021-01-15 | covidN1covidN2 | ml   | mean        | 41    |

or, gitwide table format

``` {.markdown}
    date = 2021-01-15
    covidN1covidN2_ml_mean = 41
```

-   Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMoV:

Represent the derived measure as:

long table description

``` {.markdown}
    date = 2021-01-15
    covidN1covidN2 = 2
    measureUnit = PPMV
    measureType = meanNormal
```

or,

wide table format

``` {.markdown}
    covidN1covidN2_PPMV_meanNormal = 2
```
