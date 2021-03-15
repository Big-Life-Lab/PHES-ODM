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

-	**sampleID**:(Identifiant de l'<U+FFFD>chantillon): (Primary Key) [string] Identifiant unique pour l'<U+FFFD>chantillon. Suggestion:siteID-date-index.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Site" pour d<U+FFFD>crire le point d'<U+FFFD>chantillonage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Instrument" pour d<U+FFFD>crire l'instrument utilis<U+FFFD> pour l'<U+FFFD>chantillonnage.


-	**dateTime**:(Date et heure): [datetime] Date, heure et fuseau horaire de collecte d'un <U+FFFD>chantillon ponctuel.


-	**dateTimeStart**:(Date et heure de d<U+FFFD>but): [datetime] Date, heure et fuseau horaire de d<U+FFFD>but de collecte d'un <U+FFFD>chantillon composite.


-	**dateTimeEnd**:(Date et heure de fin): [datetime] Date, heure et fuseau horaire de fin de collecte d'un <U+FFFD>chantillon composite.


-	**type**:(Type): [category] Type d'<U+FFFD>chantillon.
	-	`rawWW`: Eau us<U+FFFD>e brute
	-	`swrSed`: S<U+FFFD>diments provenant des <U+FFFD>gouts.
	-	`pstGrit`: Eau us<U+FFFD>e apr<U+FFFD>s d<U+FFFD>grillage et dessablage.
	-	`pSludge`: Boue provenant d'un d<U+FFFD>canteur primaire.
	-	`pEfflu`: Effluent obtenu apr<U+FFFD>s un d<U+FFFD>canteur primaire.
	-	`sSludge`: Boue provenant d'un d<U+FFFD>canteur secondaire.
	-	`sEfflu`: Effluent obtenu apr<U+FFFD>s un d<U+FFFD>canteur secondaire.
	-	`water`: Eau non-us<U+FFFD>e provenant de toute <U+FFFD>tendue d'eau.
	-	`faeces`: Mati<U+FFFD>re f<U+FFFD>cale.
	-	`other`: Autre type de site d'<U+FFFD>chantillonnage. Ajouter une description dans la colonne "typeOther"

-	**typeOther**:(Type autre): [string] Description d'un type d'<U+FFFD>chantillon ne faisant pas partie des options disponibles.


-	**collection**:(M<U+FFFD>thode de collecte): [category] M<U+FFFD>thode utilis<U+FFFD>e pour <U+FFFD>chantillonner.
	-	`cpTP24h`: Un <U+FFFD>chantillon composite proportionnel au temps pr<U+FFFD>lev<U+FFFD> sur 24 heures, g<U+FFFD>n<U+FFFD>ralement pr<U+FFFD>lev<U+FFFD> par un auto-<U+FFFD>chantilonneur.
	-	`cpFP24h`: Un <U+FFFD>chantillon composite proportionnel au d<U+FFFD>bit pr<U+FFFD>lev<U+FFFD> sur 24 heures, g<U+FFFD>n<U+FFFD>ralement pr<U+FFFD>lev<U+FFFD> par un auto-<U+FFFD>chantilonneur.
	-	`grb`: Un seul <U+FFFD>chantillon ponctuel repr<U+FFFD>sentatif.
	-	`grbCp8h`: Un <U+FFFD>chantillon composite pr<U+FFFD>lev<U+FFFD> sur 8 heures consitu<U+FFFD> d'<U+FFFD>chantillons ponctuels collect<U+FFFD>s une fois par heure, g<U+FFFD>n<U+FFFD>ralement pr<U+FFFD>lev<U+FFFD> manuellement.
	-	`grbCp3h`: Un <U+FFFD>chantillon composite pr<U+FFFD>lev<U+FFFD> sur 3 heures consitu<U+FFFD> d'<U+FFFD>chantillons ponctuels collect<U+FFFD>s une fois par heure, g<U+FFFD>n<U+FFFD>ralement pr<U+FFFD>lev<U+FFFD> manuellement.
	-	`grbCp3`: Un <U+FFFD>chantillon composite compos<U+FFFD> de 3 <U+FFFD>chantillons ponctuels.
	-	`mooreSw`: Un <U+FFFD>chantillon passif collect<U+FFFD> par la m<U+FFFD>thode de Moore.
	-	`other`: Autre m<U+FFFD>thode de collecte. Ajouter une description dans la colonne "descriptionOther"

-	**collectionOther**:(M<U+FFFD>thode de collecte autre): [string] Description d'une m<U+FFFD>thode d'<U+FFFD>chantillonnage ne faisant pas partie des options disponibles.


-	**preTreatment**:(Pr<U+FFFD>-traitement): [boolean] L'<U+FFFD>chantillon a-t-il <U+FFFD>t<U+FFFD> chimiquement alt<U+FFFD>r<U+FFFD> par un ajout de stabilisant ou autre?


-	**preTreatmentDescription**:(Description du pr<U+FFFD>-traitment): [string] Description du pr<U+FFFD>-traitement le cas <U+FFFD>ch<U+FFFD>ant.


-	**pooled**:(<U+FFFD>chantillon combin<U+FFFD>): [boolean] S'il s'agit d'un <U+FFFD>chantillon combin<U+FFFD>, c'est-<U+FFFD>-dire, est-il compos<U+FFFD> de plusieurs <U+FFFD>chantillons "enfants"?


-	**children**:(Enfants): [string] Si l'<U+FFFD>chantillon est li<U+FFFD>e <U+FFFD> des sous-<U+FFFD>chantillons (soit parce qu'il s'agit d'un <U+FFFD>chantillon combin<U+FFFD> ou parce que des sous-<U+FFFD>chantillons ont <U+FFFD>t<U+FFFD> pr<U+FFFD>lev<U+FFFD>s dans cet <U+FFFD>chantillon), ins<U+FFFD>rer les identifiant des <U+FFFD>chantillons enfants dans une liste s<U+FFFD>par<U+FFFD>e par des virgules.


