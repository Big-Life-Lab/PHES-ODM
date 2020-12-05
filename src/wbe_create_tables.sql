CREATE TABLE [Polygon] (
  [polygonID] int NOT NULL PRIMARY KEY,
  [polygonName] char,
  [polygonPop] integer,
  [polygonType] char,
  [polygonWKT] char,
  [polygonFile] VARBINARY(MAX),
  [polygonLink] char
);

CREATE TABLE [Reporter] (
  [reporterID] int NOT NULL PRIMARY KEY,
  [siteIDDefault] int,
  [labIDDefault]  int,
  [contactName] char,
  [contactEmail] char,
  [contactPhone] int,
  [allowAccessToSelf] bit,
  [allowAccessToFederalPublicHealthAuthorities] bit,
  [allowAccessToLocalPublicHealthAuthorities] bit,
  [allowAccessToProvinicialPublicHealthAuthorities] bit,
  [allowAccessToOtherDataProviders] bit,
  [allowAccessToAllOrganizations] bit,
  [allowAccessToPublic] bit,
  [allowAccessToSpec] char,
  [notes] char
);

CREATE TABLE [Site] (
  [siteID] int NOT NULL PRIMARY KEY,
  [siteName] char,
  [siteDescription] char,
  [reporterID]int FOREIGN KEY REFERENCES Reporter(reporterID),
  [siteType] char,
  [siteTypeOther] char,
  [sampleTypeDefault] char,
  [sampleTypeOtherDefault] char,
  [primarySourceOfWastewater] char,
  [primarySourceOfWastewaterOther] char,
  [methodCollectionDefault] char,
  [methodCollectOtherDefault] char,
  [sampleFractionDefault] char,
  [samplestorageTempCDefault] float,
  [geoLat] float,
  [geoLong] float,
  [notes] char,
  [sewerNetworkPolygonID] char,
  [sewerNetworkFileLink] char,
  [sewerNetworkFileBlob] VARBINARY(MAX)
);

CREATE TABLE [Sample] (
  [sampleID] int NOT NULL PRIMARY KEY,
  [siteID] int FOREIGN KEY REFERENCES Site(siteID),
  [sampleDateTime] dateTime,
  [sampleDateTimeStart] dateTime,
  [sampleDateTimeEnd] dateTime,
  [sampleType] char,
  [sampleTypeOther] char,
  [methodCollection] char,
  [methodCollectionOther] char,
  [sampleSizeL] float,
  [sampleStorageTempC] float,
  [notes] char
);

CREATE TABLE [AssayMethod] (
  [assayID] int NOT NULL PRIMARY KEY,
  [version] char,
  [sampleSizeL] float,
  [loq] float,
  [lod] float,
  [methodUnits] char,
  [methodUnitsOther] char,
  [assayDate] char,
  [Inhibition] char,
  [surrogateRecovery] char,
  [assayDesc] char
);



CREATE TABLE [Lab] (
  [labId] int NOT NULL PRIMARY KEY,
  [assayID] int FOREIGN KEY REFERENCES AssayMethod(assayID),
  [laboratoryName] char,
  [contactName] char,
  [contactEmail] char,
  [contactPhone] int,
  [labUpdateDate] date
);

CREATE TABLE [CovidPublicHealthData] (
  [publicHealthID] int NOT NULL PRIMARY KEY,
  [reporterID]int FOREIGN KEY REFERENCES Reporter(reporterID),
  [polygonID]int FOREIGN KEY REFERENCES Polygon(polygonID),
  [date] date,
  [dateType] char,
  [numberOfNewCases] float,
  [numberOfActiveCases] float,
  [numberOfTests] float,
  [numberOfPositiveTests] float,
  [percentPositivityRate] float
);



CREATE TABLE [Measurement] (
  [measurementID] int NOT NULL PRIMARY KEY,
  [sampleID] int FOREIGN KEY REFERENCES sample(sampleID),
  [labID] int FOREIGN KEY REFERENCES Lab(labID),
  [assayID] int FOREIGN KEY REFERENCES AssayMethod(assayID),
  [analysisDate] date,
  [reportedDate] date,
  [sampleFraction] char,
  [measureCat] char,
  [measureCatOther] char,
  [measureUnit] char,
  [measureUnitOther] char,
  [measureType] char,
  [measureTypeOther] char,
  [measureValue] float,
  [measureValueDetected] bit,
  [notes] char
);

