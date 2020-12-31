

CREATE TABLE  IF NOT EXISTS [Polygon] (
  [polygonID] char NOT NULL PRIMARY KEY,
  [polygonName] char,
  [polygonPop] integer,
  [polygonType] char,
  [polygonWKT] char,
  [polygonFile] blob null default (x''),
  [polygonLink] char
);

CREATE TABLE IF NOT EXISTS [Reporter] (
  [reporterID] char NOT NULL PRIMARY KEY,
  [siteIDDefault] char,
  [labIDDefault]  char,
  [contactName] char,
  [contactEmail] char,
  [contactPhone] int,
  [allowAccessToSelf] INTEGER,
  [allowAccessToFederalPublicHealthAuthorities] INTEGER,
  [allowAccessToLocalPublicHealthAuthorities] INTEGER,
  [allowAccessToProvinicialPublicHealthAuthorities] INTEGER,
  [allowAccessToOtherDataProviders] INTEGER,
  [allowAccessToAllOrganizations] INTEGER,
  [allowAccessToPublic] INTEGER,
  [allowAccessToSpec] char,
  [notes] char
);

CREATE TABLE  IF NOT EXISTS [Site] (
  [siteID] char NOT NULL PRIMARY KEY,
  [siteName] char,
  [siteDescription] char,
  [reporterID] char,
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
  [sewerNetworkFileBlob]  blob null default (x''),
  FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE  IF NOT EXISTS [Sample] (
  [sampleID] char NOT NULL PRIMARY KEY,
  [siteID] char,
  [DateTime] dateTime,
  [DateTimeStart] dateTime,
  [DateTimeEnd] dateTime,
  [sampleType] char,
  [sampleTypeOther] char,
  [methodCollection] char,
  [methodCollectionOther] char,
  [sampleSizeL] float,
  [sampleStorageTempC] float,
  [notes] char,
  FOREIGN KEY ([siteID]) REFERENCES Reporter(siteID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE  IF NOT EXISTS [AssayMethod] (
  [assayID] char NOT NULL PRIMARY KEY,
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



CREATE TABLE  IF NOT EXISTS [Lab] (
  [labId] char NOT NULL PRIMARY KEY,
  [assayIDDefault] char,
  [laboratoryName] char,
  [contactName] char,
  [contactEmail] char,
  [contactPhone] int,
  [labUpdateDate] date,
  FOREIGN KEY ([assayIDDefault]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE  IF NOT EXISTS [CovidPublicHealthData] (
  [publicHealthID] char NOT NULL PRIMARY KEY,
  [reporterID]char,
  [polygonID]char,
  [date] date,
  [dateType] char,
  [numberOfNewCases] float,
  [numberOfActiveCases] float,
  [numberOfTests] float,
  [numberOfPositiveTests] float,
  [percentPositivityRate] float,
  FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED

);


CREATE TABLE  IF NOT EXISTS [Lookups](
  [tableName] char,
  [columnName] char,
  [value] char,
  [description] char
);

CREATE TABLE  IF NOT EXISTS [Measurement] (
  [measurementID] char NOT NULL PRIMARY KEY,
  [sampleID] char,
  [labID] char,
  [assayID] char,
  [analysisDate] date,
  [reportedDate] date,
  [sampleFraction] char,
  [measureCat] char,
  [measureCatOther] char,
  [measureUnit] char,
  [measureUnitOther] char,
  [measureType] char,
  [measureTypeOther] char,
  [sampleIndex] char,
  [measureValue] float,
  [measureValueDetected] INTEGER,
  [notes] char,
  FOREIGN KEY ([sampleID]) REFERENCES Sample(sampleID) DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ([labID]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED
)
