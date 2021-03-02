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




## Sample

L'échantillon est un volume d'eau usée représentatif de l'eau présente sur un site, qui est ensuite analysé en laboratoire.

-	**sampleID**:(Identifiant de l'<e9>chantillon): (Primary Key) [string] Identifiant unique pour l'<e9>chantillon. Suggestion:siteID-date-index.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr<e9>e un lien avec la table "Site" pour d<e9>crire le point d'<e9>chantillonage.


-	**dateTime**:(Date et heure): [datetime] Date, heure et fuseau horaire de collecte d'un <e9>chantillon ponctuel.


-	**dateTimeStart**:(Date et heure de d<e9>but): [datetime] Date, heure et fuseau horaire de d<e9>but de collecte d'un <e9>chantillon composite.


-	**dateTimeEnd**:(Date et heure de fin): [datetime] Date, heure et fuseau horaire de fin de collecte d'un <e9>chantillon composite.


-	**type**:(Type): [category] Type d'<e9>chantillon.
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

-	**typeOther**:(Type autre): [string] Description d'un type d'<e9>chantillon ne faisant pas partie des options disponibles.


-	**collection**:(M<e9>thode de collecte): [category] M<e9>thode utilis<e9>e pour <e9>chantillonner.
	-	`cpTP24h`: Un échantillon composite proportionnel au temps prélevé sur 24 heures, généralement prélevé par un auto-échantilonneur.
	-	`cpFP24h`: Un échantillon composite proportionnel au débit prélevé sur 24 heures, généralement prélevé par un auto-échantilonneur.
	-	`grb`: Un seul échantillon ponctuel représentatif.
	-	`grbCp8h`: Un échantillon composite prélevé sur 8 heures consitué d'échantillons ponctuels collectés une fois par heure, généralement prélevé manuellement.
	-	`grbCp3h`: Un échantillon composite prélevé sur 3 heures consitué d'échantillons ponctuels collectés une fois par heure, généralement prélevé manuellement.
	-	`grbCp3`: Un échantillon composite composé de 3 échantillons ponctuels.
	-	`mooreSw`: Un échantillon passif collecté par la méthode de Moore.
	-	`other`: Autre méthode de collecte. Ajouter une description dans la colonne "descriptionOther"

-	**collectionOther**:(M<e9>thode de collecte autre): [string] Description d'une m<e9>thode d'<e9>chantillonnage ne faisant pas partie des options disponibles.


-	**preTreatment**:(Pr<e9>-traitement): [boolean] L'<e9>chantillon a-t-il <e9>t<e9> chimiquement alt<e9>r<e9> par un ajout de stabilisant ou autre?


-	**preTreatmentDescription**:(Description du pr<e9>-traitment): [string] Description du pr<e9>-traitement le cas <e9>ch<e9>ant.


-	**pooled**:(<c9>chantillon combin<e9>): [boolean] S'il s'agit d'un <e9>chantillon combin<e9>, c'est-<e0>-dire s'il est compos<e9> de plusieurs <e9>chantillons "enfants"?


-	**children**:(Enfants): [string] Si l'<e9>chantillon est li<e9>e <e0> des sous-<e9>chantillons (soit parce qu'il s'agit d'un <e9>chantillon combin<e9> ou parce que des sous-<e9>chantillons ont <e9>t<e9> pr<e9>lev<e9>s dans cet <e9>chantillon), ins<e9>rer les identifiant des <e9>chantillons enfants dans une liste s<e9>par<e9>e par des virgules.


-	**parent**:(Parent): [string] Si l'<e9>chantillon a <e9>t<e9> combin<e9> <e0> un plus grand <e9>chantillon, indiquer l'identifiant du plus grand <e9>chantillon.


-	**sizeL**:(Volume l): [float] Volume total d'eau ou de boue pr<e9>lev<e9>e.


