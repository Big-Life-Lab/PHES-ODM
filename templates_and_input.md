# Database templates and input forms

Several database templates are available to help labs enter data. Forms can be used to enter data, which can then be used to create templates for quick data entry.

## Database templates

Database templates are flat file templates (i.e. CSV file format) that are used to summarize wastewater SARS-CoV-2 measurements. There are two formats - 'wide' and 'long' that are based on the underlying primary databases that are described in Metadata.

-   **'Wide'** format - The main template is a 'wide' form that labs can use to enter one *sample* per row. The main variables are from the 'measurement' table, but there are also variables from other tables. Alternatively, variables from other tables can be collected separately.

-   **'Long'** format (TBA) - This template has one *measurement* per row. The long format more closely follows the primary databases.

## Input forms

Input forms correspond to the tables described in metadata. We have started Survey Monkey forms, which you can use to load into your Survey Monkey account. The input forms can also be used to generate database templates. The `Sample` form is used to create a wide measurement data table template. `Lab` and `Site` forms are first created to provide information to populate this form.

If you don't have a Survey Monkey account, we accept inquires if you would like to contribute data to this repository using our Survey Monkey forms. Ideally, the forms in this repository will be developed into a more robust content management system. Until that time, please provide suggestions on how to improve the forms. Use a pull request if you would like to contribute a template from other form approaches like Google Forms, Lime Survey, Red Cap, etc.

The `Measurement` form is the main form for entering sample measurements. `Lab`, `Site` and `Sample` forms are first created to provide information to populate this form.

-   **Laboratory form** - The basic Lab form is used to identify labs that perform wastewater testing. The form is based on `Lab` (lab.csv) database. Once completed, a `Site` form completed.

    Survey Monkey form: <https://ca.research.net/r/WWlab>

-   **Site form** - The Site form contains information about the site where wastewater samples are collected, such as the type of the site (i.e. Wastewater treatment plant). The form is based on the `Site` (site.csv) database. Once completed, a `Sample` form can be completed.

    Survey Monkey form: <https://ca.research.net/r/WWsite>

-   **Sample form** - The Sample form contains information about the wastewater sample, such as storage temperature. The Sample form also gene region(s) and measures which is used to create a template measurement. The Sample form based on the `Sample` (sample.csv) and `Measurement` (measurement.csv) databases.

    Survey Monkey form: <https://ca.research.net/r/WWsample>

-   **Measurement form** - The Measurement form is used to enter sample measurements. Labs use the Measurement form to rapidly enter sample measurements, which then population the wide and long summary tables.

    Survey Monkey measurement form: <https://ca.research.net/r/WWmeasurement>

    Below is an example of the Measurement form that is used for the Ottawa ROPEC wastewater treatment plant. The link includes custom variables to pre-populate the form. These variables can be customized for other labs and sites.

    At the ROPEC site, gene regions N1 and N2 are tested. Normalized mean and standard deviation are reported for each region using viral copies/copies PMMV.

    <https://ca.research.net/r/WWmeasurement?siteID=Ottawa-ROPEC&laboratoryID=uOttawa-CHEO&geneRegion_1=covidN1&geneRegion_2=covidN2&sampleUnit_1=&measureType_1=PPMV_meanNormal&measureType_2=PPMV_SDNormal>

    The data then populates the long form. [here](). The data used used for wastewater plots at [613covid.ca](https://613covid.ca/wastewater).
