CREATE TABLE IF NOT EXISTS [Sample] (
/**/
	[sampleID] VARCHAR ( 255 ) PRIMARY KEY, --
	[siteID] VARCHAR ( 255 ), --
	[dateTime] TIMESTAMP, --
	[dateTimeStart] TIMESTAMP, --
	[dateTimeEnd] TIMESTAMP, --
	[type] VARCHAR ( 255 ), --
	[typeOther] VARCHAR ( 255 ), --
	[collection] VARCHAR ( 255 ), --
	[collectionOther] VARCHAR ( 255 ), --
	[preTreatment] BOOLEAN, --
	[preTreatmentDescription] VARCHAR ( 255 ), --
	[pooled] BOOLEAN, --
	[children] VARCHAR ( 255 ), --
	[parent] VARCHAR ( 255 ), --
	[sizeL] double precision, --
	[fieldSampleTempC] double precision, --
	[shippedOnIce] BOOLEAN, --
	[storageTempC] double precision, --
	[qualityFlag] BOOLEAN, --
	[notes] VARCHAR ( 255 ), --
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID)
);

CREATE TABLE IF NOT EXISTS [WWMeasure] (
/**/
	[uWwMeasureID] VARCHAR ( 255 ) PRIMARY KEY, --
	[wwMeasureID] VARCHAR ( 255 ), --
	[sampleID] VARCHAR ( 255 ), --
	[labID] VARCHAR ( 255 ), --
	[assayID] VARCHAR ( 255 ), --
	[instrumentID] VARCHAR ( 255 ), --
	[reporterID] VARCHAR ( 255 ), --
	[analysisDate] DATE , --
	[reportDate] DATE , --
	[fractionAnalyzed] VARCHAR ( 255 ), --
	[type] VARCHAR ( 255 ), --
	[typeOther] VARCHAR ( 255 ), --
	[unit] VARCHAR ( 255 ), --
	[unitOther] VARCHAR ( 255 ), --
	[aggregation] VARCHAR ( 255 ), --
	[aggregationOther] VARCHAR ( 255 ), --
	[index] INTEGER, --
	[value] double precision, --
	[qualityFlag] BOOLEAN, --
	[accessToPublic] BOOLEAN, --
	[accessToAllOrg] BOOLEAN, --
	[accessToSelf] BOOLEAN, --
	[accessToPHAC] BOOLEAN, --
	[accessToLocalHA] BOOLEAN, --
	[accessToProvHA] BOOLEAN, --
	[accessToOtherProv] BOOLEAN, --
	[accessToDetails] BOOLEAN, --
	[notes] VARCHAR ( 255 ), --
	FOREIGN KEY ([sampleID]) REFERENCES Sample(sampleID),
	FOREIGN KEY ([labID]) REFERENCES Lab(labID),
	FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID),
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID),
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID)
);

CREATE TABLE IF NOT EXISTS [Site] (
/**/
	[siteID] VARCHAR ( 255 ) PRIMARY KEY, --
	[name] VARCHAR ( 255 ), --
	[description] VARCHAR ( 255 ), --
	[type] VARCHAR ( 255 ), --
	[typeOther] VARCHAR ( 255 ), --
	[sampleTypeDefault] VARCHAR ( 255 ), --
	[sampleTypeOtherDefault] VARCHAR ( 255 ), --
	[sampleCollectionDefault] VARCHAR ( 255 ), --
	[sampleCollectOtherDefault] VARCHAR ( 255 ), --
	[sampleStorageTempCDefault] double precision, --
	[measureFractionAnalyzedDefault] VARCHAR ( 255 ), --
	[geoLat] double precision, --
	[geoLong] double precision, --
	[notes] VARCHAR ( 255 ), --
	[polygonID] VARCHAR ( 255 ), --
	[sewerNetworkFileLink] VARCHAR ( 255 ), --
	[sewerNetworkFileBLOB] INTEGER, --
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID)
);

CREATE TABLE IF NOT EXISTS [SiteMeasure] (
/**/
	[uSiteMeasureID] VARCHAR ( 255 ) PRIMARY KEY, --
	[siteMeasureID] VARCHAR ( 255 ), --
	[siteID] VARCHAR ( 255 ), --
	[instrumentID] VARCHAR ( 255 ), --
	[reporterID] VARCHAR ( 255 ), --
	[dateTime] DATE , --
	[type] VARCHAR ( 255 ), --
	[typeOther] VARCHAR ( 255 ), --
	[typeDescription] VARCHAR ( 255 ), --
	[aggregation] VARCHAR ( 255 ), --
	[aggregationOther] VARCHAR ( 255 ), --
	[aggregationDesc] VARCHAR ( 255 ), --
	[value] double precision, --
	[unit] VARCHAR ( 255 ), --
	[qualityFlag] BOOLEAN, --
	[accessToPublic] BOOLEAN, --
	[accessToAllOrgs] BOOLEAN, --
	[accessToSelf] BOOLEAN, --
	[accessToPHAC] BOOLEAN, --
	[accessToLocalHA] BOOLEAN, --
	[accessToProvHA] BOOLEAN, --
	[accessToOtherProv] BOOLEAN, --
	[accessToDetails] BOOLEAN, --
	[notes] VARCHAR ( 255 ), --
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID),
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID),
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID)
);

