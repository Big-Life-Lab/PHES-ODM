# Inputing data

ODM has in nine data entry tables. Two tables record information on samples (SampleReport) and measures from sample (MeasureReport). The remaining seven table are generally used for initial set-up and they are not regularly updated. Example Excel data entry templates is in [templates]().

Tables that are updated regularly:

- [**SampleReport**](#SampleReport) A sample is a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).

....
....

Tables that are created initially or once, with few updates

- Address - The table that contains information about addresses.

<!-- list of tables that is generated from parts.csv -->

## [SampleReport]

A sample is a representative volume of wastewater, air, or surface substance taken from a Site which is then analysed by a lab (organization).

<!-- {{select: 'SampleReport', filter: {'Input', 'FK', 'Header', 'PK' }} -->
<!-- {{order: 'PK', 'FK', 'Header' }}                                  -->
<!-- {{entry = 'order'}}                                               -->

<!-- for each entery -->

- **{{label}}**: ({{partID}}) {{filter: "ReportTable" = {"PK" or "FK"}, value: "ReportTable"}} [{{dataType}}] {{partDescription}}. {{partNote}}
  <!-- if entry {{partType = 'measure'}} then the following to 'END partype = 'measure' -->
       - `{{label}}`: {{partDescription}}. {{partInstruction}}. [Aggreations]({{link to aggregation set}}). [Units]({{link to unit set}}).

## MeasureReport

<!-- same as Measur eTable>
