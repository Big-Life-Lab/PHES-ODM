# Inputing data

The ODM has twelve data entry tables. Three tables record information on a daily or regular basis (termed 'results tables'): SampleReport to record information regarding sampling and specific sample; MeasureReport to record information on individual measures; and MeasureSetReport to organize related measures together into sets. The remaining nine tables are program description tables, and are generally used for initial set-up and then only updated as needed. Example Excel data entry templates is in [templates]().

Tables that are updated regularly:

<!-- create list of tables from partType = table, class = results  -->
<!-- order???? -->

- [**{{label}}**]({{link to section header for each table in this list}}) PartID: [**{{partID}}**] - {{filter: partType = 'table', value: 'partInstruction`}}

<!-- create list of tables from partType = table, class = programDescription -->

Tables that are created initially or once, with few updates

<!-- create list of tables from partType = table, class = results or programDescription -->

- [**{{label}}**]({{link to section header for each table in this list}}) PartID: [**{{partID}}**] - {{description}}

<!-- list of tables that is generated from parts.csv -->

## {{first item for {{filter: partType = 'table', value: 'label`}}}}

{{value: 'description`}}

<!-- {{select: 'SampleReport', filter: {'Input', 'FK', 'Header', 'PK' }} -->
<!-- {{order: 'PK', 'FK', 'Header' }}                                  -->
<!-- {{entry = 'order'}}                                               -->

<!-- for each entery -->

- **{{label}}**: ({{partID}}) {{filter: "ReportTable" = {"PK" or "FK"}, value: "ReportTable"}} [{{dataType}}] {{partDescription}}. {{partNote}}
  <!-- if entry {{partType = 'measure'}} then the following to 'END partype = 'measure' -->
       - `{{label}}`: {{partDescription}}. {{partInstruction}}. [Aggreations]({{link to aggregation set}}). [Units]({{link to unit set}}).

## MeasureReport

<!-- same as Measur eTable>
