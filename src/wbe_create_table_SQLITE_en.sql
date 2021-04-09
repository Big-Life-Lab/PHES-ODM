CREATE TABLE IF NOT EXISTS [Sample] (
/**/
	[sampleID] char NOT NULL PRIMARY KEY, --
	[siteID] char, --
	[instrumentID] char, --
	[reporterID] char, --
	[dateTime] integer, --
	[dateTimeStart] integer, --
	[dateTimeEnd] integer, --
	[type] char, --
	[typeOther] char, --
	[collection] char, --
	[collectionOther] char, --
	[preTreatment] integer, --
	[preTreatmentDescription] char, --
	[pooled] integer, --
	[children] char, --
	[parent] char, --
	[sizeL] float, --
	[fieldSampleTempC] float, --
	[shippedOnIce] integer, --
	[storageTempC] float, --
	[qualityFlag] integer, --
	[notes] char, --
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(InstrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [WWMeasure] (
/**/
	[uWwMeasureID] char NOT NULL PRIMARY KEY, --
	[wwMeasureID] char, --
	[sampleID] char, --
	[labID] char, --
	[assayID] char, --
	[instrumentID] char, --
	[reporterID] char, --
	[analysisDate] integer, --
	[reportDate] integer, --
	[fractionAnalyzed] char, --
	[type] char, --
	[typeOther] char, --
	[unit] char, --
	[unitOther] char, --
	[aggregation] char, --
	[aggregationOther] char, --
	[index] integer, --
	[value] float, --
	[qualityFlag] integer, --
	[accessToPublic] integer, --
	[accessToAllOrg] integer, --
	[accessToSelf] integer, --
	[accessToPHAC] integer, --
	[accessToLocalHA] integer, --
	[accessToProvHA] integer, --
	[accessToOtherProv] integer, --
	[accessToDetails] integer, --
	[notes] char, --
	FOREIGN KEY ([sampleID]) REFERENCES Sample(sampleID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labID]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Site] (
/**/
	[siteID] char NOT NULL PRIMARY KEY, --
	[name] char, --
	[description] char, --
	[publicHealthDepartment] char, --
	[healthRegion] char, --
	[type] char, --
	[typeOther] char, --
	[sampleTypeDefault] char, --
	[sampleTypeOtherDefault] char, --
	[sampleCollectionDefault] char, --
	[sampleCollectOtherDefault] char, --
	[sampleStorageTempCDefault] float, --
	[measureFractionAnalyzedDefault] char, --
	[geoLat] float, --
	[geoLong] float, --
	[notes] char, --
	[polygonID] char, --
	[sewerNetworkFileLink] char, --
	[sewerNetworkFileBLOB] integer, --
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [SiteMeasure] (
/**/
	[uSiteMeasureID] char NOT NULL PRIMARY KEY, --
	[siteMeasureID] char, --
	[siteID] char, --
	[instrumentID] char, --
	[reporterID] char, --
	[sampleID] char, --
	[dateTime] integer, --
	[type] char, --
	[typeOther] char, --
	[typeDescription] char, --
	[aggregation] char, --
	[aggregationOther] char, --
	[aggregationDesc] char, --
	[value] float, --
	[unit] char, --
	[qualityFlag] integer, --
	[accessToPublic] integer, --
	[accessToAllOrgs] integer, --
	[accessToSelf] integer, --
	[accessToPHAC] integer, --
	[accessToLocalHA] integer, --
	[accessToProvHA] integer, --
	[accessToOtherProv] integer, --
	[accessToDetails] integer, --
	[notes] char, --
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([sampleID]) REFERENCES Sample(sampleID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Reporter] (
/**/
	[reporterID] char NOT NULL PRIMARY KEY, --
	[siteIDDefault] char, --
	[labIDDefault] char, --
	[contactName] char, --
	[contactEmail] char, --
	[organization] char, --
	[contactPhone] char, --
	[notes] char, --
	FOREIGN KEY ([siteIDDefault]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labIDDefault]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lab] (
/**/
	[labID] char NOT NULL PRIMARY KEY, --
	[assayMethodIDDefault] char, --
	[name] char, --
	[contactName] char, --
	[contactEmail] char, --
	[contactPhone] char, --
	[updateDate] integer, --
	FOREIGN KEY ([assayMethodIDDefault]) REFERENCES AssayMethod(assayMethodID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [AssayMethod] (
/**/
	[assayMethodID] char NOT NULL PRIMARY KEY, --
	[instrumentID] char, --
	[name] char, --
	[version] char, --
	[summary] char, --
	[referenceLink] char, --
	[date] integer, --
	[aliasID] char, --
	[extractionVolMl] float, --
	[loq] float, --
	[lod] float, --
	[unit] char, --
	[unitOther] char, --
	[methodConc] char, --
	[methodExtract] char, --
	[methodPcr] char, --
	[qualityAssQC] char, --
	[inhibition] char, --
	[surrogateRecovery] char, --
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Instrument] (
/**/
	[instrumentID] char NOT NULL PRIMARY KEY, --
	[name] char, --
	[model] char, --
	[description] char, --
	[alias] char, --
	[referenceLink] char, --
	[type] char, --
	[typeOther] char --
);

CREATE TABLE IF NOT EXISTS [Polygon] (
/**/
	[polygonID] char NOT NULL PRIMARY KEY, --
	[name] char, --
	[pop] integer, --
	[type] char, --
	[wkt] char, --
	[file] integer, --
	[link] char --
);

CREATE TABLE IF NOT EXISTS [CovidPublicHealthData] (
/**/
	[cphdID] char NOT NULL PRIMARY KEY, --
	[reporterID] char, --
	[polygonID] char, --
	[date] char, --
	[type] char, --
	[dateType] char, --
	[value] float, --
	[notes] char, --
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lookup] (
/**/
	[tableName] char, --
	[columnName] char, --
	[value] char, --
	[description] char --
)
