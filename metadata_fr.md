<!-- metadata.md is generated from metadata_template.md Please edit metadata_template.md file -->
<!-- create metadata.md with wbe_metadata_write() in generate_db_generation_sql.R -->

# Métadonnées

Huit tableaux sont décrits ci-dessous. Exemple de données stockées dans [data](données).

-	[Sample](#Sample)
-	[WWMeasure](#WWMeasure)
-	[Site](#Site)
-	[SiteMeasure](#SiteMeasure)
-	[Reporter](#Reporter)
-	[Lab](#Lab)
-	[AssayMethod](#AssayMethod)
-	[Instrument](#Instrument)
-	[Polygon](#Polygon)
-	[CovidPublicHealthData](#CovidPublicHealthData)
-	[Lookup](#Lookup)

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




## Sample

L'échantillon est un volume d'eau usée représentatif de l'eau présente sur un site, qui est ensuite analysé en laboratoire.

-	**sampleID**:(Identifiant de l'échantillon): (Primary Key) [string] Identifiant unique pour l'échantillon. Suggestion:siteID-date-index.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Crée un lien avec la table "Site" pour décrire le point d'échantillonage.


-	**dateTime**:(Date et heure): [datetime] Date, heure et fuseau horaire de collecte d'un échantillon ponctuel.


-	**dateTimeStart**:(Date et heure de début): [datetime] Date, heure et fuseau horaire de début de collecte d'un échantillon composite.


-	**dateTimeEnd**:(Date et heure de fin): [datetime] Date, heure et fuseau horaire de fin de collecte d'un échantillon composite.


-	**type**:(Type): [category] Type d'échantillon.
	-	`rawWW`: Eau usée brute
	-	`swrSed`: Sédiments provenant des égouts.
	-	`pstGrit`: Eau usée après dégrillage et dessablage.
	-	`pSludge`: Boue provenant d'un décanteur primaire.
	-	`pEfflu`: Effluent obtenu après un décanteur primaire.
	-	`sSludge`: Boue provenant d'un décanteur secondaire.
	-	`sEfflu`: Effluent obtenu après un décanteur secondaire.
	-	`water`: Eau non-usée provenant de toute étendue d'eau.
	-	`faeces`: Matière fécale.
	-	`other`: Autre type de site d'échantillonnage. Ajouter une description dans la colonne "typeOther"

-	**typeOther**:(Type autre): [string] Description d'un type d'échantillon ne faisant pas partie des options disponibles.


-	**collection**:(Méthode de collecte): [category] Méthode utilisée pour échantillonner.
	-	`cpTP24h`: Un échantillon composite proportionnel au temps prélevé sur 24 heures, généralement prélevé par un auto-échantilonneur.
	-	`cpFP24h`: Un échantillon composite proportionnel au débit prélevé sur 24 heures, généralement prélevé par un auto-échantilonneur.
	-	`grb`: Un seul échantillon ponctuel représentatif.
	-	`grbCp8h`: Un échantillon composite prélevé sur 8 heures consitué d'échantillons ponctuels collectés une fois par heure, généralement prélevé manuellement.
	-	`grbCp3h`: Un échantillon composite prélevé sur 3 heures consitué d'échantillons ponctuels collectés une fois par heure, généralement prélevé manuellement.
	-	`grbCp3`: Un échantillon composite composé de 3 échantillons ponctuels.
	-	`mooreSw`: Un échantillon passif collecté par la méthode de Moore.
	-	`other`: Autre méthode de collecte. Ajouter une description dans la colonne "descriptionOther"

-	**collectionOther**:(Méthode de collecte autre): [string] Description d'une méthode d'échantillonnage ne faisant pas partie des options disponibles.


-	**preTreatment**:(Pré-traitement): [boolean] L'échantillon a-t-il été chimiquement altéré par un ajout de stabilisant ou autre?


-	**preTreatmentDescription**:(Description du pré-traitment): [string] Description du pré-traitement le cas échéant.


-	**pooled**:(Échantillon combiné): [boolean] S'il s'agit d'un échantillon combiné, c'est-à-dire s'il est composé de plusieurs échantillons "enfants"?


-	**children**:(Enfants): [string] Si l'échantillon est liée à des sous-échantillons (soit parce qu'il s'agit d'un échantillon combiné ou parce que des sous-échantillons ont été prélevés dans cet échantillon), insérer les identifiant des échantillons enfants dans une liste séparée par des virgules.


-	**parent**:(Parent): [string] Si l'échantillon a été combiné à un plus grand échantillon, indiquer l'identifiant du plus grand échantillon.


-	**sizeL**:(Volume l): [float] Volume total d'eau ou de boue prélevée.


-	**fieldSampleTempC**:(Température de l'échantillon de terrain c): [float] Temprature à laquelle l'échantillon était stocké pendant l'échantillonnage. Ce champ est principalement pertinent pour les échantillons composites, qui peuvent être stockées à température ambiante ou réfrigérés durant l'échantillonnage.


-	**shippedOnIce**:(Expédié sur glace): [boolean] L'échantillon a-t-il été gardé au froid lors du transport vers le laboratoire?


-	**storageTempC**:(Température de stockage c): [float] Température de stockage de l'échantillon en degrés Celsius


-	**qualityFlag**:(Indicateur de mauvaise qualité): [boolean] Le reporteur a-t-il des doutes sur la qualité de l'échantillon?


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## WWMeasure

Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".

-	**uWwMeasureID**:(id u mesure eaux usées): (Primary Key) [string] Identifiant unique pour la mesure pour la table "WWMeasurement"


-	**wwMeasureID**:(id mesure eaux usées): [string] Identifiat unique utilisé dans la table horizontale seulement. Utiliser quand toutes les mesures effectuées sur un échantillon sont réalisées en même temps dans le même laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.


-	**sampleID**:(Identifiant de l'échantillon): (Foreign key) [string] Crée un lien avec la table "Sample" pour décrire l'échantillon mesuré.


-	**labID**:(Identifiant du laboratoire): (Foreign key) [string] Crée un lien avec la table "Lab" pour décrire le laboratoire effectuant la mesure.


-	**assayID**:(Identifiant de la méthode d'analyse): (Foreign key) [string] Crée un lien avec la table "AssayMethod" pour décrire la méthode employée pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Crée un lien avec la table "Instrument" l'appareil employé pour effectuer la mesure. Utiliser l'identifiant de la méthode d,analyse pour les mesures virales.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Crée un lien avec les informations propres au reporteur associé à la mesure.


-	**analysisDate**:(Date de l'analyse): [date] Date à laquelle la mesure a été réalisée en laboratoire.


-	**reportDate**:(Date de reportage de la donnée): [date] Date a laquelle la donnée a été reportée. Un échantillon pourrait avoir des mesures pour lesquelles la méthode d'analyse ou la méthode de reportage des données aurait changée. Dans ce cas, utiliser le même sampleID, mais créer une nouvelle entrée dans la table "WWMeasure avec un "MeasureID" différent, et la date de reportage de la donnée et l'identifiant de la méthode d'analyse appropriés.


-	**fractionAnalyzed**:(Fraction analysée): [category] Fraction de l'échantillon employée pour la mesure.
	-	`liquid`: Fraction liquide.
	-	`solid`: Fraction solide.
	-	`mixed`: Échantillon homogénéisé/mélangé.

-	**type**:(Type): [category] Le paramètre mesuré avec cette analyse. Exemples: Une région de gène cible (cov), un biomarqueur (n) ou un indicateur de la qualité de l'eau (wq)
	-	`covN1`: Gène nucleocapside N1 du SARS-CoV-2
	-	`covN2`: Gène nucleocapside N2 du SARS-CoV-2
	-	`covN3`: Gène nucleocapside N3 des virus similaires au SARS
	-	`covE`: Région génique E du SARS-CoV-2
	-	`varB117`: Variant B.1.1.7
	-	`varB1351`: Variant B.1.351
	-	`varP1`: Variant P.1
	-	`covRdRp`: Région génique RdRp du SARS-CoV-2
	-	`nPMMoV`: Virus de la marbrure légère du piment
	-	`ncrA`: CrAssphage
	-	`nbrsv`: Virus respiratoire syncytial bovin
	-	`wqTS`: Solides totaux
	-	`wqTSS`: Matières en suspension
	-	`wqVSS`: Matières volatiles en suspension
	-	`wqCOD`: Demande chimique en oxygène
	-	`wqOPhos`: Concentration d'ortho-phosphates
	-	`wqNH4N`: Concentrsation d'azote ammoniacal, exprimé en N.
	-	`wqTN`: Azote total, exprimé en N
	-	`wqPh`: pH
	-	`wqCond`: Conductivité
	-	`other`: Autre catégorie de mesure. Ajouter une description de la catégorie dans la colonne "categoryOther".

-	**typeOther**:(Type autre): [string] Description d'un paramètre mesuré ne faisant pas partie des options disponibles.


-	**unit**:(Unité): [category] Unité de mesure.
	-	`gcPMMoV`: Copies de gène ou de variant par copie de PMMoV
	-	`gcMl`: Copies de gène ou de variant par millilitre.
	-	`gcGs`: Copies de gène ou de variant par gramme de solides.
	-	`gcL`: Copies de gène ou de variant par litre.
	-	`gcCrA`: Copies de gène ou de variant par copie de CrAssphage
	-	`Ct`: Cycle seuil.
	-	`mgL`: Milligrammes par litre.
	-	`ph`: Unités de pH
	-	`uScm`: Microsiemens par centimètre.
	-	`detected`: Copies de gène ou de variant détecté dans "sampleGene". 1=Detecté, 0=Non-détecté.
	-	`porpVar`: Proportion du variant dans l'échantillon
	-	`pp`: Pourcentage de positifs (méthode de Moore)
	-	`pps`: Pourcentage de boues primaire (pour solides totaux)
	-	`other`: Autre mesure de copies virales ou de qualité des eaux usées. Ajouter une description dans "unitOther"

-	**unitOther**:(Unité autre): [string] Description d'une unité de mesure ne faisant pas partie des options disponibles.


-	**aggregation**:(Agrégation): [category] Indicateur statistique utilisée pour rapporter la mesure effectuée. Chaque agrégation doit être reportée comme une mesure différente (avec un identifiant différent)
	-	`single`: La valeur n'a subi aucune agrégation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut être un réplica.
	-	`mean`: Moyenne arithmétique.
	-	`meanNr`: Moyenne arithmétique normalisée.
	-	`geoMn`: Moyenne géométrique.
	-	`geoMnNr`: Moyenne géométrique normalisée.
	-	`median`: Médiane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'écart type.
	-	`sdNr`: L'écart type normalisé.
	-	`other`: Autre méthode d'agrégation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agrégation autre): [string] Description d'une agrégation ne faisant pas partie des options disponibles.


-	**index**:(Index): [integer] Index de la mesure dans le cas où la même mesure a été prise en replicata.


-	**value**:(Valeur): [float] La valeur numérique de la mesure effectuée.


-	**qualityFlag**:(Indicateur de mauvaise qualité): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualité?


-	**accessToPublic**:(Accès au public): [boolean] Si "Non", la donnée ne sera pas accessible par le public. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToAllOrg**:(Accès à toutes les organisations): [boolean] Si "Non", la donnée ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToSelf**:(Accès au reporteur lui-même): [boolean] Si "Non", la donnée ne sera pas accessible par le reporteur lui-même. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToPHAC**:(Accès à l'ASPC): [boolean] Si "Non", la donnée ne sera pas accessible par les employés de l'Agence de Santé Publique du Canada. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToLocalHA**:(Accès à l'autorité de santé publique locale): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique locales. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToProvHA**:(Accès à l'autorité de santé publique provinciale): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée sera accessible à l'autorité de santé publique de la province où l'échantillonnage a été réalisée.


-	**accessToOtherProv**:(Accès aux autres prov): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToDetails**:(Accès aux détails): [boolean] Indique si des informations supplémentaires sur la confidentialité de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Site

Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"

-	**siteID**:(Identifiant du site): (Primary Key) [string] Identifiant unique pour l'échantillon. Suggestion:siteID-date-index.


-	**name**:(Nom): [string] Nom du site d'échantillonnage. Peut être le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'égouts, etc.


-	**description**:(Description): [string] Description du site d'échantillonnage (ville, bâtiment, rue, etc.) pour mieux identifier le site d'échantillonnage.


-	**type**:(Type): [category] Type de site ou d'institution du site d'échantillonnage.
	-	`airPln`: Avion.
	-	`corFcil`: Prison.
	-	`school`: École.
	-	`hosptl`: Hôpital.
	-	`ltcf`: Établissement de soins de longue durée.
	-	`swgTrck`: Camion de vidange.
	-	`uCampus`: Campus universitaire.
	-	`mSwrPpl`: Collecteur d'égouts.
	-	`pStat`: Station de pompage.
	-	`holdTnk`: Bassin de stockage.
	-	`retPond`: Bassin de rétention.
	-	`wwtpMuC`: Station de traitement des eaux usées municipales pour égouts combinés.
	-	`wwtpMuS`: Station de traitement des eaux usées municipales pour égouts sanitaires seulement.
	-	`wwtpInd`: Station de traitement des eaux usées industrielle.
	-	`lagoon`: Système de lagunage pour traitement des eaux usées.
	-	`septTnk`: Fosse septique.
	-	`river`: Rivière, étendue d'eau naturelle.
	-	`lake`: Lac, étendue d'eau naturelle.
	-	`estuary`: Estuaire, étendue d'eau naturelle.
	-	`sea`: Mer, étendue d'eau naturelle.
	-	`ocean`: Océan, étendue d'eau naturelle.
	-	`other`: Autre type de site. Ajouter une description dans "typeOther".

-	**typeOther**:(Type autre): [string] Description du site d'échantillonnage dans le cas où une description adéquate n'est pas disponible.


-	**sampleTypeDefault**:(Type d'échantillon par défaut): [category] Type d'échantilon utilisé par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "type" dans la table "Sample"


-	**sampleTypeOtherDefault**:(Type d'échantillon autre défaut): [string] Type d'échantilon utilisé par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "typeOther" dans la table "Sample"


-	**sampleCollectionDefault**:(Prélévement d'échantillons par défaut): [category] Méthode d'échantillonnage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "collection" dans la table "Sample"


-	**sampleCollectOtherDefault**:(Prélévement d'un autre échantillon par défaut): [string] Méthode d'échantillonnage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "collectionOther" dans la table "Sample"


-	**sampleStorageTempCDefault**:(Température de stockage de l'échantillon c par défaut): [float] Tempéraure de stockage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "storageTempC" dans la table "Sample"


-	**measureFractionAnalyzedDefault**:(Fraction de mesure analysée par défaut): [category] Fraction par défaut quand une nouvelle mesure est créée pour cet échantillon. Se référer à la colonne "fracgtionAnalyzed" dans la table "WWMeasure"


-	**geoLat**:(Géo lat): [float] Position géographique du site d'échantillonnage. Latitude exprimée en coordonnées décimales (ex. 45.424721)


-	**geoLong**:(Géo long): [float] Position géographique du site d'échantillonnage. Longitude exprimée en coordonnées décimales (ex. -75.695000)


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Crée un lien vers la table "Polygon". Le polygon lié devrait englober la région qui se draine dans le site d'échantillonnage.


-	**sewerNetworkFileLink**:(Lien vers le fichier du réseau d'égouts): [string] Lien vers un fichier contenant toute information additionnelle au sujet du réseau d'égouts associé à ce site d'échantillonnage (tous les formats sont acceptés).


-	**sewerNetworkFileBLOB**:(Fichier blob du réseau d'égouts): [blob] Un fichier contenant toute information additionnelle au sujet du réseau d'égouts associé à ce site d'échantillonnage (tous les formats sont acceptés).

## SiteMeasure

Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".

-	**uSiteMeasureID**:(Identifiant unique de la mesure sur site): (Primary Key) [string] Identifiant unique pour le site d'échantillonnage.


-	**siteMeasureID**:(Identifiant de la mesure sur site): [string] Identifiat unique utilisé dans la table horizontale seulement. Utiliser quand toutes les mesures effectuées sur le même échantillon.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Crée un lien vers la table "Site" pour décrire le site d'échantillonnage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Crée un lien vers la table "Instrument" pour décrire l'appareil utilisé pour effectuer la mesure.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Crée un lien avec les informations propres au reporteur associé à la mesure.


-	**dateTime**:(Date et heure): [date] Date à laquelle la mesure a été réalisée.


-	**type**:(Type): [category] Type de mesure réalisée. Le préfixe "env" est utilisé pour une variable envioronnementale, alors que "ww" indique une mesure réalisée sur les eaux usées.
	-	`envTemp`: Température ambiante.
	-	`envRnF`: Pluie (toute précipitation sous forme liquide).
	-	`envSnwF`: Neige (toute précipitations sous forme solide).
	-	`envSnwD`: Épaisseur de neige au sol.
	-	`wwFlow`: Débit d'eau usée.
	-	`wwTemp`: Température de l'eau usée.
	-	`wwTSS`: Matières en suspension
	-	`wwCOD`: Demande chimique en oxygène
	-	`wwTurb`: Turbidité
	-	`wwOPhos`: Concentration d'ortho-phosphates
	-	`wwNH4N`: Concentrsation d'azote ammoniacal, exprimé en N.
	-	`wwTN`: Azote total, exprimé en N
	-	`wwpH`: pH
	-	`wwCond`: Conductivité

-	**typeOther**:(Type autre): [string] Description d'un paramètre mesuré ne faisant pas partie des options disponibles.


-	**typeDescription**:(Description du type): [string] Ajouter toutes notes additionnelles en lien avec la mesure effectuée.


-	**aggregation**:(Agrégation): [category] Méthode d'agrégation utiliseée pour rapporter la mesure.
	-	`single`: La valeur n'a subi aucune agrégation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut être un réplica.
	-	`mean`: Moyenne arithmétique.
	-	`meanNr`: Moyenne arithmétique normalisée.
	-	`geoMn`: Moyenne géométrique.
	-	`geoMnNr`: Moyenne géométrique normalisée.
	-	`median`: Médiane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'écart type.
	-	`sdNr`: L'écart type normalisé.
	-	`other`: Autre méthode d'agrégation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agrégation autre): [string] Description d'une agrégation ne faisant pas partie des options disponibles.


-	**aggregationDesc**:(Agrégation desc): [string] Informations (ou référence) liée(s) à la méthode d'agrégation utilisée pour rapporter la mesure.


-	**value**:(Valeur): [float] La valeur numérique de la mesure effectuée.


-	**unit**:(Unité): [string] L'unité de mesure


-	**qualityFlag**:(Indicateur de mauvaise qualité): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualité?


-	**accessToPublic**:(Accès au public): [boolean] Si "Non", la donnée ne sera pas accessible par le public. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToAllOrgs**:(Accès à toutes les organisations): [boolean] Si "Non", la donnée ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToSelf**:(Accès au reporteur lui-même): [boolean] Si "Non", la donnée ne sera pas accessible par le reporteur lui-même. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToPHAC**:(Accès à l'ASPC): [boolean] Si "Non", la donnée ne sera pas accessible par les employés de l'Agence de Santé Publique du Canada. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToLocalHA**:(Accès à l'autorité de santé publique locale): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique locales. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToProvHA**:(Accès à l'autorité de santé publique provinciale): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée sera accessible à l'autorité de santé publique de la province où l'échantillonnage a été réalisée.


-	**accessToOtherProv**:(Accès aux autres provinces): [boolean] Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée leur sera accessible.


-	**accessToDetails**:(Accès aux détails): [boolean] Indique si des informations supplémentaires sur la confidentialité de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Reporter

Le reporteur ou l'organisation responsable de la collecte de données ou responsable de la qualité des données reportées.

-	**reporterID**:(Identifiant du reporteur): (Primary Key) [string] Identifiant unique pour la personne ou l'organisation responsable des données rapportées.


-	**siteIDDefault**:(Identifiant du site par défaut): (Foreign key) [string] Identifiant de Site utilisé par défaut quand un nouvel échantillon est créé par ce reporteur. Se référer à la colonne "siteID" dans la table "Site"


-	**labIDDefault**:(Identifiant laboratoire par défaut): (Foreign key) [string] Identifiant de Lab utilisé par défaut quand un nouvel échantillon est créé par ce reporteur. Se référer à la colonne "labID" dans la table "Lab"


-	**contactName**:(Nom du contact): [string] Nom complet du reporter (personne ou organisation)


-	**contactEmail**:(Adresse électronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(Téléphone du contact): [string] Numéro de téléphone du contact.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Lab

Laboratoire effectuant des analyses d'échantillons d'eaux usées d'un ou plusieurs sites.

-	**labID**:(Identifiant du laboratoire): (Primary Key) [string] Identifiant unique pour le laboratoire.


-	**assayMethodIDDefault**:(Identifiant de la méthode d'analyse par défaut): (Foreign key) [string] Identifiant de la méthode d'analyse utilisée par défaut quand une nouvelle mesure est créé par ce laboratoire. Se référer à la colonne "assayMethodID" dans la table "AssayMethod"


-	**name**:(Nom): [string] Nom du laboratoire.


-	**contactName**:(Nom du contact): [string] Personne contact de ce laboratoire.


-	**contactEmail**:(Adresse électronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(Téléphone du contact): [string] Numéro de téléphone du contact.


-	**updateDate**:(Date de mise à jour): [date] Date où l'information a été reportée une première fois ou mise à jour.

## AssayMethod

La méthode d'analyse utilisée pour réaliser les mesures. Crée une nouvelle rangée dans cette table si des changements (améliorations) sont apportées à une technique d'analyse existante. Garder le même identifiant et modifier le numéro de version. Une nouvelle rangée représentant une nouvelle version d'une méthode existante peut inclure des informations seulement dans les colonnes qui ont changé d'une version à l'autre, cependant, nous recommandons de remplir les autres colonnes avec les valeurs provenant de la version précédente afin de décrire clairement la méthode en entier. Ajouter la date courante lorsqu'une nouvelle rangée est créée.

-	**assayMethodID**:(Identifiant de la méthode d'analyse): (Primary Key) [string] Identifiant unique pour la méthode d'analyse.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Crée un lien vers la table "Instrument" pour décrire l'appareil utilisé pour effectuer la mesure.


-	**name**:(Nom): [string] Nom de la méthode d'analyse.


-	**version**:(Version): [string] Version de la méthode d'analyse. Un versionnement de type sémantique est recommandé.


-	**summary**:(Résumé): [string] Brève description de la méthode d'analyse et de comment celle-ci diffère d'autres méthodes.


-	**referenceLink**:(Lien vers référence): [string] Lien vers la procédure standard.


-	**date**:(Date): [date] Date à laquelle la méthode d'analyse (ou une nouvelle version d'une méthode existante) a été crée.


-	**aliasID**:(Identifiant de l'alias): [string] Identifiants d'autres méthodes d'analyse présentes dans la table qui sont similaires à la méthode courante. Insérer sous forme de liste séparée par des virgules.


-	**sampleSizeL**:(Volume de l'échantillon l): [float] Volume de l'échantillon analysé (en litres)


-	**loq**:(Limite de quantification): [float] Limite de quantification pour cette méthode, le cas échéant.


-	**lod**:(Limite de détection): [float] Limite de détection pour cette méthode, le cas échéant.


-	**unit**:(Unité): [category] Unité de mesure utilisée par cette méthode et qui est applicable pour la limite de détection ou de quantification.
	-	`gcPMMoV`: Copies de gène ou de variant par copie de PMMoV
	-	`gcMl`: Copies de gène ou de variant par millilitre.
	-	`gcGms`: Copies de gène ou de variant par gramme de solides.
	-	`gcL`: Copies de gène ou de variant par litre.
	-	`gcCrA`: Copies de gène ou de variant par copie de CrAssphage
	-	`other`: Autre mesure de copies virales ou de qualité des eaux usées. Ajouter une description dans "unitOther"

-	**unitOther**:(Unité autre): [string] Unité de mesure utilisée par cette méthode et qui est applicable pour la limite de détection ou de quantification dans le cas où celle-ci n'est pas disponible.


-	**methodConc**:(Méthode de concentration): [string] Description de la méthode utilisée pour concentrer l'échantillon.


-	**methodExtract**:(Méthode d'extraction): [string] Description de la méthode utilisée pour extraire l'échantillon.


-	**methodPcr**:(Méthode PCR): [string] Description de la m.éthode PCR utiisée.


-	**qualityAssQC**:(Contrôle de qualité): [string] Description des étapes de contrôle de qualité mises en place dans la méthode.


-	**inhibition**:(Inhibition): [string] Description des paramètres d'inhibition liés à cette méthode.


-	**surrogateRecovery**:(Récupération du virus substitut): [string] Description de la méthode de récupération du virus de substitution liée à cette méthode.

## Instrument

L'instrument utilisé pour mesurer les échantillons et l'eau usée des sites d'échantillonnage. La méthode d'analyse pour les mesures virales sont décrites dans la table "AssayMethod".

-	**instrumentID**:(Identifiant de l'instrument): (Primary Key) [string] Identifiant unique pour l'instrument de mesure.


-	**name**:(Nom): [string] Nom de l'instrument de mesure.


-	**model**:(Modèle): [string] Numéro de modèle et/ou de version de l'instrument de mesure.


-	**description**:(Description): [string] Description de l'instrument.


-	**alias**:(Alias): [string] Identifiants d'autres instruments présents dans la table qui sont similaires à l'instrument courant. Insérer sous forme de liste séparée par des virgules.


-	**referenceLink**:(Lien vers référence): [string] Lien vers un document de référence pour l'instrument de mesure.


-	**type**:(Type): [category] Type de l'instrument de mesure.
	-	`online`: Capteur en ligne.
	-	`lab`: Analyse en laboratoire.
	-	`hand`: Mesure à l'aide d'un capteur manuel.
	-	`atline`: Mesure à l'aide d'un échantillonneur.
	-	`other`: Autre type d'appareil de mesure. Ajouter une description dans "instrumentTypeOther"

-	**typeOther**:(Type autre): [string] Description du type d'instrument dans le cas où il ne serait pas disponible.

## Polygon

Polygone englobant une région de la surface terrestre. Normalement, ces polygones représentent soit des bassin de drainage d'un réseau d'égouts ou une région de santé publique, ou une autre région associée à des données reportées.

-	**polygonID**:(Identifiant du polygone): (Primary Key) [string] Identifiant unique du polygone.


-	**name**:(Nom): [string] Nom du polygon (devrait être descriptif)


-	**pop**:(Population): [integer] Population approximative vivant dans la région représentée par le polygone.


-	**type**:(Type): [category] Type de polygone.
	-	`swrCat`: Zone de captage d'un réseau d'égout.
	-	`hlthReg`: Région de santé desservie par le réseau d'égout.

-	**wkt**:(Wkt): [string] Description formelle du polygone (format Well-Known-Text (wkt))


-	**file**:(Fichier): [blob] Fichier représentant la géométrie du polygone (blob).


-	**link**:(Lien): [string] Lien vers une référence externe décrivant la géométrie du polygone.

## CovidPublicHealthData

Données de patients pour la COVID-19 pour une région spécifiée par un polygone.

-	**cphdID**:(Identifiant de CPHD): (Primary Key) [string] Identifiant unique pour l'information de santé publique reportée.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Identifiant unique pour la personne ou l'organisation responsable des données rapportées.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Crée un lien vers la table "Polygon". Le polygon lié devrait englober la région représentée par les données consignées ici.


-	**date**:(Date): [string] Date de reportage des données de mesure de la COVID-19.


-	**type**:(Type): [category] Type de donnée de mesure de la COVID-19.
	-	`conf`: Nombre de cas confirmés. La mesure devrait être accompagnée d'une valeur dans la colonne "dateType"
	-	`active`: Nombre de cas actifs.
	-	`test`: Nombre de tests effectués.
	-	`posTest`: Nombre de tests positifs.
	-	`pPosRt`: Pourcentage de positivité des tests.
	-	`hospCen`: Rencensement des patients admis à un hôpital avec la COVID-19.
	-	`hospAdm`: Nombre d'admissions ou nombre de patients admis à l'hôpital.

-	**dateType**:(Type de date): [category] Type de date utiisée pour reporter les données.
	-	`episode`: Date estimée à laquelle l'épisode de maladie s'est déclaré. Habituellement calculé en se basant sur la date des premiers symptômes, la date de test ou la date de reportage.
	-	`onset`: Date à laquelle les premiers symptômes apparaissent. Cette donnée est souvent inconnue. La date d'épisode est alors communément utilisée.
	-	`report`: Date à laquelle la donnée a été reportée à la santé publique. Cette mesure est communément utilisée.
	-	`test`: Date à laquelle le test de COVID-19 a été effectué.

-	**value**:(Valeur): [float] La valeur numérique de la mesure reportée.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Lookup

Utiliser pour retrouver les valeurs associées aux colonnes contenant des données catégoriques.

-	**tableName**:(Nom de la table): [string] Nom de la table.


-	**columnName**:(Nom de la colonne): [string] Nom de la colonne.


-	**value**:(Valeur): [string] Nom de la valeur.


-	**description**:(Description): [string] Nom de la description.



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

