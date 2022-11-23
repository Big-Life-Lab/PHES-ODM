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

-	**sampleID**:(Identifiant de l'�chantillon): (Primary Key) [string] Identifiant unique pour l'�chantillon. Suggestion:siteID-date-index.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr�e un lien avec la table "Site" pour d�crire le point d'�chantillonage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr�e un lien avec la table "Instrument" pour d�crire l'instrument utilis� pour l'�chantillonnage.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr�e un lien avec la table "Reporter" pour identifier le reporteur ayant pr�lev� l'�chantillon.


-	**dateTime**:(Date et heure): [datetime] Date, heure et fuseau horaire de collecte d'un �chantillon ponctuel.


-	**dateTimeStart**:(Date et heure de d�but): [datetime] Date, heure et fuseau horaire de d�but de collecte d'un �chantillon composite.


-	**dateTimeEnd**:(Date et heure de fin): [datetime] Date, heure et fuseau horaire de fin de collecte d'un �chantillon composite.


-	**type**:(Type): [category] Type d'�chantillon.
	-	`rawWW`: Eau us�e brute
	-	`swrSed`: S�diments provenant des �gouts.
	-	`pstGrit`: Eau us�e apr�s d�grillage et dessablage.
	-	`pSludge`: Boue provenant d'un d�canteur primaire.
	-	`pEfflu`: Effluent obtenu apr�s un d�canteur primaire.
	-	`sSludge`: Boue provenant d'un d�canteur secondaire.
	-	`sEfflu`: Effluent obtenu apr�s un d�canteur secondaire.
	-	`water`: Eau non-us�e provenant de toute �tendue d'eau.
	-	`faeces`: Mati�re f�cale.
	-	`other`: Autre type de site d'�chantillonnage. Ajouter une description dans la colonne "typeOther"

-	**typeOther**:(Type autre): [string] Description d'un type d'�chantillon ne faisant pas partie des options disponibles.


-	**collection**:(M�thode de collecte): [category] M�thode utilis�e pour �chantillonner.
	-	`cpTP24h`: Un �chantillon composite proportionnel au temps pr�lev� sur 24 heures, g�n�ralement pr�lev� par un auto-�chantilonneur.
	-	`cpFP24h`: Un �chantillon composite proportionnel au d�bit pr�lev� sur 24 heures, g�n�ralement pr�lev� par un auto-�chantilonneur.
	-	`grb`: Un seul �chantillon ponctuel repr�sentatif.
	-	`grbCp8h`: Un �chantillon composite pr�lev� sur 8 heures consitu� d'�chantillons ponctuels collect�s une fois par heure, g�n�ralement pr�lev� manuellement.
	-	`grbCp3h`: Un �chantillon composite pr�lev� sur 3 heures consitu� d'�chantillons ponctuels collect�s une fois par heure, g�n�ralement pr�lev� manuellement.
	-	`grbCp3`: Un �chantillon composite compos� de 3 �chantillons ponctuels.
	-	`mooreSw`: Un �chantillon passif collect� par la m�thode de Moore.
	-	`other`: Autre m�thode de collecte. Ajouter une description dans la colonne "descriptionOther"

-	**collectionOther**:(M�thode de collecte autre): [string] Description d'une m�thode d'�chantillonnage ne faisant pas partie des options disponibles.


-	**preTreatment**:(Pr�-traitement): [boolean] L'�chantillon a-t-il �t� chimiquement alt�r� par un ajout de stabilisant ou autre?


-	**preTreatmentDescription**:(Description du pr�-traitment): [string] Description du pr�-traitement le cas �ch�ant.


-	**pooled**:(�chantillon combin�): [boolean] S'il s'agit d'un �chantillon combin�, c'est-�-dire, est-il compos� de plusieurs �chantillons "enfants"?


-	**children**:(Enfants): [string] Si l'�chantillon est li�e � des sous-�chantillons (soit parce qu'il s'agit d'un �chantillon combin� ou parce que des sous-�chantillons ont �t� pr�lev�s dans cet �chantillon), ins�rer les identifiant des �chantillons enfants dans une liste s�par�e par des virgules.


-	**parent**:(Parent): [string] Si l'�chantillon a �t� combin� � un plus grand �chantillon, indiquer l'identifiant du plus grand �chantillon.


-	**sizeL**:(Volume l): [float] Volume total d'eau ou de boue pr�lev�e.


