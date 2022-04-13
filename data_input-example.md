# Inputing data

The ODM has twelve data entry tables. Three tables record information on a daily or regular basis (termed 'results tables'): SampleReport to record information regarding sampling and specific sample; MeasureReport to record information on individual measures; and MeasureSetReport to organize related measures together into sets. The remaining nine tables are program description tables, and are generally used for initial set-up and then only updated as needed. Example Excel data entry templates is in [templates]().

Results tables:

- [**Sample Report Table**](#Sample Report Table) (PartID: _SampleReport_) The table that contains information about a sample, where a sample is defined as a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).
- ....
- ....

Program description tables:

- [**Address Table**](#Address Table) (PartID: _Address_). The table that contains information about addresses, which can be fore Sites, individuals reporting data, or organizations.
- ....
- ....
- ....
- ....
- ....
- ....
- ....
- ....

<!-- list of tables that is generated from parts.csv -->

## Sample Report Table

(PartID: _SampleReport_) The table that contains information about a sample, where a sample is defined as a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).

- **Sample Collection**: (partID: collection)(Header)[Data type: category] Method used to collect the sample.
- **Collection Date Time**: (partID: cDateTime)(Header)[Data type: datetime] for grab samples this is the date, time and timezone the sample was taken.
- **Collection Date Time End**: (partID: cDateTimeEnd)(Header)[Data type: datetime] For integrated time average samples this is the date, time and timezone the sample was finished being taken.
- **Collection Date Time Start**: (partID: cDateTimeStart)(Header)[Data type: datetime] For integrated time averaged samples this is the date, time and timezone the sample was started being taken.
- **Collection Number**: (partID: collectionNum)(Header)[Data type: integer] The number of subsamples that were combined to create the sample. Use NA for continuous, proportional or passive sampling.
- **Collection Period**: (partID: collectionPeriod)(Header)[Data type: integer] Collection period. The time period over which the sample was collected, in hours. Alternatively, use collectionStart and collectionEnd.
- **Contact ID**: (partID: contactID)(Foreign Key)[Data type: varchar] A unique identifier for a given contact person.
- **Dataset Name**: (partID: datasetID)(Foreign Key)[Data type: varchar] The name of the dataset that stores information for MeasureReport, SampleReport and other reporting tables.
- **Update date - Last Edited**: (partID: lastUpdateDate)(Header)[Data type: datetime] The date the report was last updated.
- **Method Set ID**: (partID: methodSetID)(Foreign Key)[Data type: varchar] A unique identifier for a given set of methods.
- **Notes**: (partID: notes)(Header)[Data type: varchar] A note used to describe details that are not captured in other attrbitutes
- **Sample Origin**: (partID: origin)(Header)[Data type: category] An attribute of a sample specifying the origin.
- **Parent Sample ID**: (partID: parentSampleID)(Primary Key)[Data type: varchar] If this sample has been pooled into one big sample for analysis this indicates the sample of the larger pooled sample.
- **Pooled**: (partID: pooled)(Header)[Data type: bool] Is this a pooled sample, and therefore composed of multiple child samples obtained at different sites.
- **Purpose**: (partID: purposeID)(Foreign Key)[Data type: varchar] The reason the measure or sample was taken.
  Categories:

  - _Education_ - A measure or sample taken for education or training.
  - _Multiple purposes_ - A measure or - sample taken for multiple purposes, not easily captured by the other purpose categories.
  - _Regular_ - A measure or sample taken for surveillance or epidemiology.
  - _Quality_ - A measure or sample taken for the purpose of quality control.
  - _Testing_ - A measure or sample taken to test a new method. These measures are typically used for internal lab uses and not reported to external partners.
  - _Validation study_ - A meaure or sample taken for a validation study.

- **Quality Flag**: (partID: qualityFlag)(Header)[Data type: category] Indicator for quality concerns with a sample and their nature (if applicable).
- **Replicate Type**: (partID: replicateType)(Header)[Data type: category] Attirbute of a sample, specifying whether the sample is unique, or a replicate. And if it is a replicate, what type of replicate is it?
- **SampleID**: (partID: sampleID)(Primary Key)[Data type: varchar] Unique identifier for sample. Suggestion:siteID-date-index.
- **Sample Material**: (partID: sampleMaterial)(Header)[Data type: category] The type of matter or material that comprises the given sample.
- **Date sample was sent**: (partID: sentDate)(Header)[Data type: varchar] The date the sample was sent for analyses at a laboratory.
- **Site ID**: (partID: siteID)(Foreign Key)[Data type: varchar] Unique identifier for the location where a sample was taken.

## Measure Report Table

- **measure**: (partID: measureID). A measure or observation of any substance including biologic, physical or chemical substance. Measures are organized into domains, groups, and classes. For example: Domain = biologic, Group = SARS-CoV-2, class = allele.
  - _Group:_ SARS-CoV-2. Measure the amount of SARS-CoV-2 virus. SARS-CoV-2 measures have the following classes: proteins, alleles, variants, mutations, diseases.
    - Class: Allele. Measures/methods related to alleles.
      - SARS-CoV-2-E - SARS-CoV-2 E gene.
      - SARS-CoV-2-N1 - SARS-CoV-2 nucleocapsid gene, allele N1.
      - SARS-CoV-2-N2 - SARS-CoV-2 nucleocapsid gene, allele N2.
      - SARS-CoV-2-N3 - SARS-CoV-2 nucleocapsid gene, allele N3.
      - SARS-CoV-2-RdRp - SARS-CoV-2 RdRp gene.

## ....

## Address Table

(PartID: _Address_). The table that contains information about addresses, which can be fore Sites, individuals reporting data, or organizations.

- **Address ID**: (partID: addressID)(Primary Key)[Data type: varchar] Unique identifier for a specific given address.
- **Address Line 1**: (partID: addL1)(Header)[Data type: varchar] Line 1 (the street name, number and direction) for a given address.
- **Address Line 2**: (partID: addL2)(Header)[Data type: varchar] Line 2 (the unit number) for a given address.
- **City**: (partID: city)(Header)[Data type: varchar] The city where a site or organization is located; part of the address.
- **Country**: (partID: country)(Header)[Data type: varchar] The country where a site or organization is located; part of the address.
- **Dataset Name**: (partID: datasetID)(Foreign Key)[Data type: varchar] The name of the dataset that stores information for MeasureReport, SampleReport and other reporting tables.
- **State, Province, or Region**: (partID: stateProvReg)(Header)[Data type: varchar] The state, province, or region where a site or organization is located; part of the address.
- **Zip or Postal Code**: (partID: zipCode)(Header)[Data type: varchar] The zip code or postal code for a given address, specifying a specifc geographic area.

## Contact Table ....

....
....
....
....
....
....
....

## Measures

The uniqe identification of a measure, where a measure is defined as an observation of any substance.

- **Environmental Temperature**: (partID: airTemp) A measure of environmental temperature, or the temperature of the air at the site of measurement. [linearAggrs](Linear Aggregations). [TemperatureUnits](Temperature Units).
- **5-Day Carbonaceous Biochemical Oxygen Demand**: (partID: BOD5c) The quantity of oxygen utilized for the biochemical degradation of organic matter under standard laboratory procedures in five (5) days in the presence of a nitrification inhibitor, expressed in milligrams per liter (mg/l). [linearAggrs](Linear Aggregations). [stdConcentrationUnits](Standard Concentration Units).
- ...
- ...

## Methods

The unique identifer for a method, where a medthod is defined as a procedure for collecting a sample or performing a measure.

- **nucleic acid extraction method**: (partID: extraction) Description of the method used for extracting nucleic acids or other molecules of interest from raw sample material.
  - _phenol chloroform_: (partID: phenCl) Nucleic acid extraction performed using phenol chloroform.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _4s method_: (partID: 4s) Nucleic acid extraction performed using the chemagic viral dna/rna 300 kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _chemagic viral dna/rna 300 kit_: (partID: chemVir) Nucleic acid extraction performed using the hemagic viral dna/rna 300 kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _nuclisens automated magnetic bead extraction kit_: (partID:t nucAuto) Nucleic acid extraction performed using the nuclisens automated magnetic bead extraction kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _nuclisens manual magnetic bead extraction kit_: (partID: nucManu) Nucleic acid extraction performed using the nuclisens manual magnetic bead extraction kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _promega automated tna kit_: (partID: promAuto) Nucleic acid extraction performed using the promega automated tna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _promega ht tna kit_: (partID: promHt) Nucleic acid extraction performed using the promega ht tna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _promega manual tna_: (partID: kit promManu) Nucleic acid extraction performed using the promega manual tna.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _promega wastewater large volume tna capture kit_: (partID: promWW) Nucleic acid extraction performed using the promega wastewater large volume tna capture kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen allprep dna/rna kit_: (partID: qgDNARNA) Nucleic acid extraction performed using the qiagen allprep dna/rna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen allprep powerfecal dna/rna kit_: (partID: qgPwrFecal) Nucleic acid extraction performed using the qiagen allprep powerfecal dna/rna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen allprep powerviral dna/rna kit_: (partID: qgPwrViral) Nucleic acid extraction performed using the qiagen allprep powerviral dna/rna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen ez1 virus mini kit v2.0_: (partID: qgEz1) Nucleic acid extraction performed using the qiagen ez1 virus mini kit v2.0.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen powerwater kit_: (partID: qgPwrWtr) Nucleic acid extraction performed using the qiagen powerwater kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen qiaamp buffers with epoch columns_: (partID: qgQiAmp) Nucleic acid extraction performed using qiagen qiaamp buffers with epoch columns.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen rneasy kit_: (partID: qgRneasy) Nucleic acid extraction performed using the qiagen rneasy kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _qiagen rneasy powermicrobiome kit_: (partID: qgRneasyPwr) Nucleic acid extraction performed using the qiagen rneasy powermicrobiome kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _thermo magmax microbiome ultra nucleic acid isolation kit_: (partID: thermMag) Nucleic acid extraction performed using the thermo magmax microbiome ultra nucleic acid isolation kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _trizol, zymo mag beads w/ zymo clean and concentrator_: (partID: trizol) Nucleic acid extraction performed using the trizol, zymo mag beads w/ zymo clean and concentrator.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _zymo environ water rna kit/ zymo environ water rna kit (cat. r2042)_: (partID: zymoEnv) Nucleic acid extraction performed using the zymo environ water rna kit/ zymo environ water rna kit.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
  - _zymo quick-rna fungal/bacterial miniprep #r2014_: (partID: zymoQuick) Nucleic acid extraction performed using zymo quick-rna fungal/bacterial miniprep.[Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).
- ...
- ...
- ...
- ...

## Aggregation Sets

{filter: partID = 'aggregationSetID', value: 'description`}

  <!-- if entry {{partType = 'aggregationSet'}} then the following to 'END partype = 'aggregationSet' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.
           - {{filter: "partType" = "aggregation" & "aggregationSet" = "{{label}}", print = {"label": ("partID") "partDescription"}}.

## Unit Sets

{filter: partID = 'unitSetID', value: 'description`}

  <!-- if entry {{partType = 'unitSet'}} then the following to 'END partype = 'unitSet' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.
           - {{filter: "partType" = "unit" & "unitSet" = "{{label}}", print = {"label": ("partID") "partDescription"}}.

## Category Sets

{filter: partID = 'catSetID', value: 'description`}

  <!-- if entry {{partType = 'catSet'}} then the following to 'END partype = 'catSet' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.
           - {{filter: "partType" = "category" & "catSetID" = "{{label}}", print = {"label": ("partID") "partDescription"}}.

## Domains, Groups, and Classes

###Domains
{filter: partID = 'domainID', value: 'description`}

  <!-- if entry {{partType = 'domain'}} then the following to 'END partype = 'domain' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}. [Groups]({{link to groups}}).

###Groups
{filter: partID = 'groupID', value: 'description`}

  <!-- if entry {{partType = 'group'}} then the following to 'END partype = 'group' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}. [Classes]({{link to classes}}).

###Classes
{filter: partID = 'classID', value: 'description`}

  <!-- if entry {{partType = 'class'}} then the following to 'END partype = 'class' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}. [Aggregations]({{link to aggregation set}}). [Units]({{link to unit set}}).

# Compartments

{filter: partID = 'compartmentID', value: 'description`}

  <!-- if entry {{partType = 'compartment'}} then the following to 'END partype = 'compartment' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.

# Nomenclature

{filter: partID = 'nomenclatureID', value: 'description`}

  <!-- if entry {{partType = 'nomenclature'}} then the following to 'END partype = 'nomenclature' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.

# Specimens

{filter: partID = 'specimenID', value: 'description`}

  <!-- if entry {{partType = 'specimen'}} then the following to 'END partype = 'specimen' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.

# Quality Sets

{filter: partID = 'qualitySetID', value: 'description`}

  <!-- if entry {{partType = 'qualitySet'}} then the following to 'END partype = 'qualitySet' -->

       - `{{label}}`: (partID: {{partID}}) {{partDescription}}. {{partInstruction}}.
           - {{filter: "partType" = "quality" & "qualitySetID" = "{{label}}", print = {"label": ("partID") "partDescription"}}.

# Database templates and input forms

Several database templates and input forms are underdevelopment to help labs and other partners enter data.

Templates are in the [template folder](template).

Available templates:

_Database templates_

- [`covid_wwtp_data_template.xlsx`](template/covid_wwtp_data_template.xlsx) - (do not use - an early example). This template does not adhere to the current version of the ODM. Stay tuned for an updated version.
- [wbe_create_tables.sql](src/wbe_create_tables.sql) - Code to generate a SQL database.

## Database templates

Database templates are flat file templates (i.e. Excel or CSV file format) that are used to summarize wastewater SARS-CoV-2 measurements. There are two formats - 'wide' and 'long' that are based on the underlying primary databases that are described in Metadata.

- **'Wide'** format - The 'wide' form of data entry corresponds to how labs commonly hold their own data. This form usually has one _sample_ per row. Each sample corresponds to test performed on a wastewater sample taken on a specific day. This means that each row corresponds to a single day. The main variables are from the 'measurement' table, but there are also variables from other tables. Alternatively, variables from other tables can be collected separately.

- **'Long'** format - This template has one _measurement_ per row. The long format follows the ERD and data dictionary.

## Input forms

Input forms correspond to the tables described in metadata. Survey Monkey forms are available for earlier versions of the ODM, but these are current not supported in the most recent version. We are aware of several initiatives to generate Microsoft PowerApp and ArcGIS Survey123. Updates will be provided here as those initiatives develop.

## Example of wide and long variable formats

The [metadata](metadata.md) and [Entity Relationship Diagram](metadata.md#entity-relationship-diagram) are long table formats.

### Example of reporting two viral regions (N1 and N2) on the same sample

Long table format

| date       | type  | unit   | aggregation | value |
| ---------- | ----- | ------ | ----------- | ----- |
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMov | mean        | 42    |

Wide table format

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
| ---------- | ----------------- | ----------------- |
| 2021-01-15 | 40                | 42                |

## Order of completion

Because of the multiple relationships between the tables composing the data model, it is important that some tables are completed before others can be. The following order of completion should be respected in order to ensure that the datasets are complete:

- **Step 1**: `Instrument`, `Polygon`

- **Step 2**: `Site`, `AssayMethod`

- **Step 3**: `Lab`

- **Step 4**: `Reporter`

- **Step 5**: `Sample`+`WWMeasure` OR `SiteMeasure` OR `CovidPublicHealthData`

## Naming conventions

- **Table names**: Table names use UpperCamelCase.

- **Variable and category names**: Both variables and variable categories use lowerCamelCase. Do not use special characters (only uppercase, lowercase letters and numbers). Reason: variable and category names can be combined to generate derived variables. Using special characters will generate non-allowable characters - see below. Category names a maximum of 7 characters to allow concatenation of four categories into a single variaable to comply with ArcGIS 31 character maximum for variable names.

- **Variables in wide tables**: Wide tables use `_` to concatenate variables from long tables.

- **Variable order** If a multiple measurement take place on different dates this has a natural form in the long table format, however in the pivot wider format this can be ambiguous. In this case, show a `reportDate` followed by a series of measurements taken on that date (e.g. `covN1_PPMV_mean`) followed by more measurements (e.g. `covN2_PPMV_mean`)

- **Merging tables** : Merging tables into a wide table requires additional steps when a variable does not have an unique name (when the variable name appears in more than one table). For example, variables such as `dateTime`, `notes`, `description`, `type`, `version` and `ID` variables such as `sampleID` are used in several tables. Use the following approach:

  - Variable that are not unique (they are in more than one table): add the table name to the variable by concatenate column names with `_`. e.g. `dateTime` from the `Sample` table becomes `Sample_dateTime`.
  - Variable that are unique (they are in only one table in the entire OMD). No variable name changes are needed.

- **Derived, summary or transformed measure**: These measures are generated to summarize or transform one or more variables. Naming convention follows the same approach as naming variable and category names, except use a `_` when concatenating variable or category names. Examples of a derived measure is the calculation of a mean value of one or more SARS-CoV-2 regions. Normalization and standardization are other examples of a transformed measure. Typically derived, summary or transformed measures are not reported, rather the preferred reporting approach is reporting the underlying individual measures.

- **Date time**: YYYY-MM-DD HH:mm:ss (24 hour format, in UTC)

- **Location**: [well known text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) for polygon.

- **Version**: [Semantic versioning](https://semver.org)

## Examples of how to generate wide variable and category names

### 1) Simple viral region report

A long table would represent viral measures of:

```{.markdown}
date = 2021-01-15
type = covN1
unit = nPMMoV
aggregation = mean
value = 40
```

```{.markdown}
date = 2021-01-15
type = covN2
unit = nPMMoV
aggregation = mean
value = 42
```

In a long table as:

| date       | type  | unit   | aggregation | value |
| ---------- | ----- | ------ | ----------- | ----- |
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMoV | mean        | 42    |

A wide table would represent the same measurement as:

```{.markdown}
    covidN1_PPMV_mean = 40
    covidN2_PPMV_mean = 42
```

In a wide table as:

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
| ---------- | ----------------- | ----------------- |
| 2021-01-15 | 40                | 42                |

### 2) Derived measure

To report a mean value of existing covidN1 and covidN2 measures:

```{.markdown}
    date = 2021-01-15
    type = covN1
    unit = ml
    aggregation = mean
    value = 42
```

```{.markdown}
    date = 2021-01-15
    type = covN2
    unit = ml
    aggregation = mean
    value = 40
```

Represent the derived measure as:

long table format

```{.markdown}
    date = 2021-01-15
    type = covN1covN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type       | unit | aggregation | value |
| ---------- | ---------- | ---- | ----------- | ----- |
| 2021-01-15 | covN1covN2 | ml   | mean        | 41    |

or, wide table format

```{.markdown}
    date = 2021-01-15
    covN1covN2_ml_mean = 41
```

- Viral SARS-CoV-2 copies per reference copies.

### 3) Transformed measure

To report mean viral copies of mean value N1 and N2 per viral copies of PMMoV:

Represent the derived measure as:

long table description

```{.markdown}
    date = 2021-01-15
    covN1covN2 = 2
    unit = PPMV
    type = meanNr
```

or,

wide table format

```{.markdown}
    covidN1covidN2_PPMV_meanNr = 2
```
