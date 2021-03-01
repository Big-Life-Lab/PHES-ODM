CREATE TABLE IF NOT EXISTS [Sample] (
/*L'échantillon est un volume d'eau usée représentatif de l'eau présente sur un site, qui est ensuite analysé en laboratoire.*/
	[sampleID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'échantillon. Suggestion:siteID-date-index.
	[siteID] char, --Crée un lien avec la table "Site" pour décrire le point d'échantillonage.
	[dateTime] integer, --Date, heure et fuseau horaire de collecte d'un échantillon ponctuel.
	[dateTimeStart] integer, --Date, heure et fuseau horaire de début de collecte d'un échantillon composite.
	[dateTimeEnd] integer, --Date, heure et fuseau horaire de fin de collecte d'un échantillon composite.
	[type] char, --Type d'échantillon.
	[typeOther] char, --Description d'un type d'échantillon ne faisant pas partie des options disponibles.
	[collection] char, --Méthode utilisée pour échantillonner.
	[collectionOther] char, --Description d'une méthode d'échantillonnage ne faisant pas partie des options disponibles.
	[preTreatment] integer, --L'échantillon a-t-il été chimiquement altéré par un ajout de stabilisant ou autre?
	[preTreatmentDescription] char, --Description du pré-traitement le cas échéant.
	[pooled] integer, --S'il s'agit d'un échantillon combiné, c'est-à-dire s'il est composé de plusieurs échantillons "enfants"?
	[children] char, --Si l'échantillon est liée à des sous-échantillons (soit parce qu'il s'agit d'un échantillon combiné ou parce que des sous-échantillons ont été prélevés dans cet échantillon), insérer les identifiant des échantillons enfants dans une liste séparée par des virgules.
	[parent] char, --Si l'échantillon a été combiné à un plus grand échantillon, indiquer l'identifiant du plus grand échantillon.
	[sizeL] float, --Volume total d'eau ou de boue prélevée.
	[fieldSampleTempC] float, --Temprature à laquelle l'échantillon était stocké pendant l'échantillonnage. Ce champ est principalement pertinent pour les échantillons composites, qui peuvent être stockées à température ambiante ou réfrigérés durant l'échantillonnage.
	[shippedOnIce] integer, --L'échantillon a-t-il été gardé au froid lors du transport vers le laboratoire?
	[storageTempC] float, --Température de stockage de l'échantillon en degrés Celsius
	[qualityFlag] integer, --Le reporteur a-t-il des doutes sur la qualité de l'échantillon?
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [WWMeasure] (
/*Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".*/
	[uWwMeasureID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la mesure pour la table "WWMeasurement"
	[wwMeasureID] char, --Identifiat unique utilisé dans la table horizontale seulement. Utiliser quand toutes les mesures effectuées sur un échantillon sont réalisées en même temps dans le même laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.
	[sampleID] char, --Crée un lien avec la table "Sample" pour décrire l'échantillon mesuré.
	[labID] char, --Crée un lien avec la table "Lab" pour décrire le laboratoire effectuant la mesure.
	[assayID] char, --Crée un lien avec la table "AssayMethod" pour décrire la méthode employée pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.
	[instrumentID] char, --Crée un lien avec la table "Instrument" l'appareil employé pour effectuer la mesure. Utiliser l'identifiant de la méthode d,analyse pour les mesures virales.
	[reporterID] char, --Crée un lien avec les informations propres au reporteur associé à la mesure.
	[analysisDate] integer, --Date à laquelle la mesure a été réalisée en laboratoire.
	[reportDate] integer, --Date a laquelle la donnée a été reportée. Un échantillon pourrait avoir des mesures pour lesquelles la méthode d'analyse ou la méthode de reportage des données aurait changée. Dans ce cas, utiliser le même sampleID, mais créer une nouvelle entrée dans la table "WWMeasure avec un "MeasureID" différent, et la date de reportage de la donnée et l'identifiant de la méthode d'analyse appropriés.
	[fractionAnalyzed] char, --Fraction de l'échantillon employée pour la mesure.
	[type] char, --Le paramètre mesuré avec cette analyse. Exemples: Une région de gène cible (cov), un biomarqueur (n) ou un indicateur de la qualité de l'eau (wq)
	[typeOther] char, --Description d'un paramètre mesuré ne faisant pas partie des options disponibles.
	[unit] char, --Unité de mesure.
	[unitOther] char, --Description d'une unité de mesure ne faisant pas partie des options disponibles.
	[aggregation] char, --Indicateur statistique utilisée pour rapporter la mesure effectuée. Chaque agrégation doit être reportée comme une mesure différente (avec un identifiant différent)
	[aggregationOther] char, --Description d'une agrégation ne faisant pas partie des options disponibles.
	[index] integer, --Index de la mesure dans le cas où la même mesure a été prise en replicata.
	[value] float, --La valeur numérique de la mesure effectuée.
	[qualityFlag] integer, --Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualité?
	[accessToPublic] integer, --Si "Non", la donnée ne sera pas accessible par le public. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToAllOrg] integer, --Si "Non", la donnée ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToSelf] integer, --Si "Non", la donnée ne sera pas accessible par le reporteur lui-même. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToPHAC] integer, --Si "Non", la donnée ne sera pas accessible par les employés de l'Agence de Santé Publique du Canada. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToLocalHA] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique locales. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToProvHA] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée sera accessible à l'autorité de santé publique de la province où l'échantillonnage a été réalisée.
	[accessToOtherProv] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToDetails] integer, --Indique si des informations supplémentaires sur la confidentialité de la mesure sont disponibles.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([sampleID]) REFERENCES NA(NA) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labID]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Site] (
/*Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"*/
	[siteID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'échantillon. Suggestion:siteID-date-index.
	[name] char, --Nom du site d'échantillonnage. Peut être le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'égouts, etc.
	[description] char, --Description du site d'échantillonnage (ville, bâtiment, rue, etc.) pour mieux identifier le site d'échantillonnage.
	[type] char, --Type de site ou d'institution du site d'échantillonnage.
	[typeOther] char, --Description du site d'échantillonnage dans le cas où une description adéquate n'est pas disponible.
	[sampleTypeDefault] char, --Type d'échantilon utilisé par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "type" dans la table "Sample"
	[sampleTypeOtherDefault] char, --Type d'échantilon utilisé par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "typeOther" dans la table "Sample"
	[sampleCollectionDefault] char, --Méthode d'échantillonnage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "collection" dans la table "Sample"
	[sampleCollectOtherDefault] char, --Méthode d'échantillonnage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "collectionOther" dans la table "Sample"
	[sampleStorageTempCDefault] float, --Tempéraure de stockage par défaut quand un nouvel échantillon est créé pour ce site. Se référer à la colonne "storageTempC" dans la table "Sample"
	[measureFractionAnalyzedDefault] char, --Fraction par défaut quand une nouvelle mesure est créée pour cet échantillon. Se référer à la colonne "fracgtionAnalyzed" dans la table "WWMeasure"
	[geoLat] float, --Position géographique du site d'échantillonnage. Latitude exprimée en coordonnées décimales (ex. 45.424721)
	[geoLong] float, --Position géographique du site d'échantillonnage. Longitude exprimée en coordonnées décimales (ex. -75.695000)
	[notes] char, --Ajouter toutes notes additionnelles.
	[polygonID] char, --Crée un lien vers la table "Polygon". Le polygon lié devrait englober la région qui se draine dans le site d'échantillonnage.
	[sewerNetworkFileLink] char, --Lien vers un fichier contenant toute information additionnelle au sujet du réseau d'égouts associé à ce site d'échantillonnage (tous les formats sont acceptés).
	[sewerNetworkFileBLOB] integer, --Un fichier contenant toute information additionnelle au sujet du réseau d'égouts associé à ce site d'échantillonnage (tous les formats sont acceptés).
	FOREIGN KEY ([polygonID]) REFERENCES NA(NA) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [SiteMeasure] (
/*Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".*/
	[uSiteMeasureID] char NOT NULL PRIMARY KEY, --Identifiant unique pour le site d'échantillonnage.
	[siteMeasureID] char, --Identifiat unique utilisé dans la table horizontale seulement. Utiliser quand toutes les mesures effectuées sur le même échantillon.
	[siteID] char, --Crée un lien vers la table "Site" pour décrire le site d'échantillonnage.
	[instrumentID] char, --Crée un lien vers la table "Instrument" pour décrire l'appareil utilisé pour effectuer la mesure.
	[reporterID] char, --Crée un lien avec les informations propres au reporteur associé à la mesure.
	[dateTime] integer, --Date à laquelle la mesure a été réalisée.
	[type] char, --Type de mesure réalisée. Le préfixe "env" est utilisé pour une variable envioronnementale, alors que "ww" indique une mesure réalisée sur les eaux usées.
	[typeOther] char, --Description d'un paramètre mesuré ne faisant pas partie des options disponibles.
	[typeDescription] char, --Ajouter toutes notes additionnelles en lien avec la mesure effectuée.
	[aggregation] char, --Méthode d'agrégation utiliseée pour rapporter la mesure.
	[aggregationOther] char, --Description d'une agrégation ne faisant pas partie des options disponibles.
	[aggregationDesc] char, --Informations (ou référence) liée(s) à la méthode d'agrégation utilisée pour rapporter la mesure.
	[value] float, --La valeur numérique de la mesure effectuée.
	[unit] char, --L'unité de mesure
	[qualityFlag] integer, --Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualité?
	[accessToPublic] integer, --Si "Non", la donnée ne sera pas accessible par le public. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToAllOrgs] integer, --Si "Non", la donnée ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToSelf] integer, --Si "Non", la donnée ne sera pas accessible par le reporteur lui-même. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToPHAC] integer, --Si "Non", la donnée ne sera pas accessible par les employés de l'Agence de Santé Publique du Canada. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToLocalHA] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique locales. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToProvHA] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée sera accessible à l'autorité de santé publique de la province où l'échantillonnage a été réalisée.
	[accessToOtherProv] integer, --Si "Non", la donnée ne sera pas accessible par les autorités de santé publique provinciales. Si "Oui" ou laissé vide, la donnée leur sera accessible.
	[accessToDetails] integer, --Indique si des informations supplémentaires sur la confidentialité de la mesure sont disponibles.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Reporter] (
/*Le reporteur ou l'organisation responsable de la collecte de données ou responsable de la qualité des données reportées.*/
	[reporterID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la personne ou l'organisation responsable des données rapportées.
	[siteIDDefault] char, --Identifiant de Site utilisé par défaut quand un nouvel échantillon est créé par ce reporteur. Se référer à la colonne "siteID" dans la table "Site"
	[labIDDefault] char, --Identifiant de Lab utilisé par défaut quand un nouvel échantillon est créé par ce reporteur. Se référer à la colonne "labID" dans la table "Lab"
	[contactName] char, --Nom complet du reporter (personne ou organisation)
	[contactEmail] char, --Adresse courriel du contact.
	[contactPhone] char, --Numéro de téléphone du contact.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteIDDefault]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labIDDefault]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lab] (
/*Laboratoire effectuant des analyses d'échantillons d'eaux usées d'un ou plusieurs sites.*/
	[labID] char NOT NULL PRIMARY KEY, --Identifiant unique pour le laboratoire.
	[assayMethodIDDefault] char, --Identifiant de la méthode d'analyse utilisée par défaut quand une nouvelle mesure est créé par ce laboratoire. Se référer à la colonne "assayMethodID" dans la table "AssayMethod"
	[name] char, --Nom du laboratoire.
	[contactName] char, --Personne contact de ce laboratoire.
	[contactEmail] char, --Adresse courriel du contact.
	[contactPhone] char, --Numéro de téléphone du contact.
	[updateDate] integer, --Date où l'information a été reportée une première fois ou mise à jour.
	FOREIGN KEY ([assayMethodIDDefault]) REFERENCES AssayMethod(assayMethodID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [AssayMethod] (
/*La méthode d'analyse utilisée pour réaliser les mesures. Crée une nouvelle rangée dans cette table si des changements (améliorations) sont apportées à une technique d'analyse existante. Garder le même identifiant et modifier le numéro de version. Une nouvelle rangée représentant une nouvelle version d'une méthode existante peut inclure des informations seulement dans les colonnes qui ont changé d'une version à l'autre, cependant, nous recommandons de remplir les autres colonnes avec les valeurs provenant de la version précédente afin de décrire clairement la méthode en entier. Ajouter la date courante lorsqu'une nouvelle rangée est créée.*/
	[assayMethodID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la méthode d'analyse.
	[instrumentID] char, --Crée un lien vers la table "Instrument" pour décrire l'appareil utilisé pour effectuer la mesure.
	[name] char, --Nom de la méthode d'analyse.
	[version] char, --Version de la méthode d'analyse. Un versionnement de type sémantique est recommandé.
	[summary] char, --Brève description de la méthode d'analyse et de comment celle-ci diffère d'autres méthodes.
	[referenceLink] char, --Lien vers la procédure standard.
	[date] integer, --Date à laquelle la méthode d'analyse (ou une nouvelle version d'une méthode existante) a été crée.
	[aliasID] char, --Identifiants d'autres méthodes d'analyse présentes dans la table qui sont similaires à la méthode courante. Insérer sous forme de liste séparée par des virgules.
	[sampleSizeL] float, --Volume de l'échantillon analysé (en litres)
	[loq] float, --Limite de quantification pour cette méthode, le cas échéant.
	[lod] float, --Limite de détection pour cette méthode, le cas échéant.
	[unit] char, --Unité de mesure utilisée par cette méthode et qui est applicable pour la limite de détection ou de quantification.
	[unitOther] char, --Unité de mesure utilisée par cette méthode et qui est applicable pour la limite de détection ou de quantification dans le cas où celle-ci n'est pas disponible.
	[methodConc] char, --Description de la méthode utilisée pour concentrer l'échantillon.
	[methodExtract] char, --Description de la méthode utilisée pour extraire l'échantillon.
	[methodPcr] char, --Description de la m.éthode PCR utiisée.
	[qualityAssQC] char, --Description des étapes de contrôle de qualité mises en place dans la méthode.
	[inhibition] char, --Description des paramètres d'inhibition liés à cette méthode.
	[surrogateRecovery] char, --Description de la méthode de récupération du virus de substitution liée à cette méthode.
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Instrument] (
/*L'instrument utilisé pour mesurer les échantillons et l'eau usée des sites d'échantillonnage. La méthode d'analyse pour les mesures virales sont décrites dans la table "AssayMethod".*/
	[instrumentID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'instrument de mesure.
	[name] char, --Nom de l'instrument de mesure.
	[model] char, --Numéro de modèle et/ou de version de l'instrument de mesure.
	[description] char, --Description de l'instrument.
	[alias] char, --Identifiants d'autres instruments présents dans la table qui sont similaires à l'instrument courant. Insérer sous forme de liste séparée par des virgules.
	[referenceLink] char, --Lien vers un document de référence pour l'instrument de mesure.
	[type] char, --Type de l'instrument de mesure.
	[typeOther] char --Description du type d'instrument dans le cas où il ne serait pas disponible.
);

CREATE TABLE IF NOT EXISTS [Polygon] (
/*Polygone englobant une région de la surface terrestre. Normalement, ces polygones représentent soit des bassin de drainage d'un réseau d'égouts ou une région de santé publique, ou une autre région associée à des données reportées.*/
	[polygonID] char NOT NULL PRIMARY KEY, --Identifiant unique du polygone.
	[name] char, --Nom du polygon (devrait être descriptif)
	[pop] integer, --Population approximative vivant dans la région représentée par le polygone.
	[type] char, --Type de polygone.
	[wkt] char, --Description formelle du polygone (format Well-Known-Text (wkt))
	[file] integer, --Fichier représentant la géométrie du polygone (blob).
	[link] char --Lien vers une référence externe décrivant la géométrie du polygone.
);

CREATE TABLE IF NOT EXISTS [CovidPublicHealthData] (
/*Données de patients pour la COVID-19 pour une région spécifiée par un polygone.*/
	[cphdID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'information de santé publique reportée.
	[reporterID] char, --Identifiant unique pour la personne ou l'organisation responsable des données rapportées.
	[polygonID] char, --Crée un lien vers la table "Polygon". Le polygon lié devrait englober la région représentée par les données consignées ici.
	[date] char, --Date de reportage des données de mesure de la COVID-19.
	[type] char, --Type de donnée de mesure de la COVID-19.
	[dateType] char, --Type de date utiisée pour reporter les données.
	[value] float, --La valeur numérique de la mesure reportée.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lookup] (
/*Utiliser pour retrouver les valeurs associées aux colonnes contenant des données catégoriques.*/
	[tableName] char, --Nom de la table.
	[columnName] char, --Nom de la colonne.
	[value] char, --Nom de la valeur.
	[description] char --Nom de la description.
)