-	**parent**:(Parent): [string] Si l'<U+FFFD>chantillon a <U+FFFD>t<U+FFFD> combin<U+FFFD> <U+FFFD> un plus grand <U+FFFD>chantillon, indiquer l'identifiant du plus grand <U+FFFD>chantillon.


-	**sizeL**:(Volume l): [float] Volume total d'eau ou de boue pr<U+FFFD>lev<U+FFFD>e.


-	**fieldSampleTempC**:(Temp<U+FFFD>rature de l'<U+FFFD>chantillon de terrain c): [float] Temprature <U+FFFD> laquelle l'<U+FFFD>chantillon <U+FFFD>tait stock<U+FFFD> pendant l'<U+FFFD>chantillonnage. Ce champ est principalement pertinent pour les <U+FFFD>chantillons composites, qui peuvent <U+FFFD>tre stock<U+FFFD>es <U+FFFD> temp<U+FFFD>rature ambiante ou r<U+FFFD>frig<U+FFFD>r<U+FFFD>s durant l'<U+FFFD>chantillonnage.


-	**shippedOnIce**:(Exp<U+FFFD>di<U+FFFD> sur glace): [boolean] L'<U+FFFD>chantillon a-t-il <U+FFFD>t<U+FFFD> gard<U+FFFD> au froid lors du transport vers le laboratoire?


-	**storageTempC**:(Temp<U+FFFD>rature de stockage c): [float] Temp<U+FFFD>rature de stockage de l'<U+FFFD>chantillon en degr<U+FFFD>s Celsius


-	**qualityFlag**:(Indicateur de mauvaise qualit<U+FFFD>): [boolean] Le reporteur a-t-il des doutes sur la qualit<U+FFFD> de l'<U+FFFD>chantillon?


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## WWMeasure

Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".

-	**uWwMeasureID**:(id u mesure eaux us<U+FFFD>es): (Primary Key) [string] Identifiant unique pour la mesure pour la table "WWMeasurement"


-	**wwMeasureID**:(id mesure eaux us<U+FFFD>es): [string] Identifiat unique utilis<U+FFFD> dans la table horizontale seulement. Utiliser quand toutes les mesures effectu<U+FFFD>es sur un <U+FFFD>chantillon sont r<U+FFFD>alis<U+FFFD>es en m<U+FFFD>me temps dans le m<U+FFFD>me laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.


-	**sampleID**:(Identifiant de l'<U+FFFD>chantillon): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Sample" pour d<U+FFFD>crire l'<U+FFFD>chantillon mesur<U+FFFD>.


-	**labID**:(Identifiant du laboratoire): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Lab" pour d<U+FFFD>crire le laboratoire effectuant la mesure.


-	**assayID**:(Identifiant de la m<U+FFFD>thode d'analyse): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "AssayMethod" pour d<U+FFFD>crire la m<U+FFFD>thode employ<U+FFFD>e pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Instrument" l'appareil employ<U+FFFD> pour effectuer la mesure. Utiliser l'identifiant de la m<U+FFFD>thode d'analyse pour les mesures virales.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr<U+FFFD>e un lien avec les informations propres au reporteur associ<U+FFFD> <U+FFFD> la mesure.


-	**analysisDate**:(Date de l'analyse): [date] Date <U+FFFD> laquelle la mesure a <U+FFFD>t<U+FFFD> r<U+FFFD>alis<U+FFFD>e en laboratoire.


-	**reportDate**:(Date de reportage de la donn<U+FFFD>e): [date] Date a laquelle la donn<U+FFFD>e a <U+FFFD>t<U+FFFD> rapport<U+FFFD>e. Un <U+FFFD>chantillon pourrait avoir des mesures pour lesquelles la m<U+FFFD>thode d'analyse ou la m<U+FFFD>thode de reportage des donn<U+FFFD>es aurait chang<U+FFFD>e. Dans ce cas, utiliser le m<U+FFFD>me sampleID, mais cr<U+FFFD>er une nouvelle entr<U+FFFD>e dans la table "WWMeasure avec un "MeasureID" diff<U+FFFD>rent, et la date de reportage de la donn<U+FFFD>e et l'identifiant de la m<U+FFFD>thode d'analyse appropri<U+FFFD>s.


-	**fractionAnalyzed**:(Fraction analys<U+FFFD>e): [category] Fraction de l'<U+FFFD>chantillon employ<U+FFFD>e pour la mesure.
	-	`liquid`: Fraction liquide.
	-	`solid`: Fraction solide.
	-	`mixed`: <U+FFFD>chantillon homog<U+FFFD>n<U+FFFD>is<U+FFFD>/m<U+FFFD>lang<U+FFFD>.

-	**type**:(Type): [category] Le param<U+FFFD>tre mesur<U+FFFD> avec cette analyse. Exemples: Une r<U+FFFD>gion de g<U+FFFD>ne cible (cov), un biomarqueur (n) ou un indicateur de la qualit<U+FFFD> de l'eau (wq)
	-	`covN1`: G<U+FFFD>ne nucleocapside N1 du SRAS-CoV-2
	-	`covN2`: G<U+FFFD>ne nucleocapside N2 du SRAS-CoV-2
	-	`covN3`: G<U+FFFD>ne nucleocapside N3 des virus similaires au SRAS
	-	`covE`: R<U+FFFD>gion g<U+FFFD>nique E du SRAS-CoV-2
	-	`varB117`: Variant B.1.1.7
	-	`varB1351`: Variant B.1.351
	-	`varP1`: Variant P.1
	-	`covRdRp`: R<U+FFFD>gion g<U+FFFD>nique RdRp du SRAS-CoV-2
	-	`nPMMoV`: Virus de la marbrure l<U+FFFD>g<U+FFFD>re du piment
	-	`ncrA`: CrAssphage
	-	`nbrsv`: Virus respiratoire syncytial bovin
	-	`wqTS`: Solides totaux
	-	`wqTSS`: Mati<U+FFFD>res en suspension
	-	`wqVSS`: Mati<U+FFFD>res volatiles en suspension
	-	`wqCOD`: Demande chimique en oxyg<U+FFFD>ne
	-	`wqOPhos`: Concentration d'ortho-phosphates
	-	`wqNH4N`: Concentrsation d'azote ammoniacal, exprim<U+FFFD> en N.
	-	`wqTN`: Azote total, exprim<U+FFFD> en N
	-	`wqPh`: pH
	-	`wqCond`: Conductivit<U+FFFD>
	-	`temp`: la temp<U+FFFD>rature de l'<U+FFFD>chantillon au moment o<U+FFFD> la mesure est prise, souvent <U+FFFD> son arriv<U+FFFD>e au laboratoire.
	-	`other`: Autre cat<U+FFFD>gorie de mesure. Ajouter une description de la cat<U+FFFD>gorie dans la colonne "categoryOther".

-	**typeOther**:(Type autre): [string] Description d'un param<U+FFFD>tre mesur<U+FFFD> ne faisant pas partie des options disponibles.


-	**unit**:(Unit<U+FFFD>): [category] Unit<U+FFFD> de mesure.
	-	`gcPMMoV`: Copies de g<U+FFFD>ne ou de variant par copie de PMMoV
	-	`gcMl`: Copies de g<U+FFFD>ne ou de variant par millilitre.
	-	`gcGs`: Copies de g<U+FFFD>ne ou de variant par gramme de solides.
	-	`gcL`: Copies de g<U+FFFD>ne ou de variant par litre.
	-	`gcCrA`: Copies de g<U+FFFD>ne ou de variant par copie de CrAssphage
	-	`Ct`: Cycle seuil.
	-	`mgL`: Milligrammes par litre.
	-	`ph`: Unit<U+FFFD>s de pH
	-	`uScm`: Microsiemens par centim<U+FFFD>tre.
	-	`detected`: Copies de g<U+FFFD>ne ou de variant d<U+FFFD>tect<U+FFFD> dans "sampleGene". 1=Detect<U+FFFD>, 0=Non-d<U+FFFD>tect<U+FFFD>.
	-	`propVar`: Proportion du variant dans l'<U+FFFD>chantillon
	-	`pp`: Pourcentage de positifs (m<U+FFFD>thode de Moore)
	-	`pps`: Pourcentage de boues primaire (pour solides totaux)
	-	`c`: temp<U+FFFD>ratures en degr<U+FFFD>s Celsius
	-	`bool`: Dans les cas o<U+FFFD> un oui ou un non bool<U+FFFD>en est requis, utilisez bool
	-	`other`: Autre mesure de copies virales ou de qualit<U+FFFD> des eaux us<U+FFFD>es. Ajouter une description dans "unitOther"

-	**unitOther**:(Unit<U+FFFD> autre): [string] Description d'une unit<U+FFFD> de mesure ne faisant pas partie des options disponibles.


-	**aggregation**:(Agr<U+FFFD>gation): [category] Indicateur statistique utilis<U+FFFD>e pour rapporter la mesure effectu<U+FFFD>e. Chaque agr<U+FFFD>gation doit <U+FFFD>tre report<U+FFFD>e comme une mesure diff<U+FFFD>rente (avec un identifiant diff<U+FFFD>rent)
	-	`single`: La valeur n'a subi aucune agr<U+FFFD>gation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut <U+FFFD>tre un r<U+FFFD>plica.
	-	`mean`: Moyenne arithm<U+FFFD>tique.
	-	`meanNr`: Moyenne arithm<U+FFFD>tique normalis<U+FFFD>e.
	-	`geoMn`: Moyenne g<U+FFFD>om<U+FFFD>trique.
	-	`geoMnNr`: Moyenne g<U+FFFD>om<U+FFFD>trique normalis<U+FFFD>e.
	-	`median`: M<U+FFFD>diane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'<U+FFFD>cart type.
	-	`sdNr`: L'<U+FFFD>cart type normalis<U+FFFD>.
	-	`other`: Autre m<U+FFFD>thode d'agr<U+FFFD>gation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agr<U+FFFD>gation autre): [string] Description d'une agr<U+FFFD>gation ne faisant pas partie des options disponibles.


-	**index**:(Index): [integer] Index de la mesure dans le cas o<U+FFFD> la m<U+FFFD>me mesure a <U+FFFD>t<U+FFFD> prise en replicata.


-	**value**:(Valeur): [float] La valeur num<U+FFFD>rique de la mesure effectu<U+FFFD>e. Utilise "NA" pour les valeurs manquantes et laisser une note.


-	**qualityFlag**:(Indicateur de mauvaise qualit<U+FFFD>): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<U+FFFD>?


-	**accessToPublic**:(Acc<U+FFFD>s au public): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par le public. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToAllOrg**:(Acc<U+FFFD>s <U+FFFD> toutes les organisations): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToSelf**:(Acc<U+FFFD>s au reporteur lui-m<U+FFFD>me): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par le reporteur lui-m<U+FFFD>me. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToPHAC**:(Acc<U+FFFD>s <U+FFFD> l'ASPC): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les employ<U+FFFD>s de l'Agence de Sant<U+FFFD> Publique du Canada. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToLocalHA**:(Acc<U+FFFD>s <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique locale): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique locales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToProvHA**:(Acc<U+FFFD>s <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique provinciale): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique provinciales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e sera accessible <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique de la province o<U+FFFD> l'<U+FFFD>chantillonnage a <U+FFFD>t<U+FFFD> r<U+FFFD>alis<U+FFFD>e.


-	**accessToOtherProv**:(Acc<U+FFFD>s aux autres prov): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique provinciales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToDetails**:(Acc<U+FFFD>s aux d<U+FFFD>tails): [boolean] Indique si des informations suppl<U+FFFD>mentaires sur la confidentialit<U+FFFD> de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Site

Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"

-	**siteID**:(Identifiant du site): (Primary Key) [string] Identifiant unique pour l'<U+FFFD>chantillon. Suggestion:siteID-date-index.


-	**name**:(Nom): [string] Nom du site d'<U+FFFD>chantillonnage. Peut <U+FFFD>tre le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'<U+FFFD>gouts, etc.


-	**description**:(Description): [string] Description du site d'<U+FFFD>chantillonnage (ville, b<U+FFFD>timent, rue, etc.) pour mieux identifier le site d'<U+FFFD>chantillonnage.


-	**publicHealthDepartment**:(Département ou région de santé publique): [string] NA


-	**healthRegion**:(Région de planification sanitaire): [string] NA


-	**type**:(Type): [category] Type de site ou d'institution du site d'<U+FFFD>chantillonnage.
	-	`airPln`: Avion.
	-	`corFcil`: Prison.
	-	`school`: <U+FFFD>cole.
	-	`hosptl`: H<U+FFFD>pital.
	-	`ltcf`: <U+FFFD>tablissement de soins de longue dur<U+FFFD>e.
	-	`swgTrck`: Camion de vidange.
	-	`uCampus`: Campus universitaire.
	-	`mSwrPpl`: Collecteur d'<U+FFFD>gouts.
	-	`pStat`: Station de pompage.
	-	`holdTnk`: Bassin de stockage.
	-	`retPond`: Bassin de r<U+FFFD>tention.
	-	`wwtpMuC`: Station de traitement des eaux us<U+FFFD>es municipales pour <U+FFFD>gouts combin<U+FFFD>s.
	-	`wwtpMuS`: Station de traitement des eaux us<U+FFFD>es municipales pour <U+FFFD>gouts sanitaires seulement.
	-	`wwtpInd`: Station de traitement des eaux us<U+FFFD>es industrielle.
	-	`lagoon`: Syst<U+FFFD>me de lagunage pour traitement des eaux us<U+FFFD>es.
	-	`septTnk`: Fosse septique.
	-	`river`: Rivi<U+FFFD>re, <U+FFFD>tendue d'eau naturelle.
	-	`lake`: Lac, <U+FFFD>tendue d'eau naturelle.
	-	`estuary`: Estuaire, <U+FFFD>tendue d'eau naturelle.
	-	`sea`: Mer, <U+FFFD>tendue d'eau naturelle.
	-	`ocean`: Oc<U+FFFD>an, <U+FFFD>tendue d'eau naturelle.
	-	`other`: Autre type de site. Ajouter une description dans "typeOther".

-	**typeOther**:(Type autre): [string] Description du site d'<U+FFFD>chantillonnage dans le cas o<U+FFFD> un type ad<U+FFFD>quat n'est pas disponible.


-	**sampleTypeDefault**:(Type d'<U+FFFD>chantillon par d<U+FFFD>faut): [category] Type d'<U+FFFD>chantilon utilis<U+FFFD> par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> pour ce site. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "type" dans la table "Sample"


-	**sampleTypeOtherDefault**:(Type d'<U+FFFD>chantillon autre d<U+FFFD>faut): [string] Type d'<U+FFFD>chantilon utilis<U+FFFD> par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> pour ce site. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "typeOther" dans la table "Sample"


-	**sampleCollectionDefault**:(Pr<U+FFFD>l<U+FFFD>vement d'<U+FFFD>chantillons par d<U+FFFD>faut): [category] M<U+FFFD>thode d'<U+FFFD>chantillonnage par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> pour ce site. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "collection" dans la table "Sample"


-	**sampleCollectOtherDefault**:(Pr<U+FFFD>l<U+FFFD>vement d'un autre <U+FFFD>chantillon par d<U+FFFD>faut): [string] M<U+FFFD>thode d'<U+FFFD>chantillonnage par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> pour ce site. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "collectionOther" dans la table "Sample"


-	**sampleStorageTempCDefault**:(Temp<U+FFFD>rature de stockage de l'<U+FFFD>chantillon c par d<U+FFFD>faut): [float] Temp<U+FFFD>raure de stockage par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> pour ce site. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "storageTempC" dans la table "Sample"


-	**measureFractionAnalyzedDefault**:(Fraction de mesure analys<U+FFFD>e par d<U+FFFD>faut): [category] Fraction par d<U+FFFD>faut quand une nouvelle mesure est cr<U+FFFD><U+FFFD>e pour cet <U+FFFD>chantillon. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "fractionAnalyzed" dans la table "WWMeasure"


-	**geoLat**:(G<U+FFFD>o lat): [float] Position g<U+FFFD>ographique du site d'<U+FFFD>chantillonnage. Latitude exprim<U+FFFD>e en coordonn<U+FFFD>es d<U+FFFD>cimales (ex. 45.424721)


-	**geoLong**:(G<U+FFFD>o long): [float] Position g<U+FFFD>ographique du site d'<U+FFFD>chantillonnage. Longitude exprim<U+FFFD>e en coordonn<U+FFFD>es d<U+FFFD>cimales (ex. -75.695000)


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Cr<U+FFFD>e un lien vers la table "Polygon". Le polygon li<U+FFFD> devrait englober la r<U+FFFD>gion qui se draine dans le site d'<U+FFFD>chantillonnage.


-	**sewerNetworkFileLink**:(Lien vers le fichier du r<U+FFFD>seau d'<U+FFFD>gouts): [string] Lien vers un fichier contenant toute information additionnelle au sujet du r<U+FFFD>seau d'<U+FFFD>gouts associ<U+FFFD> <U+FFFD> ce site d'<U+FFFD>chantillonnage (tous les formats sont accept<U+FFFD>s).


-	**sewerNetworkFileBLOB**:(Fichier blob du r<U+FFFD>seau d'<U+FFFD>gouts): [blob] Un fichier contenant toute information additionnelle au sujet du r<U+FFFD>seau d'<U+FFFD>gouts associ<U+FFFD> <U+FFFD> ce site d'<U+FFFD>chantillonnage (tous les formats sont accept<U+FFFD>s).

## SiteMeasure

Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".

-	**uSiteMeasureID**:(Identifiant unique de la mesure sur site): (Primary Key) [string] Identifiant unique pour le site d'<U+FFFD>chantillonnage.


-	**siteMeasureID**:(Identifiant de la mesure sur site): [string] Identifiant unique utilis<U+FFFD> dans la table horizontale seulement. Utiliser quand toutes les mesures sont effectu<U+FFFD>es sur le m<U+FFFD>me <U+FFFD>chantillon.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr<U+FFFD>e un lien vers la table "Site" pour d<U+FFFD>crire le site d'<U+FFFD>chantillonnage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<U+FFFD>e un lien vers la table "Instrument" pour d<U+FFFD>crire l'appareil utilis<U+FFFD> pour effectuer la mesure.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr<U+FFFD>e un lien avec les informations propres au reporteur associ<U+FFFD> <U+FFFD> la mesure.


-	**sampleID**:(Identifiant de l'<U+FFFD>chantillon): (Foreign key) [string] Cr<U+FFFD>e un lien avec la table "Sample" pour d<U+FFFD>crire l'<U+FFFD>chantillon mesur<U+FFFD>.


-	**dateTime**:(Date et heure): [date] Date <U+FFFD> laquelle la mesure a <U+FFFD>t<U+FFFD> r<U+FFFD>alis<U+FFFD>e.


-	**type**:(Type): [category] Type de mesure r<U+FFFD>alis<U+FFFD>e. Le pr<U+FFFD>fixe "env" est utilis<U+FFFD> pour une variable envioronnementale, alors que "ww" indique une mesure r<U+FFFD>alis<U+FFFD>e sur les eaux us<U+FFFD>es.
	-	`envTemp`: Temp<U+FFFD>rature ambiante.
	-	`envRnF`: Pluie (toute pr<U+FFFD>cipitation sous forme liquide).
	-	`envSnwF`: Neige (toute pr<U+FFFD>cipitations sous forme solide).
	-	`envSnwD`: <U+FFFD>paisseur de neige au sol.
	-	`wwFlow`: D<U+FFFD>bit d'eau us<U+FFFD>e.
	-	`wwTemp`: Temp<U+FFFD>rature de l'eau us<U+FFFD>e.
	-	`wwTSS`: Mati<U+FFFD>res en suspension
	-	`wwCOD`: Demande chimique en oxyg<U+FFFD>ne
	-	`wwTurb`: Turbidit<U+FFFD>
	-	`wwOPhos`: Concentration d'ortho-phosphates
	-	`wwNH4N`: Concentrsation d'azote ammoniacal, exprim<U+FFFD> en N.
	-	`wwTN`: Azote total, exprim<U+FFFD> en N
	-	`wwpH`: pH
	-	`wwBOD5t`: Demande biochimique totale en oxygene sur 5 jours
	-	`wwBOD5c`: Demande biochinique carbonnee en oxygene sur 5 jours
	-	`wwPtot`: Phosphates totaux
	-	`wwPP`: Phosphore total
	-	`wwCond`: Conductivit<U+FFFD>

-	**typeOther**:(Type autre): [string] Description d'un param<U+FFFD>tre mesur<U+FFFD> ne faisant pas partie des options disponibles.


-	**typeDescription**:(Description du type): [string] Ajouter toutes notes additionnelles en lien avec la mesure effectu<U+FFFD>e.


-	**aggregation**:(Agr<U+FFFD>gation): [category] M<U+FFFD>thode d'agr<U+FFFD>gation utilise<U+FFFD>e pour rapporter la mesure.
	-	`single`: La valeur n'a subi aucune agr<U+FFFD>gation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut <U+FFFD>tre un r<U+FFFD>plica.
	-	`mean`: Moyenne arithm<U+FFFD>tique.
	-	`geoMn`: Moyenne g<U+FFFD>om<U+FFFD>trique.
	-	`median`: M<U+FFFD>diane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'<U+FFFD>cart type.
	-	`other`: Autre m<U+FFFD>thode d'agr<U+FFFD>gation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agr<U+FFFD>gation autre): [string] Description d'une agr<U+FFFD>gation ne faisant pas partie des options disponibles.


-	**aggregationDesc**:(Agr<U+FFFD>gation desc): [string] Informations (ou r<U+FFFD>f<U+FFFD>rence) li<U+FFFD>e(s) <U+FFFD> la m<U+FFFD>thode d'agr<U+FFFD>gation utilis<U+FFFD>e pour rapporter la mesure.


-	**value**:(Valeur): [float] La valeur num<U+FFFD>rique de la mesure effectu<U+FFFD>e. Utilise "NA" pour les valeurs manquantes et laisser une note.


-	**unit**:(Unit<U+FFFD>): [category] L'unit<U+FFFD> de mesure
	-	`c`: Degr<e9>s Celcius
	-	`mm`: Millim<e8>tres
	-	`m3H`: M<e8>tres cubes par heure
	-	`m3D`: M<e8>tres cubes par jour
	-	`mgL`: Milligrammes par litre
	-	`pH`: Unit<e9>s de pH
	-	`usCM`: Micro-siemens par centim<e8>tre

-	**qualityFlag**:(Indicateur de mauvaise qualit<U+FFFD>): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<U+FFFD>?


-	**accessToPublic**:(Acc<U+FFFD>s au public): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par le public. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToAllOrgs**:(Acc<U+FFFD>s <U+FFFD> toutes les organisations): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToSelf**:(Acc<U+FFFD>s au reporteur lui-m<U+FFFD>me): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par le reporteur lui-m<U+FFFD>me. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToPHAC**:(Acc<U+FFFD>s <U+FFFD> l'ASPC): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les employ<U+FFFD>s de l'Agence de Sant<U+FFFD> Publique du Canada. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToLocalHA**:(Acc<U+FFFD>s <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique locale): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique locales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToProvHA**:(Acc<U+FFFD>s <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique provinciale): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique provinciales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e sera accessible <U+FFFD> l'autorit<U+FFFD> de sant<U+FFFD> publique de la province o<U+FFFD> l'<U+FFFD>chantillonnage a <U+FFFD>t<U+FFFD> r<U+FFFD>alis<U+FFFD>e.


-	**accessToOtherProv**:(Acc<U+FFFD>s aux autres provinces): [boolean] Si "Non", la donn<U+FFFD>e ne sera pas accessible par les autorit<U+FFFD>s de sant<U+FFFD> publique provinciales. Si "Oui" ou laiss<U+FFFD> vide, la donn<U+FFFD>e leur sera accessible.


-	**accessToDetails**:(Acc<U+FFFD>s aux d<U+FFFD>tails): [boolean] Indique si des informations suppl<U+FFFD>mentaires sur la confidentialit<U+FFFD> de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Reporter

Le reporteur ou l'organisation responsable de la collecte de données ou responsable de la qualité des données reportées.

-	**reporterID**:(Identifiant du reporteur): (Primary Key) [string] Identifiant unique pour la personne ou l'organisation responsable des donn<U+FFFD>es rapport<U+FFFD>es.


-	**siteIDDefault**:(Identifiant du site par d<U+FFFD>faut): (Foreign key) [string] Identifiant de Site utilis<U+FFFD> par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> par ce reporteur. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "siteID" dans la table "Site"


-	**labIDDefault**:(Identifiant laboratoire par d<U+FFFD>faut): (Foreign key) [string] Identifiant de Lab utilis<U+FFFD> par d<U+FFFD>faut quand un nouvel <U+FFFD>chantillon est cr<U+FFFD><U+FFFD> par ce reporteur. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "labID" dans la table "Lab"


-	**contactName**:(Nom du contact): [string] Nom complet du reporteur (personne ou organisation)


-	**contactEmail**:(Adresse <U+FFFD>lectronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(T<U+FFFD>l<U+FFFD>phone du contact): [string] Num<U+FFFD>ro de t<U+FFFD>l<U+FFFD>phone du contact.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Lab

Laboratoire effectuant des analyses d'échantillons d'eaux usées d'un ou plusieurs sites.

-	**labID**:(Identifiant du laboratoire): (Primary Key) [string] Identifiant unique pour le laboratoire.


-	**assayMethodIDDefault**:(Identifiant de la m<U+FFFD>thode d'analyse par d<U+FFFD>faut): (Foreign key) [string] Identifiant de la m<U+FFFD>thode d'analyse utilis<U+FFFD>e par d<U+FFFD>faut quand une nouvelle mesure est cr<U+FFFD><U+FFFD> par ce laboratoire. Se r<U+FFFD>f<U+FFFD>rer <U+FFFD> la colonne "assayMethodID" dans la table "AssayMethod"


-	**name**:(Nom): [string] Nom du laboratoire.


-	**contactName**:(Nom du contact): [string] Personne contact de ce laboratoire.


-	**contactEmail**:(Adresse <U+FFFD>lectronique du contact): [string] Adresse courriel du contact.


-	**contactPhone**:(T<U+FFFD>l<U+FFFD>phone du contact): [string] Num<U+FFFD>ro de t<U+FFFD>l<U+FFFD>phone du contact.


-	**updateDate**:(Date de mise <U+FFFD> jour): [date] Date o<U+FFFD> l'information a <U+FFFD>t<U+FFFD> report<U+FFFD>e une premi<U+FFFD>re fois ou mise <U+FFFD> jour.

## AssayMethod

La méthode d'analyse utilisée pour réaliser les mesures. Crée une nouvelle rangée dans cette table si des changements (améliorations) sont apportées à une technique d'analyse existante. Garder le même identifiant et modifier le numéro de version. Une nouvelle rangée représentant une nouvelle version d'une méthode existante peut inclure des informations seulement dans les colonnes qui ont changé d'une version à l'autre, cependant, nous recommandons de remplir les autres colonnes avec les valeurs provenant de la version précédente afin de décrire clairement la méthode en entier. Ajouter la date courante lorsqu'une nouvelle rangée est créée.

-	**assayMethodID**:(Identifiant de la m<U+FFFD>thode d'analyse): (Primary Key) [string] Identifiant unique pour la m<U+FFFD>thode d'analyse.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr<U+FFFD>e un lien vers la table "Instrument" pour d<U+FFFD>crire l'appareil utilis<U+FFFD> pour effectuer la mesure.


-	**name**:(Nom): [string] Nom de la m<U+FFFD>thode d'analyse.


-	**version**:(Version): [string] Version de la m<U+FFFD>thode d'analyse. Un versionnement de type s<U+FFFD>mantique est recommand<U+FFFD>.


-	**summary**:(R<U+FFFD>sum<U+FFFD>): [string] Br<U+FFFD>ve description de la m<U+FFFD>thode d'analyse et de comment celle-ci diff<U+FFFD>re d'autres m<U+FFFD>thodes.


-	**referenceLink**:(Lien vers r<U+FFFD>f<U+FFFD>rence): [string] Lien vers la proc<U+FFFD>dure standard.


-	**date**:(Date): [date] Date <U+FFFD> laquelle la m<U+FFFD>thode d'analyse (ou une nouvelle version d'une m<U+FFFD>thode existante) a <U+FFFD>t<U+FFFD> cr<U+FFFD>e.


-	**aliasID**:(Identifiant de l'alias): [string] Identifiants d'autres m<U+FFFD>thodes d'analyse pr<U+FFFD>sentes dans la table qui sont similaires <U+FFFD> la m<U+FFFD>thode courante. Ins<U+FFFD>rer sous forme de liste s<U+FFFD>par<U+FFFD>e par des virgules.


-	**extractionVolMl**:(Volume d'extraction ml): [float] Volume de l'<U+FFFD>chantillon analys<U+FFFD> (en millilitres)


-	**loq**:(Limite de quantification): [float] Limite de quantification pour cette m<U+FFFD>thode, le cas <U+FFFD>ch<U+FFFD>ant.


-	**lod**:(Limite de d<U+FFFD>tection): [float] Limite de d<U+FFFD>tection pour cette m<U+FFFD>thode, le cas <U+FFFD>ch<U+FFFD>ant.


-	**unit**:(Unit<U+FFFD>): [category] Unit<U+FFFD> de mesure utilis<U+FFFD>e par cette m<U+FFFD>thode et qui est applicable pour la limite de d<U+FFFD>tection ou de quantification.
	-	`gcPMMoV`: Copies de g<U+FFFD>ne ou de variant par copie de PMMoV
	-	`gcMl`: Copies de g<U+FFFD>ne ou de variant par millilitre.
	-	`gcGms`: Copies de g<U+FFFD>ne ou de variant par gramme de solides.
	-	`gcL`: Copies de g<U+FFFD>ne ou de variant par litre.
	-	`gcCrA`: Copies de g<U+FFFD>ne ou de variant par copie de CrAssphage
	-	`other`: Autre mesure de copies virales ou de qualit<U+FFFD> des eaux us<U+FFFD>es. Ajouter une description dans "unitOther"

-	**unitOther**:(Unit<U+FFFD> autre): [string] Unit<U+FFFD> de mesure utilis<U+FFFD>e par cette m<U+FFFD>thode et qui est applicable pour la limite de d<U+FFFD>tection ou de quantification dans le cas o<U+FFFD> celle-ci n'est pas disponible.


-	**methodConc**:(M<U+FFFD>thode de concentration): [string] Description de la m<U+FFFD>thode utilis<U+FFFD>e pour concentrer l'<U+FFFD>chantillon.


-	**methodExtract**:(M<U+FFFD>thode d'extraction): [string] Description de la m<U+FFFD>thode utilis<U+FFFD>e pour extraire l'<U+FFFD>chantillon.


-	**methodPcr**:(M<U+FFFD>thode PCR): [string] Description de la m.<U+FFFD>thode PCR utiis<U+FFFD>e.


-	**qualityAssQC**:(Contr<U+FFFD>le de qualit<U+FFFD>): [string] Description des <U+FFFD>tapes de contr<U+FFFD>le de qualit<U+FFFD> mises en place dans la m<U+FFFD>thode.


-	**inhibition**:(Inhibition): [string] Description des param<U+FFFD>tres d'inhibition li<U+FFFD>s <U+FFFD> cette m<U+FFFD>thode.


-	**surrogateRecovery**:(R<U+FFFD>cup<U+FFFD>ration du virus substitut): [string] Description de la m<U+FFFD>thode de r<U+FFFD>cup<U+FFFD>ration du virus de substitution li<U+FFFD>e <U+FFFD> cette m<U+FFFD>thode.

## Instrument

L'instrument utilisé pour mesurer les échantillons et l'eau usée des sites d'échantillonnage. La méthode d'analyse pour les mesures virales sont décrites dans la table "AssayMethod".

-	**instrumentID**:(Identifiant de l'instrument): (Primary Key) [string] Identifiant unique pour l'instrument de mesure.


-	**name**:(Nom): [string] Nom de l'instrument de mesure.


-	**model**:(Mod<U+FFFD>le): [string] Num<U+FFFD>ro de mod<U+FFFD>le et/ou de version de l'instrument de mesure.


-	**description**:(Description): [string] Description de l'instrument.


-	**alias**:(Alias): [string] Identifiants d'autres instruments pr<U+FFFD>sents dans la table qui sont similaires <U+FFFD> l'instrument courant. Ins<U+FFFD>rer sous forme de liste s<U+FFFD>par<U+FFFD>e par des virgules.


-	**referenceLink**:(Lien vers r<U+FFFD>f<U+FFFD>rence): [string] Lien vers un document de r<U+FFFD>f<U+FFFD>rence pour l'instrument de mesure.


-	**type**:(Type): [category] Type de l'instrument de mesure.
	-	`online`: Capteur en ligne.
	-	`lab`: Analyse en laboratoire.
	-	`hand`: Mesure <U+FFFD> l'aide d'un capteur manuel.
	-	`atline`: Mesure <U+FFFD> l'aide d'un <U+FFFD>chantillonneur.
	-	`other`: Autre type d'appareil de mesure. Ajouter une description dans "instrumentTypeOther"

-	**typeOther**:(Type autre): [string] Description du type d'instrument dans le cas o<U+FFFD> il ne serait pas disponible.

## Polygon

Polygone englobant une région de la surface terrestre. Normalement, ces polygones représentent soit des bassin de drainage d'un réseau d'égouts ou une région de santé publique, ou une autre région associée à des données reportées.

-	**polygonID**:(Identifiant du polygone): (Primary Key) [string] Identifiant unique du polygone.


-	**name**:(Nom): [string] Nom du polygon (devrait <U+FFFD>tre descriptif)


-	**pop**:(Population): [integer] Population approximative vivant dans la r<U+FFFD>gion repr<U+FFFD>sent<U+FFFD>e par le polygone.


-	**type**:(Type): [category] Type de polygone.
	-	`swrCat`: Zone de captage d'un r<U+FFFD>seau d'<U+FFFD>gout.
	-	`hlthReg`: R<U+FFFD>gion de sant<U+FFFD> desservie par le r<U+FFFD>seau d'<U+FFFD>gout.

-	**wkt**:(Wkt): [string] Description formelle du polygone (format Well-Known-Text (wkt))


-	**file**:(Fichier): [blob] Fichier repr<U+FFFD>sentant la g<U+FFFD>om<U+FFFD>trie du polygone (blob).


-	**link**:(Lien): [string] Lien vers une r<U+FFFD>f<U+FFFD>rence externe d<U+FFFD>crivant la g<U+FFFD>om<U+FFFD>trie du polygone.

## CovidPublicHealthData

Données de patients pour la COVID-19 pour une région spécifiée par un polygone.

-	**cphdID**:(Identifiant de CPHD): (Primary Key) [string] Identifiant unique pour l'information de sant<U+FFFD> publique report<U+FFFD>e.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Identifiant unique pour la personne ou l'organisation responsable des donn<U+FFFD>es rapport<U+FFFD>es.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Cr<U+FFFD>e un lien vers la table "Polygon". Le polygon li<U+FFFD> devrait englober la r<U+FFFD>gion repr<U+FFFD>sent<U+FFFD>e par les donn<U+FFFD>es consign<U+FFFD>es ici.


-	**date**:(Date): [string] Date de reportage des donn<U+FFFD>es de mesure de la COVID-19.


-	**type**:(Type): [category] Type de donn<U+FFFD>e de mesure de la COVID-19.
	-	`conf`: Nombre de cas confirm<U+FFFD>s. La mesure devrait <U+FFFD>tre accompagn<U+FFFD>e d'une valeur dans la colonne "dateType"
	-	`active`: Nombre de cas actifs.
	-	`test`: Nombre de tests effectu<U+FFFD>s.
	-	`posTest`: Nombre de tests positifs.
	-	`pPosRt`: Pourcentage de positivit<U+FFFD> des tests.
	-	`hospCen`: Rencensement des patients admis <U+FFFD> un h<U+FFFD>pital avec la COVID-19.
	-	`hospAdm`: Nombre d'admissions ou nombre de patients admis <U+FFFD> l'h<U+FFFD>pital.

-	**dateType**:(Type de date): [category] Type de date utiis<U+FFFD>e pour reporter les donn<U+FFFD>es.
	-	`episode`: Date estim<U+FFFD>e <U+FFFD> laquelle l'<U+FFFD>pisode de maladie s'est d<U+FFFD>clar<U+FFFD>. Habituellement calcul<U+FFFD> en se basant sur la date des premiers sympt<U+FFFD>mes, la date de test ou la date de reportage.
	-	`onset`: Date <U+FFFD> laquelle les premiers sympt<U+FFFD>mes apparaissent. Cette donn<U+FFFD>e est souvent inconnue. La date d'<U+FFFD>pisode est alors commun<U+FFFD>ment utilis<U+FFFD>e.
	-	`report`: Date <U+FFFD> laquelle la donn<U+FFFD>e a <U+FFFD>t<U+FFFD> report<U+FFFD>e <U+FFFD> la sant<U+FFFD> publique. Cette mesure est commun<U+FFFD>ment utilis<U+FFFD>e.
	-	`test`: Date <U+FFFD> laquelle le test de COVID-19 a <U+FFFD>t<U+FFFD> effectu<U+FFFD>.

-	**value**:(Valeur): [float] La valeur num<U+FFFD>rique de la mesure effectu<U+FFFD>e. Utilise "NA" pour les valeurs manquantes et laisser une note.


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

