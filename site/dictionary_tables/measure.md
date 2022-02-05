# Expanding the scope of ODM to include a wider range of measures

The ODM currently focuses on Covid-19 and includes PCR allele measures inching variant alleles, normalization biomarkers (PMMoV) and water quality parameters (i.e. total solids concentration).

Stakeholders request expansion of measures including more variant information (mutations and sequence data), quality control and assurance measures, other biologics and chemicals.

We propose to expand the model to Version 2 to reflect a change in the approach to reporting measures, in addition to new validation and sharing applications (not discussed here). Breaking changes will be minimal.

## Specifications

### 1) Maintain the same ODM principles.

- a single measure per row as the primary data form.
- human-readable and usable dictionary. Most wastewater labs maintain their data in Excel using manual processes.
- all variables names are supported in open source software including python and R.

### 2) Change 'type' to 'measure' with a definition that follows the LOINC concept and dictionary definition of measure.

- current definition of `type`, "The variable that is being measured on the sample, e.g. a SARS-CoV-2 gene target region (cov), a biomarker for normalisation (n) or a water quality parameter (wq)."

- proposed definition of measure, "A substance or entity being measured or observed. Covid-19 N1 gene region is an measure.

### 3) A measure has the following attributes:

- _measure ID_ (measureID): A unique identifier. The identifier is comprised of the domain first two letters and a sequential number.

- _Short name_ (shortName): a short measure variable name. The name must adhere to common variable name support in open software: pascal case, no special characters.

- _Long name_ (fullName): a name that uniquely identifies a measure based on its attributes.

- _Common name_ (commonNameEN, commonNameFR): a human-readable name of the measure.

- _Description_ (descriptionEN, descriptionFR): Optional. Add a sentence or two to describe the measure, if the common name is not sufficient.

- _Specimen_ (specimenID) - the type of measure. The current two specimen types are a wastewater sample and site sample. Other future samples include surface and air testing.

There are five optional attributes to describe group or describe an measure: measure group, class and part.

- _Domain_ (domainID) - domains of environmental testing. To be defined. Provisionally include: biologic (i.e. Covid-19, chemical (i.e. nitrogen), physical measure (temperature).

- _Measure group_ (measureGroupID) - one or more analyses can be grouped together. For example, Covid-19 is an measureGroup and within this group there are measure cases including RNA alleles (N1, N2, E, etc.) mutations (E484K0), an entire sequence, viral proteins, etc.

- _Measure class_ (measureClassID) - an measure group can have difference classes of specific measure parts. Alleles and mutations are examples of an analyze class.

- _Measure part_ (measurePart) - the name of that uniquely describes the measure within an measureClass. The gene region N1 is an measurePart within the class 'allele'.

- _Measure nomeclature_ (measureNomeclature) - the name of the nomeclature for reporting the measure part. Pangolin and Nexclade are two nomeclactures used to report variants. Variants is the only measure class that uses the nomeclature attribute at this time.

There are two attributes to describe how the measure can be reported: aggregate and unit. Many measures can be reported using different aggregations and units. Aggregations for a Covid-19 variant include: detection (true|false) and proportion (faction of total variants). Units for a Covid-19 N1 Cycle threshold (CT) measure include: mean, median, min, max, single measure, etc.

There are three attributes to describe the status of the measure: measure status, first release and last updated.

- _measure status_ (measureStatus): a flag (active|inactive) to describe whether the measure is currently available within the ODM dictionary.

- _First released_ (firstReleased): the ODM version when the measure was first released.

- _Last updated_ (lastUpdated): the ODM version when the measure was last updated.

### Schema for wide table measure names

The wide table format has one day per row with columns representing measures. The wide table format is commonly used by laboratories and data analysts. A schema for naming measures in a wide table is required.

TBA - see _shortValueName_ and _fullValueName_.
