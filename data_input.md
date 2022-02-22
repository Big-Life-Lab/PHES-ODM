<!-- metadata.md is generated from metadata_template.md Please edit metadata_template.md file -->
<!-- create metadata.md with wbe_metadata_write() in generate_db_generation_sql.R -->

# Inputing data

ODM has in nine data entry tables. Two tables record information on samples (SampleReport) and measures from sample (MeasureReport). The remaining seven table are generally used for initial set-up and they are not regularly updated. Example Excel data entry templates is in [templates]().

<!-- We could automate the text in next section more, but I am not sure if it is worth the effort -->
Tables that are updated regularly:
- [SampleReport]({{link to section header for each table in this list}}) - {{filter: partID = 'sampleReportTable', value: 'partInstruction`}}
- MeasureReport - {{filter: partID = 'measureReportTable', value: 'partInstruction`}}

Tables that are created initially or once, with few updates
- Address - {{filter: partID = 'addressTable', value: 'partInstruction`}}
- Contact - {{filter: partID = 'contactTable', value: 'partInstruction`}}
- Instrument - {{filter: partID = 'instrumentTable', value: 'partInstruction`}}
- MethodStep - {{filter: partID = 'methodStepTable', value: 'partInstruction`}}
- MethodSet - {{filter: partID = 'methodSetTable', value: 'partInstruction`}}
- Organization - {{filter: partID = 'organizationTable', value: 'partInstruction`}}
- Polygon - {{filter: partID = 'polygonTable', value: 'partInstruction`}
- Site - - {{filter: partID = 'siteTable', value: 'partInstruction`}}

<!-- list of tables that is generated from parts.csv -->

## SampleReport

{{filter: partID = 'sampleReportTable', value: 'partInstruction`}}

<!-- {{select: 'SampleReport', filter: {'Input', 'FK', 'Header', 'PK' }} -->
<!-- {{order: 'PK', 'FK', 'Header' }}                                  -->
<!-- {{entry = 'order'}}                                               -->

<!-- for each entery -->
- **{{label}}**: ({{partID}}) {{filter: "ReportTable" = {"PK" or "FK"}, value: "ReportTable"}} [{{dataType}}] {{partDescription}}. {{partNote}}
<!-- if entry {{partType = 'measure'}} then the following to 'END partype = 'measure' -->
     - `{{label}}`: {{partDescription}}. {{partInstruction}}. [Aggreations]({{link to aggregation set}}). [Units]({{link to unit set}}).

## MeasureReport
<!-- same as Measur eTable>
