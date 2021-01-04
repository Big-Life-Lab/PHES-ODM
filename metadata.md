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

Results for a measurement of a single property of SARS-CoV-2 wastewater test, for either a viral region or wastewater treatment plant.

-   **uID**: (Primary key) Unique identification for measurement table.

-   **ID**: Unique identification for a given analysis, where analysis means you performed all steps needed to get the measurement, but measurements are not independent.

-   **sample.ID**: (Foreign key) Links with the identified sample.

-   **lab.ID**: (Foreign key) Links with the identified Lab that performed the analysis.

-   **assay.ID**: (Foreign key) Links with the AssayMethod table used to perform the analysis.

-   **analysisDate**: Date the data was analysed in the lab.

-   **reportDate**: Data the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original `sampleID` but updated `measurementID`, `reportDate` and `assayID` (if needed).

-   **fractionAnalysed**: Faction of the sample that is analyzed.

    -   `liquid`: Liquid fraction
    -   `solid`: Solid fraction
    -   `mixed`: Mixed/homogenized sample

-   **category**: Gene target region (`covid-`) or wastewater treatment plant parameter (`ww-param-`).

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
    -   `wwParamTss`: Total Suspended solids
    -   `wwParamBod`: BOD or biological oxygen demand of the water
    -   `wwParamCod`: COD or chemical oxygen demand of the water
    -   `wwParamPh`: pH of the water sampled
    -   `catOther`: Other measurement category

