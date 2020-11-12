

# Metadata for files

There are eight tables that are described below. example data is stored in [data](data). 

- [Measurement](#Measurement) ([Measurements.csv](data/Measurements.csv))
- [Sample](#Sample) ([Sample.csv](data/Sample.csv))
- [Site](#Site) ([Site.csv](data/Site.csv))
- [Reporter](#Reporter) ([Reporter.csv](data/Reporter.csv))
- [Lab](#Lab) ([Lab.csv](data/Lab.csv))
- [AssayMethod](#AssayMethod) (AssayMethod.csv = **TBA**)
- [Polygon ](#Polygon ) (Polygon .csv - **TBA**)
- [CovidPublicHealthData](#CovidPublicHealthData) (CovidPublicHealthData.csv - **TBA**)

Entity Relationship Diagram [here](#erd).


## Entity Relationship Diagram <span id="erd"><span>

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/lucidchart/023490f3-6cc5-41be-bc2d-d96425f3c68f/edit?page=0_0#?folder_id=home&browser=icon)





## Measurement (Measurement.csv) <span id="Measurement"><span>

Results for a measurement of a single property of SARS-CoV-2 wastewater test, for either a viral region or wastewater treatment plant. 

- **MeasurementID**: Unique identification for measurement (Primary Key)
- **sampleID**: links with the identified sample  (foreign key)
- **labID**: links with the identified Lab that performed the analysis (foreign key)
- **assayID**: links with the AssayMethod table used to perform the analysis  (foreign key)
- **analysisDate**: Date the data was analysed in the lab
- **sampleFraction**: Faction of the sample that is analyzed.
  - `liquid`: Liquid fraction
  - `solid`:  Solid fraction
  - `mixed`:  Mixed/homogenized sample- 
- **measureCat**: Gene target region (`covid-`) or wastewater treatment plant parameter (`ww-param-`)
  - `covid-unspecified (default)`
  - `covid-N1`
  - `covid-N2`
  - `covid-N3`
  - `covid-E`
  - `covid-RdRp`
  - `covid-N1N2avg`
  - `ww-param-flow`
  - `ww-param-tss`
  - `ww-param-bod`
  - `catOther`
- **measureCatOther**: Description for other target region (use prefix `covid-` or wastewater treatment plant parameter (use prefix `ww-param-`.  See `measureCat`.
- **measureUnit**: Unit of SARS-CoV-2 measurement.
  - `PMMoV`: Viral copies/copies PMMoV
  - `ml`:    Viral copies/mL
  - `gms`:   Viral copies/gm solids
  - `l`:     Viral copies/L
  - `crA`:   Viral copies/copies crAssphage
  - `m3_s`: meters cubed per second
  - `mg_l`:  milligrams  per liter
  - `mgO_l`: milligrams of oxygen per liter
  - `measureOther`: Other measurement of viral copies or wastewater treatment plant parameter. Also add `measureUnitOther`.
- **measureUnitOther**: Description for other type of SARS-CoV-2 measurement unit. See `measureUnit`.
- **measureType**: Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each measureType has a corresponding value (measureValue).
  - `sampleMean`: Sample mean
  - `sampleSD`: Sample standard deviation
  - `sampleMeanNormal`: Sample mean, normalized
  - `sampleSDNormal`: Sample standard deviation, normalized
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
  - `grab sample`: sample was a simple grab sample 
  - `continous-flow-proportional`:
  - `continous-constant`:
  - `continous-other`:  
  - `discrete-time-proportional`:
  - `discrete-time-proportional-24hq1h`: 24-hour composite, every 1 hr
  - `discrete-time-proportional-24hq4h`: 24-hour composite, every 4 hr
  - `discrete-time-proportional-24hq6h`: 24-hour composite, every 6 hr
  - `discrete-flow-proportional`:
  - `discrete-volume-propotional`:
  - `discrete-other`:  
  - `integrated-other`:  
- **methodCollectionOther**: Description for other type of method when any option with `other` is selected `methodCollection`.
- **sampleSize_L**: total volume of water or sludge sampled
- **sampleStorageTemp_C**: temperature that the sample is stored at in Celcius.

## Site (Site.csv) <span id="Site"><span>

The site of wastewater sampling, including several *defaults* that can be used to populate new samples.

- **siteID**:	(Primary Key) Unique identifier for the location where wastewater sample was taken. 
- **siteName**:	Name corresponding to `siteID`. Location name could be a treatment plant, campus, institution or sewer location, etc.
- **siteDescription**: Description of wastewater site (city, building, street, etc., to identify location sampled).
- **reporterID**: links with the reporter that is responsible for the data (foreign key) 
- **siteType**: Type site where the sampling is taken. 
  - `sewer access point - flowing water`
  - `sewer access point - standing water`
  - `treatment plant - influent`
  - `treatment plant - effluent`
  -  `lagoon`
  -  `other`
- **siteTypeOther**: Description of site where the site is other. See `siteType`
- **SampleType_default**: used as default when new samples records are created see `SampleType` in `Sample` table
- **SampleTypeOther_default**: used as default when new `Sample` records are created see `SampleTypeOther` in `Sample` table- 
- **methodCollection_default**: used as default when new `Sample` records are created see `methodCollection` in `Sample` table
- **methodCollectOther_default**: used as default when new `Sample` records are created see `methodCollectionOther` in `Sample` table
- **sampleFraction_default**: Used as the default when new `Measurement` records are created
- **sampleTemp_C_default**: Used as the default when new `Sample` records are created
- **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)
- **geoLong**: Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)
- **notes**: Any additional notes.
- **sewerNetworkPolygonID**: Links with the Polygon table (foreign key) 
- **sewerNetworkFileLink**: Link to a file that has any detailed information about the sewer network associated with the site (any format)
- **sewerNetworkFileBLOB**: a file BLOB that has any detailed information about the sewer network associated with the site (any format)



## Reporter (Reporter.csv) <span id="Reporter"><span>

The individual or organization that is reporting and responsible for the quality of the data.

- **reporterID**:	(Primary Key) Unique identifier for the person or organization that is reporting the data
- **siteID_default**:	Used as the default when new `Sample` records are created by this `reporter`
- **labID_default**:	Used as the default when new `Sample` records are created by this `reporter`
 - **contactName**:	Full Name of the reporter, either an organization or individual
 - **contactEmail**: Contact e-mail address.
- **contactPhone**: Contact phone number.
- **confidentialRequirements**: how is this raw data allowed to be shared
  - `Public Access` : data can be shared freely and openly
  - `Internal Only` : shared internally 
  - `Internal and Partners`: shared internally and with partner organizations
  - `other`: specific sharing requirements 
- **confidentialRequirementsOther**: details or specifics on confidentiality



## Lab(Lab.csv) <span id="Lab"><span>

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

- **labID**: Unique identifier for the laboratory. (Primary Key)
- **assayID_default**: Unique identifier for the assay normally performed by this lab, use to populate new `measurement` records .(foreign key)
- **laboraotryName**: Name corresponding to lab.
- **contactName**: Contact person or group, for the lab.
- **contactEmail**: Contact e-mail address, for the lab.
- **contactPhone**: Contact phone number, for the lab.
- **labUpdateDate**: Date information was provided or updated.

## AssayMethod(AssayMethod.csv) <span id="AssayMethod"><span>

The assay method that was used to perform testing. This database will be developed in consultation with testing labs to identify key assay features that can affect SARS-CoV-2 results. 

- **assayID** (Primary key) Unique identifier for the assay method
- **version** Version of the assay. [Semantic versioning](https://semver.org) is recommended
- **assayDate** Date the assayMethod was created or updated (for version update)
- **assayDesc** Description of assay

## Polygon (Polygon .csv) <span id="Polygon"><span>

a simple polygon that encloses an are on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area

- **polygonID** (Primary key) Unique identifier for the polygon 
- **polygonName** Name of the polygon (eg G.E. Booth catchment area, Ottawa Health Region)
- **polygonPop** Approximate population size of living inside a given polygon
- **polygonType** type of polygon
  - `sewer network` : 
  - `Health Region` : 
- **polygonWKT** [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) of the polygon 
- **polygonFile** file for storing the polygon BLOB format
- **polygonLink** link to an external file that describes the geometry

## CovidPublicHealthData(CovidPublicHealthData.csv) <span id="CovidPublicHealthData"><span>

Saves some information about Covid in a given polygon

- **publicHealthID**: (Primary key) Unique identifier for the table 
- **PolygonID**:  links with the `Polygon` table (foreign key) 
- **date**: date that data is taken
- **numberOfNewCases**: 
- **numberOfActiveCases**: 
- **numberOfTests**:  
- **numberOfPositiveTests**:  
- **percentPositivityRate**:  
 


