# Ottawa Data Model (ODM) for Wastewater-Based Surveillance

## Description

This repository includes:

- A relational **dictionary** that captures wastewater based surveillance data and metadata. It consists of 150+ variables categorized in 10 tables. Both English and French versions are supported;
- **Documentation** describing how to use the data model;
- **Template files** that can be used to record data in the ODM format;
- **Scripts** to set up a relational database according to the ODM schema.

## Background
Wastewater-based surveillance (WBS) of SARS-CoV-2 is developing and expanding rapidly during the current COVID-19 pandemic. WBS has demonstrated itself as valuable public health tool with an increasing number of municipalities that have identified new SARS-CoV-2 transmission using wastewater testing prior to clinical testing. Wastewater testing has also identified new surges and waves that has informed early public health response. Internationally, there are over 2000 testing sites in over 50 countries.

WBS has a history informing public health action through its use to monitor health threats such as polio, antimicrobial resistance, as well as illicit drugs, among others. However, as a surveillance tool for pandemic purposes, the program is relatively new and there are implementation gaps. Currently, there is little to no controlled vocabulary on how WBS results should ideally be reported. Hence, the idea of a WBS data model that captures all relevant fields that should ideally be reported on when sharing WBS data.

The ODM strives to improve wastewater surveillance through the development of an open data structure, including metadata and vocabulary. OMD operates under the guidance of an international [steering committee](https://github.com/Big-Life-Lab/covid-19-wastewater/wiki). Working groups can be ongoing or created to address specific tasks and projects. Note that we adhere to the [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) with recognition of benefit from a common data structure, including metadata and vocabulary.

## Data and metadata dictionary

See [metadata](metadata_en.md) for variable names and definitions. Cliquez [ici](metadata_fr.md) pour la version française.

## Collaborate

Issues, suggestions and pull requests are welcomed. See [contributing](CONTRIBUTING.md) for more information. See [GH issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues) or email [dmanuel\@ohri.ca](mailto:dmanuel@ohri.ca).

Follow the [`dev`](https://github.com/Big-Life-Lab/covid-19-wastewater/tree/dev) branch for upcoming changes. Also follow version changes in [issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues), [discussions](https://github.com/Big-Life-Lab/covid-19-wastewater/discussions), and [projects](%3Chttps://github.com/Big-Life-Lab/covid-19-wastewater/projects).


## Application

Institues across Canada and worldwide have adopted the ODM to structure SARS-CoV-2 WBS data. Programs that use the ODM include Canada's National Microbiology Laboratory (NML), Ontario's Wastewater Initiative by the Ministry of Environment, Conservation, and Parks (MECP), uOttawa, le Centre québécois de recherche sur la gestion de l'eau, Université Laval, and [CETO Epidemiologic platform](https://ceto.ca).

A dashboard using the Ottawa data can be found at: [613covid.ca](https://613covid.ca/wastewater). The [CentrEau](https://www.centreau.ulaval.ca/covid/) webpage host the dashboard for the province of Québec. 

## Work-in-progress

- data validation;
- data cleaning and data transformation;
- data visualization;
- data modelling;

See [roadmap](roadmap.md) for more details.

## Additional tools

Working group members maintain other repositories with tools that use the OMD, including:

- [data visualization](https://github.com/Big-Life-Lab/Ottawa-COVID-Projection).
- methods to convert Excel tables that are not in [ODM format into ODM data frame](https://github.com/jeandavidt/ODM-Import).

## License

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

See [license](LICENSE) for more information.

## Acknowledgements

Development and maintenance of the ODM is the result of a collaboration between researchers from multiple institutions:
- uOttawa
- The Ottawa Hospital
- Ottawa Public Health
- CHEO Research Institute
- Université Laval
- modelEAU
- CentrEau - Centre québécois de recherche sur la gestion de l'eau
- Public Health Agency Canada
- Ministry of Environment, Conservation, and Parks - MECP Ontario
- ...

## References
Nicolaï N., Therrien J.-D., Maere. T, Pileggi V., Swerdfeger H., Vanrolleghem P.A., Manuel D. (2021) Open Data Model for collecting, quality-ensuring and sharing of SARS-CoV-2 data and metadata, EU4S Sewage Sentinel System for SARS CoV-2 - 5th Town Hall Meeting, e-poster, https://api.ltb.io/show/ABCWX
