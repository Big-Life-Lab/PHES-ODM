# Metadata for files

There are three databases that are described below. Data is stored in [data](data). 

- [Wastewater sample results](#test_results) ([wastewater_covid-19.csv](data/wastewater_virus.csv))
- [Wastewater site information](#site) ([wastewater_site.csv](data/wastewater_site.csv)) 
- [Wastewater laboratory information](#lab) (wastewater_lab.csv - **TBA**)

For discussion: Is a database of assay information needed? Should assay methods be recorded and described, or does the site information suffice and remain unchanged?

Entity Relationship Diagram [here](#erd).

### File naming convention
- **date**: MM/DD/YYYY HH:mm:ss  (24 hour format, in UTC).
- **location** TBD

## SARS-CoV-2 test results (wastewater_covid-19.csv) <span id="test_results"><span>

Results for a single SARS-CoV-2 wastewater test.

- **sampleID**: Unique identification for sample. Suggest siteID-date-sample#. e.g. Ottawa1_2020-10-10-1 (Primary Key)
- **sampleDate**: Date wastewater sample collected. End date for continuous testing. Additional location information in `wastewater_site.csv`.
- **siteID**: Identifier for location where wastewater sample was taken. Additional location information in `wastewater_site.csv`.
- **genRegion**: Gene target region.
  - `N1`
  - `N2`
  - `N3`
  - `E`
  - `RdRp`
- **sampleUnit**: Unit of SARS-CoV-2 measurement.
  - `PMMoV`: Viral copies/copies PMMoV
  - `ml`:    Viral copies/mL
  - `gms`:   Viral copies/gm solids
  - `l`:     Viral copies/L
  - `crA`:   Viral copies/copies crAssphage
  - `other`: Other measurement of viral copies. Also add `sampleUnitOther`.
- **sampleUnitOther**: Description for other type of SARS-CoV-2 measurement unit. See `sampleUnit`.
- **sampleMean**: Sample mean Ct/Cq.
- **sampleVariance**: Sample variance Ct/Cq.
- **sampleMeanNormal**: Sample mean normalizing Ct/Cq.
- **sampleVarianceNormal**: Sample variance normalizing Ct/Cq.

## Site (wastewater_site.csv) <span id="site"><span>

Site of SARS-CoV-2 wastewater sampling, including how the sample was collected and stored. Each SARS-CoV-2 test result corresponds to one site.

- **siteID**:	Unique identifier for the location where wastewater sample was taken. `locationID` is the same in `wastewater_covid-19.csv`. (Primary Key)
- **siteName**:	Name corresponding to `siteID`. Location name could be a treatment plant, campus, institution or sewer location, etc. 
- **siteDescription**: Description of wastewater site (city, building, street, etc., to identify location sampled).
- **laboratoryID**: Unique identification of laboratory that is perform testing at the site.
- **siteType**: Type of sample collected at site. 
  - `sludge`: Primary clarified sludge
  - `rawCollector`: Raw wastewater (in collector system)
  - `rawPostGrit`: Raw wastewater (post-grit)
  - `other`: Other type of sample. Add description to `sampleTypeOther`.
- **methodCollection**: method of sample collection.
  - `24hq1h`: 24-hour composite, every 1 hr
  - `24hq4h`: 24-hour composite, every 4 hr
  - `24hq6h`: 24-hour composite, every 6 hr
  - `grab`:   Grab sample
  - `other`:  Other method collection type. Add description to `methodCollectOther`.
- **methodCollectOther**: Description of other type of method of sample collection. see `methodCollection`.
- **sampleFraction**: Faction of the sample that is analyzed.
  - `liquid`: Liquid fraction
  - `solid`:  Solid fraction
  - `mixed`:  Mixed/homogenized sample
- **geoLat**: Site geographical location, latitude in decimal coordinates, ie.: (45.424721)
- **geoLong**: Site geographical location, longitudein decimal coordinates, ie.: (-75.695000)
- **storageTemp**: Storage conditions/temperature of sample (degree Celcius).
- **contactName**: Person to contact about data collection at the site.
- **contactEmail**: Email addrss for `contactName`.
- **conatctPhone**: Phone number for `contactName`.
- **catchmentPop**: Approximate population size of catchment area corresponding to site. The number of people resprested in the wastewater sample.
- **notes**: Any addtional notes.

## Laboratory (wastewater_lab.csv) <span id="lab"><span>

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

- **laboratoryID**: Unique identifier for the laboratory. (Primary Key)
- **laboraotryName**: Name corresponding to `siteID`.
- **contactName**: Contact person or group.
- **contactEmail**: Contact e-mail address.
- **contactPhone**: Contact phone number.
- **date**: Date information was provided or updated.


## Entity Relationship Diagram <span id="erd"><span>

![](img/ERD.svg)

Comment on the ERD in [Lucidcharts](https://lucid.app/invitations/accept/781822fc-6ac5-4aa7-9023-323fd4b6b04f)

## Changelog

2020-10-18

- change `locationID` to `siteID`. 
- change `locationName` to `siteName`