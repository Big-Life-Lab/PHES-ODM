# Inputing data

The ODM has twelve data entry tables. Three tables record information on a daily or regular basis (termed 'results tables'): SampleReport to record information regarding sampling and specific sample; MeasureReport to record information on individual measures; and MeasureSetReport to organize related measures together into sets. The remaining nine tables are program description tables, and are generally used for initial set-up and then only updated as needed. Example Excel data entry templates is in [templates]().

Results tables:

- [**Sample Report Table**](#Sample Report Table) (PartID: *SampleReport*) The table that contains information about a sample, where a sample is defined as a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).
....
....

Program description tables:

- [**Address Table**](#Address Table) (PartID: *Address*). The table that contains information about addresses, which can be fore Sites, individuals reporting data, or organizations.
....
....
....
....
....
....
....
....

<!-- list of tables that is generated from parts.csv -->

##  Sample Report Table

(PartID: *SampleReport*) The table that contains information about a sample, where a sample is defined as a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).

- **  **: (partID: collection)[Data type: varchar] 
- **  **: (partID: collectionDateTime)[Data type: varchar] 
- **  **: (partID: collectionDateTimeEnd)[Data type: varchar] 
- **  **: (partID: collectionDateTimeStart)[Data type: varchar] 
- **  **: (partID: collectionNum)[Data type: varchar] 
- **  **: (partID: collectionPer)[Data type: varchar] 
- **  **: (partID: contactID)(Foreign Key)[Data type: varchar] 
- **  **: (partID: datasetID)(Foreign Key)[Data type: varchar] 
- **  **: (partID: lastEdited)[Data type: varchar] 
- **  **: (partID: methodSetID)(Foreign Key)[Data type: varchar] 
- **  **: (partID: notes)[Data type: varchar] 
- **  **: (partID: origin)[Data type: varchar] 
- **  **: (partID: parentSampleID)(Primary Key)[Data type: varchar] 
- **  **: (partID: pooled)[Data type: varchar] 
- **  **: (partID: purposeID)(Foreign Key)[Data type: varchar] 
- **  **: (partID: qualityFlag)[Data type: varchar] 
- **  **: (partID: replicateType)[Data type: varchar] 
- **  **: (partID: sampleID)(Primary Key)[Data type: varchar] 
- **  **: (partID: sampleMaterial)[Data type: varchar] 
- **Date sample was sent**: (partID: sentDate)[Data type: varchar] The date the sample was sent for analyses at a laboratory.
- **Site ID**: (partID: siteID)(Foreign Key)[Data type: varchar] Unique identifier for the location where a sample was taken.

....
....
<!-- {{select: 'SampleReport', filter: {'Input', 'FK', 'Header', 'PK' }} -->
<!-- {{order: 'PK', 'FK', 'Header' }}                                  -->
<!-- {{entry = 'order'}}                                               -->

<!-- for each entery -->

- **{{label}}**: ({{partID}}) {{filter: "ReportTable" = {"PK" or "FK"}, value: "ReportTable"}} [{{dataType}}] {{partDescription}}. {{partNote}}
  <!-- if entry {{partType = 'measure'}} then the following to 'END partype = 'measure' -->
       - `{{label}}`: {{partDescription}}. {{partInstruction}}. [Aggreations]({{link to aggregation set}}). [Units]({{link to unit set}}).

## Address Table
(PartID: *Address*). The table that contains information about addresses, which can be fore Sites, individuals reporting data, or organizations.

- **Address ID**: (partID: addressID)(Primary Key)[Data type: varchar] Unique identifier for a specific given address.

....
....
....
....
....
....
....
....