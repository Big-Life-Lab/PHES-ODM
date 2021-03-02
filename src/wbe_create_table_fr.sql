CREATE TABLE IF NOT EXISTS [Sample] (
/*L'échantillon est un volume d'eau usée représentatif de l'eau présente sur un site, qui est ensuite analysé en laboratoire.*/
	[sampleID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'<e9>chantillon. Suggestion:siteID-date-index.
	[siteID] char, --Cr<e9>e un lien avec la table "Site" pour d<e9>crire le point d'<e9>chantillonage.
	[dateTime] integer, --Date, heure et fuseau horaire de collecte d'un <e9>chantillon ponctuel.
	[dateTimeStart] integer, --Date, heure et fuseau horaire de d<e9>but de collecte d'un <e9>chantillon composite.
	[dateTimeEnd] integer, --Date, heure et fuseau horaire de fin de collecte d'un <e9>chantillon composite.
	[type] char, --Type d'<e9>chantillon.
	[typeOther] char, --Description d'un type d'<e9>chantillon ne faisant pas partie des options disponibles.
	[collection] char, --M<e9>thode utilis<e9>e pour <e9>chantillonner.
	[collectionOther] char, --Description d'une m<e9>thode d'<e9>chantillonnage ne faisant pas partie des options disponibles.
	[preTreatment] integer, --L'<e9>chantillon a-t-il <e9>t<e9> chimiquement alt<e9>r<e9> par un ajout de stabilisant ou autre?
	[preTreatmentDescription] char, --Description du pr<e9>-traitement le cas <e9>ch<e9>ant.
	[pooled] integer, --S'il s'agit d'un <e9>chantillon combin<e9>, c'est-<e0>-dire s'il est compos<e9> de plusieurs <e9>chantillons "enfants"?
	[children] char, --Si l'<e9>chantillon est li<e9>e <e0> des sous-<e9>chantillons (soit parce qu'il s'agit d'un <e9>chantillon combin<e9> ou parce que des sous-<e9>chantillons ont <e9>t<e9> pr<e9>lev<e9>s dans cet <e9>chantillon), ins<e9>rer les identifiant des <e9>chantillons enfants dans une liste s<e9>par<e9>e par des virgules.
	[parent] char, --Si l'<e9>chantillon a <e9>t<e9> combin<e9> <e0> un plus grand <e9>chantillon, indiquer l'identifiant du plus grand <e9>chantillon.
	[sizeL] float, --Volume total d'eau ou de boue pr<e9>lev<e9>e.
	[fieldSampleTempC] float, --Temprature <e0> laquelle l'<e9>chantillon <e9>tait stock<e9> pendant l'<e9>chantillonnage. Ce champ est principalement pertinent pour les <e9>chantillons composites, qui peuvent <ea>tre stock<e9>es <e0> temp<e9>rature ambiante ou r<e9>frig<e9>r<e9>s durant l'<e9>chantillonnage.
	[shippedOnIce] integer, --L'<e9>chantillon a-t-il <e9>t<e9> gard<e9> au froid lors du transport vers le laboratoire?
	[storageTempC] float, --Temp<e9>rature de stockage de l'<e9>chantillon en degr<e9>s Celsius
	[qualityFlag] integer, --Le reporteur a-t-il des doutes sur la qualit<e9> de l'<e9>chantillon?
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [WWMeasure] (
/*Résultat de mesure (une seule variable à la fois) pour un échantillon d'eau usée. Cette table inclut des données typiquement collectées par les techniciens de laboratoires d'analyse des eaux usées. Ces mesures sont réalisées à l'aide d'une méthode d'analyse (voir la table "AssayMethod") ou encore à l'aide d'un instrument spécifique (voir la table "Instrument'). Les mesures réalise in-situ au site d'échantilonnage sont reportées dans la table "SiteMeasure".*/
	[uWwMeasureID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la mesure pour la table "WWMeasurement"
	[wwMeasureID] char, --Identifiat unique utilis<e9> dans la table horizontale seulement. Utiliser quand toutes les mesures effectu<e9>es sur un <e9>chantillon sont r<e9>alis<e9>es en m<ea>me temps dans le m<ea>me laboratoire. Suggestion: siteID_sampleID_LabID_reportDate_ID.
	[sampleID] char, --Cr<e9>e un lien avec la table "Sample" pour d<e9>crire l'<e9>chantillon mesur<e9>.
	[labID] char, --Cr<e9>e un lien avec la table "Lab" pour d<e9>crire le laboratoire effectuant la mesure.
	[assayID] char, --Cr<e9>e un lien avec la table "AssayMethod" pour d<e9>crire la m<e9>thode employ<e9>e pour effectuer la mesure. Utiliser l'identifiant de l'instrument pour des mesures non virales.
	[instrumentID] char, --Cr<e9>e un lien avec la table "Instrument" l'appareil employ<e9> pour effectuer la mesure. Utiliser l'identifiant de la m<e9>thode d,analyse pour les mesures virales.
	[reporterID] char, --Cr<e9>e un lien avec les informations propres au reporteur associ<e9> <e0> la mesure.
	[analysisDate] integer, --Date <e0> laquelle la mesure a <e9>t<e9> r<e9>alis<e9>e en laboratoire.
	[reportDate] integer, --Date a laquelle la donn<e9>e a <e9>t<e9> report<e9>e. Un <e9>chantillon pourrait avoir des mesures pour lesquelles la m<e9>thode d'analyse ou la m<e9>thode de reportage des donn<e9>es aurait chang<e9>e. Dans ce cas, utiliser le m<ea>me sampleID, mais cr<e9>er une nouvelle entr<e9>e dans la table "WWMeasure avec un "MeasureID" diff<e9>rent, et la date de reportage de la donn<e9>e et l'identifiant de la m<e9>thode d'analyse appropri<e9>s.
	[fractionAnalyzed] char, --Fraction de l'<e9>chantillon employ<e9>e pour la mesure.
	[type] char, --Le param<e8>tre mesur<e9> avec cette analyse. Exemples: Une r<e9>gion de g<e8>ne cible (cov), un biomarqueur (n) ou un indicateur de la qualit<e9> de l'eau (wq)
	[typeOther] char, --Description d'un param<e8>tre mesur<e9> ne faisant pas partie des options disponibles.
	[unit] char, --Unit<e9> de mesure.
	[unitOther] char, --Description d'une unit<e9> de mesure ne faisant pas partie des options disponibles.
	[aggregation] char, --Indicateur statistique utilis<e9>e pour rapporter la mesure effectu<e9>e. Chaque agr<e9>gation doit <ea>tre report<e9>e comme une mesure diff<e9>rente (avec un identifiant diff<e9>rent)
	[aggregationOther] char, --Description d'une agr<e9>gation ne faisant pas partie des options disponibles.
	[index] integer, --Index de la mesure dans le cas o<f9> la m<ea>me mesure a <e9>t<e9> prise en replicata.
	[value] float, --La valeur num<e9>rique de la mesure effectu<e9>e.
	[qualityFlag] integer, --Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<e9>?
	[accessToPublic] integer, --Si "Non", la donn<e9>e ne sera pas accessible par le public. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToAllOrg] integer, --Si "Non", la donn<e9>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToSelf] integer, --Si "Non", la donn<e9>e ne sera pas accessible par le reporteur lui-m<ea>me. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToPHAC] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les employ<e9>s de l'Agence de Sant<e9> Publique du Canada. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToLocalHA] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique locales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToProvHA] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e sera accessible <e0> l'autorit<e9> de sant<e9> publique de la province o<f9> l'<e9>chantillonnage a <e9>t<e9> r<e9>alis<e9>e.
	[accessToOtherProv] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToDetails] integer, --Indique si des informations suppl<e9>mentaires sur la confidentialit<e9> de la mesure sont disponibles.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([sampleID]) REFERENCES Sample(sampleID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labID]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([assayID]) REFERENCES AssayMethod(assayID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Site] (
/*Le site de collecte des échantilons d'eau usée. Cette table inclus plusieurs paramètres par défaut facilitant la création de nouvaux échantillons dans la table "Sample"*/
	[siteID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'<e9>chantillon. Suggestion:siteID-date-index.
	[name] char, --Nom du site d'<e9>chantillonnage. Peut <ea>tre le nom d'une station de traitement, d'une station de pompage, d'un campus, d'un regard d'<e9>gouts, etc.
	[description] char, --Description du site d'<e9>chantillonnage (ville, b<e2>timent, rue, etc.) pour mieux identifier le site d'<e9>chantillonnage.
	[type] char, --Type de site ou d'institution du site d'<e9>chantillonnage.
	[typeOther] char, --Description du site d'<e9>chantillonnage dans le cas o<f9> une description ad<e9>quate n'est pas disponible.
	[sampleTypeDefault] char, --Type d'<e9>chantilon utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "type" dans la table "Sample"
	[sampleTypeOtherDefault] char, --Type d'<e9>chantilon utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "typeOther" dans la table "Sample"
	[sampleCollectionDefault] char, --M<e9>thode d'<e9>chantillonnage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "collection" dans la table "Sample"
	[sampleCollectOtherDefault] char, --M<e9>thode d'<e9>chantillonnage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "collectionOther" dans la table "Sample"
	[sampleStorageTempCDefault] float, --Temp<e9>raure de stockage par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> pour ce site. Se r<e9>f<e9>rer <e0> la colonne "storageTempC" dans la table "Sample"
	[measureFractionAnalyzedDefault] char, --Fraction par d<e9>faut quand une nouvelle mesure est cr<e9><e9>e pour cet <e9>chantillon. Se r<e9>f<e9>rer <e0> la colonne "fracgtionAnalyzed" dans la table "WWMeasure"
	[geoLat] float, --Position g<e9>ographique du site d'<e9>chantillonnage. Latitude exprim<e9>e en coordonn<e9>es d<e9>cimales (ex. 45.424721)
	[geoLong] float, --Position g<e9>ographique du site d'<e9>chantillonnage. Longitude exprim<e9>e en coordonn<e9>es d<e9>cimales (ex. -75.695000)
	[notes] char, --Ajouter toutes notes additionnelles.
	[polygonID] char, --Cr<e9>e un lien vers la table "Polygon". Le polygon li<e9> devrait englober la r<e9>gion qui se draine dans le site d'<e9>chantillonnage.
	[sewerNetworkFileLink] char, --Lien vers un fichier contenant toute information additionnelle au sujet du r<e9>seau d'<e9>gouts associ<e9> <e0> ce site d'<e9>chantillonnage (tous les formats sont accept<e9>s).
	[sewerNetworkFileBLOB] integer, --Un fichier contenant toute information additionnelle au sujet du r<e9>seau d'<e9>gouts associ<e9> <e0> ce site d'<e9>chantillonnage (tous les formats sont accept<e9>s).
	FOREIGN KEY ([polygonID]) REFERENCES Polygon(polygonID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [SiteMeasure] (
/*Résultat de mesure (une seule variable à la fois) pour un site d'échantillonnage. Cette table inclut des données typiquement collectées dans des stations de traitement des eaux usées et des sites d'échantillonnage de terrain. Ces mesures ne sont pas réalisées sur un échantillon, mais elles ajoutent des informations pertinentes pour l'analyse des résultats provenant des échantillons. Les mesures effectuées sur les échantilons eux-mêmes sont dans la table "WWMeasure".*/
	[uSiteMeasureID] char NOT NULL PRIMARY KEY, --Identifiant unique pour le site d'<e9>chantillonnage.
	[siteMeasureID] char, --Identifiat unique utilis<e9> dans la table horizontale seulement. Utiliser quand toutes les mesures effectu<e9>es sur le m<ea>me <e9>chantillon.
	[siteID] char, --Cr<e9>e un lien vers la table "Site" pour d<e9>crire le site d'<e9>chantillonnage.
	[instrumentID] char, --Cr<e9>e un lien vers la table "Instrument" pour d<e9>crire l'appareil utilis<e9> pour effectuer la mesure.
	[reporterID] char, --Cr<e9>e un lien avec les informations propres au reporteur associ<e9> <e0> la mesure.
	[dateTime] integer, --Date <e0> laquelle la mesure a <e9>t<e9> r<e9>alis<e9>e.
	[type] char, --Type de mesure r<e9>alis<e9>e. Le pr<e9>fixe "env" est utilis<e9> pour une variable envioronnementale, alors que "ww" indique une mesure r<e9>alis<e9>e sur les eaux us<e9>es.
	[typeOther] char, --Description d'un param<e8>tre mesur<e9> ne faisant pas partie des options disponibles.
	[typeDescription] char, --Ajouter toutes notes additionnelles en lien avec la mesure effectu<e9>e.
	[aggregation] char, --M<e9>thode d'agr<e9>gation utilise<e9>e pour rapporter la mesure.
	[aggregationOther] char, --Description d'une agr<e9>gation ne faisant pas partie des options disponibles.
	[aggregationDesc] char, --Informations (ou r<e9>f<e9>rence) li<e9>e(s) <e0> la m<e9>thode d'agr<e9>gation utilis<e9>e pour rapporter la mesure.
	[value] float, --La valeur num<e9>rique de la mesure effectu<e9>e.
	[unit] char, --L'unit<e9> de mesure
	[qualityFlag] integer, --Le reporteur de la mesure suspecte-t-il que la mesure est de mauvaise qualit<e9>?
	[accessToPublic] integer, --Si "Non", la donn<e9>e ne sera pas accessible par le public. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToAllOrgs] integer, --Si "Non", la donn<e9>e ne sera pas accessible par toute organisation partenaire. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToSelf] integer, --Si "Non", la donn<e9>e ne sera pas accessible par le reporteur lui-m<ea>me. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToPHAC] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les employ<e9>s de l'Agence de Sant<e9> Publique du Canada. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToLocalHA] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique locales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToProvHA] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e sera accessible <e0> l'autorit<e9> de sant<e9> publique de la province o<f9> l'<e9>chantillonnage a <e9>t<e9> r<e9>alis<e9>e.
	[accessToOtherProv] integer, --Si "Non", la donn<e9>e ne sera pas accessible par les autorit<e9>s de sant<e9> publique provinciales. Si "Oui" ou laiss<e9> vide, la donn<e9>e leur sera accessible.
	[accessToDetails] integer, --Indique si des informations suppl<e9>mentaires sur la confidentialit<e9> de la mesure sont disponibles.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteID]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([reporterID]) REFERENCES Reporter(reporterID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Reporter] (
/*Le reporteur ou l'organisation responsable de la collecte de données ou responsable de la qualité des données reportées.*/
	[reporterID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la personne ou l'organisation responsable des donn<e9>es rapport<e9>es.
	[siteIDDefault] char, --Identifiant de Site utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> par ce reporteur. Se r<e9>f<e9>rer <e0> la colonne "siteID" dans la table "Site"
	[labIDDefault] char, --Identifiant de Lab utilis<e9> par d<e9>faut quand un nouvel <e9>chantillon est cr<e9><e9> par ce reporteur. Se r<e9>f<e9>rer <e0> la colonne "labID" dans la table "Lab"
	[contactName] char, --Nom complet du reporter (personne ou organisation)
	[contactEmail] char, --Adresse courriel du contact.
	[contactPhone] char, --Num<e9>ro de t<e9>l<e9>phone du contact.
	[notes] char, --Ajouter toutes notes additionnelles.
	FOREIGN KEY ([siteIDDefault]) REFERENCES Site(siteID) DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY ([labIDDefault]) REFERENCES Lab(labID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Lab] (
/*Laboratoire effectuant des analyses d'échantillons d'eaux usées d'un ou plusieurs sites.*/
	[labID] char NOT NULL PRIMARY KEY, --Identifiant unique pour le laboratoire.
	[assayMethodIDDefault] char, --Identifiant de la m<e9>thode d'analyse utilis<e9>e par d<e9>faut quand une nouvelle mesure est cr<e9><e9> par ce laboratoire. Se r<e9>f<e9>rer <e0> la colonne "assayMethodID" dans la table "AssayMethod"
	[name] char, --Nom du laboratoire.
	[contactName] char, --Personne contact de ce laboratoire.
	[contactEmail] char, --Adresse courriel du contact.
	[contactPhone] char, --Num<e9>ro de t<e9>l<e9>phone du contact.
	[updateDate] integer, --Date o<f9> l'information a <e9>t<e9> report<e9>e une premi<e8>re fois ou mise <e0> jour.
	FOREIGN KEY ([assayMethodIDDefault]) REFERENCES AssayMethod(assayMethodID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [AssayMethod] (
/*La méthode d'analyse utilisée pour réaliser les mesures. Crée une nouvelle rangée dans cette table si des changements (améliorations) sont apportées à une technique d'analyse existante. Garder le même identifiant et modifier le numéro de version. Une nouvelle rangée représentant une nouvelle version d'une méthode existante peut inclure des informations seulement dans les colonnes qui ont changé d'une version à l'autre, cependant, nous recommandons de remplir les autres colonnes avec les valeurs provenant de la version précédente afin de décrire clairement la méthode en entier. Ajouter la date courante lorsqu'une nouvelle rangée est créée.*/
	[assayMethodID] char NOT NULL PRIMARY KEY, --Identifiant unique pour la m<e9>thode d'analyse.
	[instrumentID] char, --Cr<e9>e un lien vers la table "Instrument" pour d<e9>crire l'appareil utilis<e9> pour effectuer la mesure.
	[name] char, --Nom de la m<e9>thode d'analyse.
	[version] char, --Version de la m<e9>thode d'analyse. Un versionnement de type s<e9>mantique est recommand<e9>.
	[summary] char, --Br<e8>ve description de la m<e9>thode d'analyse et de comment celle-ci diff<e8>re d'autres m<e9>thodes.
	[referenceLink] char, --Lien vers la proc<e9>dure standard.
	[date] integer, --Date <e0> laquelle la m<e9>thode d'analyse (ou une nouvelle version d'une m<e9>thode existante) a <e9>t<e9> cr<e9>e.
	[aliasID] char, --Identifiants d'autres m<e9>thodes d'analyse pr<e9>sentes dans la table qui sont similaires <e0> la m<e9>thode courante. Ins<e9>rer sous forme de liste s<e9>par<e9>e par des virgules.
	[sampleSizeL] float, --Volume de l'<e9>chantillon analys<e9> (en litres)
	[loq] float, --Limite de quantification pour cette m<e9>thode, le cas <e9>ch<e9>ant.
	[lod] float, --Limite de d<e9>tection pour cette m<e9>thode, le cas <e9>ch<e9>ant.
	[unit] char, --Unit<e9> de mesure utilis<e9>e par cette m<e9>thode et qui est applicable pour la limite de d<e9>tection ou de quantification.
	[unitOther] char, --Unit<e9> de mesure utilis<e9>e par cette m<e9>thode et qui est applicable pour la limite de d<e9>tection ou de quantification dans le cas o<f9> celle-ci n'est pas disponible.
	[methodConc] char, --Description de la m<e9>thode utilis<e9>e pour concentrer l'<e9>chantillon.
	[methodExtract] char, --Description de la m<e9>thode utilis<e9>e pour extraire l'<e9>chantillon.
	[methodPcr] char, --Description de la m.<e9>thode PCR utiis<e9>e.
	[qualityAssQC] char, --Description des <e9>tapes de contr<f4>le de qualit<e9> mises en place dans la m<e9>thode.
	[inhibition] char, --Description des param<e8>tres d'inhibition li<e9>s <e0> cette m<e9>thode.
	[surrogateRecovery] char, --Description de la m<e9>thode de r<e9>cup<e9>ration du virus de substitution li<e9>e <e0> cette m<e9>thode.
	FOREIGN KEY ([instrumentID]) REFERENCES Instrument(instrumentID) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS [Instrument] (
/*L'instrument utilisé pour mesurer les échantillons et l'eau usée des sites d'échantillonnage. La méthode d'analyse pour les mesures virales sont décrites dans la table "AssayMethod".*/
	[instrumentID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'instrument de mesure.
	[name] char, --Nom de l'instrument de mesure.
	[model] char, --Num<e9>ro de mod<e8>le et/ou de version de l'instrument de mesure.
	[description] char, --Description de l'instrument.
	[alias] char, --Identifiants d'autres instruments pr<e9>sents dans la table qui sont similaires <e0> l'instrument courant. Ins<e9>rer sous forme de liste s<e9>par<e9>e par des virgules.
	[referenceLink] char, --Lien vers un document de r<e9>f<e9>rence pour l'instrument de mesure.
	[type] char, --Type de l'instrument de mesure.
	[typeOther] char --Description du type d'instrument dans le cas o<f9> il ne serait pas disponible.
);

CREATE TABLE IF NOT EXISTS [Polygon] (
/*Polygone englobant une région de la surface terrestre. Normalement, ces polygones représentent soit des bassin de drainage d'un réseau d'égouts ou une région de santé publique, ou une autre région associée à des données reportées.*/
	[polygonID] char NOT NULL PRIMARY KEY, --Identifiant unique du polygone.
	[name] char, --Nom du polygon (devrait <ea>tre descriptif)
	[pop] integer, --Population approximative vivant dans la r<e9>gion repr<e9>sent<e9>e par le polygone.
	[type] char, --Type de polygone.
	[wkt] char, --Description formelle du polygone (format Well-Known-Text (wkt))
	[file] integer, --Fichier repr<e9>sentant la g<e9>om<e9>trie du polygone (blob).
	[link] char --Lien vers une r<e9>f<e9>rence externe d<e9>crivant la g<e9>om<e9>trie du polygone.
);

CREATE TABLE IF NOT EXISTS [CovidPublicHealthData] (
/*Données de patients pour la COVID-19 pour une région spécifiée par un polygone.*/
	[cphdID] char NOT NULL PRIMARY KEY, --Identifiant unique pour l'information de sant<e9> publique report<e9>e.
	[reporterID] char, --Identifiant unique pour la personne ou l'organisation responsable des donn<e9>es rapport<e9>es.
	[polygonID] char, --Cr<e9>e un lien vers la table "Polygon". Le polygon li<e9> devrait englober la r<e9>gion repr<e9>sent<e9>e par les donn<e9>es consign<e9>es ici.
	[date] char, --Date de reportage des donn<e9>es de mesure de la COVID-19.
	[type] char, --Type de donn<e9>e de mesure de la COVID-19.
	[dateType] char, --Type de date utiis<e9>e pour reporter les donn<e9>es.
	[value] float, --La valeur num<e9>rique de la mesure report<e9>e.
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
