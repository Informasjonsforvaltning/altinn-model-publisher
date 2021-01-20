"""OR catalog test data."""
or_catalog_turtle = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.altinn.no/models/or> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "OR informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/3314-245> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Ar44-repformat-6> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Ar44-repformat-6" ;
    dct:title "Ar44-repformat-6"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetAdresse-datadef-15> a ns1:Attribute ;
    dct:title "enhetAdresse-datadef-15"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetNavn-datadef-1> a ns1:Attribute ;
    dct:title "enhetNavn-datadef-1"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetOrganisasjonsnummer-datadef-18> a ns1:Attribute ;
    dct:title "enhetOrganisasjonsnummer-datadef-18"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetPostnummer-datadef-6673> a ns1:Attribute ;
    dct:title "enhetPostnummer-datadef-6673"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetPoststed-datadef-6674> a ns1:Attribute ;
    dct:title "enhetPoststed-datadef-6674"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/oppgavegiverFodselsnummer-datadef-26> a ns1:Attribute ;
    dct:title "oppgavegiverFodselsnummer-datadef-26"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BelopHeltall15-repformat-37> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BelopHeltall15-repformat-37" ;
    dct:title "BelopHeltall15-repformat-37"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/avgiver-grp-1125> a ns1:Composition ;
    dct:title "avgiver-grp-1125"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/regnskapsforer-grp-2633> a ns1:Composition ;
    dct:title "regnskapsforer-grp-2633"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/skjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404> a ns1:Attribute ;
    dct:title "skjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Heltall7-repformat-116> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Heltall7-repformat-116" ;
    dct:title "Heltall7-repformat-116"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerAdresseSpesifisertBil-datadef-7587> a ns1:Attribute ;
    dct:title "bilBrukerAdresseSpesifisertBil-datadef-7587"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerFodselsnummerSpesifisertBil-datadef-7586> a ns1:Attribute ;
    dct:title "bilBrukerFodselsnummerSpesifisertBil-datadef-7586"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerNavnSpesifisertBil-datadef-7585> a ns1:Attribute ;
    dct:title "bilBrukerNavnSpesifisertBil-datadef-7585"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerPostnummerSpesifisertBil-datadef-7588> a ns1:Attribute ;
    dct:title "bilBrukerPostnummerSpesifisertBil-datadef-7588"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerPoststedSpesifisertBil-datadef-7589> a ns1:Attribute ;
    dct:title "bilBrukerPoststedSpesifisertBil-datadef-7589"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilKjorebokSpesifisertBil-datadef-3118> a ns1:Attribute ;
    dct:title "bilKjorebokSpesifisertBil-datadef-3118"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/omBil-grp-5667> a ns1:Composition ;
    dct:title "omBil-grp-5667"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilArsmodellSpesifisertBil-datadef-30560> a ns1:Attribute ;
    dct:title "bilArsmodellSpesifisertBil-datadef-30560"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilBruksomradeSpesifisertBil-datadef-7584> a ns1:Attribute ;
    dct:title "bilBruksomradeSpesifisertBil-datadef-7584"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKilometerstandFjoraretSpesifisertBil-datadef-7582> a ns1:Attribute ;
    dct:title "bilKilometerstandFjoraretSpesifisertBil-datadef-7582"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKilometerstandSpesifisertBil-datadef-7581> a ns1:Attribute ;
    dct:title "bilKilometerstandSpesifisertBil-datadef-7581"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116> a ns1:Attribute ;
    dct:title "bilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilListeprisSpesifisertBil-datadef-3114> a ns1:Attribute ;
    dct:title "bilListeprisSpesifisertBil-datadef-3114"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilMerkeTypeSpesifisertBil-datadef-7580> a ns1:Attribute ;
    dct:title "bilMerkeTypeSpesifisertBil-datadef-7580"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringAdresseSpesifisertBil-datadef-30405> a ns1:Attribute ;
    dct:title "bilParkeringAdresseSpesifisertBil-datadef-30405"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringAnnetStedSpesifisertBil-datadef-7667> a ns1:Attribute ;
    dct:title "bilParkeringAnnetStedSpesifisertBil-datadef-7667"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringVarierendeStedSpesifisertBil-datadef-30406> a ns1:Attribute ;
    dct:title "bilParkeringVarierendeStedSpesifisertBil-datadef-30406"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilRegistreringsnummerSpesifisertBil-datadef-7579> a ns1:Attribute ;
    dct:title "bilRegistreringsnummerSpesifisertBil-datadef-7579"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilkategoriSpesifisertBil-datadef-7576> a ns1:Attribute ;
    dct:title "bilkategoriSpesifisertBil-datadef-7576"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/driftskostnaderSpesifisertBil-datadef-34484> a ns1:Attribute ;
    dct:title "driftskostnaderSpesifisertBil-datadef-34484"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg2JaNei-repformat-4> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg2JaNei-repformat-4" ;
    dct:title "KodelisteEttValg2JaNei-repformat-4"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 3 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg3TypeSkatteoppgave-repformat-1051> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg3TypeSkatteoppgave-repformat-1051" ;
    dct:title "KodelisteEttValg3TypeSkatteoppgave-repformat-1051"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 2 ;
    xsd:minLength 2 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg4AdresseHjemmeVirksomhetAnnen-repformat-867> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg4AdresseHjemmeVirksomhetAnnen-repformat-867" ;
    dct:title "KodelisteEttValg4AdresseHjemmeVirksomhetAnnen-repformat-867"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 25 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/hvemBrukerBilenUtenomArbeidstiden-grp-1139> a ns1:Composition ;
    dct:title "hvemBrukerBilenUtenomArbeidstiden-grp-1139"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/informasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771> a ns1:Composition ;
    dct:title "informasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/spesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150> a ns1:Composition ;
    dct:title "spesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerAdresse-datadef-281> a ns1:Attribute ;
    dct:title "regnskapsforerAdresse-datadef-281"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerNavn-datadef-280> a ns1:Attribute ;
    dct:title "regnskapsforerNavn-datadef-280"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerPostnummer-datadef-6678> a ns1:Attribute ;
    dct:title "regnskapsforerPostnummer-datadef-6678"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerPoststed-datadef-6679> a ns1:Attribute ;
    dct:title "regnskapsforerPoststed-datadef-6679"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema" ;
    dct:title "Skjema"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/blankettnummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/etatid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/generellInformasjon-grp-1124>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/informasjonOmBil-grp-3497>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/skjemanummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/spesifikasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/tittel> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/blankettnummer> a ns1:Attribute ;
    dct:title "blankettnummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/etatid> a ns1:Attribute ;
    dct:title "etatid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/generellInformasjon-grp-1124> a ns1:Composition ;
    dct:title "generellInformasjon-grp-1124"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/informasjonOmBil-grp-3497> a ns1:Composition ;
    dct:title "informasjonOmBil-grp-3497"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/skjemanummer> a ns1:Attribute ;
    dct:title "skjemanummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#Integer> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/spesifikasjonsnummer> a ns1:Attribute ;
    dct:title "spesifikasjonsnummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#Integer> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/tittel> a ns1:Attribute ;
    dct:title "tittel"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilgodtgjorelseMottattSpesifisertBil-datadef-3115> a ns1:Attribute ;
    dct:title "bilgodtgjorelseMottattSpesifisertBil-datadef-3115"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591> a ns1:Attribute ;
    dct:title "bilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250> a ns1:Attribute ;
    dct:title "bilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249> a ns1:Attribute ;
    dct:title "bilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderDrivstoffSpesifisertBil-datadef-7596> a ns1:Attribute ;
    dct:title "driftskostnaderDrivstoffSpesifisertBil-datadef-7596"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590> a ns1:Attribute ;
    dct:title "driftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderLeasingleieSpesifisertBil-datadef-11252> a ns1:Attribute ;
    dct:title "driftskostnaderLeasingleieSpesifisertBil-datadef-11252"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderOverskuddSpesifisertBil-datadef-7594> a ns1:Attribute ;
    dct:title "driftskostnaderOverskuddSpesifisertBil-datadef-7594"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderSpesifisertBil-datadef-7578> a ns1:Attribute ;
    dct:title "driftskostnaderSpesifisertBil-datadef-7578"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderUnderskuddSpesifisertBil-datadef-7595> a ns1:Attribute ;
    dct:title "driftskostnaderUnderskuddSpesifisertBil-datadef-7595"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderVedlikeholdSpesifisertBil-datadef-11251> a ns1:Attribute ;
    dct:title "driftskostnaderVedlikeholdSpesifisertBil-datadef-11251"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderYrketSpesifisertBil-datadef-11254> a ns1:Attribute ;
    dct:title "driftskostnaderYrketSpesifisertBil-datadef-11254"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/saldoavskrivningSpesifisertBil-datadef-11253> a ns1:Attribute ;
    dct:title "saldoavskrivningSpesifisertBil-datadef-11253"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1000-repformat-77> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1000-repformat-77" ;
    dct:title "Tekst1000-repformat-77"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 1000 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst105-repformat-9> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst105-repformat-9" ;
    dct:title "Tekst105-repformat-9"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 105 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1111Modulus11-repformat-18> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1111Modulus11-repformat-18" ;
    dct:title "Tekst1111Modulus11-repformat-18"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst15-repformat-61> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst15-repformat-61" ;
    dct:title "Tekst15-repformat-61"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 15 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst175-repformat-8> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst175-repformat-8" ;
    dct:title "Tekst175-repformat-8"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 175 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst35-repformat-3> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst35-repformat-3" ;
    dct:title "Tekst35-repformat-3"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 35 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst44BareTall-repformat-10> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst44BareTall-repformat-10" ;
    dct:title "Tekst44BareTall-repformat-10"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst99Modulus11-repformat-1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst99Modulus11-repformat-1" ;
    dct:title "Tekst99Modulus11-repformat-1"@nb ;
    xsd:anyURI xsd:string .