-   **categoryOther**: Description for other target region (use prefix `covid` or wastewater treatment plant parameter (use prefix `wwParam`. See `measureCat`.

-   **unit**: Unit of SARS-CoV-2 measurement.

    -   `PMMoV`: Viral copies/copies PMMoV
    -   `ml`: Viral copies/mL
    -   `gms`: Viral copies/gm solids
    -   `l`: Viral copies/L
    -   `crA`: Viral copies/copies crAssphage
    -   `m3s`: meters cubed per second
    -   `mgl`: milligrams per liter
    -   `mgOl`: milligrams of oxygen per liter
    -   `ph`: pH units (unitless)
    -   `bool`: unit is a pass fail value like if covid is detected or not, or sample is frozen or not.
    -   `other`: Other measurement of viral copies or wastewater treatment plant parameter. Also add `UnitOther`.

-   **unitOther**: Description for other type of SARS-CoV-2 measurement unit. See `measureUnit`.

-   **aggregation**: Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each aggregation has a corresponding value (Value).

    -   `geoMean`: GeoMean of results
    -   `single`: This value is not an aggregate measurement in any way, and thus is not a `mean`, `median`, `geomean` or other
    -   `mean`: Sample mean
    -   `meanNormal`: Sample mean, normalized
    -   `median`: Median of results
    -   `rangeLowestValue`: Lowest value in a range of values
    -   `rangeHighestValue`: Highest value in a range of values
    -   `SD`: Sample standard deviation
    -   `SDNormal`: Sample standard deviation, normalized
    -   `typeOther`: Other measures

-   **aggregationeOther**: Description for other type of measurement type. See `measurementUnit`.

-   **index**: Index if the measurement was taken multiple times (int)

-   **value**: Value of measureType.

-   **valueDetected**: Boolean Value if True then covid-19 was detected.

-   **qualityFlag**: Boolean Value if True if the measurement might have some quality control issue

-   **notes**: Any additional notes.

## Sample (Sample.csv) <span id="Sample"><span>

The sample is an amount of water taken from a site which is then analysed by a lab.

-   **sampleID**: (Primary Key) Unique identification for sample. Suggest siteID-date-sample, or siteID-.

-   **site.ID**: (Foreign key) Links with the site table.

-   **dateTime**: for grab samples this is the date and time and timezone the sample was taken.

-   **dateTimeStart**: for integrated time average samples this is the date and time and timezone the sample was started being taken.

-   **dateTimeEnd**: for integrated time average samples this is the date and time and timezone the sample was finished being taken.

-   **sampleType**: type of sample.

    -   `sludge`: Primary clarified sludge
    -   `rawCollector`: Raw wastewater (in collector system)
    -   `rawPostGrit`: Raw wastewater (post-grit)
    -   `other`: Other type of site. Add description to `sampleTypeOther`.

-   **sampleTypeOther**: Description for other type of sample type. See `sampleType`.

-   **methodCollection**: method used to collect the data.

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
    -   `integratedOther`: Integrated other

-   **methodCollectionOther**: Description for other type of method when any option with `other` is selected `methodCollection`.

-   **sampleSizeL**: Total volume of water or sludge sampled.

-   **sampleStorageTempC**: Temperature that the sample is stored at in Celsius.

-   **notes**: Any additional notes.

-   **site.ID**: (Foreign key) Links with the site table.

-   **dateTime**: For grab samples this is the date and time and timezone the sample was taken.

-   **dateTimeStart**: For integrated time average samples this is the date and time and timezone the sample was started being taken.

-   **dateTimeEnd**: For integrated time average samples this is the date and time and timezone the sample was finished being taken.

-   **type**: Type of sample.

    -   `sludge`: Primary clarified sludge
    -   `rawCollector`: Raw wastewater (in collector system)
    -   `rawPostGrit`: Raw wastewater (post-grit)
    -   `other`: Other type of site. Add description to `sampleTypeOther`.

-   **typeOther**: Description for other type of sample type. See `sampleType`.

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
    -   `integratedOther`: Integrated other

-   **collectionOther**: Description for other type of method when any option with `other` is selected `methodCollection`.

-   **collectionTriggerTime** Time between sub-samples for `discTimeProp` numeric value given in minutes

-   **preTreatment**: was the sample chemically treated in anyway with the addition of stabilizers or other (boolean)

    -   `True`
    -   `False`

-   **preTreatmentDescription**: Describe the treatment that was performed

-   **childID**: If this is a sample with many smaller samples either because of pooling or sub-sampling this indicates a coma seperated list of child samples.

-   **parentID** : If this sample has been pooled into one big sample for analysis this indicates the sampleID of the larger pooled sample

-   **sizeL**: Total volume of water or sludge sampled.

-   **storageTempC**: Temperature that the sample is stored at in Celsius.

-   **qualityFlag**: Boolean Value True if the sample might have some quality control issue

-   **notes**: Any additional notes.

## Site (Site.csv) <span id="Site"><span>

The site of wastewater sampling, including several *defaults* that can be used to populate new samples.

-   **ID**: (Primary Key) Unique identifier for the location where wastewater sample was taken.

-   **name**: Name corresponding to `siteID`. Location name could be a treatment plant, campus, institution or sewer location, etc.

-   **description**: Description of wastewater site (city, building, street, etc., to identify location sampled).

-   **reporter.ID**: (Foreign key) Links with the reporter that is responsible for the data.

-   **type**: Type of site or institution where sample was taken.

    -   `airplane`: Airplane
    -   `correctionalFacility`: Federal or provincial correctional facility or jail
    -   `elementraryScool`: Elementary school
    -   `lagoon`: Lagoon
    -   `longTermCareHome`: Long-term care home
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
    -   `buildingCleanout`: Building cleanout
    -   `propertyLineCleanout`: Property line cleanout

-   **accessTypeOther**: Description of access point where the access type is other is selected for `accessType`.

-   **sample.typeDefault**: Used as default when new samples records are created see `SampleType` in `Sample` table.

-   **sample.typeOtherDefault**: Used as default when new `Sample` records are created see `SampleTypeOther` in `Sample` table.

-   **sample.collectionDefault**: Used as default when new `Sample` records are created see `methodCollection` in `Sample` table.

-   **sample.collectOtherDefault**: Used as default when new `Sample` records are created see `methodCollectionOther` in `Sample` table.

-   **measurement.fractionAnalysedDefault**: Used as the default when new `Measurement` records are created.

-   **sample.tempCdefault**: Used as the default when new `Sample` records are created

-   **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)

-   **geoLong**: Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)

