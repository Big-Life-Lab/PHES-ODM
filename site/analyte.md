# Expanding the scope of ODM to include a wider range of measures

The ODM currently focuses on Covid-19 and includes PCR allele measures inching variant alleys, normalization biomarkers (PPMoV) and water quality parameters (i.e. total solid concentration).

Stakeholders request expansion of measures including more variant information (mutations and sequence data), quality control and assurance measures, other biologics and chemicals.

We propose to expand the model to Version 2 to reflect a change in the approach to reporting measures, in addition to new validation and sharing applications (not discussed here). Breaking changes will be minimal.

## Specifications

### 1) Maintain the same ODM principles.

- a single measure per row as the primary data form.
- human-readable and usable dictionary. Most wastewater labs maintain their data in Excel using manual processes.
- all variables names are supported in open source software including python and R.

### 2) Change 'type' to 'analyte' with a definition that follows the LOINC concept and dictionary definition of analyte.

- current definition of `type`, "The variable that is being measured on the sample, e.g. a SARS-CoV-2 gene target region (cov), a biomarker for normalisation (n) or a water quality parameter (wq)."

- proposed definition of analyte, "A substance or entity being measured or observed. Covid-19 N1 gene region is an analyte. In some cases, an analyte can be how a sample is measured. For example pH and temperature are analytes."

### 3) A analyte is a unique measure with the following attributes:

- _Analyte ID_ (analyteID): A unique identifier. The identifier is comprised of the domain first two letters and a sequential number.

- _Short name_ (shortName): a short analyte variable name. The name must adhere to common variable name support in open software: pascal case, no special characters.

- _Long name_ (full): a name that uniquely identifies a analyte based on its attributes.

- _Common name_ (commonNameEN, commonNameFR): a human-readable name of the analyte.

- _Description_ (descriptionEN, descriptionFR): Optional. Add a sentence or two to describe the analyte, if the common name is not sufficient.

- _Specimen_ (specimenID) - the type of analyte. The current two specimen types are a wastewater sample and site sample. Other future samples include surface and air testing.

There are five optional attributes to describe group or describe an analyte: analyte group, class and part.

- _Domain_ (domainID) - domains of environmental testing. To be defined. Provisionally include: biologic (i.e. Covid-19, chemical (i.e. nitrogen), physical measure (temperature).

- _Analyte group_ (AnalyteGroupID) - one or more analyses can be grouped together. For example, Covid-19 is an analyteGroup and within this group there are analyte cases including RNA alleles (N1, N2, E, etc.) mutations (E484K0), an entire sequence, viral proteins, etc.

- _Analyte class_ (AnalyteClassID) - an analyte group can have difference classes of specific analyte parts. Alleles and mutations are examples of an analyze class.

- _Analyte part_ (analytePart) - the name of that describes the uniquely describes the analyte within an analyteClass. The gene region N1 is an analytePart within the class 'allele'.

- _Analyte nomeclature_ (analyteNomeclature) - the name of the nomeclature for reporting the analyte part. Pangolin and Nexclade are two nomeclactures used to report vairiants. Variants is the only analyte class that uses the nomeclature attribute at this time.

There are two attributes to describe how the analyte can be reported: aggregate and unit. Many analytes can be reported using different aggressions and units. Aggressions for a Covid-19 variant include: detection (true|false) and proportion (faction of total variants). Units for a Covid-19 N1 Cycle threshold (CT) measure include: mean, median, min, max, single measure, etc.

Aggregations and units are described as sets that reference a list of the specific aggressions and units for the analyte.

- _Aggregate set_ (aggregateSetID): a reference to a list of aggregations for the analyte. An aggregate set is list of 'aggregations', as defined in WWMeasure_aggregation in variableCategories. Aggregrations will be refactored into a new table `aggregations.csv`.

- _Unit set_ (unitSetID): a reference to a list of units for the analyte. An unit set is list of 'units', as defined in WWMeasure_unit in variableCategories. Units will be refactored into a new table `units.csv`.
- 
There are three attributes to describe the status and province of the analyte: analyte status, first release and last updated.

- _Analyte status_ (analyteStatus): a flag (active|inactive) to describe whether the analyte is currently available within the ODM dictionary.

- _First released_ (firstReleased): the ODM version when the analyte was first released.

- _Last updated_ (lastUpdated): the ODM version when the analyte was last updated.

### Schema for wide table analyte names

Wide table format have one day per row with columns representing analyte measurments. The wide table format is commonly used by laboratories and data analysts. A schema for naming analytes in a wide table is required.

TBA - see _shortValueName_ and _fullValueName_.
