

# Metadata

There are eight tables that are described below. example data is stored in [data](data). 

- [Measurement](#Measurement) ([Measurements.csv](data/Measurements.csv))
- [Sample](#Sample) ([Sample.csv](data/Sample.csv))
- [Site](#Site) ([Site.csv](data/Site.csv))
- [Reporter](#Reporter) ([Reporter.csv](data/Reporter.csv))
- [Lab](#Lab) ([Lab.csv](data/Lab.csv))
- [AssayMethod](#AssayMethod) (AssayMethod.csv - **TBA**)
- [Polygon ](#Polygon ) (Polygon.csv - **TBA**)
- [CovidPublicHealthData](#CovidPublicHealthData) (CovidPublicHealthData.csv - **TBA**)

Entity Relationship Diagram [here](#erd).

## Entity Relationship Diagram <span id="erd"><span>

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/023490f3-6cc5-41be-bc2d-d96425f3c68f/edit?page=0_0#?folder_id=home&browser=icon)


## Measurement (Measurement.csv) <span id="Measurement"><span>

Results for a measurement of a single property of SARS-CoV-2 wastewater test, for either a viral region or wastewater treatment plant. 

- **MeasurementID**: Unique identification for measurement (Primary Key).
- **sampleID**: Links with the identified sample  (foreign key).
- **labID**: Links with the identified Lab that performed the analysis (foreign key).
- **assayID**: Links with the AssayMethod table used to perform the analysis  (foreign key)
- **analysisDate**: Date the data was analysed in the lab.
- **reportDate**: Data the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the orginal `sampleID` but updated `measurementID`, `reportDate` and  `assayID` (if needed).
- **sampleFraction**: Faction of the sample that is analyzed.
  - `liquid`: Liquid fraction
  - `solid`:  Solid fraction
  - `mixed`:  Mixed/homogenized sample- 
- **measureCat**: Gene target region (`covid-`) or wastewater treatment plant parameter (`ww-param-`).
  - `covidUnspecified (default)`
  - `covidN1`
  - `covidN2`
  - `covidN3`
  - `covidE`
  - `covidRdRp`
  - `covidN1N2avg`
  - `wwParamFlow`
  - `wwParamTss`
  - `wwParamBod`
  - `catOther`
- **measureCatOther**: Description for other target region (use prefix `covid-` or wastewater treatment plant parameter (use prefix `ww-param-`.  See `measureCat`.
- **measureUnit**: Unit of SARS-CoV-2 measurement.
  - `PMMV`: Viral copies/copies PMMoV
  - `ml`:    Viral copies/mL
  - `gms`:   Viral copies/gm solids
  - `l`:     Viral copies/L
  - `crA`:   Viral copies/copies crAssphage
  -  `Ct`: 
  - `m3s`: meters cubed per second
  - `mgl`:  milligrams  per liter
  - `mgOl`: milligrams of oxygen per liter
  - `measureOther`: Other measurement of viral copies or wastewater treatment plant parameter. Also add `measureUnitOther`.
- **measureUnitOther**: Description for other type of SARS-CoV-2 measurement unit. See `measureUnit`.
- **measureType**: Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each measureType has a corresponding value (measureValue).
  - `mean`: Sample mean
  - `SD`: Sample standard deviation
  - `meanNormal`: Sample mean, normalized
  - `SDNormal`: Sample standard deviation, normalized
  - `typeOther`: Other measures
- **measureTypeOther**: Description for other type of measurement type. See `measurementUnit`.
- **measureValue**: Value of measureType. 

## Sample (Sample.csv) <span id="Sample"><span>

The sample is an amount of water taken from a site which is then analysed by a Lab

- **sampleID**: Unique identification for sample. Suggest siteID-date-sample, or siteID-. (Primary Key)
- **siteID**: links with the site table. (foreign key)
- **dateTime**: for grab samples this is the date and time and timezone the sample was taken.
- **dateTimeStart**: for integrated time average samples this is the date and time and timezone the sample was started being taken.
- **dateTimeEnd**: for integrated time average samples this is the date and time and timezone the sample was finished being taken.
- **sampleType**: type of sample.
  - `sludge`: Primary clarified sludge
  - `rawCollector`: Raw wastewater (in collector system)
  - `rawPostGrit`: Raw wastewater (post-grit)
  - `other`: Other type of site. Add description to `sampleTypeOther`.
- **sampleTypeOther**: Description for other type of sample type. See `sampleType`.
- **methodCollection**: method used to collect the data.
  - `grab sample`: Sample was a simple grab sample 
  - `contFlowProp`: Continuous flow proportional
  - `contConstant`: Continuous constant
  - `contOther`:  Continuous other
  - `discTimeProp`: Discrete time proportional
  - `discTimeProp24hq1h`: Discrete time proportional 24-hour composite, every 1 hr
  - `discTimeProp24hq4h`: Discrete time proportional 24-hour composite, every 4 hr
  - `discTimeProp24hq6h`: Discrete time proportional 24-hour composite, every 6 hr
  - `discFlowProp`: Discrete flow proportional
  - `discVolumeProp`: Discrete volume proportional
  - `discOther`: Discrete other
  - `integratedOther`: Integrated other
- **methodCollectionOther**: Description for other type of method when any option with `other` is selected `methodCollection`.
- **sampleSizeL**: total volume of water or sludge sampled
- **sampleStorageTempC**: temperature that the sample is stored at in Celsius.

## Site (Site.csv) <span id="Site"><span>

The site of wastewater sampling, including several *defaults* that can be used to populate new samples.

- **siteID**:	(Primary Key) Unique identifier for the location where wastewater sample was taken. 
- **siteName**:	Name corresponding to `siteID`. Location name could be a treatment plant, campus, institution or sewer location, etc.
- **siteDescription**: Description of wastewater site (city, building, street, etc., to identify location sampled).
- **reporterID**: links with the reporter that is responsible for the data (foreign key) 
- **siteType**: Type site where the sampling is taken. 
  - `SAPFlowWater`: Sewer access point flowing water
  - `SAPStandingWater`: Sewer access point standing water
  - `treatPlantInfluent`: Treatment plant influent
  - `treatPlantEffluent`: Treatment plant effluent
  -  `lagoon`: Lagoon
  -  `other`: Other
- **siteTypeOther**: Description of site where the site is other. See `siteType`
- **SampleTypeDefault**: used as default when new samples records are created see `SampleType` in `Sample` table
- **SampleTypeOtherDefault**: used as default when new `Sample` records are created see `SampleTypeOther` in `Sample` table- 
- **methodCollectionDefault**: used as default when new `Sample` records are created see `methodCollection` in `Sample` table
- **methodCollectOtherDefault**: used as default when new `Sample` records are created see `methodCollectionOther` in `Sample` table
- **sampleFractionDefault**: Used as the default when new `Measurement` records are created
- **sampleTempCdefault**: Used as the default when new `Sample` records are created
- **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)
- **geoLong**: Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)
- **notes**: Any additional notes.
- **sewerNetworkPolygonID**: Links with the Polygon table (foreign key) 
- **sewerNetworkFileLink**: Link to a file that has any detailed information about the sewer network associated with the site (any format)
- **sewerNetworkFileBLOB**: a file BLOB that has any detailed information about the sewer network associated with the site (any format)


## Reporter (Reporter.csv) <span id="Reporter"><span>

The individual or organization that is reporting and responsible for the quality of the data.

- **reporterID**:	(Primary Key) Unique identifier for the person or organization that is reporting the data
- **siteIDDefault**:	Used as the default when new `Sample` records are created by this `reporter`
- **labIDDefault**:	Used as the default when new `Sample` records are created by this `reporter`
 - **contactName**:	Full Name of the reporter, either an organization or individual
 - **contactEmail**: Contact e-mail address.
- **contactPhone**: Contact phone number.
- **confidentialRequirements**: how is this raw data allowed to be shared
  - `Public Access` : data can be shared freely and openly
  - `Internal Only` : shared internally 
  - `Internal and Partners`: shared internally and with partner organizations
  - `other`: specific sharing requirements 
- **confidentialRequirementsOther**: details or specifics on confidentiality


## Lab (Lab.csv) <span id="Lab"><span>

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

- **labID**: Unique identifier for the laboratory. (Primary Key)
- **assayIDDefault**: Unique identifier for the assay normally performed by this lab, use to populate new `measurement` records .(foreign key)
- **laboratoryName**: Name corresponding to lab.
- **contactName**: Contact person or group, for the lab.
- **contactEmail**: Contact e-mail address, for the lab.
- **contactPhone**: Contact phone number, for the lab.
- **labUpdateDate**: Date information was provided or updated.

## AssayMethod (AssayMethod.csv) <span id="AssayMethod"><span>

The assay method that was used to perform testing. This database will be developed in consultation with testing labs to identify key assay features that can affect SARS-CoV-2 results. 

- **assayID**: (Primary key) Unique identifier for the assay method
- **version**: Version of the assay. [Semantic versioning](https://semver.org) is recommended
- **assayDate**: Date the assayMethod was created or updated (for version update)
- **assayDesc**: Description of assay

## Polygon (Polygon.csv) <span id="Polygon"><span>

a simple polygon that encloses an are on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area

- **polygonID**: (Primary key) Unique identifier for the polygon 
- **polygonName**: Name of the polygon (eg G.E. Booth catchment area, Ottawa Health Region)
- **polygonPop**: Approximate population size of living inside a given polygon
- **polygonType**: Type of polygon
  - `sewerNetwork` : Sewer network
  - `healthRegion` : Health region served by the sewer network
- **polygonWKT** [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) of the polygon 
- **polygonFile** file for storing the polygon BLOB format
- **polygonLink** link to an external file that describes the geometry

## CovidPublicHealthData (CovidPublicHealthData.csv) <span id="CovidPublicHealthData"><span>

Saves some information about covid-19 in a given polygon

- **publicHealthID**: (Primary key) Unique identifier for the table 
- **PolygonID**:  links with the `Polygon` table (foreign key) 
- **date**: Date of covid-19 measure
- **confirmed**: Number of confirmed cases
- **active**:  Number of active cases
- **tests**:  Number of tests
- **positiveTests**: Number of positive tests
- **percentPositivityRate**:  Percent postivity rate
- **hospitalCensus**: Hospital census or the number of people admitted with covid-19
- **hospitalAdmit**: Hospital admissions or patients newly admitted to hospital
 
## File naming convention
- **variable and category names**: Both variables and variable categoties use camelCase with long tables. Wide tables use `_` to concatenate variables from long tables. 

A long table would represent a test sample as the following:
```
measureCat = covidN1
measureUnit = PPMoV
measureType = Mean
measureValue = 42
```

A wide table would represent the same sample as:
```
covidN1_PPMV_mean = 42
```

- **date**: MM/DD/YYYY HH:mm:ss  (24 hour format, in UTC)
- **location**: TBD
- **versions**: [Semantic versioning](https://semver.org)