-	**fieldSampleTempC**:(Temp�rature de l'�chantillon de terrain c): [float] Temprature � laquelle l'�chantillon �tait stock� pendant l'�chantillonnage. Ce champ est principalement pertinent pour les �chantillons composites, qui peuvent �tre stock�es � temp�rature ambiante ou r�frig�r�s durant l'�chantillonnage.


-	**shippedOnIce**:(Exp�di� sur glace): [boolean] L'�chantillon a-t-il �t� gard� au froid lors du transport vers le laboratoire?


-	**storageTempC**:(Temp�rature de stockage c): [float] Temp�rature de stockage de l'�chantillon en degr�s Celsius


-	**qualityFlag**:(Indicateur de mauvaise qualit�): [boolean] Le reporteur a-t-il des doutes sur la qualit� de l'�chantillon?


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## WWMeasure

Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".

-	**uWwMeasureID**:(id u mesure eaux us�es): (Primary Key) [string] Identifiant unique pour la mesure pour la table "WWMeasurement"


-	**wwMeasureID**:(id mesure eaux us�es): [string] Identifiat unique utilis� dans la table horizontale seulement. Utiliser quand toutes les mesures effectu�es sur un �chantillon sont r�alis�es en m�me temps dans le m�me laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.


-	**sampleID**:(Identifiant de l'�chantillon): (Foreign key) [string] Cr�e un lien avec la table "Sample" pour d�crire l'�chantillon mesur�.


-	**labID**:(Identifiant du laboratoire): (Foreign key) [string] Cr�e un lien avec la table "Lab" pour d�crire le laboratoire effectuant la mesure.


-	**assayID**:(Identifiant de la m�thode d'analyse): (Foreign key) [string] Cr�e un lien avec la table "AssayMethod" pour d�crire la m�thode employ�e pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr�e un lien avec la table "Instrument" l'appareil employ� pour effectuer la mesure. Utiliser l'identifiant de la m�thode d'analyse pour les mesures virales.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr�e un lien avec les informations propres au reporteur associ� � la mesure.


-	**analysisDate**:(Date de l'analyse): [date] Date � laquelle la mesure a �t� r�alis�e en laboratoire.


-	**reportDate**:(Date de reportage de la donn�e): [date] Date a laquelle la donn�e a �t� rapport�e. Un �chantillon pourrait avoir des mesures pour lesquelles la m�thode d'analyse ou la m�thode de reportage des donn�es aurait chang�e. Dans ce cas, utiliser le m�me sampleID, mais cr�er une nouvelle entr�e dans la table "WWMeasure avec un "MeasureID" diff�rent, et la date de reportage de la donn�e et l'identifiant de la m�thode d'analyse appropri�s.


-	**fractionAnalyzed**:(Fraction analys�e): [category] Fraction de l'�chantillon employ�e pour la mesure.
	-	`liquid`: Fraction liquide.
	-	`solid`: Fraction solide.
	-	`mixed`: �chantillon homog�n�is�/m�lang�.

-	**type**:(Type): [category] Le param�tre mesur� avec cette analyse. Exemples: Une r�gion de g�ne cible (cov), un biomarqueur (n) ou un indicateur de la qualit� de l'eau (wq)
	-	`covN1`: G�ne nucleocapside N1 du SRAS-CoV-2
	-	`covN2`: G�ne nucleocapside N2 du SRAS-CoV-2
	-	`covN3`: G�ne nucleocapside N3 des virus similaires au SRAS
	-	`covE`: R�gion g�nique E du SRAS-CoV-2
	-	`varB117`: Variant B.1.1.7
	-	`varB1351`: Variant B.1.351
	-	`varP1`: Variant P.1
	-	`covRdRp`: R�gion g�nique RdRp du SRAS-CoV-2
	-	`nPMMoV`: Virus de la marbrure l�g�re du piment
	-	`ncrA`: CrAssphage
	-	`nbrsv`: Virus respiratoire syncytial bovin
	-	`wqTS`: Solides totaux
	-	`wqTSS`: Mati�res en suspension
	-	`wqVSS`: Mati�res volatiles en suspension
	-	`wqCOD`: Demande chimique en oxyg�ne
	-	`wqOPhos`: Concentration d'ortho-phosphates
	-	`wqNH4N`: Concentrsation d'azote ammoniacal, exprim� en N.
	-	`wqTN`: Azote total, exprim� en N
	-	`wqPh`: pH
	-	`wqCond`: Conductivit�
	-	`temp`: la temp�rature de l'�chantillon au moment o� la mesure est prise, souvent � son arriv�e au laboratoire.
	-	`other`: Autre cat�gorie de mesure. Ajouter une description de la cat�gorie dans la colonne "categoryOther".

-	**typeOther**:(Type autre): [string] Description d'un param�tre mesur� ne faisant pas partie des options disponibles.


-	**unit**:(Unit�): [category] Unit� de mesure.
	-	`gcPMMoV`: Copies de g�ne ou de variant par copie de PMMoV
	-	`gcMl`: Copies de g�ne ou de variant par millilitre.
	-	`gcGs`: Copies de g�ne ou de variant par gramme de solides.
	-	`gcL`: Copies de g�ne ou de variant par litre.
	-	`gcCrA`: Copies de g�ne ou de variant par copie de CrAssphage
	-	`Ct`: Cycle seuil.
	-	`mgL`: Milligrammes par litre.
	-	`ph`: Unit�s de pH
	-	`uScm`: Microsiemens par centim�tre.
	-	`detected`: Copies de g�ne ou de variant d�tect� dans "sampleGene". 1=Detect�, 0=Non-d�tect�.
	-	`propVar`: Proportion du variant dans l'�chantillon
	-	`pp`: Pourcentage de positifs (m�thode de Moore)
	-	`pps`: Pourcentage de boues primaire (pour solides totaux)
	-	`c`: temp�ratures en degr�s Celsius
	-	`bool`: Dans les cas o� un oui ou un non bool�en est requis, utilisez bool
	-	`other`: Autre mesure de copies virales ou de qualit� des eaux us�es. Ajouter une description dans "unitOther"

-	**unitOther**:(Unit� autre): [string] Description d'une unit� de mesure ne faisant pas partie des options disponibles.


-	**aggregation**:(Agr�gation): [category] Indicateur statistique utilis�e pour rapporter la mesure effectu�e. Chaque agr�gation doit �tre report�e comme une mesure diff�rente (avec un identifiant diff�rent)
	-	`single`: La valeur n'a subi aucune agr�gation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut �tre un r�plica.
	-	`mean`: Moyenne arithm�tique.
	-	`meanNr`: Moyenne arithm�tique normalis�e.
	-	`geoMn`: Moyenne g�om�trique.
	-	`geoMnNr`: Moyenne g�om�trique normalis�e.
	-	`median`: M�diane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'�cart type.
	-	`sdNr`: L'�cart type normalis�.
	-	`other`: Autre m�thode d'agr�gation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agr�gation autre): [string] Description d'une agr�gation ne faisant pas partie des options disponibles.


-	**index**:(Index): [integer] Index de la mesure dans le cas o� la m�me mesure a �t� prise en replicata.


-	**value**:(Valeur): [float] La valeur num�rique de la mesure effectu�e. Utilise "NA" pour les valeurs manquantes et laisser une note.


-	**qualityFlag**:(Indicateur de mauvaise qualit�): [boolean] Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit�?


-	**accessToPublic**:(Acc�s au public): [boolean] Si "Non", la donn�e ne sera pas accessible par le public. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToAllOrg**:(Acc�s � toutes les organisations): [boolean] Si "Non", la donn�e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToSelf**:(Acc�s au reporteur lui-m�me): [boolean] Si "Non", la donn�e ne sera pas accessible par le reporteur lui-m�me. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToPHAC**:(Acc�s � l'ASPC): [boolean] Si "Non", la donn�e ne sera pas accessible par les employ�s de l'Agence de Sant� Publique du Canada. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToLocalHA**:(Acc�s � l'autorit� de sant� publique locale): [boolean] Si "Non", la donn�e ne sera pas accessible par les autorit�s de sant� publique locales. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToProvHA**:(Acc�s � l'autorit� de sant� publique provinciale): [boolean] Si "Non", la donn�e ne sera pas accessible par les autorit�s de sant� publique provinciales. Si "Oui" ou laiss� vide, la donn�e sera accessible � l'autorit� de sant� publique de la province o� l'�chantillonnage a �t� r�alis�e.


-	**accessToOtherProv**:(Acc�s aux autres prov): [boolean] Si "Non", la donn�e ne sera pas accessible par les autorit�s de sant� publique provinciales. Si "Oui" ou laiss� vide, la donn�e leur sera accessible.


-	**accessToDetails**:(Acc�s aux d�tails): [boolean] Indique si des informations suppl�mentaires sur la confidentialit� de la mesure sont disponibles.


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.

## Site

Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"

-	**siteID**:(Identifiant du site): (Primary Key) [string] Identifiant unique pour l'�chantillon. Suggestion:siteID-date-index.


-	**name**:(Nom): [string] Nom du site d'�chantillonnage. Peut �tre le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'�gouts, etc.


-	**description**:(Description): [string] Description du site d'�chantillonnage (ville, b�timent, rue, etc.) pour mieux identifier le site d'�chantillonnage.


-	**publicHealthDepartment**:(Département ou région de santé publique): [string] NA


-	**healthRegion**:(Région de planification sanitaire): [string] NA


-	**type**:(Type): [category] Type de site ou d'institution du site d'�chantillonnage.
	-	`airPln`: Avion.
	-	`corFcil`: Prison.
	-	`school`: �cole.
	-	`hosptl`: H�pital.
	-	`ltcf`: �tablissement de soins de longue dur�e.
	-	`swgTrck`: Camion de vidange.
	-	`uCampus`: Campus universitaire.
	-	`mSwrPpl`: Collecteur d'�gouts.
	-	`pStat`: Station de pompage.
	-	`holdTnk`: Bassin de stockage.
	-	`retPond`: Bassin de r�tention.
	-	`wwtpMuC`: Station de traitement des eaux us�es municipales pour �gouts combin�s.
	-	`wwtpMuS`: Station de traitement des eaux us�es municipales pour �gouts sanitaires seulement.
	-	`wwtpInd`: Station de traitement des eaux us�es industrielle.
	-	`lagoon`: Syst�me de lagunage pour traitement des eaux us�es.
	-	`septTnk`: Fosse septique.
	-	`river`: Rivi�re, �tendue d'eau naturelle.
	-	`lake`: Lac, �tendue d'eau naturelle.
	-	`estuary`: Estuaire, �tendue d'eau naturelle.
	-	`sea`: Mer, �tendue d'eau naturelle.
	-	`ocean`: Oc�an, �tendue d'eau naturelle.
	-	`other`: Autre type de site. Ajouter une description dans "typeOther".

-	**typeOther**:(Type autre): [string] Description du site d'�chantillonnage dans le cas o� un type ad�quat n'est pas disponible.


-	**sampleTypeDefault**:(Type d'�chantillon par d�faut): [category] Type d'�chantilon utilis� par d�faut quand un nouvel �chantillon est cr�� pour ce site. Se r�f�rer � la colonne "type" dans la table "Sample"


-	**sampleTypeOtherDefault**:(Type d'�chantillon autre d�faut): [string] Type d'�chantilon utilis� par d�faut quand un nouvel �chantillon est cr�� pour ce site. Se r�f�rer � la colonne "typeOther" dans la table "Sample"


-	**sampleCollectionDefault**:(Pr�l�vement d'�chantillons par d�faut): [category] M�thode d'�chantillonnage par d�faut quand un nouvel �chantillon est cr�� pour ce site. Se r�f�rer � la colonne "collection" dans la table "Sample"


-	**sampleCollectOtherDefault**:(Pr�l�vement d'un autre �chantillon par d�faut): [string] M�thode d'�chantillonnage par d�faut quand un nouvel �chantillon est cr�� pour ce site. Se r�f�rer � la colonne "collectionOther" dans la table "Sample"


-	**sampleStorageTempCDefault**:(Temp�rature de stockage de l'�chantillon c par d�faut): [float] Temp�raure de stockage par d�faut quand un nouvel �chantillon est cr�� pour ce site. Se r�f�rer � la colonne "storageTempC" dans la table "Sample"


-	**measureFractionAnalyzedDefault**:(Fraction de mesure analys�e par d�faut): [category] Fraction par d�faut quand une nouvelle mesure est cr��e pour cet �chantillon. Se r�f�rer � la colonne "fractionAnalyzed" dans la table "WWMeasure"


-	**geoLat**:(G�o lat): [float] Position g�ographique du site d'�chantillonnage. Latitude exprim�e en coordonn�es d�cimales (ex. 45.424721)


-	**geoLong**:(G�o long): [float] Position g�ographique du site d'�chantillonnage. Longitude exprim�e en coordonn�es d�cimales (ex. -75.695000)


-	**notes**:(Notes): [string] Ajouter toutes notes additionnelles.


-	**polygonID**:(Identifiant du polygone): (Foreign key) [string] Cr�e un lien vers la table "Polygon". Le polygon li� devrait englober la r�gion qui se draine dans le site d'�chantillonnage.


-	**sewerNetworkFileLink**:(Lien vers le fichier du r�seau d'�gouts): [string] Lien vers un fichier contenant toute information additionnelle au sujet du r�seau d'�gouts associ� � ce site d'�chantillonnage (tous les formats sont accept�s).


-	**sewerNetworkFileBLOB**:(Fichier blob du r�seau d'�gouts): [blob] Un fichier contenant toute information additionnelle au sujet du r�seau d'�gouts associ� � ce site d'�chantillonnage (tous les formats sont accept�s).

## SiteMeasure

Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".

-	**uSiteMeasureID**:(Identifiant unique de la mesure sur site): (Primary Key) [string] Identifiant unique pour le site d'�chantillonnage.


-	**siteMeasureID**:(Identifiant de la mesure sur site): [string] Identifiant unique utilis� dans la table horizontale seulement. Utiliser quand toutes les mesures sont effectu�es sur le m�me �chantillon.


-	**siteID**:(Identifiant du site): (Foreign key) [string] Cr�e un lien vers la table "Site" pour d�crire le site d'�chantillonnage.


-	**instrumentID**:(Identifiant de l'instrument): (Foreign key) [string] Cr�e un lien vers la table "Instrument" pour d�crire l'appareil utilis� pour effectuer la mesure.


-	**reporterID**:(Identifiant du reporteur): (Foreign key) [string] Cr�e un lien avec les informations propres au reporteur associ� � la mesure.


-	**sampleID**:(Identifiant de l'�chantillon): (Foreign key) [string] Cr�e un lien avec la table "Sample" pour d�crire l'�chantillon mesur�.


-	**dateTime**:(Date et heure): [date] Date � laquelle la mesure a �t� r�alis�e.


-	**type**:(Type): [category] Type de mesure r�alis�e. Le pr�fixe "env" est utilis� pour une variable envioronnementale, alors que "ww" indique une mesure r�alis�e sur les eaux us�es.
	-	`envTemp`: Temp�rature ambiante.
	-	`envRnF`: Pluie (toute pr�cipitation sous forme liquide).
	-	`envSnwF`: Neige (toute pr�cipitations sous forme solide).
	-	`envSnwD`: �paisseur de neige au sol.
	-	`wwFlow`: D�bit d'eau us�e.
	-	`wwTemp`: Temp�rature de l'eau us�e.
	-	`wwTSS`: Mati�res en suspension
	-	`wwCOD`: Demande chimique en oxyg�ne
	-	`wwTurb`: Turbidit�
	-	`wwOPhos`: Concentration d'ortho-phosphates
	-	`wwNH4N`: Concentrsation d'azote ammoniacal, exprim� en N.
	-	`wwTN`: Azote total, exprim� en N
	-	`wwpH`: pH
	-	`wwBOD5t`: Demande biochimique totale en oxygene sur 5 jours
	-	`wwBOD5c`: Demande biochinique carbonnee en oxygene sur 5 jours
	-	`wwPtot`: Phosphates totaux
	-	`wwPP`: Phosphore total
	-	`wwCond`: Conductivit�

-	**typeOther**:(Type autre): [string] Description d'un param�tre mesur� ne faisant pas partie des options disponibles.


-	**typeDescription**:(Description du type): [string] Ajouter toutes notes additionnelles en lien avec la mesure effectu�e.


-	**aggregation**:(Agr�gation): [category] M�thode d'agr�gation utilise�e pour rapporter la mesure.
	-	`single`: La valeur n'a subi aucune agr�gation (donc, la valeur n'est pas une moyenne, un maximum, etc.). La valeur peut �tre un r�plica.
	-	`mean`: Moyenne arithm�tique.
	-	`geoMn`: Moyenne g�om�trique.
	-	`median`: M�diane.
	-	`min`: La valeur la plus basse dans un ensemble.
	-	`max`: La valeur la plus haute dans un ensemble.
	-	`sd`: L'�cart type.
	-	`other`: Autre m�thode d'agr�gation. Ajouter une description dans "aggregationOther".

-	**aggregationOther**:(Agr�gation autre): [string] Description d'une agr�gation ne faisant pas partie des options disponibles.


-	**aggregationDesc**:(Agr�gation desc): [string] Informations (ou r�f�rence) li�e(s) � la m�thode d'agr�gation utilis�e pour rapporter la mesure.


-	**value**:(Valeur): [float] La valeur num�rique de la mesure effectu�e. Utilise "NA" pour les valeurs manquantes et laisser une note.


-	**unit**:(Unit�): [category] L'unit� de mesure
	-	`c`: Degr

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

