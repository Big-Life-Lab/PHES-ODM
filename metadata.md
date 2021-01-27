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

## Sample

The sample is a representative volume of wastewater taken from a [Site](#Site) which is then analysed by a lab.

-   **sampleID**: (Primary Key) Unique identification for sample. Suggestion: *siteID-date-index*.

-   **siteID**: (Foreign key) Links with the Site table to describe the location of sampling.

-   **dateTime**: For grab samples this is the *date, time and timezone* the sample was taken.

-   **dateTimeStart**: For integrated time averaged samples this is the *date, time and timezone* the sample was started being taken.

-   **dateTimeEnd**: For integrated time average samples this is the *date, time and timezone* the sample was finished being taken.

-   **type**: Type of sample.

    -   `rawWW`: Raw wastewater.
    -   `swrSed`: Sediments obtained in sewer.
    -   `pstGrit`: Raw wastewater after a treatment plant's headworks.
    -   `pSludge`: Sludge produced by primary clarifiers.
    -   `pEfflu`: Effluent obtained after primary clarifiers.
    -   `sSludge`: Sludge produced by secondary clarifiers.
    -   `sEfflu`: Effluent obtained after secondary clarifiers.
    -   `water`: Non-wastewater, coming from any kind of water body.
    -   `faeces`: Fecal matter.
    -   `other`: Other type of site. Add description to `typeOther`.

-   **typeOther**: Description for other type of sample not listed in `type`.

-   **collection**: Method used to collect the data.

    -   `cpTP24h`: A time proportional 24-hour composite sample generally collected by an autosampler.
    -   `cpFP24h`: A flow proportional 24-hour composite sample generally collected by an autosampler.
    -   `grb`: A single large representative grab sample.
    -   `grbCp8h`: An 8-hour composite with 8 grab samples each taken once per hour, generally manually performed.
    -   `grbCp3h`: A 3-hour composite with 3 grab samples each taken once per hour, generally manually performed.
    -   `grbCp3`: A grab-composite sample composed of 3 separate grab samples.  
    -   `mooreSw`: Moore swab passive sample.
    -   `other`: Other type of collection method. Add description to `collectionOther`.

-   **collectionOther**: Description for other type of method not listed in `collection`.

-   **collectionTriggerTime** Time between sub-samples for `discTimeProp` numeric value given in minutes.

-   **preTreatment**: Was the sample chemically treated in anyway with the addition of stabilizers or other?

-   **preTreatmentDescription**: If `preTreatment` then describe the treatment that was performed.

-   **children**: If this is a sample with many smaller samples either because of pooling or sub-sampling this indicates *a comma separated list of child sampleIDs*.

-   **parent** : If this sample has been pooled into one big sample for analysis this indicates the *sampleID of the larger pooled sample*.

-   **sizeL**: Total volume of water or sludge sampled.

-   **fieldSampleTempC**: Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples which are either kept at ambient temperature or refrigerated while being sampled.

-   **shippedOnIce**: Was the sample kept cool while being shipped to the lab?

-   **storageTempC**: Temperature that the sample is stored at in Celsius.

-   **qualityFlag**: Does the reporter suspect the sample having some quality issues?

-   **notes**: Any additional notes.

## WWMeasure

Measurement result (ie. single variable) from a wastewater sample. `WWMeaasure` includes data that is commonly collected by staff at wastewater laboratories where measurement is performed using an assay method (see [AssayMethod](#assaymethod)), but can also be performed using specific instruments (see [Instruments](#instrument). Measures performed at the site of the wastewater sample are reported in `SiteMeasure`.

-   **uWwMeasureID**: (Primary key) Unique identifier a measurement within the measurement table.

-   **wwMeasureID**: Unique identifier for wide table only. Use when all measures are performed on a single sample at the same time and same laboratory. Suggestion: _siteID_sampleID_LabID_reportDate_ID_.

-   **sampleID**: (Foreign key) Links with the identified Sample.

-   **labID**: (Foreign key) Links with the identified Lab that performed the analysis.

-   **assayID**: (Foreign key) Links with the `AssayMethod` used to perform the analysis. Use `instrument.ID` for measures that are not viral measures.

-   **instrumentID**: (Foreign key) Links with the `Instrument` used to perform the analysis. Use `assay.ID` for viral measures.

-   **reporterID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **analysisDate**: Date the measurement was performed in the lab.

-   **reportDate**: Date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original `sampleID` but updated `MeasureID`, `reportDate` and `assayID` (if needed).

-   **fractionAnalyzed**: Faction of the sample that is analyzed.

    -   `liquid`: Liquid fraction
    -   `solid`: Solid fraction
    -   `mixed`: Mixed/homogenized sample

-   **type**: The variable that is being measured on the sample, e.g. a SARS-CoV-2 gene target region (`cov`), a biomarker for normalisation (`n`) or a water quality parameter (`wq`).

    -   `covN1`: SARS-CoV-2 nucleocapsid gene N1
    -   `covN2`: SARS-CoV-2 nucleocapsid gene N2
    -   `covN3`: SARS-like coronaviruses nucleocapsid gene N3
    -   `covE`: SARS-CoV-2 gene region E
    -   `covRdRp`: SARS-CoV-2 gene region RdRp
    -   `nPMMoV`: Pepper mild mottle virus
    -   `ncrA`: cross-assembly phage
    -   `wqTS`: Total solids concentration.
    -   `wqTSS`: Total suspended solids concentration.
    -   `wqVSS`: Volatile suspended solids concentration.
    -   `wqCOD`: Chemical oxygen demand.
    -   `wqOPhos`: Ortho-phosphate concentration.
    -   `wqNH4N`: Ammonium nitrogen concentration, as N.
    -   `wqTN`: Total nitrogen concentration, as N.
    -   `wqPh`: pH.
    -   `wqCond`: Conductivity.
    -   `other`: Other measurement category. Add description to `categoryOther`.

-   **typeOther**: Description for an other variable not listed in `category`.

-   **unit**: Unit of the measurement.

    -   `gcPMMoV`: Gene copies per copy of PMMoV.
    -   `gcMl`: Gene copies per milliliter.
    -   `gcGs`: Gene copies per gram solids.
    -   `gcL`: Gene copies per liter.
    -   `gcCrA`: Gene copies per copy of crAssphage.
    -   `Ct`: Cycle threshold.
    -   `mgL`: Milligrams per liter.
    -   `ph`: pH units
    -   `uScm`: Micro-siemens per centimeter.
    -   `pp`: Percent positive, for Moore swab.
    -   `pps`: Percent primary sludge, for total solids.
    -   `other`: Other measurement of viral copies or wastewater treatment plant parameter. Add description to `UnitOther`.

-   **unitOther**: Description for other measurement unit not listed in `unit`.

-   **aggregation**: Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each aggregation has a corresponding value.

    -   `single`: This value is not an aggregate measurement in any way (ie. not a `mean`, `median`, `max` or any other) and can be a replicate value.
    -   `mean`: Arithmetic mean
    -   `meanNr`: Arithmetic mean, normalized
    -   `geoMn`: Geometric mean
    -   `geoMnNr`: Geometric mean, normalized
    -   `median`: Median
    -   `min`: Lowest value in a range of values
    -   `max`: Highest value in a range of values
    -   `sd`: Standard deviation
    -   `sdNr`: Standard deviation, normalized
    -   `other`: Other aggregation method. Add description to `aggregationOther`

-   **aggregationOther**: Description for other type of aggregation not listed in `aggregation`.

-   **index**: Index number in case the measurement was taken multiple times.

-   **value**: The actual measurement value that was obtained through analysis.

-   **qualityFlag**: Does the reporter suspect the measurement having some quality issues?

-   **noAccessToPublic**: If this is True, this data will not be available to the public. If missing, data will be available to the public.

-   **noAccessToAllOrg**: If this is True, this data will not be available to any partner organization. If missing, data will be available to the all organizations.

-   **noAccessToSelf**: If this is True, this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.

-   **noAccessToPHAC**: If this is True, the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.

-   **noAccessToLocalHA**: If this is True the, data will not be available to local health authorities. If missing, data will be available to local health authorities.

-   **noAccessToProvHA**: If this is True, this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.

-   **noAccessToOtherProv**: If this is True, this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before

-   **noAccessToDetails**: More details on the existing confidentiality requirements of this measurement.

-   **notes**: Any additional notes.

## Site

The site of wastewater sampling, including several *defaults* that can be used to populate new samples upon creation.

-   **siteID**: (Primary Key) Unique identifier for the location where wastewater sample was taken.

-   **name**: Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.

-   **description**: Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.

-   **type**: Type of site or institution where sample was taken.

    -   `airPln`: Airplane.
    -   `corFcil`: Correctional facility.
    -   `school`: School.
    -   `hosptl`: Hospital.
    -   `ltcf`: Long-term care facility.
    -   `swgTrck`: Sewage truck.
    -   `uCampus`: University campus.
    -   `mSwrPpl`: Major sewer pipeline.
    -   `pStat`: Pumping station.
    -   `holdTnk`: Hold tank.
    -   `retPond`: Retention pond.
    -   `wwtpMuC`: Municipal wastewater treatment plant for combined sewage.
    -   `wwtpMuS`: Municipal wastewater treatment plant for sanitary sewage only.
    -   `wwtpInd`: Industrial wastewater treatment plant.
    -   `lagoon`: Logoon system for extensive wastewater treatment.
    -   `septTnk`: Septic tank.
    -   `river`: River, natural water body.
    -   `lake`: Lake, natural water body.
    -   `estuary`: Estuary, natural water body
    -   `sea`: Sea, natural water body.
    -   `ocean`: Ocean, natural water body.
    -   `other`: Other site type. Add description to `typeOther`.

-   **typeOther**: Description of the site when the site is not listed. See `siteType`.

-   **typeDefault**: Used as default when a new sample is created for this site. See `type` in `Sample` table.

-   **typeOtherDefault**: Used as default when a new sample is created for this site. See `typeOther` in `Sample` table.

-   **collectionDefault**: Used as default when a new sample is created for this site. See `collection` in `Sample` table.

-   **collectOtherDefault**: Used as default when a new sample is created for this site. See `collectionOther` in `Sample` table.

-   **storageTempCDefault**: Used as default when a new sample is created for this site. See `storageTempC` in `Sample` table.

-   **fractionAnalyzedDefault**: Used as default when a new measurement is created for this site. See `fractionAnalyzed` in `Measurement` table.

-   **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)

-   **geoLong**: Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)

-   **notes**: Any additional notes.

-   **polygonID**: (Foreign key) Links with the Polygon table, this should encompass the area that typically drains into this site.

-   **sewerNetworkFileLink**: Link to a file that has any detailed information about the sewer network associated with the site (any format).

-   **sewerNetworkFileBLOB**: A file BLOB that has any detailed information about the sewer network associated with the site (any format).

## SiteMeasure

Measurement result (ie. single variable) obtained by at the site of wastewater sample.`SiteMeasure` includes data that is commonly collected by staff at wastewater treatment facilities and field sample locations. These measures that are not performed on the wastewater sample but provide additional context necessary for the interpretation of the results. Measures performed on the wastewater sample are reported in `WWMeasure`.

-   **uSiteMeasureID**: (Primary Key) Unique identifier for each measurement for a site.

-   **siteMeasureID**: Unique identifier for wide table only. Use when all measures are performed on a single sample.

-   **siteID**: (Foreign Key) Links with the Site table to describe the location of measurement.

-   **instrumentID**: (Foreign Key) Links with the `Instrument` table to describe instrument used for the measurement.

-   **reporterID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **dateTime**: The date and time the measurement was performed.

-   **type**: The type of measurement that was performed. The prefix `env` is used for environmental variables, whereas `ww` indicates a measurement on wastewater.

    -   `envTemp`: Environmental temperature.
    -   `envRnF`: Rain fall, i.e. amount of precipitation in the form of rain.
    -   `envSnwF`: Snow fall, i.e. amount of precipitation in the form of snow.
    -   `envSnwD`: Total depth of snow on the ground.
    -   `wwFlow`: Flow of wastewater.
    -   `wwTemp`: Temperature of the wastewater.
    -   `wwTSS`: Total suspended solids concentration of the wastewater.
    -   `wwCOD`: Chemical oxygen demand of the wastewater.
    -   `wwTurb`: Turbidity of the wastewater.
    -   `wwOPhos`: Ortho-phosphate concentration.
    -   `wwNH4N`: Ammonium nitrogen concentration, as N.
    -   `wwTN`: Total nitrogen concentration, as N.
    -   `wwpH`: pH of the wastewater.
    -   `wwCond`: Conductivity of the wastewater.
    -   `other`: An other type of measurement. Add description to `typeOther`.

-   **typeOther**: Description of the measurement in case it is not listed in `type`.

-   **typeDescription**: Additional information on the performed measurement.

-   **aggregation**: When reporting an aggregate measurement, this field describes the method used.

    -   `single`: This value is not an aggregate measurement in any way (ie. not a `mean`, `median`, `max` or any other) and can be a replicate value.
    -   `mean`: Arithmetic mean
    -   `meanNr`: Arithmetic mean, normalized
    -   `geoMn`: Geometric mean
    -   `geoMnNr`: Geometric mean, normalized
    -   `median`: Median
    -   `min`: Lowest value in a range of values
    -   `max`: Highest value in a range of values
    -   `sd`: Standard deviation
    -   `sdNr`: Standard deviation, normalized
    -   `other`: Other aggregation method. Add description to `aggregationOther`

-   **aggregationOther**: Description for other type of aggregation not listed in `aggregation`.

-   **aggregationDesc**: Information on OR reference to which measurements that were included to calculate the aggregated measurement that is being reported.

-   **value**: The actual value that is being reported for this measurement.

-   **unit**: The engineering unit of the measurement.

-   **qualityFlag**: Does the reporter suspect quality issues with the value of this measurement?

-   **noAccessToPublic**: If this is True, this data will not be available to the public. If missing, data will be available to the public.

-   **noAccessToAllOrg**: If this is True, this data will not be available to any partner organization. If missing, data will be available to the all organizations.

-   **noAccessToSelf**: If this is True, this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.

-   **noAccessToPHAC**: If this is True, the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.

-   **noAccessToLocalHA**: If this is True the, data will not be available to local health authorities. If missing, data will be available to local health authorities.

-   **noAccessToProvHA**: If this is True, this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.

-   **noAccessToOtherProv**: If this is True, this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before

-   **noAccessToDetails**: More details on the existing confidentiality requirements of this measurement.

-   **notes**: Any additional notes.

## Reporter

The individual or organization that is reporting and responsible for the quality of the data.

-   **reporterID**: (Primary Key) Unique identifier for the person or organization that is reporting the data.

-   **siteIDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Site` table.

-   **labIDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Lab` table.

-   **contactName**: Full Name of the reporter, either an organization or individual.

-   **contactEmail**: Contact e-mail address.

-   **contactPhone**: Contact phone number.

-   **notes**: Any additional notes.

## Lab

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

-   **labID**: (Primary key) Unique identifier for the laboratory.

-   **assayIDDefault**: (Foreign key) Used as default when a new measurement is created for this lab. See `ID` in `AssayMethod` table.

-   **name**: Name corresponding to lab.

-   **contactName**: Contact person or group, for the lab.

-   **contactEmail**: Contact e-mail address, for the lab.

-   **contactPhone**: Contact phone number, for the lab.

-   **updateDate**: Date information was provided or updated.

## AssayMethod

The assay method that was used to perform testing. Create a new record if there are changes (improvements) to an existing assay method. Keep the same `ID` and use an updated `version`. A new record for a new version can include only the fields that changed, however, we recommend duplicating existing fields to allow each record to clearly describe all steps. Add a current `date` when recording a new version to an assay.

-   **assayMethodID**: (Primary key) Unique identifier for the assay method.

-   **instrumentID**: (Foreign Key) Links with the `Instrument` table to describe instruments used for the measurement.

-   **name**: Name of the assay method.

-   **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended.

-   **summary**: Short description of the assay and how it is different from the other assay methods.

-   **referenceLink**: Link to standard operating procedure.

-   **date**: Date on which the assayMethod was created or updated (for version update).

-   **aliasID**: ID of an assay that is the same or similar. *a comma separated list*.

-   **sampleSizeL**: Size of the sample that is analyzed in liters.

-   **loq**: Limit of quantification (LOQ) for this method if one exists.

-   **lod**: Limit of detection (LOD) for this method if one exists.

-   **unit**: Unit used by this method, and applicable to the LOD and LOQ.

    -   `gcPMMoV`: Gene copies per copy of PMMoV.
    -   `gcMl`: Gene copies per milliliter.
    -   `gcGms`: Gene copies per gram solids.
    -   `gcL`: Gene copies per liter.
    -   `gcCrA`: Gene copies per copy of crAssphage.
    -   `other`: Other measurement of viral copies. Add description to `unitOther`.

-   **unitOther**: Unit used by this method, that are applicable to the LOD and LOQ.

-   **methodConc**: Description of the method used to concentrate the sample

-   **methodExtract**: Description of the method used to extract the sample

-   **methodPcr**: Description of the PCR method used

-   **qualityAssuranceQC**: Description of the quality control steps taken

-   **inhibition**: Description of the inhibition parameters.

-   **surrogateRecovery**: Description of the surrogate recovery for this method.

## Instrument

Instruments that are used for measures in `WWMeasure` and `SiteMeasure`. The assay method for viral measurement are described in `AssayMethod`.

-   **instrumentID**: (Primary key) Unique identifier for the assay method.

-   **name**: Name of the instrument used to perform the measurement.

-   **model** Model number or version of the instrument.

-   **description** Description of the instrument.

-   **alias**: ID of an assay that is the same or similar. A comma separated list.

-   **referenceLink**: Link to reference for the instrument.

-   **type**: Type of instrument used to perform the measurement.

    -   `online`: An online sensor
    -   `lab`: Offline laboratory analysis
    -   `hand`: A handheld measurement analyzer.
    -   `atline`: An atline analyzer with sampler.
    -   `other:` An other type of measurement instrument. Add description to instrumentTypeOther.

-   **typeOther**: Description of the instrument in case it is not listed in instrumentType.

## Polygon

A simple polygon that encloses an area on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area.

-   **polygonID**: (Primary key) Unique identifier for the polygon.

-   **name**: Descriptive name of the polygon.

-   **pop**: Approximate population size of people living inside the polygon.

-   **type**: Type of polygon.

    -   `swrCat`: Sewer catchment area.
    -   `hlthReg`: Health region served by the sewer network

-   **wkt**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) of the polygon

