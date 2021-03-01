<!-- metadata.md is generated from metadata_template.md Please edit metadata_template.md file -->
<!-- create metadata.md with wbe_metadata_write() in generate_db_generation_sql.R -->

# Métadonnées

Huit tableaux sont décrits ci-dessous. Exemple de données stockées dans [data](données).

FOR_REPLACE_LIST_OF_TABLES

## Diagramme des relations entre les entités

Utilisez le diagramme des relations entre les entités pour identifier le type de variable.

- **BLOB** : La chaîne codée en ASCII en minuscules représentant le type de média du Blob. Plus [détails](https://w3c.github.io/FileAPI/#dfn-type)
- **bool** : boolean, TRUE, FALSE
- **char** : Chaîne codée en ASCII
- **cat** : catégorie définie à l'aide d'une chaîne de caractères codée en ASCII, telle que définie pour la variable
- **dateHeure** : YYYY-MM-DD HH:mm:ss (format 24 heures, en UTC)
- **email** : adresse électronique
- **float** : valeur numérique à virgule flottante
- **int** : nombre entier
- **téléphone** : numéro de téléphone, soit ###-###-#### ou #-###-###-####
- **url** : Identificateur de ressources uniformes



![](img/ERD.svg)

Commentaire sur l'ERD dans [Lucidcharts](https://lucid.app/lucidchart/invitations/accept/adc1784b-e237-4a2f-947e-4503544d4510)




FOR_REPLACE_LIST_OF_TABLES_DETAILS


# Modèles de base de données et formulaires de saisie

Plusieurs modèles de base de données et formulaires de saisie sont en cours d'élaboration pour aider les laboratoires et autres partenaires à saisir les données.

Les modèles se trouvent dans le dossier [template](template).

Modèles disponibles :

*Modèles de base de données


- [`covid_wwtp_data_template.xlsx`](template/covid_wwtp_data_template.xlsx) - (ne pas utiliser - un premier exemple). Ce modèle n'est pas conforme à la version actuelle de l'ODM. Restez à l'écoute pour une version mise à jour.
- [wbe_create_tables.sql](src/wbe_create_tables.sql) - Code permettant de générer une base de données SQL.

## Modèles de base de données

Les modèles de base de données sont des modèles de fichiers plats (c'est-à-dire au format Excel ou CSV) qui sont utilisés pour résumer les mesures du SRAS-CoV-2 des eaux usées. Il existe deux formats - "large" et "long" - qui sont basés sur les bases de données primaires sous-jacentes décrites dans les métadonnées.

- Format "large "** - La forme "large" de saisie des données correspond à la manière dont les laboratoires conservent généralement leurs propres données. Ce formulaire comporte généralement un *échantillon* par ligne. Chaque échantillon correspond à un test effectué sur un échantillon d'eau usée prélevé un jour donné. Cela signifie que chaque ligne correspond à un seul jour. Les principales variables proviennent du tableau des "mesures", mais il existe également des variables provenant d'autres tableaux. Il est également possible de collecter séparément les variables d'autres tableaux.

- Format "long "** - Ce modèle comporte une *mesure* par ligne. Le format long suit l'ERD et le dictionnaire de données.

## Formulaires de saisie

Les formulaires de saisie correspondent aux tableaux décrits dans les métadonnées. Les formulaires Survey Monkey sont disponibles pour les versions antérieures de l'ODM, mais ils ne sont pas pris en charge dans la version la plus récente. Nous sommes au courant de plusieurs initiatives visant à générer Microsoft PowerApp et ArcGIS Survey123. Des mises à jour seront fournies ici à mesure que ces initiatives se développeront.

## Exemple de formats variables larges et longs

Les [métadonnées](metadata.md) et le [diagramme des relations entre les entités](metadata.md#entity-relationship-diagram) sont des formats de tableaux longs. 

### Exemple de déclaration de deux régions virales (N1 et N2) sur le même échantillon

Format de tableau long

|date |type|unité|agrégation|valeur
|----------|------|--------|-----------|-----|
|2021-01-15|covN1 |nPPMoV |moyenne |40 |
|2021-01-15|covN2 |nPPMov |moyenne |42 |

Format tableau large

|date |covN1_nPPMoV_mean|covN2_nPPMoV_mean|
|----------|-----------------|-----------------|
|2021-01-15|40 |42 |


## Ordre d'achèvement

En raison des relations multiples entre les tableaux composant le modèle de données, il est important que certains tableaux soient complétés avant que d'autres ne le soient. L'ordre d'achèvement suivant doit être respecté afin de s'assurer que les ensembles de données sont complets :

- Étape 1** : Instrument", "Polygone

- **Etape 2** : Site, méthode d'essai

- **Etape 3** : Labo

- **Etape 4** : "Rapporteur

- **Etape 5** : Échantillon + mesure de la santé publique ou mesure du site ou données de santé publique valables




## Conventions d'appellation

- **Noms de tables** : Les noms des tables utilisent la casse supérieure (UpperCamelCase).

- **Noms de variables et de catégories** : Les variables et les catégories de variables utilisent toutes deux la casse inférieure (lowerCamelCase). N'utilisez pas de caractères spéciaux (uniquement des majuscules, des minuscules et des chiffres). Raison : les noms de variables et de catégories peuvent être combinés pour générer des variables dérivées. L'utilisation de caractères spéciaux générera des caractères non autorisés - voir ci-dessous. Les noms de catégories ne doivent pas comporter plus de 7 caractères pour permettre la concaténation de quatre catégories en une seule variable afin de respecter le maximum de 31 caractères ArcGIS pour les noms de variables. 

- **Variables dans des tableaux larges** : Les tableaux larges utilisent `_` pour concaténer les variables des tableaux longs.

- **Ordre des variables** Si une mesure multiple a lieu à des dates différentes, cela a une forme naturelle dans le format de tableau long, cependant dans le format pivot large cela peut être ambigu. Dans ce cas, affichez un "reportDate" suivi d'une série de mesures prises à cette date (par exemple, `covN1_PPMV_mean`), puis d'autres mesures (par exemple, `covN2_PPMV_mean`)

- **Tableaux de fusion** : La fusion de tableaux en un tableau large nécessite des étapes supplémentaires lorsqu'une variable n'a pas de nom unique (lorsque le nom de la variable apparaît dans plus d'un tableau). Par exemple, des variables telles que "date/heure", "notes", "description", "type", "version" et "ID" comme "sampleID" sont utilisées dans plusieurs tableaux. Utilisez l'approche suivante :

    - Variables qui ne sont pas uniques (elles sont dans plus d'une table) : ajoutez le nom de la table à la variable en concaténant les noms de colonnes avec `_`. Par exemple, `dateTime` de la table `Sample` devient `Sample_dateTime`.
    - Variable qui sont uniques (elles ne se trouvent que dans une seule table dans l'OMD entier). Aucun changement de nom de variable n'est nécessaire.

- **Mesure dérivée, résumée ou transformée** : Ces mesures sont générées pour résumer ou transformer une ou plusieurs variables. La convention d'appellation suit la même approche que pour les noms de variables et de catégories, sauf qu'il faut utiliser un `_` lors de la concaténation des noms de variables ou de catégories.  Le calcul d'une valeur moyenne d'une ou plusieurs régions de la CoV-2 du SRAS est un exemple de mesure dérivée. La normalisation et la standardisation sont d'autres exemples de mesures transformées. Généralement, les mesures dérivées, résumées ou transformées ne sont pas rapportées, mais l'approche préférée est de rapporter les mesures individuelles sous-jacentes.

- **Date heure** : YYYY-MM-DD HH:mm:ss (format 24 heures, en UTC)

- **Localisation** : [texte bien connu](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) pour polygone.

- **Version** : [version sémantique](https://semver.org)

## Exemples de génération de noms de variables et de catégories larges

### 1) Rapport simple sur les régions virales

Un long tableau représenterait les mesures virales de :


``` {.markdown}
date = 2021-01-15
type = covN1
unit = nPMMoV
aggregation = mean
value = 40
```

``` {.markdown}
date = 2021-01-15
type = covN2
unit = nPMMoV
aggregation = mean
value = 42
```

Dans une longue table comme :

| date       | type  | unit   | aggregation | value |
|------------|-------|--------|-------------|-------|
| 2021-01-15 | covN1 | nPPMoV | mean        | 40    |
| 2021-01-15 | covN2 | nPPMoV | mean        | 42    |

Une large table représenterait la même mesure que :

``` {.markdown}
    covidN1_PPMV_mean = 40
    covidN2_PPMV_mean = 42
```

Dans une large table comme :

| date       | covN1_nPPMoV_mean | covN2_nPPMoV_mean |
|------------|-------------------|-------------------|
| 2021-01-15 | 40                | 42                |


### 2) Mesure dérivée

Pour communiquer une valeur moyenne des mesures existantes de covidN1 et covidN2 :

``` {.markdown}
    date = 2021-01-15
    type = covN1
    unit = ml
    aggregation = mean
    value = 42
```

``` {.markdown}
    date = 2021-01-15
    type = covN2
    unit = ml
    aggregation = mean
    value = 40
```

Représenter la mesure dérivée comme :

tableau long

``` {.markdown}
    date = 2021-01-15
    type = covN1covN2
    unit = ml
    aggreation = mean
    value = 41
```

| date       | type       | unit | aggregation | value |
|------------|------------|------|-------------|-------|
| 2021-01-15 | covN1covN2 | ml   | mean        | 41    |

ou, format tableau large

``` {.markdown}
    date = 2021-01-15
    covN1covN2_ml_mean = 41
```

- Copies de référence pour le SRAS-CoV-2.

### 3) Mesure transformée

Signaler les copies virales moyennes de valeur N1 et N2 par copie virale de PMMoV :

Représenter la mesure dérivée comme :

description longue du tableau

``` {.markdown}
    date = 2021-01-15
    covN1covN2 = 2
    unit = PPMV
    type = meanNr
```

ou,

format tableau large

``` {.markdown}
    covidN1covidN2_PPMV_meanNr = 2
```

