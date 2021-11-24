# <img src="img/ODM-logo.png" align="right" alt="" width="180"/> The Public Health Environmental Surveillance Open Data Model (PHES-ODM, or ODM)

<!-- badges: start -->

[![Lifecycle:
development](https://img.shields.io/badge/lifecycle-stable-green.svg)](https://lifecycle.r-lib.org/articles/stages.html#stable-1)
![](https://img.shields.io/github/v/release/big-life-lab/covid-19-wastewater?color=green&label=GitHub)
[![License: MIT](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![](https://img.shields.io/badge/doi-10.17605/OSF.IO/49Z2B-yellowgreen.svg)](https://osf.io/49z2b/)

<!-- badges: end -->

## Description

This repository includes:

- A relational **dictionary** that captures wastewater based surveillance data and metadata. It consists of 150+ variables categorized in 10 tables. Both English and French versions are supported;
- **Documentation** describing how to use the data model;
- **Template files** that can be used to record data in the ODM format;
- **Scripts** to set up a relational database according to the ODM schema.

## Background

Wastewater-based surveillance (WBS) of SARS-CoV-2 is developing and expanding rapidly during the current COVID-19 pandemic. WBS has demonstrated itself as valuable public health tool with an increasing number of municipalities that have identified new SARS-CoV-2 transmission using wastewater testing prior to clinical testing. Wastewater testing has also identified new surges and waves that has informed early public health response. Internationally, there are over 2000 testing sites in over 50 countries.

WBS has a history informing public health action through its use to monitor health threats such as polio, antimicrobial resistance, as well as illicit drugs, among others. However, as a surveillance tool for pandemic purposes, the program is relatively new and there are implementation gaps. Currently, there is little to no controlled vocabulary on how WBS results should ideally be reported. Hence, the idea of a WBS data model that captures all relevant fields that should ideally be reported on when sharing WBS data.

The ODM strives to improve wastewater surveillance through the development of an open data structure, including metadata and vocabulary. ODM operates under the guidance of an international [steering committee](https://github.com/Big-Life-Lab/covid-19-wastewater/wiki). Working groups can be ongoing or created to address specific tasks and projects. Note that we adhere to the [FAIR Guiding Principles](https://www.go-fair.org/fair-principles/) with recognition of benefit from a common data structure, including metadata and vocabulary.

## Data and metadata dictionary

The ODM is comprised of ten primary tables and one lookup table, linked to each other based on logic relationships. The following figure provides an overview of the different data sources that are currently captured.

![Schematic representation of the ODM](img/wastewater-map.png)

See [metadata](metadata_en.md) for more detailed information on variable names and definitions. Cliquez [ici](metadata_fr.md) pour la version française.

## Collaborate

Issues, suggestions and pull requests are welcomed. [contributing](CONTRIBUTING.md) for more information.

- [GH issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues) or email [phesd_odm@ohri.ca](mailto::phesd_odm@ohri.caa).
- [Code of conduct](CODE_OF_CONDUCT.md).
- Follow the [`dev`](https://github.com/Big-Life-Lab/covid-19-wastewater/tree/dev) branch for upcoming changes. Also follow version changes in [issues](https://github.com/Big-Life-Lab/covid-19-wastewater/issues), [discussions](https://github.com/Big-Life-Lab/covid-19-wastewater/discussions), and [projects](%3Chttps://github.com/Big-Life-Lab/covid-19-wastewater/projects).

## Keep in touch

Subscribe to OMD newletters to receive e-mails about new releases, working group announcements or general updates. [here](https://us20.list-manage.com/survey?u=dd9d7217c4c3932d1ee9ffcfe&id=e2feb67749&attribution=false).

Questions? E-mail at [phesd_odm@ohri.ca](mailto::phesd_odm@ohri.ca).

## Application

Institues across Canada and worldwide have adopted the ODM to structure SARS-CoV-2 WBS data. Programs that use the ODM include Canada's National Microbiology Laboratory (NML), Ontario's Wastewater Initiative by the Ministry of Environment, Conservation, and Parks (MECP), uOttawa, le Centre québécois de recherche sur la gestion de l'eau, Université Laval, and [CETO Epidemiologic platform](https://ceto.ca).

A dashboard using the Ottawa data can be found at: [613covid.ca](https://613covid.ca/wastewater). The [CentrEau](https://www.centreau.ulaval.ca/covid/) webpage hosts the dashboard for the province of Québec.

## Work-in-progress

- data dictionary - development of version 2.0 uderway, enhancements include the ability to reprot variants of concern, mutations, other environment testing sites (surface and air, inaddition to wastewater), improve reporting appraoch for quatlity control and quality assurance (QC and QA).
- data validation - ability to validate weather data adheres to the ODM dictionary.
- data cleaning and data transformation -
  - templates that allows wastewater labs to map their data format to ODM format.
  - an [application](https://github.com/martinwellman/odm-qpcr-analyzer) to map RT-PCR output to ODM format, including performing QC and QA.
- data visualization - visualizations based on ODM data format.
- data modelling - modelling based on ODM data format.

See [roadmap](roadmap.md) for more details.

What's coming to version 2.0.

<a href= "https://vimeo.com/649254159" title="Link Title"><img src="img/ODM-V2-video.png" alt="What's coming to version 2.0" width="350"/></a>

## Additional tools

Working group members maintain other repositories with tools that use the ODM, including:

- [data visualization](https://github.com/Big-Life-Lab/Ottawa-COVID-Projection).
- methods to convert Excel tables that are not in [ODM format into ODM data frame](https://github.com/jeandavidt/ODM-Import).

## License

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

See [license](LICENSE) for more information.

## Acknowledgements

Development and maintenance of the ODM is the result of a collaboration between researchers from multiple institutions:

- [CIHR Coronavirus Variants Rapid Response Network (CoVaRR-Net)](https://covarrnet.ca)- uOttawa
- The Ottawa Hospital
- Université Laval
- CHEO Research Institute
- modelEAU
- CentrEau - Centre québécois de recherche sur la gestion de l'eau
- Public Health Agency Canada
- Ministry of Environment, Conservation, and Parks - MECP Ontario
- European Union DG Joint Research Centre

## References

Nicolaï N., Therrien J.-D., Maere. T, Pileggi V., Swerdfeger H., Vanrolleghem P.A., Manuel D. (2021) Open Data Model for collecting, quality-ensuring and sharing of SARS-CoV-2 data and metadata, EU4S Sewage Sentinel System for SARS CoV-2 - 5th Town Hall Meeting, e-poster, https://api.ltb.io/show/ABCWX