-   **file**: File containing the geometry of the polygon, BLOB format.

-   **link**: Link to an external reference that describes the geometry of the polygon.

## CovidPublicHealthData

Covid-19 patient data for a specified polygon.

-   **cphdID**: (Primary key) Unique identifier for the table.

-   **reporterID**: (Foreign key) ID of the reporter who gave this data.

-   **polygonID**: (Foreign key) Links with the `Polygon` table.

-   **date**: Date of reporting for covid-19 measure.

-   **type**: Type of covid-19 patient data.

    -   `conf`: Number of confirmed cases. This measure should be accompanied by `dateType`.
    -   `active`: Number of active cases.
    -   `test`: Number of tests performed.
    -   `posTest`: Number of positive tests.
    -   `pPosRt`: Percent positivity rate.
    -   `hospCen`: Hospital census or the number of people admitted with covid-19.
    -   `hospAdm`: Hospital admissions or patients newly admitted to hospital.

-   **dateType**: Type of date used for `conf` cases. Typically `report` or `episode` are reported. `onset` and `test` date is not usually reported within aggregate data.

    -   `episode` : Episode date is the earliest of onset, test or reported date.
    -   `onset`: Earliest that symptoms were reported for this case. This data is often not known and reported. In lieu, `episode` is used.
    -   `report`: Date that the numbers were reported publicly. Typically, `reported` data and this measure is most commonly reported and used.
    -   `test`: Date that the covid-19 test was performed.