<https://altinn.fellesdatakatalog.digdir.no/models/3314-245> a ns1:InformationModel ;
    dct:title "Sensitive role Reporting"@nb ;
    ns1:containsModelElement <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Ar44-repformat-6>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BelopHeltall15-repformat-37>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Heltall7-repformat-116>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg2JaNei-repformat-4>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg3TypeSkatteoppgave-repformat-1051>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/KodelisteEttValg4AdresseHjemmeVirksomhetAnnen-repformat-867>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1000-repformat-77>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst105-repformat-9>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst1111Modulus11-repformat-18>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst15-repformat-61>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst175-repformat-8>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst35-repformat-3>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst44BareTall-repformat-10>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Tekst99Modulus11-repformat-1> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125" ;
    dct:title "Avgiver-grp-1125"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetAdresse-datadef-15>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetNavn-datadef-1>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetOrganisasjonsnummer-datadef-18>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetPostnummer-datadef-6673>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/enhetPoststed-datadef-6674>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/oppgavegiverFodselsnummer-datadef-26> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560" ;
    dct:title "BilArsmodellSpesifisertBil-datadef-30560"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587" ;
    dct:title "BilBrukerAdresseSpesifisertBil-datadef-7587"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586" ;
    dct:title "BilBrukerFodselsnummerSpesifisertBil-datadef-7586"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585" ;
    dct:title "BilBrukerNavnSpesifisertBil-datadef-7585"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588" ;
    dct:title "BilBrukerPostnummerSpesifisertBil-datadef-7588"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589" ;
    dct:title "BilBrukerPoststedSpesifisertBil-datadef-7589"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584" ;
    dct:title "BilBruksomradeSpesifisertBil-datadef-7584"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582" ;
    dct:title "BilKilometerstandFjoraretSpesifisertBil-datadef-7582"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581" ;
    dct:title "BilKilometerstandSpesifisertBil-datadef-7581"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118" ;
    dct:title "BilKjorebokSpesifisertBil-datadef-3118"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116" ;
    dct:title "BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114" ;
    dct:title "BilListeprisSpesifisertBil-datadef-3114"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580" ;
    dct:title "BilMerkeTypeSpesifisertBil-datadef-7580"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405" ;
    dct:title "BilParkeringAdresseSpesifisertBil-datadef-30405"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667" ;
    dct:title "BilParkeringAnnetStedSpesifisertBil-datadef-7667"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406" ;
    dct:title "BilParkeringVarierendeStedSpesifisertBil-datadef-30406"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579" ;
    dct:title "BilRegistreringsnummerSpesifisertBil-datadef-7579"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115" ;
    dct:title "BilgodtgjorelseMottattSpesifisertBil-datadef-3115"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576" ;
    dct:title "BilkategoriSpesifisertBil-datadef-7576"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591" ;
    dct:title "BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250" ;
    dct:title "BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249" ;
    dct:title "BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596" ;
    dct:title "DriftskostnaderDrivstoffSpesifisertBil-datadef-7596"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590" ;
    dct:title "DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252" ;
    dct:title "DriftskostnaderLeasingleieSpesifisertBil-datadef-11252"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594" ;
    dct:title "DriftskostnaderOverskuddSpesifisertBil-datadef-7594"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484" ;
    dct:title "DriftskostnaderSpesifisertBil-datadef-34484"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578" ;
    dct:title "DriftskostnaderSpesifisertBil-datadef-7578"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595" ;
    dct:title "DriftskostnaderUnderskuddSpesifisertBil-datadef-7595"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251" ;
    dct:title "DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254" ;
    dct:title "DriftskostnaderYrketSpesifisertBil-datadef-11254"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15" ;
    dct:title "EnhetAdresse-datadef-15"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1" ;
    dct:title "EnhetNavn-datadef-1"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18" ;
    dct:title "EnhetOrganisasjonsnummer-datadef-18"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673" ;
    dct:title "EnhetPostnummer-datadef-6673"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674" ;
    dct:title "EnhetPoststed-datadef-6674"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124" ;
    dct:title "GenerellInformasjon-grp-1124"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/avgiver-grp-1125>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/regnskapsforer-grp-2633>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/skjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139" ;
    dct:title "HvemBrukerBilenUtenomArbeidstiden-grp-1139"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerAdresseSpesifisertBil-datadef-7587>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerFodselsnummerSpesifisertBil-datadef-7586>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerNavnSpesifisertBil-datadef-7585>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerPostnummerSpesifisertBil-datadef-7588>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilBrukerPoststedSpesifisertBil-datadef-7589>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/bilKjorebokSpesifisertBil-datadef-3118>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497" ;
    dct:title "InformasjonOmBil-grp-3497"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/omBil-grp-5667> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771" ;
    dct:title "InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilArsmodellSpesifisertBil-datadef-30560>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilBruksomradeSpesifisertBil-datadef-7584>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKilometerstandFjoraretSpesifisertBil-datadef-7582>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKilometerstandSpesifisertBil-datadef-7581>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilListeprisSpesifisertBil-datadef-3114>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilMerkeTypeSpesifisertBil-datadef-7580>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringAdresseSpesifisertBil-datadef-30405>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringAnnetStedSpesifisertBil-datadef-7667>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilParkeringVarierendeStedSpesifisertBil-datadef-30406>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilRegistreringsnummerSpesifisertBil-datadef-7579>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/bilkategoriSpesifisertBil-datadef-7576>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/driftskostnaderSpesifisertBil-datadef-34484>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667" ;
    dct:title "OmBil-grp-5667"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/hvemBrukerBilenUtenomArbeidstiden-grp-1139>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/informasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/spesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26" ;
    dct:title "OppgavegiverFodselsnummer-datadef-26"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633" ;
    dct:title "Regnskapsforer-grp-2633"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerAdresse-datadef-281>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerNavn-datadef-280>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerPostnummer-datadef-6678>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/regnskapsforerPoststed-datadef-6679> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281" ;
    dct:title "RegnskapsforerAdresse-datadef-281"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280" ;
    dct:title "RegnskapsforerNavn-datadef-280"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678" ;
    dct:title "RegnskapsforerPostnummer-datadef-6678"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679" ;
    dct:title "RegnskapsforerPoststed-datadef-6679"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253" ;
    dct:title "SaldoavskrivningSpesifisertBil-datadef-11253"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404" ;
    dct:title "SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150" ;
    dct:title "SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilgodtgjorelseMottattSpesifisertBil-datadef-3115>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/bilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderDrivstoffSpesifisertBil-datadef-7596>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderLeasingleieSpesifisertBil-datadef-11252>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderOverskuddSpesifisertBil-datadef-7594>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderSpesifisertBil-datadef-7578>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderUnderskuddSpesifisertBil-datadef-7595>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderVedlikeholdSpesifisertBil-datadef-11251>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/driftskostnaderYrketSpesifisertBil-datadef-11254>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/saldoavskrivningSpesifisertBil-datadef-11253> .

<https://altinn.fellesdatakatalog.digdir.no#Integer> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#Integer" ;
    dct:title "Integer"@en ;
    xsd:anyURI xsd:decimal .

<https://altinn.fellesdatakatalog.digdir.no#String> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#String" ;
    dct:title "String"@en ;
    xsd:anyURI xsd:string .

<https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#PositiveInteger" ;
    dct:title "PositiveInteger"@en ;
    xsd:anyURI xsd:decimal ."""