-	**fieldSampleTempC**:(Temp<e9>rature de l'<e9>chantillon de terrain c): [float] Temprature <e0> laquelle l'<e9>chantillon <e9>tait stock<e9> pendant l'<e9>chantillonnage. Ce champ est principalement pertinent pour les <e9>chantillons composites, qui peuvent <ea>tre stock<e9>es <e0> temp<e9>rature ambiante ou r<e9>frig<e9>r<e9>s durant l'<e9>chantillonnage.


-	**shippedOnIce**:(Exp<e9>di<e9> sur glace): [boolean] L'<e9>chantillon a-t-il <e9>t<e9> gard<e9> au froid lors du transport vers le laboratoire?


-	**storageTempC**:(Temp<e9>rature de stockage c): [float] Temp<e9>rature de stockage de l'<e9>chantillon en degr<e9>s Celsius


-	**qualityFlag**:(Indicateur de mauvaise qualit<e9>): [boolean] Le reporteur a-t-il des doutes sur la qualit<e9> de l'<e9>chantillon?


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## WWMeasure

Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".

-	**uWwMeasureID**:(id u mesure eaux us<e9>es): (Primary Key) [string] Identifiant unique pour la mesure pour la table "WWMeasurement"


-	**wwMeasureID**:(id mesure eaux us<e9>es): [string] Identifiat unique utilis<e9> dans la table horizontale seulement. Utiliser quand toutes les mesures effectu<e9>es sur un <e9>chantillon sont r<e9>alis<e9>es en m<ea>me temps dans le m<ea>me laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.


-	**sampleID**:(Identifiant de l'<e9>chantillon): (Foreign key) [string] Cr<e9>e un lien avec la table "Sample" pour d<e9>crire l'<e9>chantillon mesur<e9>.


-	**labID**:(Identifiant du laboratoire): (Foreign key) [string] Cr<e9>e un lien avec la table "Lab" pour d<e9>crire le laboratoire effectuant la mesure.


-	**assayID**:(Identifiant de la m<e9>thode d'analyse): (Foreign key) [string] Cr<e9>e un lien avec la table "AssayMethod" pour d<e9>crire la m<e9>thode employ<e9>e pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<e9>e un lien avec la table "Instrument" l'appareil employ<e9> pour effectuer la mesure. Utiliser l'identifiant de la m<e9>thode d,analyse pour les mesures virales.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr<e9>e un lien avec les informations propres au reporteur associ<e9> <e0> la mesure.


-	**analysisDate**:(Date de l'analyse): [date] Date <e0> laquelle la mesure a <e9>t<e9> r<e9>alis<e9>e en laboratoire.


-	**reportDate**:(Date de reportage de la donn<e9>e): [date] Date a laquelle la donn<e9>e a <e9>t<e9> report<e9>e. Un <e9>chantillon pourrait avoir des mesures pour lesquelles la m<e9>thode d'analyse ou la m<e9>thode de reportage des donn<e9>es aurait chang<e9>e. Dans ce cas, utiliser le m<ea>me sampleID, mais cr<e9>er une nouvelle entr<e9>e dans la table "WWMeasure avec un "MeasureID" diff<e9>rent, et la date de reportage de la donn<e9>e et l'identifiant de la m<e9>thode d'analyse appropri<e9>s.


-	**fractionAnalyzed**:(Fraction analys<e9>e): [category] Fraction de l'<e9>chantillon employ<e9>e pour la mesure.
	-	`liquid`: Fraction liquide.
	-	`solid`: Fraction solide.
	-	`mixed`: Échantillon homogénéisé/mélangé.

-	**type**:(Type): [category] Le param<e8>tre mesur<e9> avec cette analyse. Exemples: Une r<e9>gion de g<e8>ne cible (cov), un biomarqueur (n) ou un indicateur de la qualit<e9> de l'eau (wq)
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

-	**typeOther**:(Type autre): [string] Description d'un param<e8>tre mesur<e9> ne faisant pas partie des options disponibles.


-	**unit**:(Unit<e9>): [category] Unit<e9> de mesure.
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

-	**unitOther**:(Unit<e9> autre): [string] Description d'une unit<e9> de mesure ne faisant pas partie des options disponibles.


-	**aggregation**:(Agr<e9>gation): [category] Indicateur statistique utilis<e9>e pour rapporter la mesure effectu<e9>e. Chaque agr<e9>gation doit <ea>tre report<e9>e comme une mesure diff<e9>rente (avec un identifiant diff<e9>rent)
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

-	**aggregationOther**:(Agr<e9>gation autre): [string] Description d'une agr<e9>gation ne faisant pas partie des options disponibles.


-	**index**:(Index): [integer] Index de la mesure dans le cas o<f9> la m<ea>me mesure a <e9>t<e9> prise en replicata.


-	**value**:(Valeur): [float] La valeur num<e9>rique de la mesure effectu<e9>e.


-	**qualityFlag**:(Indicateur de mauvaise qualit<e9>): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<e9>?


-	**accessToPublic**:(Acc<e8>s au public): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par le public. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToAllOrg**:(Acc<e8>s <e0> toutes les organisations): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToSelf**:(Acc<e8>s au reporteur lui-m<ea>me): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par le reporteur lui-m<ea>me. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToPHAC**:(Acc<e8>s <e0> l'ASPC): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les employ<e9>s de l'Agence de Sant<e9> Publique du Canada. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToLocalHA**:(Acc<e8>s <e0> l'autorit<e9> de sant<e9> publique locale): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique locales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToProvHA**:(Acc<e8>s <e0> l'autorit<e9> de sant<e9> publique provinciale): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e sera accessible <e0> l'autorit<e9> de sant<e9> publique de la province o<f9> l'<e9>chantillonnage a <e9>t<e9> r<e9>alis<e9>e.


-	**accessToOtherProv**:(Acc<e8>s aux autres prov): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToDetails**:(Acc<e8>s aux d<e9>tails): [boolean] Indique si des informations suppl<e9>mentaires sur la confidentialit<e9> de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Site

Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"

-	**siteID**:(Identifiant du site): (Primary Key) [string] Identifiant unique pour l'<e9>chantillon. Suggestion:siteID-date-index.


-	**name**:(Nom): [string] Nom du site d'<e9>chantillonnage. Peut <ea>tre le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'<e9>gouts, etc.


-	**description**:(Description): [string] Description du site d'<e9>chantillonnage (ville, b<e2>timent, rue, etc.) pour mieux identifier le site d'<e9>chantillonnage.


-	**type**:(Type): [category] Type de site ou d'institution du site d'<e9>chantillonnage.
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

-	**typeOther**:(Type autre): [string] Description du site d'<e9>chantillonnage dans le cas o<f9> une description ad<e9>quate n'est pas disponible.


-	**sampleTypeDefault**:(Type d'<e9>chantillon par d<e9>faut): [category] Type d'<e9>chantilon utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "type" dans la table "Sample"


-	**sampleTypeOtherDefault**:(Type d'<e9>chantillon autre d<e9>faut): [string] Type d'<e9>chantilon utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "typeOther" dans la table "Sample"


-	**sampleCollectionDefault**:(Pr<e9>l<e9>vement d'<e9>chantillons par d<e9>faut): [category] M<e9>thode d'<e9>chantillonnage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "collection" dans la table "Sample"


-	**sampleCollectOtherDefault**:(Pr<e9>l<e9>vement d'un autre <e9>chantillon par d<e9>faut): [string] M<e9>thode d'<e9>chantillonnage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "collectionOther" dans la table "Sample"


-	**sampleStorageTempCDefault**:(Temp<e9>rature de stockage de l'<e9>chantillon c par d<e9>faut): [float] Temp<e9>raure de stockage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "storageTempC" dans la table "Sample"


-	**measureFractionAnalyzedDefault**:(Fraction de mesure analys<e9>e par d<e9>faut): [category] Fraction par d<e9>faut quand une nouvelle mesure est cr<e9><e9>e pour cet <e9>chantillon. Se r<e9>f<e9>rer <e0> la colonne "fracgtionAnalyzed" dans la table "WWMeasure"


-	**geoLat**:(G<e9>o lat): [float] Position g<e9>ographique du site d'<e9>chantillonnage. Latitude exprim<e9>e en coordonn<e9>es d<e9>cimales (ex. 45.424721)


-	**geoLong**:(G<e9>o long): [float] Position g<e9>ographique du site d'<e9>chantillonnage. Longitude exprim<e9>e en coordonn<e9>es d<e9>cimales (ex. -75.695000)


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Cr<e9>e un lien vers la table "Polygon". Le polygon li<e9> devrait englober la r<e9>gion qui se draine dans le site d'<e9>chantillonnage.


-	**sewerNetworkFileLink**:(Lien vers le fichier du r<e9>seau d'<e9>gouts): [string] Lien vers un fichier contenant toute information additionnelle au sujet du r<e9>seau d'<e9>gouts associ<e9> <e0> ce site d'<e9>chantillonnage (tous les formats sont accept<e9>s).


-	**sewerNetworkFileBLOB**:(Fichier blob du r<e9>seau d'<e9>gouts): [blob] Un fichier contenant toute information additionnelle au sujet du r<e9>seau d'<e9>gouts associ<e9> <e0> ce site d'<e9>chantillonnage (tous les formats sont accept<e9>s).

## SiteMeasure

Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".

-	**uSiteMeasureID**:(Identifiant unique de la mesure sur site): (Primary Key) [string] Identifiant unique pour le site d'<e9>chantillonnage.


-	**siteMeasureID**:(Identifiant de la mesure sur site): [string] Identifiat unique utilis<e9> dans la table horizontale seulement. Utiliser quand toutes les mesures effectu<e9>es sur le m<ea>me <e9>chantillon.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr<e9>e un lien vers la table "Site" pour d<e9>crire le site d'<e9>chantillonnage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<e9>e un lien vers la table "Instrument" pour d<e9>crire l'appareil utilis<e9> pour effectuer la mesure.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr<e9>e un lien avec les informations propres au reporteur associ<e9> <e0> la mesure.


-	**dateTime**:(Date et heure): [date] Date <e0> laquelle la mesure a <e9>t<e9> r<e9>alis<e9>e.


-	**type**:(Type): [category] Type de mesure r<e9>alis<e9>e. Le pr<e9>fixe "env" est utilis<e9> pour une variable envioronnementale, alors que "ww" indique une mesure r<e9>alis<e9>e sur les eaux us<e9>es.
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

-	**typeOther**:(Type autre): [string] Description d'un param<e8>tre mesur<e9> ne faisant pas partie des options disponibles.


-	**typeDescription**:(Description du type): [string] Ajouter toutes notes additionnelles en lien avec la mesure effectu<e9>e.


-	**aggregation**:(Agr<e9>gation): [category] M<e9>thode d'agr<e9>gation utilise<e9>e pour rapporter la mesure.
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

-	**aggregationOther**:(Agr<e9>gation autre): [string] Description d'une agr<e9>gation ne faisant pas partie des options disponibles.


-	**aggregationDesc**:(Agr<e9>gation desc): [string] Informations (ou r<e9>f<e9>rence) li<e9>e(s) <e0> la m<e9>thode d'agr<e9>gation utilis<e9>e pour rapporter la mesure.


-	**value**:(Valeur): [float] La valeur num<e9>rique de la mesure effectu<e9>e.


-	**unit**:(Unit<e9>): [string] L'unit<e9> de mesure


-	**qualityFlag**:(Indicateur de mauvaise qualit<e9>): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<e9>?


-	**accessToPublic**:(Acc<e8>s au public): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par le public. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToAllOrgs**:(Acc<e8>s <e0> toutes les organisations): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToSelf**:(Acc<e8>s au reporteur lui-m<ea>me): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par le reporteur lui-m<ea>me. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToPHAC**:(Acc<e8>s <e0> l'ASPC): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les employ<e9>s de l'Agence de Sant<e9> Publique du Canada. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToLocalHA**:(Acc<e8>s <e0> l'autorit<e9> de sant<e9> publique locale): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique locales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToProvHA**:(Acc<e8>s <e0> l'autorit<e9> de sant<e9> publique provinciale): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e sera accessible <e0> l'autorit<e9> de sant<e9> publique de la province o<f9> l'<e9>chantillonnage a <e9>t<e9> r<e9>alis<e9>e.


-	**accessToOtherProv**:(Acc<e8>s aux autres provinces): [boolean] Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.


-	**accessToDetails**:(Acc<e8>s aux d<e9>tails): [boolean] Indique si des informations suppl<e9>mentaires sur la confidentialit<e9> de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Reporter

Le reporteur ou l'organisation responsable de la collecte de données ou responsable de la qualité des données reportées.

-	**reporterID**:(Identifiant du reporteur): (Primary Key) [string] Identifiant unique pour la personne ou l'organisation responsable des donn<e9>es rapport<e9>es.


-	**siteIDDefault**:(Identifiant du site par d<e9>faut): (Foreign key) [string] Identifiant de Site utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> par ce reporteur. Se r<e9>f<e9>rer <e0> la colonne "siteID" dans la table "Site"


-	**labIDDefault**:(Identifiant laboratoire par d<e9>faut): (Foreign key) [string] Identifiant de Lab utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> par ce reporteur. Se r<e9>f<e9>rer <e0> la colonne "labID" dans la table "Lab"


-	**contactName**:(Nom du contact): [string] Nom complet du reporter (personne ou organisation)


-	**contactEmail**:(Adresse <e9>lectronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(T<e9>l<e9>phone du contact): [string] Num<e9>ro de t<e9>l<e9>phone du contact.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Lab

Laboratoire effectuant des analyses d'échantillons d'eaux usées d'un ou plusieurs sites.

-	**labID**:(Identifiant du laboratoire): (Primary Key) [string] Identifiant unique pour le laboratoire.


-	**assayMethodIDDefault**:(Identifiant de la m<e9>thode d'analyse par d<e9>faut): (Foreign key) [string] Identifiant de la m<e9>thode d'analyse utilis<e9>e par d<e9>faut quand une nouvelle mesure est cr<e9><e9> par ce laboratoire. Se r<e9>f<e9>rer <e0> la colonne "assayMethodID" dans la table "AssayMethod"


-	**name**:(Nom): [string] Nom du laboratoire.


-	**contactName**:(Nom du contact): [string] Personne contact de ce laboratoire.


-	**contactEmail**:(Adresse <e9>lectronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(T<e9>l<e9>phone du contact): [string] Num<e9>ro de t<e9>l<e9>phone du contact.


-	**updateDate**:(Date de mise <e0> jour): [date] Date o<f9> l'information a <e9>t<e9> report<e9>e une premi<e8>re fois ou mise <e0> jour.

## AssayMethod

La méthode d'analyse utilisée pour réaliser les mesures. Crée une nouvelle rangée dans cette table si des changements (améliorations) sont apportées à une technique d'analyse existante. Garder le même identifiant et modifier le numéro de version. Une nouvelle rangée représentant une nouvelle version d'une méthode existante peut inclure des informations seulement dans les colonnes qui ont changé d'une version à l'autre, cependant, nous recommandons de remplir les autres colonnes avec les valeurs provenant de la version précédente afin de décrire clairement la méthode en entier. Ajouter la date courante lorsqu'une nouvelle rangée est créée.

-	**assayMethodID**:(Identifiant de la m<e9>thode d'analyse): (Primary Key) [string] Identifiant unique pour la m<e9>thode d'analyse.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<e9>e un lien vers la table "Instrument" pour d<e9>crire l'appareil utilis<e9> pour effectuer la mesure.


-	**name**:(Nom): [string] Nom de la m<e9>thode d'analyse.


-	**version**:(Version): [string] Version de la m<e9>thode d'analyse. Un versionnement de type s<e9>mantique est recommand<e9>.


-	**summary**:(R<e9>sum<e9>): [string] Br<e8>ve description de la m<e9>thode d'analyse et de comment celle-ci diff<e8>re d'autres m<e9>thodes.


-	**referenceLink**:(Lien vers r<e9>f<e9>rence): [string] Lien vers la proc<e9>dure standard.


-	**date**:(Date): [date] Date <e0> laquelle la m<e9>thode d'analyse (ou une nouvelle version d'une m<e9>thode existante) a <e9>t<e9> cr<e9>e.


-	**aliasID**:(Identifiant de l'alias): [string] Identifiants d'autres m<e9>thodes d'analyse pr<e9>sentes dans la table qui sont similaires <e0> la m<e9>thode courante. Ins<e9>rer sous forme de liste s<e9>par<e9>e par des virgules.


-	**sampleSizeL**:(Volume de l'<e9>chantillon l): [float] Volume de l'<e9>chantillon analys<e9> (en litres)


-	**loq**:(Limite de quantification): [float] Limite de quantification pour cette m<e9>thode, le cas <e9>ch<e9>ant.


-	**lod**:(Limite de d<e9>tection): [float] Limite de d<e9>tection pour cette m<e9>thode, le cas <e9>ch<e9>ant.


-	**unit**:(Unit<e9>): [category] Unit<e9> de mesure utilis<e9>e par cette m<e9>thode et qui est applicable pour la limite de d<e9>tection ou de quantification.
	-	`gcPMMoV`: Copies de gène ou de variant par copie de PMMoV
	-	`gcMl`: Copies de gène ou de variant par millilitre.
	-	`gcGms`: Copies de gène ou de variant par gramme de solides.
	-	`gcL`: Copies de gène ou de variant par litre.
	-	`gcCrA`: Copies de gène ou de variant par copie de CrAssphage
	-	`other`: Autre mesure de copies virales ou de qualité des eaux usées. Ajouter une description dans "unitOther"

-	**unitOther**:(Unit<e9> autre): [string] Unit<e9> de mesure utilis<e9>e par cette m<e9>thode et qui est applicable pour la limite de d<e9>tection ou de quantification dans le cas o<f9> celle-ci n'est pas disponible.


-	**methodConc**:(M<e9>thode de concentration): [string] Description de la m<e9>thode utilis<e9>e pour concentrer l'<e9>chantillon.


-	**methodExtract**:(M<e9>thode d'extraction): [string] Description de la m<e9>thode utilis<e9>e pour extraire l'<e9>chantillon.


-	**methodPcr**:(M<e9>thode PCR): [string] Description de la m.<e9>thode PCR utiis<e9>e.


-	**qualityAssQC**:(Contr<f4>le de qualit<e9>): [string] Description des <e9>tapes de contr<f4>le de qualit<e9> mises en place dans la m<e9>thode.


-	**inhibition**:(Inhibition): [string] Description des param<e8>tres d'inhibition li<e9>s <e0> cette m<e9>thode.


-	**surrogateRecovery**:(R<e9>cup<e9>ration du virus substitut): [string] Description de la m<e9>thode de r<e9>cup<e9>ration du virus de substitution li<e9>e <e0> cette m<e9>thode.

## Instrument

L'instrument utilisé pour mesurer les échantillons et l'eau usée des sites d'échantillonnage. La méthode d'analyse pour les mesures virales sont décrites dans la table "AssayMethod".

-	**instrumentID**:(Identifiant de l'instrument): (Primary Key) [string] Identifiant unique pour l'instrument de mesure.


-	**name**:(Nom): [string] Nom de l'instrument de mesure.


-	**model**:(Mod<e8>le): [string] Num<e9>ro de mod<e8>le et/ou de version de l'instrument de mesure.


-	**description**:(Description): [string] Description de l'instrument.


-	**alias**:(Alias): [string] Identifiants d'autres instruments pr<e9>sents dans la table qui sont similaires <e0> l'instrument courant. Ins<e9>rer sous forme de liste s<e9>par<e9>e par des virgules.


-	**referenceLink**:(Lien vers r<e9>f<e9>rence): [string] Lien vers un document de r<e9>f<e9>rence pour l'instrument de mesure.


-	**type**:(Type): [category] Type de l'instrument de mesure.
	-	`online`: Capteur en ligne.
	-	`lab`: Analyse en laboratoire.
	-	`hand`: Mesure à l'aide d'un capteur manuel.
	-	`atline`: Mesure à l'aide d'un échantillonneur.
	-	`other`: Autre type d'appareil de mesure. Ajouter une description dans "instrumentTypeOther"

-	**typeOther**:(Type autre): [string] Description du type d'instrument dans le cas o<f9> il ne serait pas disponible.

## Polygon

Polygone englobant une région de la surface terrestre. Normalement, ces polygones représentent soit des bassin de drainage d'un réseau d'égouts ou une région de santé publique, ou une autre région associée à des données reportées.

-	**polygonID**:(Identifiant du polygone): (Primary Key) [string] Identifiant unique du polygone.


-	**name**:(Nom): [string] Nom du polygon (devrait <ea>tre descriptif)


-	**pop**:(Population): [integer] Population approximative vivant dans la r<e9>gion repr<e9>sent<e9>e par le polygone.


-	**type**:(Type): [category] Type de polygone.
	-	`swrCat`: Zone de captage d'un réseau d'égout.
	-	`hlthReg`: Région de santé desservie par le réseau d'égout.

-	**wkt**:(Wkt): [string] Description formelle du polygone (format Well-Known-Text (wkt))


-	**file**:(Fichier): [blob] Fichier repr<e9>sentant la g<e9>om<e9>trie du polygone (blob).


-	**link**:(Lien): [string] Lien vers une r<e9>f<e9>rence externe d<e9>crivant la g<e9>om<e9>trie du polygone.

## CovidPublicHealthData

Données de patients pour la COVID-19 pour une région spécifiée par un polygone.

-	**cphdID**:(Identifiant de CPHD): (Primary Key) [string] Identifiant unique pour l'information de sant<e9> publique report<e9>e.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Identifiant unique pour la personne ou l'organisation responsable des donn<e9>es rapport<e9>es.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Cr<e9>e un lien vers la table "Polygon". Le polygon li<e9> devrait englober la r<e9>gion repr<e9>sent<e9>e par les donn<e9>es consign<e9>es ici.


-	**date**:(Date): [string] Date de reportage des donn<e9>es de mesure de la COVID-19.


-	**type**:(Type): [category] Type de donn<e9>e de mesure de la COVID-19.
	-	`conf`: Nombre de cas confirmés. La mesure devrait être accompagnée d'une valeur dans la colonne "dateType"
	-	`active`: Nombre de cas actifs.
	-	`test`: Nombre de tests effectués.
	-	`posTest`: Nombre de tests positifs.
	-	`pPosRt`: Pourcentage de positivité des tests.
	-	`hospCen`: Rencensement des patients admis à un hôpital avec la COVID-19.
	-	`hospAdm`: Nombre d'admissions ou nombre de patients admis à l'hôpital.

-	**dateType**:(Type de date): [category] Type de date utiis<e9>e pour reporter les donn<e9>es.
	-	`episode`: Date estimée à laquelle l'épisode de maladie s'est déclaré. Habituellement calculé en se basant sur la date des premiers symptômes, la date de test ou la date de reportage.
	-	`onset`: Date à laquelle les premiers symptômes apparaissent. Cette donnée est souvent inconnue. La date d'épisode est alors communément utilisée.
	-	`report`: Date à laquelle la donnée a été reportée à la santé publique. Cette mesure est communément utilisée.
	-	`test`: Date à laquelle le test de COVID-19 a été effectué.

-	**value**:(Valeur): [float] La valeur num<e9>rique de la mesure report<e9>e.


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

