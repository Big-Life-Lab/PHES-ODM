CREATE TABLE IF NOT EXISTS [Sample] (
/*The sample is a representative volume of wastewater taken from a Site which is then analysed by a lab.*/
	[sampleID] char NOT NULL PRIMARY KEY, --Unique identification for sample. Suggestion:siteID-date-index.
	[siteID] char, --Links with the Site table to describe the location of sampling.
	[dateTime] integer, --for grab samples this is the date, time and timezone the sample was taken.
	[dateTimeStart] integer, --For integrated time averaged samples this is the date, time and timezone the sample was started being taken.
	[dateTimeEnd] integer, --For integrated time average samples this is the date, time and timezone the sample was finished being taken.
	[type] char, --Type of sample.
	[typeOther] char, --Description for other type of sample not listed in
	[collection] char, --Method used to collect the data.
	[collectionOther] char, --Description for other type of method not listed in collection.
	[preTreatment] integer, --Was the sample chemically treated in anyway with the addition of stabilizers or other
	[preTreatmentDescription] char, --If preTreatment then describe the treatment that was performed.
	[pooled] integer, --Is this a pooled sample, and therefore composed of multiple child samples obtained at different sites
	[children] char, --If this is a sample with many smaller samples either because of pooling or sub-sampling this indicates a comma separated list of child sampleID's.
	[parent] char, --If this sample has been pooled into one big sample for analysis this indicates the sampleID of the larger pooled sample.
	[sizeL] float, --Total volume of water or sludge sampled.
	[fieldSampleTempC] float, --Temperature that the sample is stored at while it is being sampled. This field is mainly relevant for composite samples which are either kept at ambient temperature or refrigerated while being sampled.
	[shippedOnIce] integer, --Was the sample kept cool while being shipped to the lab
	[storageTempC] float, --Temperature that the sample is stored at in Celsius.
	[qualityFlag] integer, --Does the reporter suspect the sample having some quality issues
	[notes] char, --Any additional notes.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [WWMeasure] (
/*Measurement result (ie. single variable) from a wastewater sample. WWMeaasure includes data that is commonly collected by staff at wastewater laboratories where measurement is performed using an assay method (see AssayMethod), but can also be performed using specific instruments (see Instruments. Measures performed at the site of the wastewater sample are reported in SiteMeasure.*/
	[uWwMeasureID] char NOT NULL PRIMARY KEY, --Unique identifier a measurement within the measurement table.
	[wwMeasureID] char, --Unique identifier for wide table only. Use when all measures are performed on a single sample at the same time and same laboratory. Suggestion: siteID_sampleID_LabID_reportDate_ID.
	[sampleID] char, --Links with the identified Sample
	[labID] char, --Links with the identified Lab that performed the analysis.
	[assayID] char, --Links with the AssayMethod used to perform the analysis. Use instrument.ID for measures that are not viral measures.
	[instrumentID] char, --Links with the Instrument used to perform the analysis. Use assay.ID for viral measures.
	[reporterID] char, --Links with the reporter that is responsible for the data.
	[analysisDate] integer, --date the measurement was performed in the lab.
	[reportDate] integer, --date the data was reported. One sampleID may have updated reports based on updates to assay method or reporting standard. In this situation, use the original sampleID but updated MeasureID, reportDate and assayID (if needed).
	[fractionAnalyzed] char, --Faction of the sample that is analyzed.
	[type] char, --The variable that is being measured on the sample, e.g. a SARS-CoV-2 gene target region (cov), a biomarker for normalisation (n) or a water quality parameter (wq).
	[typeOther] char, --Description for an other variable not listed in category.
	[unit] char, --Unit of the measurement.
	[unitOther] char, --Description for other measurement unit not listed in unit.
	[aggregation] char, --Statistical measures used to report the sample units of Ct/Cq, unless otherwise stated. Each aggregation has a corresponding value.
	[aggregationOther] char, --Description for other type of aggregation not listed in aggregation.
	[index] integer, --Index number in case the measurement was taken multiple times.
	[value] float, --The actual measurement value that was obtained through analysis.
	[qualityFlag] integer, --Does the reporter suspect the measurement having some quality issues
	[accessToPublic] integer, --If this is 'no', this data will not be available to the public. If missing, data will be available to the public.
	[accessToAllOrg] integer, --If this is 'no', this data will not be available to any partner organization. If missing, data will be available to the all organizations.
	[accessToSelf] integer, --If this is 'no', this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.
	[accessToPHAC] integer, --If this is 'no', the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.
	[accessToLocalHA] integer, --If this is 'no', the, data will not be available to local health authorities. If missing, data will be available to local health authorities.
	[accessToProvHA] integer, --If this is 'no', this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.
	[accessToOtherProv] integer, --If this is 'no', this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before
	[accessToDetails] integer, --More details on the existing confidentiality requirements of this measurement.
	[notes] char, --Any additional notes.
	FOREIGN KEY ([sampleID]) REFERENCES NA(NA) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labID]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Site] (
/*The site of wastewater sampling, including several defaults that can be used to populate new samples upon creation.*/
	[siteID] char NOT NULL PRIMARY KEY, --Unique identifier for the location where wastewater sample was taken.
	[name] char, --Given name to the site. Location name could be a treatment plant, campus, institution or sewer location, etc.
	[description] char, --Description of wastewater site (city, building, street, etc.) to better identify the location of the sampling point.
	[type] char, --Type of site or institution where sample was taken.
	[typeOther] char, --Description of the site when the site is not listed. See siteType.
	[SampleTypeDefault] char, --Used as default when a new sample is created for this site. See type in Sample table.
	[SampleTypeOtherDefault] char, --Used as default when a new sample is created for this site. See typeOther in Sample table.
	[SampleCollectionDefault] char, --Used as default when a new sample is created for this site. See collection in Sample table.
	[SampleCollectOtherDefault] char, --Used as default when a new sample is created for this site. See collectionOther in Sample table.
	[SampleStorageTempCDefault] float, --Used as default when a new sample is created for this site. See storageTempC in Sample table.
	[MeasureFractionAnalyzedDefault] char, --Used as default when a new measurement is created for this site. See fractionAnalyzed in Measurement table.
	[geoLat] float, --Site geographical location, latitude in decimal coordinates, ie.: (45.424721)
	[geoLong] float, --Site geographical location, longitude in decimal coordinates, ie.: (-75.695000)
	[notes] char, --Any additional notes.
	[polygonID] char, --Links with the Polygon table, this should encompass the area that typically drains into this site.
	[sewerNetworkFileLink] char, --Link to a file that has any detailed information about the sewer network associated with the site (any format).
	[sewerNetworkFileBLOB] integer, --A file blob that has any detailed information about the sewer network associated with the site (any format).
	FOREIGN KEY ([polygonID]) REFERENCES NA(NA) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [SiteMeasure] (
/*Measurement result (ie. single variable) obtained by at the site of wastewater sample.SiteMeasure includes data that is commonly collected by staff at wastewater treatment facilities and field sample locations. These measures that are not performed on the wastewater sample but provide additional context necessary for the interpretation of the results. Measures performed on the wastewater sample are reported in WWMeasure.*/
	[uSiteMeasureID] char NOT NULL PRIMARY KEY, --Unique identifier for each measurement for a site.
	[siteMeasureID] char, --Unique identifier for wide table only. Use when all measures are performed on a single sample.
	[siteID] char, --Links with the Site table to describe the location of measurement.
	[instrumentID] char, --Links with the Instrument table to describe instrument used for the measurement.
	[reporterID] char, --Links with the reporter that is responsible for the data.
	[dateTime] integer, --The date and time the measurement was performed.
	[type] char, --The type of measurement that was performed. The prefix env is used for environmental variables, whereas ww indicates a measurement on wastewater.
	[typeOther] char, --Description of the measurement in case it is not listed in type.
	[typeDescription] char, --Additional information on the performed measurement.
	[aggregation] char, --When reporting an aggregate measurement, this field describes the method used.
	[aggregationOther] char, --Description for other type of aggregation not listed in aggregation.
	[aggregationDesc] char, --Information on OR reference to which measurements that were included to calculate the aggregated measurement that is being reported.
	[value] float, --The actual value that is being reported for this measurement.
	[unit] char, --The engineering unit of the measurement.
	[qualityFlag] integer, --Does the reporter suspect quality issues with the value of this measurement
	[accessToPublic] integer, --If this is 'no', this data will not be available to the public. If missing, data will be available to the public.
	[accessToAllOrgs] integer, --If this is 'no', this data will not be available to any partner organization. If missing, data will be available to the all organizations.
	[accessToSelf] integer, --If this is 'no', this data will not be shown on the portal when this reporter logs in. If missing, data will be available to this reporter.
	[accessToPHAC] integer, --If this is 'no', the data will not be available to employees of the Public Health Agency of Canada - PHAC. If missing, data will be available to employees of the Public Health Agency of Canada - PHAC.
	[accessToLocalHA] integer, --If this is 'no', data will not be available to local health authorities. If missing, data will be available to local health authorities.
	[accessToProvHA] integer, --If this is 'no', this data will not be available to provincial health authorities. If missing, data will be available to provincial health authorities.
	[accessToOtherProv] integer, --If this is 'no', this data will not be available to other data providers not listed before. If missing, data will be available to other data providers not listed before.
	[accessToDetails] integer, --More details on the existing confidentiality requirements of this measurement.
	[notes] char, --Any additional notes.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Reporter] (
/*The individual or organization that is reporting and responsible for the quality of the data.*/
	[reporterID] char NOT NULL PRIMARY KEY, --Unique identifier for the person or organization that is reporting the data.
	[siteIDDefault] char, --Used as default when a new sample is created by this reporter. See ID in Site table.
	[labIDDefault] char, --Used as default when a new sample is created by this reporter. See ID in Lab table.
	[contactName] char, --Full Name of the reporter, either an organization or individual.
	[contactEmail] char, --Contact e-mail address.
	[contactPhone] char, --Contact phone number.
	[notes] char, --Any additional notes.
	FOREIGN KEY ([siteIDDefault]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labIDDefault]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lab] (
/*Laboratory that performs SARS-CoV-2 wastewater testing at one or more sites.*/
	[labID] char NOT NULL PRIMARY KEY, --Unique identifier for the laboratory.
	[assayMethodIDDefault] char, --Used as default when a new measurement is created for this lab. See ID in AssayMethod table.
	[name] char, --Name corresponding to lab.
	[contactName] char, --Contact person or group, for the lab.
	[contactEmail] char, --Contact e-mail address, for the lab.
	[contactPhone] char, --Contact phone number, for the lab.
	[updateDate] integer, --date information was provided or updated.
	FOREIGN KEY ([assayMethodIDDefault]) REFERENCES AssayMethod(assayMethodID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [AssayMethod] (
/*The assay method that was used to perform testing. Create a new record if there are changes (improvements) to an existing assay method. Keep the same ID and use an updated version. A new record for a new version can include only the fields that changed, however, we recommend duplicating existing fields to allow each record to clearly describe all steps. Add a current date when recording a new version to an assay.*/
	[assayMethodID] char NOT NULL PRIMARY KEY, --Unique identifier for the assay method.
	[instrumentID] char, --Links with the Instrument table to describe instruments used for the measurement.
	[name] char, --Name of the assay method.
	[version] char, --Version of the assay. Semantic versioning is recommended.
	[summary] char, --Short description of the assay and how it is different from the other assay methods.
	[referenceLink] char, --Link to standard operating procedure.
	[date] integer, --date on which the assayMethod was created or updated (for version update).
	[aliasID] char, --ID of an assay that is the same or similar. a comma separated list.
	[sampleSizeL] float, --Size of the sample that is analyzed in liters.
	[loq] float, --Limit of quantification (LOQ) for this method if one exists.
	[lod] float, --Limit of detection (LOD) for this method if one exists.
	[unit] char, --Unit used by this method, and applicable to the LOD and LOQ.
	[unitOther] char, --Unit used by this method, that are applicable to the LOD and LOQ.
	[methodConc] char, --Description of the method used to concentrate the sample
	[methodExtract] char, --Description of the method used to extract the sample
	[methodPcr] char, --Description of the PCR method used
	[qualityAssQC] char, --Description of the quality control steps taken
	[inhibition] char, --Description of the inhibition parameters.
	[surrogateRecovery] char, --Description of the surrogate recovery for this method.
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Instrument] (
/*Instruments that are used for measures in WWMeasure and SiteMeasure. The assay method for viral measurement are described in AssayMethod.*/
	[instrumentID] char NOT NULL PRIMARY KEY, --Unique identifier for the assay method.
	[name] char, --Name of the instrument used to perform the measurement.
	[model] char, --Model number or version of the instrument.
	[description] char, --Description of the instrument.
	[alias] char, --ID of an assay that is the same or similar. A comma separated list.
	[referenceLink] char, --Link to reference for the instrument.
	[type] char, --Type of instrument used to perform the measurement.
	[typeOther] char --Description of the instrument in case it is not listed in instrumentType.
);

CREATE TABLE IF NOT EXISTS [Polygon] (
/*A simple polygon that encloses an area on the surface of the earth, normally these polygons will either be of a sewer catchment area or of a health region or other reporting area.*/
	[polygonID] char NOT NULL PRIMARY KEY, --Unique identifier for the polygon.
	[name] char, --Descriptive name of the polygon.
	[pop] integer, --Approximate population size of people living inside the polygon.
	[type] char, --Type of polygon.
	[wkt] char, --well known text of the polygon
	[file] integer, --File containing the geometry of the polygon, blob format.
	[link] char --Link to an external reference that describes the geometry of the polygon.
);

CREATE TABLE IF NOT EXISTS [CovidPublicHealthData] (
/*Covid-19 patient data for a specified polygon.*/
	[cphdID] char NOT NULL PRIMARY KEY, --Unique identifier for the table.
	[reporterID] char, --ID of the reporter who gave this data.
	[polygonID] char, --Links with the Polygon table.
	[date] char, --date of reporting for covid-19 measure.
	[type] char, --Type of covid-19 patient data.
	[dateType] char, --Type of date used for conf cases. Typically report or episode are reported. onset and test date is not usually reported within aggregate data.
	[value] float, --The numeric value that is being reported.
	[notes] char, --Any additional notes.
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lookup] (
/*Used for lookup values of all category based columns*/
	[tableName] char, --Name of the Table
	[columnName] char, --Name for the column
	[value] char, --Name of the value
	[description] char --Name of the description
)
