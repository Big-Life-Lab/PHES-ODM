# How to use Excel data templates

Example of how to use git!

The description below describes how to use the Ontario Data Model Excel
Template, developed for the Ontario's Wastewater Testing Initiative by
Vince Pileggi and Menglu Wang. The template is intended to record
wastewater sampling data for those users who already use Excel for
recording wastewater data. The template can be modified for use in
juradictions outside Ontario. For example, the data template has drop
down list for Ontario's public health departments and health regions
(Local Health Integration Networks). You can replace these dropdown
lists for corresponding regions in for your location.

The Data Template includes built-in metadata (e.g., Definition of Terms,
pop-up text) and data validation rules (e.g., cell-type formatting,
value constraints) to minimize data entry errors and to ensure the
integrity and consistency of data.The purpose of the [*Ottawa Data
Model* (ODM)](https://github.com/Big-Life-Lab/covid-19-wastewater/) is
to improve wastewater surveillance through the development of a common
data structure. An [Entity-Relationship Diagram (ERD)](link) outlining
the structure of the *Ottawa Data Model* describes the tables used to
collect data.

## Data Template Tables

The [XX Data Template](link) includes 8 data tables: 3 wastewater sample
and analysis tables that are updated regularly (i.e., Sample, WWMeasure,
SiteMeasure) and 5 background information tables that are static (i.e.,
Site, Reporter, Lab, Instrument, AssayMethod). Two additional
spreadsheets (i.e., Definition of Terms, Drop-Down Lists) include
reference information. Detailed information about each table and the
values they contain is available in the \_Definition of Terms_table.

### Wastewater Sample and Analysis Tables

The Sample, WWMeasure, and SiteMeasure tables contain different
components of the information necessary to analyze wastewater trends.
The sample is a representative volume of wastewater taken from a Site
which is then analyzed by a lab. WWMeasure includes data that is
commonly collected by staff at wastewater laboratories where the
measurement is performed. SiteMeasure includes data that is commonly
collected by staff at wastewater treatment facilities and field sample
locations and provides additional context necessary for the
interpretation of the results.

### Background Information Tables

The Site, Reporter, Lab, Instrument, and AssayMethod tables are static
or updated infrequently and contain details about the responsible party,
methodology, and location of each wastewater sample.

## Data Input

### Data Template Integrity

The Data Template's structure and built-in data validation rules are
intended to minimize potential data-entry errors. To minimize the
potential for data-entry errors, step-by-step instructions and examples
are provided below under [*Best Practices*](#_Best_Practices), [*General
Data Entry Instructions*](#_General_Data_Entry), and [*Table Specific
Instructions*](#_Site).

## Best Practices

-   **Data entry:** Write your values directly into each cell. In
    situations where copy-and-paste cannot be avoided, you must
    double-click the cell and paste your values in directly (or ensure
    that the value you are pasting follows the correct format and data
    validation for the column). Otherwise, copy-and-paste overwrites the
    cell formatting and data validation rules that ensure data that can
    be loaded and processed in the consolidated Wastewater Surveillance
    Initiative database.
-   **Template:** Do not change the Excel template structure. This is
    critical for loading data into the hub.
-   **Backup:** Always back up your own excel template. You are
    responsible for maintaining and backing up your own excel file.
-   **Blank cells:** Try not to leave any cell values blank. "Other" and
    "notes" fields are optional.

## General Data Entry Instructions

The following table outlines general instructions for different data
types found in the Data Template. A pop-up message for each column
displays specific data-input instructions for that field. The pop-up
message in each cell can be dragged and moved.

| **Field Type**                                      | **Data Entry Instructions** |
|-----------------------------------------------------|-----------------------------|
| **ID Fields\*\*** (e.g., sampleID, labID, etc.)\*\* |                             |

-   Each table has a **primary ID** field. The first ID column of each
    table should be \_ **unique** \_unless otherwise specified in the
    pop-up message. Ensure each entry into this field is **not null** ,
    otherwise records will not be loaded into the central repository.

-   Other ID fields that represent "foreign keys" linking to different
    tables have drop-down menus. These drop-down menus are populated
    from IDs listed in the corresponding table. \| \| **Drop-Down
    Fields\*\*** (e.g., unit, type)\*\* \|

-   Select a value from the defined drop-down list.

-   If you choose to copy-and-paste values into these fields, ensure the
    pasted value is \_ **identical** \_ to one of the predefined
    options. \| \| **--Other Fields\*\*** (e.g., unitOther,
    typeOther)\*\* \|

-   Some drop-down fields have an "other" option. If you select "other"
    from the list, enter the missing value in the adjacent **--Other**
    field. \| \| **Date & dateTime Fields\*\*** (e.g., analysisDate,
    dateTimeStart)\*\* \|

-   **Date** fields must be in the following format: yyyy-mm-dd

-   **dateTime** fields must be in the following format: yyyy-mm-dd
    hh:mm

-   All dates should be between 2020-01-01 and current date. \| \|
    **Note & Description Fields** \|

-   Optional fields for including additional notes. \|

-   **Filtering:** Filtering is enabled in the Data Template file and
    will not impact the records loaded into the central repository.
    Find-and-replace is restricted in the file, though the Find function
    is still available. The **qualityFlag** in the **WWMeasure** table
    can be used to indicate a measurement has quality issues, allowing
    these records to be filtered out.

| **Site Fields** | **Additional Data Entry Instructions for Select Fields** |
|-----------------|----------------------------------------------------------|
| **siteID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository. \| \| **name** \|
-   Provide a descriptive name that can be used for labelling in data
    visualization and presentation. \| \| **type, typeOther** \|
-   This field is **critical** for mapping and analytical purpose.
-   If none of the listed options are applicable to the site, select
    "other" from the drop-down list and enter another site type in the
    **typeOther** column. \| \| **healthRegion** \|
-   Identify the LHIN (Local Health Integration Network) where each site
    is located at
    [www.lhins.on.ca](https://ontariogov.sharepoint.com/sites/MECPDataValidationGroup/Shared%20Documents/General/www.lhins.on.ca).
-   The dropdown list can be modified for people outside Ontario. The
    Ontario list has been left for illustration. \| \|
    **publicHealthDepartment** \|
-   Identify the PHU (Public Health Unit) where each site is located at
    [www.phdapps.health.gov.on.ca/phulocator](https://ontariogov.sharepoint.com/sites/MECPDataValidationGroup/Shared%20Documents/General/www.phdapps.health.gov.on.ca/phulocator)
-   The dropdown list can be modified for people outside Ontario. The
    Ontario list has been left for illustration. \| \| **geoLat,
    geoLong** \|
-   This field is **critical** for mapping purpose.
-   Enter coordinates for the site location. Latitude and longitude
    (decimal degrees e.g. 43.7668287, -79.1507006) in geographic
    coordinate system, using North American Datum of 1983 (NAD83).
-   If assistance is needed to identify the site coordinates, [please
    contact the team for support.](#_top) \|

## Table Specific Instructions

### ![](RackMultipart20210504-4-k7kk6f_html_9233d232cf82e7dc.png)Site

### Reporter

![](RackMultipart20210504-4-k7kk6f_html_5e13ee8acb8556df.png)

| **Reporter Fields** | **Additional Data Entry Instructions for Select Fields** |
|---------------------|----------------------------------------------------------|
| **reporterID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository.

### ![](RackMultipart20210504-4-k7kk6f_html_29d5f3a9b054ea33.png)Lab

| **Lab Fields** | **Additional Data Entry Instructions for Select Fields** |
|----------------|----------------------------------------------------------|
| **labID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository.

### ![](RackMultipart20210504-4-k7kk6f_html_3d97f6ef9fef1462.png)Instrument

| **Instrument Fields** | **Additional Data Entry Instructions for Select Fields** |
|-----------------------|----------------------------------------------------------|
| **instrumentID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository. \| \| **name,
    model** \|
-   Provide a descriptive name and model of the instrument used to
    perform the analysis. \| \| **referenceLink** \|
-   Provide a link of reference for the instrument. Links may direct to
    a website or PDF document. \| \| **type, typeOther** \|
-   Select the type of instrument used to perform the measurement. See
    Definition of Terms for descriptions of the options provided.
-   If none of the listed options are applicable to the instrument,
    select "other" from the drop-down list and enter another instrument
    type in the **typeOther** column. \|

| **AssayMethod Fields** | **Additional Data Entry Instructions for Select Fields** |
|------------------------|----------------------------------------------------------|
| **assayMethodID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository. \| \| **name,
    version** \|
-   Provide a descriptive name and version to identify the assay method
    used for analysis. \| \| **referenceLink** \|
-   Provide a PDF link to the standards of practice document of the
    assay method.
-   If methods are not published, have an editable dropbox link to the
    methods pdf. \| \| **sampleSizeL** \|
-   Enter the volume of the sample analyzed in litres. \| \| **loq,
    lod** \|
-   Enter the Limit of quantification (LOQ) and detection (LOD) values
    for this method, if they exist. \| \| **unit, unitOther** \|
-   Select unit of measurement that is used by the method, and is
    applicable to the LOQ and LOD. See Definition of Terms table for
    definitions of the provided options.
-   If none of the listed options are applicable to the assay method,
    select "other" from the drop-down list and enter another unit of
    measurement in the **unitOther** column. \|

### ![](RackMultipart20210504-4-k7kk6f_html_3226e8f25de57b37.png)AssayMethod

### 

| **Sample Fields** | **Additional Data Entry Instructions for Select Fields** |
|-------------------|----------------------------------------------------------|
| **sampleID**      |                                                          |

-   Ensure each entry is **unique** and **not null** , otherwise records
    will not be loaded into the central repository. \| \| **siteID** \|
-   Ensure each entry is **not null** , otherwise records will not be
    loaded into the central repository. \| \| **collection** \|
-   Collection method must be defined -- it determines what date and
    time information is required for each record.
-   If collection method is "grab", dateTime needs to be filled out.
    (Otherwise leave it empty.)
-   If collection method is "composite", then dateTimeStart \_ **and**
    \_ dateTimeEnd need to be filled out. (Otherwise leave them empty.)
    \| \| **dateTime** \| \| **dateTimeStart** \| \| **dateTimeEnd** \|

### ![](RackMultipart20210504-4-k7kk6f_html_9a9189020cbf7ed1.png)Sample

### ![](RackMultipart20210504-4-k7kk6f_html_7b24e02723224d54.png) WWMeasure

| **WWMeasure Fields** | **Additional Data Entry Instructions for Select Fields** |
|----------------------|----------------------------------------------------------|
| **uWwMeasureID**     |                                                          |

      - Ensure each entry is **unique** and **not null** , otherwise records will not be loaded into the central repository.
      - Pre-formatted formula concatenating **row number** , **sampleID** , **type** , and **index** values to create a unique ID.

| 
| **sampleID** \| - Ensure each entry is **not null** , otherwise records will not be loaded into the central repository. - Each "sampleID" (from the sample table) must have at least 5 records. - Each "sample ID" (from the sample table) must have at least three different types, and for each type must have at least 2 values (not applicable for nPMMoV).
| 
| **index** \| - Enter aninteger to identify a replicate for the measured sample. It is recommended to keep the index value simple (i.e., 1, 2, 3).
| 
| **value** \| - Enter the genetic content per mL or L of wastewater or primary sludge sample obtained through analysis. - Please enter actual values for LOD and LOQ
| 

| **SiteMeasure Fields** | **Data Entry Instructions** |
|------------------------|-----------------------------|
| **uSiteMeasureID**     |                             |

      - Ensure each entry is **unique** and **not null** , otherwise records will not be loaded into the central repository.

| 
| **siteID** \| - Ensure each entry is **not null** , otherwise records will not be loaded into the central repository.
| 
| **sampleID** \| - This field is **critical** for easily linking samples back to the site measurements, without the need for comparing dates.
| 
| **dateTime** \| - This field is **critical** for interpretation of wastewater results. - The field needs to be between 2020-01-01 and current date. - Format: yyyy-mm-dd hh:mm
| 
| **type, typeOther** \| - This field is **critical** for interpretation of wastewater results. - **wwFlow** is necessary for analyzing wastewater trends. - If none of the listed options are applicable to the measurement, select "other" from the drop-down list and enter another type in the **typeOther** column.
| 
| **value** \| - This field is **critical** for interpretation of wastewater results.
| 
| **unit** \| - This field is **critical** for interpretation of wastewater results. - For pH reading (and other values without units), leave this field blank.

### ![](RackMultipart20210504-4-k7kk6f_html_8048a6868adbc72b.png)SiteMeasure

## Appendix

## Entity-Relationship Diagram ![](RackMultipart20210504-4-k7kk6f_html_25bbdc5a4656f67d.jpg)

        2. **Drop-down List Options**

![](RackMultipart20210504-4-k7kk6f_html_2d4b53d3734c863b.jpg)

![](RackMultipart20210504-4-k7kk6f_html_5e4eeddeb86ff8ac.gif)