-   **notes**: Any additional notes.

-   **Polygon.ID**: (Foreign key) Links with the Polygon table, this should encumpase the area that typically drains into this site.

-   **sewerNetworkFileLink**: Link to a file that has any detailed information about the sewer network associated with the site (any format).

-   **sewerNetworkFileBLOB**: A file BLOB that has any detailed information about the sewer network associated with the site (any format).

## Reporter (Reporter.csv) <span id="Reporter"><span>

The individual or organization that is reporting and responsible for the quality of the data.

-   **ID**: (Primary Key) Unique identifier for the person or organization that is reporting the data.
-   **site.IDDefault**: (Foreign key) Used as the default when new `Sample` records are created by this `reporter`.
-   **lab.IDDefault**: (Foreign key) Used as the default when new `Sample` records are created by this `reporter`.
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
-   **assay.IDDefault**: (Foreign key) Unique identifier for the assay normally performed by this lab, use to populate new `measurement` records.
-   **laboratoryName**: Name corresponding to lab.
-   **contactName**: Contact person or group, for the lab.
-   **contactEmail**: Contact e-mail address, for the lab.
-   **contactPhone**: Contact phone number, for the lab.
-   **labUpdateDate**: Date information was provided or updated.

## AssayMethod (AssayMethod.csv) <span id="AssayMethod"><span>

The assay method that was used to perform testing. This database will be developed in consultation with testing labs to identify key assay features that can affect SARS-CoV-2 results.

-   **ID**: (Primary key) Unique identifier for the assay method.

-   **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended.

-   **sampleSizeL**: Size of the sample that is analysed in liters.

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
    -   `measureOther`: Other measurement of viral copies or wastewater treatment plant parameter. Also add `measureUnitOther`.

-   **unitsOther**: Units used by this method, that are applicable to the LOD and LOQ.
-   **concentrationMethod**: Description of the method used to concentrate the sample
-   **extractionMethod**: Description of the method used to extract the sample
-   **pcrMethod**: Description of the PCR method used
-   **qualityAssuranceQC** : Description of the quality control steps taken
-   **inhibition**: Description of the inhibition parameters.
-   **surrogateRecovery**: Description of the surrogate recovery for this method.
-   **assayDesc**: Description of the assay.
-   **assayDate**: Date on which the assayMethod was created or updated (for version update).

## Polygon (Polygon.csv) <span id="Polygon"><span>

A simple polygon that encloses an are on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area.

-   **ID**: (Primary key) Unique identifier for the polygon.
-   **name**: Name of the polygon (e.g. G.E. Booth catchment area, Ottawa Health Region).
-   **pop**: Approximate population size of living inside a given polygon.
-   **type**: Type of polygon

    -   `sewerNetwork` : Sewer network
    -   `healthRegion` : Health region served by the sewer network

-   **wkt** [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) of the polygon
-   **file** File for storing the polygon BLOB format.
-   **link** Link to an external file that describes the geometry.

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

    -   `confirmed` : Number of confirmed cases.
    -   `active`:Number of active cases.
    -   `tests`:Number Number of tests.
    -   `positiveTests`: Number of positive tests.
    -   `percentPositivityRate` Percent positivity rate.
    -   `hospitalCensus` Hospital census or the number of people admitted with covid-19.
    -   `hospitalAdmit` Hospital admissions or patients newly admitted to hospital.

-   **Value**:numeric

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


## Examples of how to generate wide and long variable and cateogory names

### 1) Simple viral region report

A long table would represent a test viral measurement as:

    category = covidN1
    unit = PPMoV
    aggregation = Mean
    value = 42

A wide table would represent the same measurement as:

    measurment.covidN1_PPMV_mean = 42

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

wide table fromat

    covidN1_covidN2-PPMV-meanNormal = 2
