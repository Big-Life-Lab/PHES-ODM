# Metadata

There are eight tables that are described below. example data is stored in [data](data).

-   [Sample](#sample)
-   [WWMeasure](#wwmeasure)
-   [Site](#Site)
-   [SiteMeasure](#sitemeasure)
-   [Reporter](#reporter)
-   [Lab](#lab)
-   [AssayMethod](#assaymethod)
-   [Polygon](#polygon)
-   [CovidPublicHealthData](#covidpublicHealthdata)
-   [Lookups](#lookups)

Entity Relationship Diagram [here](#entity-relationship-diagram).

## Entity Relationship Diagram {#entity-relationship-diagram}

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/023490f3-6cc5-41be-bc2d-d96425f3c68f/edit?page=0_0#?folder_id=home&browser=icon)

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

-   **sample.ID**: (Foreign key) Links with the identified Sample.

-   **lab.ID**: (Foreign key) Links with the identified Lab that performed the analysis.

-   **assay.ID**: (Foreign key) Links with the AssayMethod used to perform the analysis.

-   **analysisDate**: Date the measurement was performed in the lab.

-   **reportDate**: Date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original `sampleID` but updated `MeasureID`, `reportDate` and `assayID` (if needed).

-   **fractionAnalyzed**: Faction of the sample that is analyzed.

    -   `liquid`: Liquid fraction
    -   `solid`: Solid fraction
    -   `mixed`: Mixed/homogenized sample

-   **category**: The variable that is being measured on the sample, e.g. gene target region (`covid`) or water quality parameter (`wq`).

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

-   **categoryOther**: Description for an other variable not listed in `category`.

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

-   **notes**: Any additional notes.

## Site {#site}

The site of wastewater sampling, including several *defaults* that can be used to populate new samples upon creation.

-   **ID**: (Primary Key) Unique identifier for the location where wastewater sample was taken.

-   **name**: Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.

-   **description**: Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.

-   **reporter.ID**: (Foreign key) Links with the reporter that is responsible for the data.

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

-   **Site.ID**: (Foreign Key) Links with the Site table to describe the location of measurement.

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

-   **instrumentName**: Name of the instrument used to perform the measurement.

-   **instrumentType**: Type of instrument used to perform the measurement.

    -   `online`: An online sensor.
    -   `lab`: Offline laboratory analysis.
    -   `handheld`: A handheld measurement analyzer.
    -   `atlineAnalyzer`: An atline analyzer with sampler.
    -   `other`: An other type of measurement instrument. Add description to `instrumentTypeOther`.

-   **instrumentTypeOther**: Description of the instrument in case it is not listed in `instrumentType`.

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

-   **notes**: Any additional notes.

## Reporter {#reporter}

The individual or organization that is reporting and responsible for the quality of the data.

-   **ID**: (Primary Key) Unique identifier for the person or organization that is reporting the data.

-   **site.IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Site` table.

-   **lab.IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Lab` table.

-   **contactName**: Full Name of the reporter, either an organization or individual.

-   **contactEmail**: Contact e-mail address.

-   **contactPhone**: Contact phone number.

-   **allowAccessToSelf**: Default: True. If this is False the data will not be shown on the portal when the data provider logs in

-   **allowAccessToFederalPublicHealthAuthorities**: Default: True. If this is False the data will not be available to employees of PHAC

-   **allowAccessToLocalPublicHealthAuthorities**: Default: True. If this is False data will not be available when local health Authorities log in.

-   **allowAccessToProvincialPublicHealthAuthorities**: Default: True. If this is False data will not available when provincial health Authorities log in.

-   **allowAccessToOtherDataProviders**: Default: True. If this is False data will not be available when other data providers login.

-   **allowAccessToAllOrganizations**: Default: True. If this is False data will not be available when any partner organization logs into the system

-   **allowAccessToPublic**: Default: True. If this is False data will not be available to the public.

-   **allowAccessToSpec**: Details or specifics on confidentiality requirements.

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

-   **name**: Name of the assay method.

-   **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended.

-   **description**: Description of the assay.

-   **date**: Date on which the assayMethod was created or updated (for version update).

-   **referenceLink**: Link to standard operating procedure (assay reference method).

-   **alaisID**: ID of an assay that is the same or similar. *a coma separated list*.

-   **sampleSizeL**: Size of the sample that is analyzed in liters.

-   **loq**: Limit of quantification (LOQ) for this method if one exists.

-   **lod**: Limit of detection (LOD) for this method if one exists.

-   **units**: Units used by this method, that are applicable to the LOD and LOQ.

    -   `vcPMMoV`: Viral copies/copies PMMoV
    -   `vcMl`: Viral copies/millilitres
    -   `vcGms`: Viral copies/grams solids
    -   `vcL`: Viral copies/L
    -   `vcCrA`: Viral copies/copies crAssphage
    -   `m3s`: meters cubed per second
    -   `mgl`: milligrams per liter
    -   `mgOl`: milligrams of oxygen per liter
    -   `other`: Other measurement of viral copies or wastewater treatment plant parameter. Add description to `unitOther`.

-   **unitsOther**: Units used by this method, that are applicable to the LOD and LOQ.

-   **methodConcentration**: Description of the method used to concentrate the sample

-   **methodExtraction**: Description of the method used to extract the sample

-   **methodPcr**: Description of the PCR method used

-   **qualityAssuranceQC** : Description of the quality control steps taken

-   **inhibition**: Description of the inhibition parameters.

-   **surrogateRecovery**: Description of the surrogate recovery for this method.

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

Covid-19 patient data in a given polygon. Note that data can be presented as wide data format, see [examples](#wide).

-   **ID**: (Primary key) Unique identifier for the table.

-   **Reporter.ID**: (Foreign key) ID of the reporter who gave this data.

-   **Polygon.ID**: (Foreign key) Links with the `Polygon` table.

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
-   **variable and category names**: Both variables and variable categories use lowerCamelCase.
-   **variables in Wide tables**: Wide tables use `_` to concatenate variables from long tables.
-   **Variable order** if a multiple measurement take place on different dates this has a natural form in the long table format, however in the pivot wider format this can be ambiguous. In this case, show a `analysisDate` followed by a series of measurements taken on that date ex(`temp_c_singleton`) then another `covidN1_PPMV_mean` followed by more measurements ex(`covidN1_PPMV_mean`)
-   **merging Tables** : when you merge tables concatenate column names with `.` . So `dateTime` from the `Sample` table becomes `Sample.dateTime`.
-   **Derived, summary or transformed measures**: Follows the same approach as naming variable and category names, except use a `_` when concatenating variable or category names. These three types measures are generated to summarize or transform one or more variables. An example is calculating the mean value of one or more SARS-CoV-2 regions. Normalization and standardization are other examples of a transformed measure.
-   **date**: MM/DD/YYYY HH:mm:ss (24 hour format, in UTC)
-   **location**: TBD
-   **versions**: [Semantic versioning](https://semver.org)

## Examples of how to generate wide variable and category names (\#wide)

### 1) Simple viral region report

A long table would represent viral measures of:

``` {.markdown}
date = 2021-01-15
type = covidN1
unit = vcPMMoV
aggregation = Mean
value = 40
```

``` {.markdown}
date = 2021-01-15
type = covidN2
unit = vcPMMoV
aggregation = Mean
value = 42
```

In a long table as:

| date       | type    | unit    | aggregation | value |
|------------|---------|---------|-------------|-------|
| 2021-01-15 | covidN1 | vcPPMoV | mean        | 40    |
| 2021-01-15 | covidN2 | vcPPMoV | mean        | 42    |

A wide table would represent the same measurement as:

``` {.markdown}
    WWMeasure.covidN1_PPMV_mean = 40
    WWMeasure.covidN2_PPMV_mean = 42
```

In a wide table as:

| date       | WWMeasure.covidN1\_vcPPMoV\_mean | WWMeasure.covidN2\_vcPPMoV\_mean |
|------------|----------------------------------|----------------------------------|
| 2021-01-15 | 40                               | 42                               |

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
    type = covidN1-covidN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type            | unit | aggregation | value |
|------------|-----------------|------|-------------|-------|
| 2021-01-15 | covidN1-covidN2 | ml   | mean        | 41    |

or, wide table format

``` {.markdown}
    date = 2021-01-15
    covidN1-covidN2_ml_mean = 41
```

-   Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMoV:

Represent the derived measure as:

long table description

``` {.markdown}
    date = 2021-01-15
    covidN1-covidN2 = 2
    measureUnit = PPMV
    measureType = meanNormal
```

or,

wide table format

``` {.markdown}
    covidN1-covidN2_PPMV_meanNormal = 2
```
