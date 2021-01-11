# Metadata

There are eight tables that are described below. example data is stored in [data](data).

-   [Measurement](#Measurement) ([Measurements.csv](data/Measurements.csv))
-   [Sample](#Sample) ([Sample.csv](data/Sample.csv))
-   [Site](#Site) ([Site.csv](data/Site.csv))
-   [Reporter](#Reporter) ([Reporter.csv](data/Reporter.csv))
-   [Lab](#Lab) ([Lab.csv](data/Lab.csv))
-   [AssayMethod](#AssayMethod) (AssayMethod.csv - **TBA**)
-   [Polygon](#Polygon) (Polygon.csv - **TBA**)
-   [CovidPublicHealthData](#CovidPublicHealthData) (CovidPublicHealthData.csv - **TBA**)
-   [Lookups](#Lookups) (Lookups.csv - **TBA**)

Entity Relationship Diagram [here](#erd).

## Entity Relationship Diagram <span id="erd"><span>

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/023490f3-6cc5-41be-bc2d-d96425f3c68f/edit?page=0_0#?folder_id=home&browser=icon)

## Measurement (Measurement.csv) <span id="Measurement"><span>

Measurement result (ie. single variable) of a potentially positive SARS-CoV-2 wastewater sample.

-   **uID**: (Primary key) Unique identifier within the measurement table.

-   **ID**: Unique identifier for a given analysis, where analysis means you performed all steps needed to get the measurement, but measurements are not independent.

-   **sample.ID**: (Foreign key) Links with the identified Sample.

-   **lab.ID**: (Foreign key) Links with the identified Lab that performed the analysis.

-   **assay.ID**: (Foreign key) Links with the AssayMethod used to perform the analysis.

-   **analysisDate**: Date the measurement was performed in the lab.

-   **reportDate**: Date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original `sampleID` but updated `measurementID`, `reportDate` and `assayID` (if needed).

-   **fractionAnalyzed**: Faction of the sample that is analyzed.

    -   `liquid`: Liquid fraction
    -   `solid`: Solid fraction
    -   `mixed`: Mixed/homogenized sample

-   **category**: The variable that is being measured, e.g. gene target region (`covid`), water quality parameter (`wqParam`), wastewater treatment plant parameter (`wwParam`).

    -   `covidUnspecified (default)`:
    -   `covidN1`: SARS-CoV-2 gene region N1
    -   `covidN2`: SARS-CoV-2 gene region N2
    -   `covidN3`: SARS-CoV-2 gene region N3
    -   `covidE`: SARS-CoV-2 gene region E
    -   `covidRdRp`: SARS-CoV-2 gene region RdRp
    -   `covidN1N2avg`: SARS-CoV-2 gene region average of N1 and N2
    -   `PMMoV`: pepper virus is being measured
    -   `crA`: crAssphage is being measured
    -   `wwParamFlow`: Flow rate of the waste water at point of sampling
    -   `wqParamTss`: Total Suspended solids
    -   `wqParamBod`: BOD or biological oxygen demand of the water
    -   `wqParamCod`: COD or chemical oxygen demand of the water
    -   `wqParamPh`: pH of the water sampled
    -   `catOther`: Other measurement category

-   **categoryOther**: Description for an other variable not listed in `category`.

-   **unit**: Unit of the measurement.

    -   `PMMoV`: Viral copies/copies PMMoV
    -   `ml`: Viral copies/mL
    -   `gms`: Viral copies/gm solids (dry weight)
    -   `l`: Viral copies/L
    -   `crA`: Viral copies/copies crAssphage
    -   `Ct`: Cycle threshold
    -   `m3s`: meters cubed per second
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

## Sample (Sample.csv) <span id="Sample"><span>

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

-   **samplingTempC**: Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples wich are either kept at ambient temperature or refrigerated while being sampled.

-   **mailedOnIce**: Was the sample kept cool while being sent to the lab? (Boolean)

-   **storageTempC**: Temperature that the sample is stored at in Celsius.

-   **qualityFlag**: Does the reporter suspect the sample having some quality issues? (Boolean)

-   **notes**: Any additional notes.

## Site (Site.csv) <span id="Site"><span>

The site of wastewater sampling, including several *defaults* that can be used to populate new samples upon creation.

-   **ID**: (Primary Key) Unique identifier for the location where wastewater sample was taken.

-   **name**: Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.

-   **description**: Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.

-   **reporter.ID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **type**: Type of site or institution where sample was taken.

    -   `airplane`: Airplane
    -   `correctionalFacility`: Federal or provincial correctional facility or jail
    -   `elementrarySchool`: Elementary school
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
    -   `lagoonEffluent`: Wastewater tretment lagoon effluent
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

## Reporter (Reporter.csv) <span id="Reporter"><span>

The individual or organization that is reporting and responsible for the quality of the data.

-   **ID**: (Primary Key) Unique identifier for the person or organization that is reporting the data.

-   **site.IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Site` table.

-   **lab.IDDefault**: (Foreign Key) Used as default when a new sample is created by this reporter. See `ID` in `Lab` table.

-   **contactName**: Full Name of the reporter, either an organization or individual.

-   **contactEmail**: Contact e-mail address.

-   **contactPhone**: Contact phone number.

-   **allowAcceesToSelf**: Default: True. If this is False the data will not be shown on the portal when the data provider logs in

-   **allowAccessToFederalPublicHealthAuthorities**: Default: True. If this is False the data will not be available to employees of PHAC

-   **allowAccessToLocalPublicHealthAuthorities**: Default: True. If this is False data will not be available when local health Authorities log in.

-   **allowAccessToProvincialPublicHealthAuthorities**: Default: True. If this is False data will not available when provincial health Authorities log in.

-   **allowAccessToOtherDataProviders**: Default: True. If this is False data will not be available when other data providers login.

-   **allowAccessToAllOrganizations**: Default: True. If this is False data will not be available when any partner organization logs into the system

-   **allowAccessToPublic**: Default: True. If this is False data will not be available to the public.

-   **allowAccessToSpec**: Details or specifics on confidentiality requirements.

-   **notes**: Any additional notes.

## Lab (Lab.csv) <span id="Lab"><span>

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

-   **ID**: (Primary key) Unique identifier for the laboratory.

-   **assay.IDDefault**: (Foreign key) Used as default when a new measurement is created for this lab. See `ID` in `AssayMethod` table.

-   **name**: Name corresponding to lab.

-   **contactName**: Contact person or group, for the lab.

-   **contactEmail**: Contact e-mail address, for the lab.

-   **contactPhone**: Contact phone number, for the lab.

-   **updateDate**: Date information was provided or updated.

## AssayMethod (AssayMethod.csv) <span id="AssayMethod"><span>

The assay method that was used to perform testing. This database will be developed in consultation with testing labs to identify key assay features that can affect SARS-CoV-2 results.

-   **ID**: (Primary key) Unique identifier for the assay method.

-   **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended.

-   **sampleSizeL**: Size of the sample that is analyzed in liters.

-   **loq**: Limit of quantification (LOQ) for this method if one exists.

-   **lod**: Limit of detection (LOD) for this method if one exists.

-   **units**: Units used by this method, that are applicable to the LOD and LOQ.

    -   `PMMoV`: Viral copies/copies PMMoV
    -   `ml`: Viral copies/mL
    -   `gms`: Viral copies/gm solids
    -   `l`: Viral copies/L
    -   `crA`: Viral copies/copies crAssphage
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

-   **description**: Description of the assay.

-   **date**: Date on which the assayMethod was created or updated (for version update).

-   **referenceLink**: Link to standard operating procedure (assay reference method)

## Polygon (Polygon.csv) <span id="Polygon"><span>

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

## CovidPublicHealthData (CovidPublicHealthData.csv) <span id="CovidPublicHealthData"><span>

Saves some information about covid-19 in a given polygon.

-   **ID**: (Primary key) Unique identifier for the table.

-   **Reporter.ID**: (Foreign key) ID of the reporter who gave this data.

-   **Polygon.ID**: (Foreign key) Links with the `Polygon` table.

-   **date**: Date of covid-19 measure.

-   **dateType**: Type of date used.

    -   `episodeDate` : Episode date is usually just the earliest of a list of dates available as not every case has every date
    -   `onsetDate`: Earliest that symptoms were reported for this case
    -   `reportedDate`: Date that the numbers were reported publicly

-   **valueType**: Type of date used.

    -   `confirmed`: Number of confirmed cases.
    -   `active`: Number of active cases.
    -   `tests`: Number of tests performed.
    -   `positiveTests`: Number of positive tests.
    -   `percentPositivityRate`: Percent positivity rate.
    -   `hospitalCensus`: Hospital census or the number of people admitted with covid-19.
    -   `hospitalAdmit`: Hospital admissions or patients newly admitted to hospital.

-   **value**: The numeric value that is being reported.

-   **notes**: Any additional notes.

## Lookups (Lookups.csv) <span id="Lookups"><span>

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


## Examples of how to generate wide and long variable and category names

### 1) Simple viral region report

A long table would represent a test viral measurement as:

    category = covidN1
    unit = PPMoV
    aggregation = Mean
    value = 42

A wide table would represent the same measurement as:

    measurement.covidN1_PPMV_mean = 42

### 2) Derived measure

To report a mean value of existing covidN1 and covidN2 measures:

    measureCat = covidN1
    measureUnit = ml
    measureType = mean
    measureValue = 42

    measureCat = covidN2
    measureUnit = ml
    measureType = mean
    measureValue = 40

Represent the derived measure as:

long table format

    measureCat = covidN1_covidN2
    measureUnit = ml
    measureType = mean
    measureValue = 41

or,

wide table format

    covidN1_covidN2_ml_mean = 41

-   Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMV:

Represent the derived measure as:

long table description

    covidN1_covidN2 = 2
    measureUnit = PPMV
    measureType = meanNormal

or,

wide table format

    covidN1_covidN2-PPMV-meanNormal = 2
