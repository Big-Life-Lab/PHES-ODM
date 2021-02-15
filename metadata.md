<!-- metadata.md is generated from metadata_template.md Please edit metadata_template.md file -->

# Metadata

There are eight tables that are described below. example data is stored in [data](data).

-	[Sample](#Sample)
-	[WWMeasure](#WWMeasure)
-	[Site](#Site)
-	[SiteMeasure](#SiteMeasure)
-	[Reporter](#Reporter)
-	[Lab](#Lab)
-	[AssayMethod](#AssayMethod)
-	[Instrument](#Instrument)
-	[Polygon](#Polygon)
-	[CovidPublicHealthData](#CovidPublicHealthData)
-	[Lookup](#Lookup)

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

The sample is a representative volume of wastewater taken from a Site which is then analysed by a lab.

-	**sampleID**: (Primary Key) [string] Unique identification for sample. Suggestion:siteID-date-index.


-	**siteID**: (Foreign key) [string] Links with the Site table to describe the location of sampling.


-	**dateTime**: [datetime] for grab samples this is the date, time and timezone the sample was taken.


-	**dateTimeStart**: [datetime] For integrated time averaged samples this is the date, time and timezone the sample was started being taken.


-	**dateTimeEnd**: [datetime] For integrated time average samples this is the date, time and timezone the sample was finished being taken.


-	**type**: [category] Type of sample.
	-	`rawWW`: Raw wastewater.
	-	`swrSed`: Sediments obtained in sewer.
	-	`pstGrit`: Raw wastewater after a treatment plant's headworks.
	-	`pSludge`: Sludge produced by primary clarifiers.
	-	`pEfflu`: Effluent obtained after primary clarifiers.
	-	`sSludge`: Sludge produced by secondary clarifiers.
	-	`sEfflu`: Effluent obtained after secondary clarifiers.
	-	`water`: Non-wastewater, coming from any kind of water body.
	-	`faeces`: Fecal matter.
	-	`other`: Other type of site. Add description to typeOther.

-	**typeOther**: [string] Description for other type of sample not listed in


-	**collection**: [category] Method used to collect the data.
	-	`cpTP24h`: A time proportional 24-hour composite sample generally collected by an autosampler.
	-	`cpFP24h`: A flow proportional 24-hour composite sample generally collected by an autosampler.
	-	`grb`: A single large representative grab sample.
	-	`grbCp8h`: A 8-hour composite with 8 grab samples each taken once per hour, generally manually performed.
	-	`grbCp3h`: A 3-hour composite with 3 grab samples each taken once per hour, generally manually performed.
	-	`grbCp3`: A grab-composite sample composed of 3 separate grab samples.
	-	`mooreSw`: Moore swab passive sample.
	-	`other`: Other type of collection method. Add description to collectionOther.

-	**collectionOther**: [string] Description for other type of method not listed in collection.


-	**preTreatment**: [boolean] Was the sample chemically treated in anyway with the addition of stabilizers or other


-	**preTreatmentDescription**: [string] If preTreatment then describe the treatment that was performed.


-	**pooled**: [boolean] Is this a pooled sample, and therefore composed of multiple child samples obtained at different sites


-	**children**: [string] If this is a sample with many smaller samples either because of pooling or sub-sampling this indicates a comma separated list of child sampleID's.


-	**parent**: [string] If this sample has been pooled into one big sample for analysis this indicates the sampleID of the larger pooled sample.


-	**sizeL**: [float] Total volume of water or sludge sampled.


-	**fieldSampleTempC**: [float] Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples which are either kept at ambient temperature or refrigerated while being sampled.


-	**shippedOnIce**: [boolean] Was the sample kept cool while being shipped to the lab


-	**storageTempC**: [float] Temperature that the sample is stored at in Celsius.


-	**qualityFlag**: [boolean] Does the reporter suspect the sample having some quality issues


-	**notes**: [string] Any additional notes.

## WWMeasure

Measurement result (ie. single variable) from a wastewater sample. WWMeaasure includes data that is commonly collected by staff at wastewater laboratories where measurement is performed using an assay method (see AssayMethod), but can also be performed using specific instruments (see Instruments. Measures performed at the site of the wastewater sample are reported in SiteMeasure.

-	**uWwMeasureID**: (Primary Key) [string] Unique identifier a measurement within the measurement table.


-	**wwMeasureID**: [string] Unique identifier for wide table only. Use when all measures are performed on a single sample at the same time and same laboratory. Suggestion: siteID_sampleID_LabID_reportDate_ID.


-	**sampleID**: (Foreign key) [string] Links with the identified Sample


-	**labID**: (Foreign key) [string] Links with the identified Lab that performed the analysis.


-	**assayID**: (Foreign key) [string] Links with the AssayMethod used to perform the analysis. Use instrument.ID for measures that are not viral measures.


-	**instrumentID**: (Foreign key) [string] Links with the Instrument used to perform the analysis. Use assay.ID for viral measures.


-	**reporterID**: (Foreign key) [string] Links with the reporter that is responsible for the data.


-	**analysisDate**: [date] date the measurement was performed in the lab.


-	**reportDate**: [date] date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original sampleID but updated MeasureID, reportDate and assayID (if needed).


-	**fractionAnalyzed**: [category] Faction of the sample that is analyzed.
	-	`liquid`: Liquid fraction
	-	`solid`: Solid fraction
	-	`mixed`: Mixed/homogenized sample

-	**type**: [category] The variable that is being measured on the sample, e.g. a SARS-CoV-2 gene target region (cov), a biomarker for normalisation (n) or a water quality parameter (wq).
	-	`covN1`: SARS-CoV-2 nucleocapsid gene N1
	-	`covN2`: SARS-CoV-2 nucleocapsid gene N2
	-	`covN3`: SARS-like coronaviruses nucleocapsid gene N3
	-	`covE`: SARS-CoV-2 gene region E
	-	`covRdRp`: SARS-CoV-2 gene region RdRp
	-	`nPMMoV`: Pepper mild mottle virus
	-	`ncrA`: cross-assembly phage
	-	`nbrsv`: bovine respiratory syncytial virus
	-	`wqTS`: Total solids concentration.
	-	`wqTSS`: Total suspended solids concentration.
	-	`wqVSS`: Volatile suspended solids concentration.
	-	`wqCOD`: Chemical oxygen demand.
	-	`wqOPhos`: Ortho-phosphate concentration.
	-	`wqNH4N`: Ammonium nitrogen concentration, as N.
	-	`wqTN`: Total nitrogen concentration, as N.
	-	`wqPh`: pH
	-	`wqCond`: Conductivity
	-	`other`: Other measurement category. Add description to categoryOther.

-	**typeOther**: [string] Description for an other variable not listed in category.


-	**unit**: [category] Unit of the measurement.
	-	`gcPMMoV`: Gene copies per copy of PMMoV.
	-	`gcMl`: Gene copies per milliliter.
	-	`gcGs`: Gene copies per gram solids.
	-	`gcL`: Gene copies per liter.
	-	`gcCrA`: Gene copies per copy of crAssphage.
	-	`Ct`: Cycle threshold.
	-	`mgL`: Milligrams per liter.
	-	`ph`: pH units
	-	`uScm`: Micro-siemens per centimeter.
	-	`pp`: Percent positive, for Moore swab.
	-	`pps`: Percent primary sludge, for total solids.
	-	`other`: Other measurement of viral copies or wastewater treatment plant parameter. Add description to UnitOther.

-	**unitOther**: [string] Description for other measurement unit not listed in unit.


-	**aggregation**: [category] Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each aggregation has a corresponding value.
	-	`single`: This value is not an aggregate measurement in any way (ie. not a mean, median, max or any other) and can be a replicate value.
	-	`mean`: Arithmetic mean
	-	`meanNr`: Arithmetic mean, normalized
	-	`geoMn`: Geometric mean
	-	`geoMnNr`: Geometric mean, normalized
	-	`median`: Median
	-	`min`: Lowest value in a range of values
	-	`max`: Highest value in a range of values
	-	`sd`: Standard deviation
	-	`sdNr`: Standard deviation, normalized
	-	`other`: Other aggregation method. Add description to aggregationOther

-	**aggregationOther**: [string] Description for other type of aggregation not listed in aggregation.


-	**index**: [integer] Index number in case the measurement was taken multiple times.


-	**value**: [float] The actual measurement value that was obtained through analysis.


-	**qualityFlag**: [boolean] Does the reporter suspect the measurement having some quality issues


-	**accessToPublic**: [boolean] If this is 'no', this data will not be available to the public. If missing, data will be available to the public.


-	**accessToAllOrg**: [boolean] If this is 'no', this data will not be available to any partner organization. If missing, data will be available to the all organizations.


-	**accessToSelf**: [boolean] If this is 'no', this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.


-	**accessToPHAC**: [boolean] If this is 'no', the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.


-	**accessToLocalHA**: [boolean] If this is 'no', the, data will not be available to local health authorities. If missing, data will be available to local health authorities.


-	**accessToProvHA**: [boolean] If this is 'no', this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.


-	**accessToOtherProv**: [boolean] If this is 'no', this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before


-	**accessToDetails**: [boolean] More details on the existing confidentiality requirements of this measurement.


-	**notes**: [string] Any additional notes.

## Site

The site of wastewater sampling, including several defaults that can be used to populate new samples upon creation.

-	**siteID**: (Primary Key) [string] Unique identifier for the location where wastewater sample was taken.


-	**name**: [string] Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.


-	**description**: [string] Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.


-	**type**: [category] Type of site or institution where sample was taken.
	-	`airPln`: Airplane.
	-	`corFcil`: Correctional facility.
	-	`school`: School
	-	`hosptl`: Hospital
	-	`ltcf`: Long-term care facility.
	-	`swgTrck`: Sewage truck.
	-	`uCampus`: University campus.
	-	`mSwrPpl`: Major sewer pipeline.
	-	`pStat`: Pumping station.
	-	`holdTnk`: Hold tank.
	-	`retPond`: Retention pond.
	-	`wwtpMuC`: Municipal wastewater treatment plant for combined sewage.
	-	`wwtpMuS`: Municipal wastewater treatment plant for sanitary sewage only.
	-	`wwtpInd`: Industrial wastewater treatment plant.
	-	`lagoon`: Logoon system for extensive wastewater treatment.
	-	`septTnk`: Septic tank.
	-	`river`: River, natural water body.
	-	`lake`: Lake, natural water body.
	-	`estuary`: Estuary, natural water body
	-	`sea`: Sea, natural water body.
	-	`ocean`: Ocean, natural water body.
	-	`other`: Other site type. Add description to typeOther.

-	**typeOther**: [string] Description of the site when the site is not listed. See siteType.


-	**SampleTypeDefault**: [category] Used as default when a new sample is created for this site. See type in Sample table.
	-	`rawWW`: Raw wastewater.
	-	`swrSed`: Sediments obtained in sewer.
	-	`pstGrit`: Raw wastewater after a treatment plant's headworks.
	-	`pSludge`: Sludge produced by primary clarifiers.
	-	`pEfflu`: Effluent obtained after primary clarifiers.
	-	`sSludge`: Sludge produced by secondary clarifiers.
	-	`sEfflu`: Effluent obtained after secondary clarifiers.
	-	`water`: Non-wastewater, coming from any kind of water body.
	-	`faeces`: Fecal matter.
	-	`other`: Other type of site. Add description to typeOther.

-	**SampleTypeOtherDefault**: [string] Used as default when a new sample is created for this site. See typeOther in Sample table.


-	**SampleCollectionDefault**: [category] Used as default when a new sample is created for this site. See collection in Sample table.
	-	`cpTP24h`: A time proportional 24-hour composite sample generally collected by an autosampler.
	-	`cpFP24h`: A flow proportional 24-hour composite sample generally collected by an autosampler.
	-	`grb`: A single large representative grab sample.
	-	`grbCp8h`: An 8-hour composite with 8 grab samples each taken once per hour, generally manually performed.
	-	`grbCp3h`: A 3-hour composite with 3 grab samples each taken once per hour, generally manually performed.
	-	`grbCp3`: A grab-composite sample composed of 3 separate grab samples.
	-	`mooreSw`: Moore swab passive sample.
	-	`other`: Other type of collection method. Add description to collectionOther.

-	**SampleCollectOtherDefault**: [string] Used as default when a new sample is created for this site. See collectionOther in Sample table.


-	**SampleStorageTempCDefault**: [float] Used as default when a new sample is created for this site. See storageTempC in Sample table.


-	**MeasureFractionAnalyzedDefault**: [category] Used as default when a new measurement is created for this site. See fractionAnalyzed in Measurement table.
	-	`liquid`: Liquid fraction
	-	`solid`: Solid fraction
	-	`mixed`: Mixed/homogenized sample

-	**geoLat**: [float] Site geographical location, latitude in decimal coordinates, ie.: (45.424721)


-	**geoLong**: [float] Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)


-	**notes**: [string] Any additional notes.


-	**polygonID**: (Foreign key) [string] Links with the Polygon table, this should encompass the area that typically drains into this site.


-	**sewerNetworkFileLink**: [string] Link to a file that has any detailed information about the sewer network associated with the site (any format).


-	**sewerNetworkFileBLOB**: [blob] A file blob that has any detailed information about the sewer network associated with the site (any format).

## SiteMeasure

Measurement result (ie. single variable) obtained by at the site of wastewater sample.SiteMeasure includes data that is commonly collected by staff at wastewater treatment facilities and field sample locations. These measures that are not performed on the wastewater sample but provide additional context necessary for the interpretation of the results. Measures performed on the wastewater sample are reported in WWMeasure.

-	**uSiteMeasureID**: (Primary Key) [string] Unique identifier for each measurement for a site.


-	**siteMeasureID**: [string] Unique identifier for wide table only. Use when all measures are performed on a single sample.


-	**siteID**: (Foreign key) [string] Links with the Site table to describe the location of measurement.


-	**instrumentID**: (Foreign key) [string] Links with the Instrument table to describe instrument used for the measurement.


-	**reporterID**: (Foreign key) [string] Links with the reporter that is responsible for the data.


-	**dateTime**: [date] The date and time the measurement was performed.


-	**type**: [category] The type of measurement that was performed. The prefix env is used for environmental variables, whereas ww indicates a measurement on wastewater.
	-	`envTemp`: Environmental temperature.
	-	`envRnF`: Rain fall, i.e. amount of precipitation in the form of rain.
	-	`envSnwF`: Snow fall, i.e. amount of precipitation in the form of snow.
	-	`envSnwD`: Total depth of snow on the ground.
	-	`wwFlow`: Flow of wastewater.
	-	`wwTemp`: Temperature of the wastewater.
	-	`wwTSS`: Total suspended solids concentration of the wastewater.
	-	`wwCOD`: Chemical oxygen demand of the wastewater.
	-	`wwTurb`: Turbidity of the wastewater.
	-	`wwOPhos`: Ortho-phosphate concentration.
	-	`wwNH4N`: Ammonium nitrogen concentration, as N.
	-	`wwTN`: Total nitrogen concentration, as N.
	-	`wwpH`: pH of the wastewater.
	-	`wwCond`: Conductivity of the wastewater.

-	**typeOther**: [string] Description of the measurement in case it is not listed in type.


-	**typeDescription**: [string] Additional information on the performed measurement.


-	**aggregation**: [category] When reporting an aggregate measurement, this field describes the method used.
	-	`single`: This value is not an aggregate measurement in any way (ie. not a mean, median, max or any other) and can be a replicate value.
	-	`mean`: Arithmetic mean
	-	`meanNr`: Arithmetic mean, normalized
	-	`geoMn`: Geometric mean
	-	`geoMnNr`: Geometric mean, normalized
	-	`median`: Median
	-	`min`: Lowest value in a range of values
	-	`max`: Highest value in a range of values
	-	`sd`: Standard deviation
	-	`sdNr`: Standard deviation, normalized
	-	`other`: Other aggregation method. Add description to aggregationOther

-	**aggregationOther**: [string] Description for other type of aggregation not listed in aggregation.


-	**aggregationDesc**: [string] Information on OR reference to which measurements that were included to calculate the aggregated measurement that is being reported.


-	**value**: [float] The actual value that is being reported for this measurement.


-	**unit**: [string] The engineering unit of the measurement.


-	**qualityFlag**: [boolean] Does the reporter suspect quality issues with the value of this measurement


-	**accessToPublic**: [boolean] If this is 'no', this data will not be available to the public. If missing, data will be available to the public.


-	**accessToAllOrgs**: [boolean] If this is 'no', this data will not be available to any partner organization. If missing, data will be available to the all organizations.


-	**accessToSelf**: [boolean] If this is 'no', this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.


-	**accessToPHAC**: [boolean] If this is 'no', the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.


-	**accessToLocalHA**: [boolean] If this is 'no', data will not be available to local health authorities. If missing, data will be available to local health authorities.


-	**accessToProvHA**: [boolean] If this is 'no', this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.


-	**accessToOtherProv**: [boolean] If this is 'no', this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before.


-	**accessToDetails**: [boolean] More details on the existing confidentiality requirements of this measurement.


-	**notes**: [string] Any additional notes.

## Reporter

The individual or organization that is reporting and responsible for the quality of the data.

-	**reporterID**: (Primary Key) [string] Unique identifier for the person or organization that is reporting the data.


-	**siteIDDefault**: (Foreign key) [string] Used as default when a new sample is created by this reporter. See ID in Site table.


-	**labIDDefault**: (Foreign key) [string] Used as default when a new sample is created by this reporter. See ID in Lab table.


-	**contactName**: [string] Full Name of the reporter, either an organization or individual.


-	**contactEmail**: [string] Contact e-mail address.


-	**contactPhone**: [string] Contact phone number.


-	**notes**: [string] Any additional notes.

## Lab

Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.

-	**labID**: (Primary Key) [string] Unique identifier for the laboratory.


-	**assayMethodIDDefault**: (Foreign key) [string] Used as default when a new measurement is created for this lab. See ID in AssayMethod table.


-	**name**: [string] Name corresponding to lab.


-	**contactName**: [string] Contact person or group, for the lab.


-	**contactEmail**: [string] Contact e-mail address, for the lab.


-	**contactPhone**: [string] Contact phone number, for the lab.


-	**updateDate**: [date] date information was provided or updated.

## AssayMethod

The assay method that was used to perform testing. Create a new record if there are changes (improvements) to an existing assay method. Keep the same ID and use an updated version. A new record for a new version can include only the fields that changed, however, we recommend duplicating existing fields to allow each record to clearly describe all steps. Add a current date when recording a new version to an assay.

-	**assayMethodID**: (Primary Key) [string] Unique identifier for the assay method.


-	**instrumentID**: (Foreign key) [string] Links with the Instrument table to describe instruments used for the measurement.


-	**name**: [string] Name of the assay method.


-	**version**: [string] Version of the assay. Semantic versioning is recommended.


-	**summary**: [string] Short description of the assay and how it is different from the other assay methods.


-	**referenceLink**: [string] Link to standard operating procedure.


-	**date**: [date] date on which the assayMethod was created or updated (for version update).


-	**aliasID**: [string] ID of an assay that is the same or similar. a comma separated list.


-	**sampleSizeL**: [float] Size of the sample that is analyzed in liters.


-	**loq**: [float] Limit of quantification (LOQ) for this method if one exists.


-	**lod**: [float] Limit of detection (LOD) for this method if one exists.


-	**unit**: [category] Unit used by this method, and applicable to the LOD and LOQ.
	-	`gcPMMoV`: Gene copies per copy of PMMoV.
	-	`gcMl`: Gene copies per milliliter.
	-	`gcGms`: Gene copies per gram solids.
	-	`gcL`: Gene copies per liter.
	-	`gcCrA`: Gene copies per copy of crAssphage.
	-	`other`: Other measurement of viral copies. Add description to unitOther.

-	**unitOther**: [string] Unit used by this method, that are applicable to the LOD and LOQ.


-	**methodConc**: [string] Description of the method used to concentrate the sample


-	**methodExtract**: [string] Description of the method used to extract the sample


-	**methodPcr**: [string] Description of the PCR method used


-	**qualityAssQC**: [string] Description of the quality control steps taken


-	**inhibition**: [string] Description of the inhibition parameters.


-	**surrogateRecovery**: [string] Description of the surrogate recovery for this method.

## Instrument

Instruments that are used for measures in WWMeasure and SiteMeasure. The assay method for viral measurement are described in AssayMethod.

-	**instrumentID**: (Primary Key) [string] Unique identifier for the assay method.


-	**name**: [string] Name of the instrument used to perform the measurement.


-	**model**: [string] Model number or version of the instrument.


-	**description**: [string] Description of the instrument.


-	**alias**: [string] ID of an assay that is the same or similar. A comma separated list.


-	**referenceLink**: [string] Link to reference for the instrument.


-	**type**: [category] Type of instrument used to perform the measurement.
	-	`online`: An online sensor
	-	`lab`: Offline laboratory analysis
	-	`hand`: A handheld measurement analyzer.
	-	`atline`: An atline analyzer with sampler.
	-	`other`: An other type of measurement instrument. Add description to instrumentTypeOther.

-	**typeOther**: [string] Description of the instrument in case it is not listed in instrumentType.

## Polygon

A simple polygon that encloses an area on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area.

-	**polygonID**: (Primary Key) [string] Unique identifier for the polygon.


-	**name**: [string] Descriptive name of the polygon.


-	**pop**: [integer] Approximate population size of people living inside the polygon.


-	**type**: [category] Type of polygon.
	-	`swrCat`: Sewer catchment area.
	-	`hlthReg`: Health region served by the sewer network

-	**wkt**: [string] well known text of the polygon


-	**file**: [blob] File containing the geometry of the polygon, blob format.


-	**link**: [string] Link to an external reference that describes the geometry of the polygon.

## CovidPublicHealthData

Covid-19 patient data for a specified polygon.

-	**cphdID**: (Primary Key) [string] Unique identifier for the table.


-	**reporterID**: (Foreign key) [string] ID of the reporter who gave this data.


-	**polygonID**: (Foreign key) [string] Links with the Polygon table.


-	**date**: [string] date of reporting for covid-19 measure.


-	**type**: [category] Type of covid-19 patient data.
	-	`conf`: Number of confirmed cases. This measure should be accompanied by dateType.
	-	`active`: Number of active cases.
	-	`test`: Number of tests performed.
	-	`posTest`: Number of positive tests.
	-	`pPosRt`: Percent positivity rate.
	-	`hospCen`: Hospital census or the number of people admitted with covid-19.
	-	`hospAdm`: Hospital admissions or patients newly admitted to hospital.

-	**dateType**: [category] Type of date used for conf cases. Typically report or episode are reported. onset and test date is not usually reported within aggregate data.
	-	`episode`: Episode date is the earliest of onset, test or reported date.
	-	`onset`: Earliest that symptoms were reported for this case. This data is often not known and reported. In lieu, episode is used.
	-	`report`: Date that the numbers were reported publicly. Typically, reported data and this measure is most commonly reported and used.
	-	`test`: Date that the covid-19 test was performed.

-	**value**: [float] The numeric value that is being reported.


-	**notes**: [string] Any additional notes.

## Lookup

Used for lookup values of all category based columns

-	**tableName**: [string] Name of the Table


-	**columnName**: [string] Name for the column


-	**value**: [string] Name of the value


-	**description**: [string] Name of the description





# Database templates and input forms

Several database templates and input forms are underdevelopment to help labs and other partners enter data.

Templates are in the [template folder](template).

Available templates:

*Database templates*


-   [`covid_wwtp_data_template.xlsx`](template/covid_wwtp_data_template.xlsx) - (do not use - an early example). This template does not adhere to the current version of the ODM. Stay tuned for an updated version.
-   [wbe_create_tables.sql](src/wbe_create_tables.sql) - Code to generate a SQL database.

## Database templates

Database templates are flat file templates (i.e. Excel or CSV file format) that are used to summarize wastewater SARS-CoV-2 measurements. There are two formats - 'wide' and 'long' that are based on the underlying primary databases that are described in Metadata.

-   **'Wide'** format - The 'wide' form of data entry corresponds to how labs commonly hold their own data. This form usually has one *sample* per row. Each sample corresponds to test performed on a wastewater sample taken on a specific day. This means that each row corresponds to a single day. The main variables are from the 'measurement' table, but there are also variables from other tables. Alternatively, variables from other tables can be collected separately.

-   **'Long'** format - This template has one *measurement* per row. The long format follows the ERD and data dictionary.

## Input forms

Input forms correspond to the tables described in metadata. Survey Monkey forms are available for earlier versions of the ODM, but these are current not supported in the most recent version. We are aware of several initiatives to generate Microsoft PowerApp and ArcGIS Survey123. Updates will be provided here as those initiatives develop.

## Example of wide and long variable formats

The [metadata](metadata.md) and [Entity Relationship Diagram](metadata.md#entity-relationship-diagram) are long table formats. 

### Example of reporting two viral regions (N1 and N2) on the same sample

Long table format

|date      |type|unit|aggregation|value|
|----------|------|--------|-----------|-----|
|2021-01-15|covN1 |nPPMoV  |mean       |40   |
|2021-01-15|covN2 |nPPMov  |mean       |42   |

Wide table format

|date      |covN1_nPPMoV_mean|covN2_nPPMoV_mean|
|----------|-----------------|-----------------|
|2021-01-15|40               |42               |


## Order of completion

Because of the multiple relationships between the tables composing the data model, it is important that some tables are completed before others can be. The following order of completion should be respected in order to ensure that the datasets are complete:

- **Step 1**: `Instrument`, `Polygon`

- **Step 2**: `Site`, `AssayMethod`

- **Step 3**: `Lab`

- **Step 4**: `Reporter`

- **Step 5**: `Sample`+`WWMeasure` OR `SiteMeasure` OR `CovidPublicHealthData`



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