-   **value**: The numeric value that is being reported.

-   **notes**: Any additional notes.

## Lookup

Used for lookup values of all category based columns

-   **tableName**: Name of the Table

-   **columnName**: Name for the column

-   **value**: Name of the value

-   **description**: Name of the description

## Naming conventions

-   **Table names**: Table names use UpperCamelCase.

-   **Variable and category names**: Both variables and variable categories use lowerCamelCase. Do not use special characters (only uppercase, lowercase letters and numbers). Reason: variable and category names can be combined to generate derived variables. Using special characters will generate non-allowable characters - see below. Category names a maximum of 7 characters to allow concatenation of four categories into a single variaable to comply with ArcGIS 31 character maximum for variable names. 

-   **Variables in wide tables**: Wide tables use `_` to concatenate variables from long tables.

-   **Variable order** If a multiple measurement take place on different dates this has a natural form in the long table format, however in the pivot wider format this can be ambiguous. In this case, show a `reportDate` followed by a series of measurements taken on that date (e.g. `covN1_PPMV_mean`) followed by more measurements (e.g. `covN2_PPMV_mean`)

-   **Merging tables** : Merging tables into a wide table requires additional steps when a variable does not have an unique name (when the variable name appears in more than one table). For example, variables such as `dateTime`, `notes`, `description`, `type`, `version` and `ID` variables such as `sampleID` are used in several tables. Use the following approach:

    -   Variable that are not unique (they are in more than one table): add the table name to the variable by concatenate column names with `_`. e.g. `dateTime` from the `Sample` table becomes `Sample_dateTime`.
    -   Variable that are unique (they in only one table in the entire OMD). No variable name changes are needed.

-   **Derived, summary or transformed measure**: These measures are generated to summarize or transform one or more variables. Naming convention follows the same approach as naming variable and category names, except use a `_` when concatenating variable or category names.  Examples of derived measure the calculation of a mean mean value of one or more SARS-CoV-2 regions. Normalization and standardization are other examples of a transformed measure. Typically derived, summary or transform measures are not reported, rather the preferred reporting approach reporting the underlying measures. 

-   **Date time**: YYYY-MM-DD HH:mm:ss (24 hour format, in UTC)

-   **Location**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) for polygon.

-   **Version**: [Semantic versioning](https://semver.org)

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
