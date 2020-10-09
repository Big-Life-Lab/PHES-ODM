  # Ottawa Covid-19 Wastewater Dataset

This respoistory contains Ottawa covid-19 wastewater surveillance data. The metadata and reportin approach is evolving (see Collaborate).

### File naming convention
- **date**: MM/DD/YYYY HH:mm:ss  (24 hour format, in UTC).
- **location** TBD

## Wastewater singnal results (wastewater_covid-19.csv)
- **sampleDate**: Date wastewater sample collected. End date for continuous testing. Additional location information in `wastewater_site.csv`.
- **locationID**: Identifier for location where wastewater sample was taken. 
- **locationName**: Name corresponding to `locationName`: location name cojld be a treatment plant, campus, institution or sewer location, etc.
- **sampleID**: Unique sample identifier; locationID appended with sampleDate.
- **N1_PMMV_mean**:	mean SARS-CoV-2 N1 gene region standardized to Pepper mild mottle virus (PMMV) (mean SARV-CoV-2 copies per copies of PMMV).
- **N1_PMMV_sd**:	standard deviation of `N1_PMMV_mean`.
- **N2_PPMV_mean**:	mean SARS-CoV-2 N2 gene region standardized to Pepper mild mottle virus (PMMV) (mean SARV-CoV-2 copies per copies of PMMV).
- **N2_PPM_sd**: standard deviation of `N2_PMMV_mean`.
- **PMMV_Ct**: TBD

## Wastewater site information (wastewater_site.csv)
- **locationID**:	Identifier for location where wastewater sample was taken. `locationID` is the same in `wastewater_covid-19.csv`.
- **locationName**:	Name corresponding to `locationName`: location name cojld be a treatment plant, campus, institution or sewer location, etc. Additional location information in `wastewater_site.csv`.
- **sampleType**: Type of wastewater sample: 
  - sludge - 
- **catchmentPop**:	Number of people represented in the wastewater sample.
- **assayMethod**: Method used to assay viral signals.
- **creator**:	Person 
- **creatorEmail**:	
- **maintainer**:	
- **description**:
- **notes**:




## Colloborate to share wastewater data

## API

## Licence 

Website content is published under a Creative Commons CC BY 4.0 license, which requires users to attribute the source and license type (CC BY 4.0) when sharing our data or website content.

## Acknowledgement