CREATE TABLE IF NOT EXISTS [Reporter] (
/**/
	[reporterID] VARCHAR ( 255 ) PRIMARY KEY, --
	[siteIDDefault] VARCHAR ( 255 ), --
	[labIDDefault] VARCHAR ( 255 ), --
	[contactName] VARCHAR ( 255 ), --
	[contactEmail] VARCHAR ( 255 ), --
	[contactPhone] VARCHAR ( 255 ), --
	[notes] VARCHAR ( 255 ), --
	FOREIGN KEY ([siteIDDefault]) REFERENCES Site(siteID),
	FOREIGN KEY ([labIDDefault]) REFERENCES Lab(labID)
);

CREATE TABLE IF NOT EXISTS [Lab] (
/**/
	[labID] VARCHAR ( 255 ) PRIMARY KEY, --
	[assayMethodIDDefault] VARCHAR ( 255 ), --
	[name] VARCHAR ( 255 ), --
	[contactName] VARCHAR ( 255 ), --
	[contactEmail] VARCHAR ( 255 ), --
	[contactPhone] VARCHAR ( 255 ), --
	[updateDate] DATE , --
	FOREIGN KEY ([assayMethodIDDefault]) REFERENCES AssayMethod(assayMethodID)
);

CREATE TABLE IF NOT EXISTS [AssayMethod] (
/**/
	[assayMethodID] VARCHAR ( 255 ) PRIMARY KEY, --
	[instrumentID] VARCHAR ( 255 ), --
	[name] VARCHAR ( 255 ), --
	[version] VARCHAR ( 255 ), --
	[summary] VARCHAR ( 255 ), --
	[referenceLink] VARCHAR ( 255 ), --
	[date] DATE , --
	[aliasID] VARCHAR ( 255 ), --
	[sampleSizeL] double precision, --
	[loq] double precision, --
	[lod] double precision, --
	[unit] VARCHAR ( 255 ), --
	[unitOther] VARCHAR ( 255 ), --
	[methodConc] VARCHAR ( 255 ), --
	[methodExtract] VARCHAR ( 255 ), --
	[methodPcr] VARCHAR ( 255 ), --
	[qualityAssQC] VARCHAR ( 255 ), --
	[inhibition] VARCHAR ( 255 ), --
	[surrogateRecovery] VARCHAR ( 255 ), --
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID)
);

CREATE TABLE IF NOT EXISTS [Instrument] (
/**/
	[instrumentID] VARCHAR ( 255 ) PRIMARY KEY, --
	[name] VARCHAR ( 255 ), --
	[model] VARCHAR ( 255 ), --
	[description] VARCHAR ( 255 ), --
	[alias] VARCHAR ( 255 ), --
	[referenceLink] VARCHAR ( 255 ), --
	[type] VARCHAR ( 255 ), --
	[typeOther] VARCHAR ( 255 ) --
);

CREATE TABLE IF NOT EXISTS [Polygon] (
/**/
	[polygonID] VARCHAR ( 255 ) PRIMARY KEY, --
	[name] VARCHAR ( 255 ), --
	[pop] INTEGER, --
	[type] VARCHAR ( 255 ), --
	[wkt] VARCHAR ( 255 ), --
	[file] INTEGER, --
	[link] VARCHAR ( 255 ) --
);

CREATE TABLE IF NOT EXISTS [CovidPublicHealthData] (
/**/
	[cphdID] VARCHAR ( 255 ) PRIMARY KEY, --
	[reporterID] VARCHAR ( 255 ), --
	[polygonID] VARCHAR ( 255 ), --
	[date] VARCHAR ( 255 ), --
	[type] VARCHAR ( 255 ), --
	[dateType] VARCHAR ( 255 ), --
	[value] double precision, --
	[notes] VARCHAR ( 255 ), --
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID),
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID)
);

CREATE TABLE IF NOT EXISTS [Lookup] (
/**/
	[tableName] VARCHAR ( 255 ), --
	[columnName] VARCHAR ( 255 ), --
	[value] VARCHAR ( 255 ), --
	[description] VARCHAR ( 255 ) --
)
