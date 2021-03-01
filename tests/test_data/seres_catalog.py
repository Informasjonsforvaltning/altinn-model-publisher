"""Seres catalog test data."""
seres_catalog_turtle = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.altinn.no/models/seres> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "Seres informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/2365-3442>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3906-3940> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1_RestriksjonAdresselinje1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1_RestriksjonAdresselinje1" ;
    dct:title "Adresselinje1_RestriksjonAdresselinje1"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 175 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon" ;
    dct:title "ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744_Verdirestriksjon" ;
    dct:title "ArsresultatNegativSisteToAr-23744_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering-23767_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon" ;
    dct:title "AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon" ;
    dct:title "AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12_Verdirestriksjon" ;
    dct:title "Boolean_S12_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13_Verdirestriksjon" ;
    dct:title "Boolean_S13_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14_Verdirestriksjon" ;
    dct:title "Boolean_S14_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15_Verdirestriksjon" ;
    dct:title "Boolean_S15_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16_Verdirestriksjon" ;
    dct:title "Boolean_S16_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17_Verdirestriksjon" ;
    dct:title "Boolean_S17_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18_Verdirestriksjon" ;
    dct:title "Boolean_S18_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19_Verdirestriksjon" ;
    dct:title "Boolean_S19_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20_Verdirestriksjon" ;
    dct:title "Boolean_S20_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21_Verdirestriksjon" ;
    dct:title "Boolean_S21_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22_Verdirestriksjon" ;
    dct:title "Boolean_S22_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23_Verdirestriksjon" ;
    dct:title "Boolean_S23_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24_Verdirestriksjon" ;
    dct:title "Boolean_S24_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25_Verdirestriksjon" ;
    dct:title "Boolean_S25_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26_Verdirestriksjon" ;
    dct:title "Boolean_S26_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27_Verdirestriksjon" ;
    dct:title "Boolean_S27_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30_Verdirestriksjon" ;
    dct:title "Boolean_S30_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31_Verdirestriksjon" ;
    dct:title "Boolean_S31_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32_Verdirestriksjon" ;
    dct:title "Boolean_S32_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33_Verdirestriksjon" ;
    dct:title "Boolean_S33_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34_Verdirestriksjon" ;
    dct:title "Boolean_S34_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35_Verdirestriksjon" ;
    dct:title "Boolean_S35_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36_Verdirestriksjon" ;
    dct:title "Boolean_S36_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742_Verdirestriksjon" ;
    dct:title "DriftsresultatNegativSisteToAr-23742_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775_Verdirestriksjon" ;
    dct:title "EgenkapitalAndel10-23775_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776_Verdirestriksjon" ;
    dct:title "EgenkapitalKorrigertNegativ-23776_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2" ;
    dct:title "EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielleAndre-23758_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon" ;
    dct:title "EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon" ;
    dct:title "EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719_Verdirestriksjon" ;
    dct:title "EnhetBransje-23719_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon" ;
    dct:title "EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon" ;
    dct:title "EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722_Verdirestriksjon" ;
    dct:title "EnhetKonsernregnskap-23722_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon" ;
    dct:title "EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01_Verdirestriksjon" ;
    dct:title "Epost_S01_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02_Verdirestriksjon" ;
    dct:title "Epost_S02_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon" ;
    dct:title "FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065_Heltall9-408_1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065_Heltall9-408_1" ;
    dct:title "ForetakBorsverdi-34065_Heltall9-408_1"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn_RestriksjonForetaksnavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn_RestriksjonForetaksnavn" ;
    dct:title "Foretaksnavn_RestriksjonForetaksnavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon" ;
    dct:title "GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon" ;
    dct:title "GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102" ;
    dct:title "Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 24 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01_RestriksjonHeltall_1_S01> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01_RestriksjonHeltall_1_S01" ;
    dct:title "Heltall_1_S01_RestriksjonHeltall_1_S01"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02_RestriksjonHeltall_1_S02> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02_RestriksjonHeltall_1_S02" ;
    dct:title "Heltall_1_S02_RestriksjonHeltall_1_S02"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03_RestriksjonHeltall_1_S03> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03_RestriksjonHeltall_1_S03" ;
    dct:title "Heltall_1_S03_RestriksjonHeltall_1_S03"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04_RestriksjonHeltall_1_S04> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04_RestriksjonHeltall_1_S04" ;
    dct:title "Heltall_1_S04_RestriksjonHeltall_1_S04"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05_RestriksjonHeltall_1_S05> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05_RestriksjonHeltall_1_S05" ;
    dct:title "Heltall_1_S05_RestriksjonHeltall_1_S05"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06_RestriksjonHeltall_1_S06> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06_RestriksjonHeltall_1_S06" ;
    dct:title "Heltall_1_S06_RestriksjonHeltall_1_S06"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07_RestriksjonHeltall_1_S07> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07_RestriksjonHeltall_1_S07" ;
    dct:title "Heltall_1_S07_RestriksjonHeltall_1_S07"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08_RestriksjonHeltall_1_S08> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08_RestriksjonHeltall_1_S08" ;
    dct:title "Heltall_1_S08_RestriksjonHeltall_1_S08"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01_RestriksjonHeltall_2_S01> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01_RestriksjonHeltall_2_S01" ;
    dct:title "Heltall_2_S01_RestriksjonHeltall_2_S01"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon" ;
    dct:title "IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller_Verdirestriksjon" ;
    dct:title "Ifrs16harforklartforskjeller_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon" ;
    dct:title "Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730_Verdirestriksjon" ;
    dct:title "InsentivordningAksjebasert-23730_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/rapport> a ns1:Attribute ;
    dct:title "rapport"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/rapportKRT-1003> a ns1:Attribute ;
    dct:title "rapportKRT-1003"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/skjemainnholdKRT-1003> a ns1:Attribute ;
    dct:title "skjemainnholdKRT-1003"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon" ;
    dct:title "KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon" ;
    dct:title "KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer_Verdirestriksjon" ;
    dct:title "LEI-nummer_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778_Verdirestriksjon" ;
    dct:title "LanebetingelserBruddDispensasjon-23778_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Maalform/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Maalform_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Maalform_Verdirestriksjon" ;
    dct:title "Maalform_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding" ;
    dct:title "Melding"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatVersion> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01_RestriksjonNavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01_RestriksjonNavn" ;
    dct:title "Navn_S01_RestriksjonNavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02_RestriksjonNavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02_RestriksjonNavn" ;
    dct:title "Navn_S02_RestriksjonNavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745_Verdirestriksjon" ;
    dct:title "Nedskrivninger-23745_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon" ;
    dct:title "Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon" ;
    dct:title "Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon" ;
    dct:title "NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214_KodelisteEttValg2JaNei-4_101> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214_KodelisteEttValg2JaNei-4_101" ;
    dct:title "Obligasjon-34214_KodelisteEttValg2JaNei-4_101"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 19 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer_RestriksjonOrganisasjonsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer_RestriksjonOrganisasjonsnummer" ;
    dct:title "Organisasjonsnummer_RestriksjonOrganisasjonsnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 9 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype_Verdirestriksjon" ;
    dct:title "Periodetype_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer_RestriksjonPostnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer_RestriksjonPostnummer" ;
    dct:title "Postnummer_RestriksjonPostnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed_RestriksjonPoststed> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed_RestriksjonPoststed" ;
    dct:title "Poststed_RestriksjonPoststed"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 35 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid_RestriksjonRapporteringsId> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid_RestriksjonRapporteringsId" ;
    dct:title "Rapporteringsid_RestriksjonRapporteringsId"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 50 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102_Ar1980AretsAr-107> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102_Ar1980AretsAr-107" ;
    dct:title "RegnskapAr-17102_Ar1980AretsAr-107"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959_Verdirestriksjon" ;
    dct:title "Regnskapsstandard-31959_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066_Verdirestriksjon" ;
    dct:title "RevisjonsberetningUtenAvvik-34066_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon" ;
    dct:title "SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon" ;
    dct:title "SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S01_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S02_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S03_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S04_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S05_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S06_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S07_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S103_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S104_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S105_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S106_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S107_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S11_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S12_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S13_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S14_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S15_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S16_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S17_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S18_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S19_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S20_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S21_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S22_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S23_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S30_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S31_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S32_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S33_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S34_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S39_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S40_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S41_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S42_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S43_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S44_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S45_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S46_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S50_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S51_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S52_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S53_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S54_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S55_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S56_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S58_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S59_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S60_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S61_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S62_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S63_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S64_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S65_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S66_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S67_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S86_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S87_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S88_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S89_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S91_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S92_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S93_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S94_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S95_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S96_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S97_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S98_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S99_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1_RestriksjonTekst_10_S1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1_RestriksjonTekst_10_S1" ;
    dct:title "Tekst_10_S1_RestriksjonTekst_10_S1"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 10 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10_RestriksjonTekst_255_S10> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10_RestriksjonTekst_255_S10" ;
    dct:title "Tekst_255_S10_RestriksjonTekst_255_S10"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T01_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T02_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T03_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T04_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T05_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T06_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T07_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T08_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T09_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T10_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T11_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T12_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T13_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01_RestriksjonTelefon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01_RestriksjonTelefon" ;
    dct:title "TelefonNummer_S01_RestriksjonTelefon"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02_RestriksjonTelefon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02_RestriksjonTelefon" ;
    dct:title "TelefonNummer_S02_RestriksjonTelefon"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01_RestriksjonTelefonPrefiks> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01_RestriksjonTelefonPrefiks" ;
    dct:title "TelefonPrefiks_S01_RestriksjonTelefonPrefiks"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02_RestriksjonTelefonPrefiks> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02_RestriksjonTelefonPrefiks" ;
    dct:title "TelefonPrefiks_S02_RestriksjonTelefonPrefiks"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761_Verdirestriksjon" ;
    dct:title "UtsattSkattefordel-23761_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon" ;
    dct:title "UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon" ;
    dct:title "UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon" ;
    dct:title "UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon" ;
    dct:title "UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon" ;
    dct:title "UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100" ;
    dct:title "VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 13 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746_Verdirestriksjon> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746_Verdirestriksjon" ;
    dct:title "VerdsettelsePrisBok1-23746_Verdirestriksjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/grunnpensjonsbeloep> a ns1:Attribute ;
    dct:title "grunnpensjonsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/heravEtterlattepensjon> a ns1:Attribute ;
    dct:title "heravEtterlattepensjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/pensjonsgrad> a ns1:Attribute ;
    dct:title "pensjonsgrad"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tilleggspensjonsbeloep> a ns1:Attribute ;
    dct:title "tilleggspensjonsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/ufoeregrad> a ns1:Attribute ;
    dct:title "ufoeregrad"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe" ;
    dct:title "AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/antallTimerPerUkeSomEnFullStillingTilsvarer> a ns1:Attribute ;
    dct:title "antallTimerPerUkeSomEnFullStillingTilsvarer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/arbeidstidsordning> a ns1:Attribute ;
    dct:title "arbeidstidsordning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/avloenningstype> a ns1:Attribute ;
    dct:title "avloenningstype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/fartoey> a ns1:Attribute ;
    dct:title "fartoey"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/loennsansiennitet> a ns1:Attribute ;
    dct:title "loennsansiennitet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/loennstrinn> a ns1:Attribute ;
    dct:title "loennstrinn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/permisjon> a ns1:Attribute ;
    dct:title "permisjon"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sisteDatoForStillingsprosentendring> a ns1:Attribute ;
    dct:title "sisteDatoForStillingsprosentendring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sisteLoennsendringsdato> a ns1:Attribute ;
    dct:title "sisteLoennsendringsdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sluttdato> a ns1:Attribute ;
    dct:title "sluttdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/startdato> a ns1:Attribute ;
    dct:title "startdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/stillingsprosent> a ns1:Attribute ;
    dct:title "stillingsprosent"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/typeArbeidsforhold> a ns1:Attribute ;
    dct:title "typeArbeidsforhold"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforholdstype> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/yrke> a ns1:Attribute ;
    dct:title "yrke"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForSone> a ns1:Attribute ;
    dct:title "fradragIGrunnlagetForSone"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForUtenlandsk> a ns1:Attribute ;
    dct:title "fradragIGrunnlagetForUtenlandsk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/loennOgGodtgjoerelse> a ns1:Attribute ;
    dct:title "loennOgGodtgjoerelse"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/tilskuddOgPremieTilPensjon> a ns1:Attribute ;
    dct:title "tilskuddOgPremieTilPensjon"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedFastAvgiftsbeloep> a ns1:Attribute ;
    dct:title "utenlandskeMedFastAvgiftsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedSaerskiltProsentsats> a ns1:Attribute ;
    dct:title "utenlandskeMedSaerskiltProsentsats"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/avgiftsgrunnlagBeloep> a ns1:Attribute ;
    dct:title "avgiftsgrunnlagBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/beregningskodeForArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "beregningskodeForArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/prosentsatsForAvgiftsberegning> a ns1:Attribute ;
    dct:title "prosentsatsForAvgiftsberegning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/sone> a ns1:Attribute ;
    dct:title "sone"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeskrivelseGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeskrivelseGruppe" ;
    dct:title "BeskrivelseGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "sumArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumFinansskattLoenn> a ns1:Attribute ;
    dct:title "sumFinansskattLoenn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumForskuddstrekk> a ns1:Attribute ;
    dct:title "sumForskuddstrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antallKilometer> a ns1:Attribute ;
    dct:title "antallKilometer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antallReiser> a ns1:Attribute ;
    dct:title "antallReiser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/bilregistreringsnummer> a ns1:Attribute ;
    dct:title "bilregistreringsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erAnnenBil> a ns1:Attribute ;
    dct:title "erAnnenBil"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erBilUtenforStandardregelen> a ns1:Attribute ;
    dct:title "erBilUtenforStandardregelen"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erBilpool> a ns1:Attribute ;
    dct:title "erBilpool"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/heravAntallKilometerMellomHjemOgArbeid> a ns1:Attribute ;
    dct:title "heravAntallKilometerMellomHjemOgArbeid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/listeprisForBil> a ns1:Attribute ;
    dct:title "listeprisForBil"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/personklassifiseringAvBilbruker> a ns1:Attribute ;
    dct:title "personklassifiseringAvBilbruker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaatGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaatGruppe" ;
    dct:title "BilOgBaatGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/aaretUtbetalingenGjelderFor> a ns1:Attribute ;
    dct:title "aaretUtbetalingenGjelderFor"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaretGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaretGruppe" ;
    dct:title "BonusFraForsvaretGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/antallBarn> a ns1:Attribute ;
    dct:title "antallBarn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/antallMaaneder> a ns1:Attribute ;
    dct:title "antallMaaneder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBoligGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBoligGruppe" ;
    dct:title "DagmammaIEgenBoligGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M" ;
    dct:title "EDAG_M"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/leveranse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/leveranse> a ns1:Attribute ;
    dct:title "leveranse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EtterbetalingsperiodeGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EtterbetalingsperiodeGruppe" ;
    dct:title "EtterbetalingsperiodeGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/fartsomraade> a ns1:Attribute ;
    dct:title "fartsomraade"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/skipsregister> a ns1:Attribute ;
    dct:title "skipsregister"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/skipstype> a ns1:Attribute ;
    dct:title "skipstype"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/avgiftsfradragBeloep> a ns1:Attribute ;
    dct:title "avgiftsfradragBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/beregningskodeForArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "beregningskodeForArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/prosentsatsForAvgiftsberegning> a ns1:Attribute ;
    dct:title "prosentsatsForAvgiftsberegning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/sone> a ns1:Attribute ;
    dct:title "sone"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk/avgiftsfradragBeloep> a ns1:Attribute ;
    dct:title "avgiftsfradragBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk/prosentsatsForAvgiftsberegning> a ns1:Attribute ;
    dct:title "prosentsatsForAvgiftsberegning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/ansattnummer> a ns1:Attribute ;
    dct:title "ansattnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/foedselsdato> a ns1:Attribute ;
    dct:title "foedselsdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/navn> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt" ;
    dct:title "Inntekt"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/aaretUtbetalingenGjelderFor> a ns1:Attribute ;
    dct:title "aaretUtbetalingenGjelderFor"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallBarn> a ns1:Attribute ;
    dct:title "antallBarn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallDager> a ns1:Attribute ;
    dct:title "antallDager"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallKilometer> a ns1:Attribute ;
    dct:title "antallKilometer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallMaaneder> a ns1:Attribute ;
    dct:title "antallMaaneder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallReiser> a ns1:Attribute ;
    dct:title "antallReiser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/betaltSkattebeloepIUtlandet> a ns1:Attribute ;
    dct:title "betaltSkattebeloepIUtlandet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilinformasjon> a ns1:Attribute ;
    dct:title "bilinformasjon"@nb ;
    xsd:maxOccurs 1 .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilregistreringsnummer> a ns1:Attribute ;
    dct:title "bilregistreringsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erAnnenBil> a ns1:Attribute ;
    dct:title "erAnnenBil"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erBilUtenforStandardregelen> a ns1:Attribute ;
    dct:title "erBilUtenforStandardregelen"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erBilpool> a ns1:Attribute ;
    dct:title "erBilpool"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/gjelderLoennFoerste60Dager> a ns1:Attribute ;
    dct:title "gjelderLoennFoerste60Dager"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/grunnpensjonsbeloep> a ns1:Attribute ;
    dct:title "grunnpensjonsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/heravAntallKilometerMellomHjemOgArbeid> a ns1:Attribute ;
    dct:title "heravAntallKilometerMellomHjemOgArbeid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/heravEtterlattepensjon> a ns1:Attribute ;
    dct:title "heravEtterlattepensjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inntektsaar> a ns1:Attribute ;
    dct:title "inntektsaar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inntjeningsforhold> a ns1:Attribute ;
    dct:title "inntjeningsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/listeprisForBil> a ns1:Attribute ;
    dct:title "listeprisForBil"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/oppgrossingsgrunnlag> a ns1:Attribute ;
    dct:title "oppgrossingsgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/oppgrossingstabellnummer> a ns1:Attribute ;
    dct:title "oppgrossingstabellnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/pensjonsgrad> a ns1:Attribute ;
    dct:title "pensjonsgrad"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/personklassifiseringAvBilbruker> a ns1:Attribute ;
    dct:title "personklassifiseringAvBilbruker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/persontype> a ns1:Attribute ;
    dct:title "persontype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tilleggsinformasjon> a ns1:Attribute ;
    dct:title "tilleggsinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tilleggspensjonsbeloep> a ns1:Attribute ;
    dct:title "tilleggspensjonsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/totaltUtbetaltBeloep> a ns1:Attribute ;
    dct:title "totaltUtbetaltBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/trukketArtistskatt> a ns1:Attribute ;
    dct:title "trukketArtistskatt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/ufoeregrad> a ns1:Attribute ;
    dct:title "ufoeregrad"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektGruppe" ;
    dct:title "InntektGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/alleFelter> a ns1:Attribute ;
    dct:title "alleFelter"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bilOgBaat> a ns1:Attribute ;
    dct:title "bilOgBaat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bonusFraForsvaret> a ns1:Attribute ;
    dct:title "bonusFraForsvaret"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/dagmammaIEgenBolig> a ns1:Attribute ;
    dct:title "dagmammaIEgenBolig"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/etterbetalingsperiode> a ns1:Attribute ;
    dct:title "etterbetalingsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntektPaaNorskKontinentalsokkel> a ns1:Attribute ;
    dct:title "inntektPaaNorskKontinentalsokkel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntjeningsforhold> a ns1:Attribute ;
    dct:title "inntjeningsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/livrente> a ns1:Attribute ;
    dct:title "livrente"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/loennsinntekt> a ns1:Attribute ;
    dct:title "loennsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/lottOgPart> a ns1:Attribute ;
    dct:title "lottOgPart"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/naeringsinntekt> a ns1:Attribute ;
    dct:title "naeringsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/nettoloenn> a ns1:Attribute ;
    dct:title "nettoloenn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjon> a ns1:Attribute ;
    dct:title "pensjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjonEllerTrygd> a ns1:Attribute ;
    dct:title "pensjonEllerTrygd"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/reiseKostOgLosji> a ns1:Attribute ;
    dct:title "reiseKostOgLosji"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/tilleggsinformasjon> a ns1:Attribute ;
    dct:title "tilleggsinformasjon"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/utenlandskArtist> a ns1:Attribute ;
    dct:title "utenlandskArtist"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa1> a ns1:Attribute ;
    dct:title "valgNivaa1"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa2> a ns1:Attribute ;
    dct:title "valgNivaa2"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa3> a ns1:Attribute ;
    dct:title "valgNivaa3"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa4> a ns1:Attribute ;
    dct:title "valgNivaa4"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/arbeidsforhold> a ns1:Attribute ;
    dct:title "arbeidsforhold"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/forskuddstrekk> a ns1:Attribute ;
    dct:title "forskuddstrekk"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/fradrag> a ns1:Attribute ;
    dct:title "fradrag"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/identifiserendeInformasjon> a ns1:Attribute ;
    dct:title "identifiserendeInformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/inntekt> a ns1:Attribute ;
    dct:title "inntekt"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/internasjonalIdentifikator> a ns1:Attribute ;
    dct:title "internasjonalIdentifikator"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/norskIdentifikator> a ns1:Attribute ;
    dct:title "norskIdentifikator"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/oppholdPaaSvalbardJanMayenOgBilandene> a ns1:Attribute ;
    dct:title "oppholdPaaSvalbardJanMayenOgBilandene"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/sjoefolksrelatertInformasjon> a ns1:Attribute ;
    dct:title "sjoefolksrelatertInformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/inntjeningsforhold> a ns1:Attribute ;
    dct:title "inntjeningsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntjeningsforholdGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntjeningsforholdGruppe" ;
    dct:title "InntjeningsforholdGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/identifikator> a ns1:Attribute ;
    dct:title "identifikator"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/identifikatortype> a ns1:Attribute ;
    dct:title "identifikatortype"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/land> a ns1:Attribute ;
    dct:title "land"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/annenBagatellmessigStoette> a ns1:Attribute ;
    dct:title "annenBagatellmessigStoette"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/betalingsinformasjon> a ns1:Attribute ;
    dct:title "betalingsinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/virksomhet> a ns1:Attribute ;
    dct:title "virksomhet"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/kalendermaaned> a ns1:Attribute ;
    dct:title "kalendermaaned"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/kildesystem> a ns1:Attribute ;
    dct:title "kildesystem"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/leveringstidspunkt> a ns1:Attribute ;
    dct:title "leveringstidspunkt"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/meldingsId> a ns1:Attribute ;
    dct:title "meldingsId"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/oppgave> a ns1:Attribute ;
    dct:title "oppgave"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/opplysningspliktig> a ns1:Attribute ;
    dct:title "opplysningspliktig"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/spraakForTilbakemelding> a ns1:Attribute ;
    dct:title "spraakForTilbakemelding"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasValueFrom <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/totaltUtbetaltBeloep> a ns1:Attribute ;
    dct:title "totaltUtbetaltBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LivrenteGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LivrenteGruppe" ;
    dct:title "LivrenteGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LoennsinntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LoennsinntektGruppe" ;
    dct:title "LoennsinntektGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/antallDager> a ns1:Attribute ;
    dct:title "antallDager"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiskeGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiskeGruppe" ;
    dct:title "LottOgPartInnenFiskeGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding" ;
    dct:title "Melding"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatVersion> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NaeringsinntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NaeringsinntektGruppe" ;
    dct:title "NaeringsinntektGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/betaltSkattebeloepIUtlandet> a ns1:Attribute ;
    dct:title "betaltSkattebeloepIUtlandet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/bilinformasjon> a ns1:Attribute ;
    dct:title "bilinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/oppgrossingstabellnummer> a ns1:Attribute ;
    dct:title "oppgrossingstabellnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NettoloennsordningGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NettoloennsordningGruppe" ;
    dct:title "NettoloennsordningGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/gjelderLoennFoerste60Dager> a ns1:Attribute ;
    dct:title "gjelderLoennFoerste60Dager"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkelGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkelGruppe" ;
    dct:title "NorskKontinentalsokkelGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/oppholdsId> a ns1:Attribute ;
    dct:title "oppholdsId"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/sluttdato> a ns1:Attribute ;
    dct:title "sluttdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/startdato> a ns1:Attribute ;
    dct:title "startdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig/norskIdentifikator> a ns1:Attribute ;
    dct:title "norskIdentifikator"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdGruppe" ;
    dct:title "PensjonEllerTrygdGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode/sluttdato> a ns1:Attribute ;
    dct:title "sluttdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode/startdato> a ns1:Attribute ;
    dct:title "startdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/permisjonId> a ns1:Attribute ;
    dct:title "permisjonId"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/permisjonsprosent> a ns1:Attribute ;
    dct:title "permisjonsprosent"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/sluttdato> a ns1:Attribute ;
    dct:title "sluttdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/startdato> a ns1:Attribute ;
    dct:title "startdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/antallReiser> a ns1:Attribute ;
    dct:title "antallReiser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/persontype> a ns1:Attribute ;
    dct:title "persontype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosjiGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosjiGruppe" ;
    dct:title "ReiseKostOgLosjiGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonIdentifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonIdentifikator" ;
    dct:title "RestriksjonIdentifikator"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 150 .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonTekstfelt> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonTekstfelt" ;
    dct:title "RestriksjonTekstfelt"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon/antallDoegnOmbord> a ns1:Attribute ;
    dct:title "antallDoegnOmbord"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon/antallDoegnOmbordUtenDekkedeSmaautgifter> a ns1:Attribute ;
    dct:title "antallDoegnOmbordUtenDekkedeSmaautgifter"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/erOpptjentPaaHjelpefartoey> a ns1:Attribute ;
    dct:title "erOpptjentPaaHjelpefartoey"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/erOpptjentPaaKontinentalsokkel> a ns1:Attribute ;
    dct:title "erOpptjentPaaKontinentalsokkel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/opptjeningsland> a ns1:Attribute ;
    dct:title "opptjeningsland"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/skattemessigBosattILand> a ns1:Attribute ;
    dct:title "skattemessigBosattILand"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/antall> a ns1:Attribute ;
    dct:title "antall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/arbeidsforholdId> a ns1:Attribute ;
    dct:title "arbeidsforholdId"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/beloep> a ns1:Attribute ;
    dct:title "beloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/beskrivelse> a ns1:Attribute ;
    dct:title "beskrivelse"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/fordel> a ns1:Attribute ;
    dct:title "fordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/inngaarIGrunnlagForTrekk> a ns1:Attribute ;
    dct:title "inngaarIGrunnlagForTrekk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/inntektsaar> a ns1:Attribute ;
    dct:title "inntektsaar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/oppgrossingsgrunnlag> a ns1:Attribute ;
    dct:title "oppgrossingsgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/skatteOgAvgiftsregel> a ns1:Attribute ;
    dct:title "skatteOgAvgiftsregel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/sluttdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "sluttdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/startdatoOpptjeningsperiode> a ns1:Attribute ;
    dct:title "startdatoOpptjeningsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/trukketArtistskatt> a ns1:Attribute ;
    dct:title "trukketArtistskatt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/utloeserArbeidsgiveravgift> a ns1:Attribute ;
    dct:title "utloeserArbeidsgiveravgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtistGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtistGruppe" ;
    dct:title "UtenlandskArtistGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep/antallAvgiftsgrunnlagPersoner> a ns1:Attribute ;
    dct:title "antallAvgiftsgrunnlagPersoner"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep/beloepssatsForAvgiftsberegning> a ns1:Attribute ;
    dct:title "beloepssatsForAvgiftsberegning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats/avgiftsgrunnlagBeloep> a ns1:Attribute ;
    dct:title "avgiftsgrunnlagBeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats/prosentsatsForAvgiftsberegning> a ns1:Attribute ;
    dct:title "prosentsatsForAvgiftsberegning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/arbeidsgiveravgift> a ns1:Attribute ;
    dct:title "arbeidsgiveravgift"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/inntektsmottaker> a ns1:Attribute ;
    dct:title "inntektsmottaker"@nb ;
    ns1:containsObjectType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/norskIdentifikator> a ns1:Attribute ;
    dct:title "norskIdentifikator"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator> .

<http://seres.no/guid/Finanstilsynet/DataTypeegenskap/aksjeutsteder/446028> a ns1:Attribute ;
    dct:title "aksjeutsteder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215> .

<http://seres.no/guid/Finanstilsynet/DataTypeegenskap/grunnfondsbevisutsteder/446026> a ns1:Attribute ;
    dct:title "grunnfondsbevisutsteder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128> .

<http://seres.no/guid/Finanstilsynet/DataTypeegenskap/obligasjonsutsteder/446027> a ns1:Attribute ;
    dct:title "obligasjonsutsteder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/OBX-utvalg/445915> a ns1:Attribute ;
    dct:title "oBX-utvalg"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/PBOver1/445927> a ns1:Attribute ;
    dct:title "pBOver1"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/adresselinje1/660280> a ns1:Attribute ;
    dct:title "adresselinje1"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/aksjeStørstOppgangNedgang/445914> a ns1:Attribute ;
    dct:title "aksjeStoerstOppgangNedgang"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/aksjebasertInsentivordning/445930> a ns1:Attribute ;
    dct:title "aksjebasertInsentivordning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/andelUnder10/445956> a ns1:Attribute ;
    dct:title "andelUnder10"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/andre/771959> a ns1:Attribute ;
    dct:title "andre"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/anginote/771940> a ns1:Attribute ;
    dct:title "anginote"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annenMåte/622379> a ns1:Attribute ;
    dct:title "annenMaate"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/622390> a ns1:Attribute ;
    dct:title "annet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771891> a ns1:Attribute ;
    dct:title "annet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771912> a ns1:Attribute ;
    dct:title "annet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771924> a ns1:Attribute ;
    dct:title "annet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklar/771890> a ns1:Attribute ;
    dct:title "annetforklar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklar/771958> a ns1:Attribute ;
    dct:title "andreforklar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklaring/771911> a ns1:Attribute ;
    dct:title "annetforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklaring/771923> a ns1:Attribute ;
    dct:title "annetforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ansvarlige/665145> a ns1:Attribute ;
    dct:title "ansvarlige"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/antallAlternativeResultatmål/664867> a ns1:Attribute ;
    dct:title "antallAlternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/antallMøterRevisorOgRevisjonsutvalg/622407> a ns1:Attribute ;
    dct:title "antallMoeterRevisorOgRevisjonsutvalg"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtGoodwill/600742> a ns1:Attribute ;
    dct:title "balansefoertGoodwill"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver10/445944> a ns1:Attribute ;
    dct:title "balansefoertOver10"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver10Egenkapital/446016> a ns1:Attribute ;
    dct:title "balansefoertOver10Egenkapital"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver50/445943> a ns1:Attribute ;
    dct:title "balansefoertOver50"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver50Egenkapital/446015> a ns1:Attribute ;
    dct:title "balansefoertOver50Egenkapital"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/balansesum/771915> a ns1:Attribute ;
    dct:title "balansesum"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/bankogfinans/665148> a ns1:Attribute ;
    dct:title "bankogfinans"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/benytterAlternativeResultatmål/664868> a ns1:Attribute ;
    dct:title "benytterAlternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/bransje/445917> a ns1:Attribute ;
    dct:title "bransje"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/bruddDispensasjonLånebetingelser/445987> a ns1:Attribute ;
    dct:title "bruddDispensasjonLaanebetingelser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/brukEksperterBransjeerfaring/622386> a ns1:Attribute ;
    dct:title "brukEksperterBransjeerfaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/bruttoEndringTotaleEiendelerOver10/445921> a ns1:Attribute ;
    dct:title "bruttoEndringTotaleEiendelerOver10"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/bruttoEndringTotaleEiendelerOver25/445920> a ns1:Attribute ;
    dct:title "bruttoEndringTotaleEiendelerOver25"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/børsverdiForetak/445913> a ns1:Attribute ;
    dct:title "boersverdiForetak"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/coveredbondbenchmark/665141> a ns1:Attribute ;
    dct:title "coveredbondbenchmark"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/diskutertKamAvslutning/664857> a ns1:Attribute ;
    dct:title "diskutertKamAvslutning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/diskutertKamPlanlegging/664858> a ns1:Attribute ;
    dct:title "diskutertKamPlanlegging"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/driftsaktivitetOverstigerÅrsresultat/445909> a ns1:Attribute ;
    dct:title "driftsaktivitetOverstigerAArsresultat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ebitda/771913> a ns1:Attribute ;
    dct:title "ebitda"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/egenkapitalAksjeeierMorforetak/445954> a ns1:Attribute ;
    dct:title "egenkapitalAksjeeierMorforetak"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/eksternRevisorPåpektSvakhetSystemKontrollRisikostyring/622406> a ns1:Attribute ;
    dct:title "eksternRevisorPaapektSvakhetSystemKontrollRisikostyring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/eksternRevisorSkiftet/445931> a ns1:Attribute ;
    dct:title "eksternRevisorSkiftet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/endretAlternativeResultatmål/664865> a ns1:Attribute ;
    dct:title "endretAlternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/endringGjeldOver5/664859> a ns1:Attribute ;
    dct:title "endringGjeldOver5"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/endringRegnskapsprinppEndringStandard/664861> a ns1:Attribute ;
    dct:title "endringRegnskapsprinppEndringStandard"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/endringRegnskapsprinsippFrivillig/664862> a ns1:Attribute ;
    dct:title "endringRegnskapsprinsippFrivillig"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/epost/637646> a ns1:Attribute ;
    dct:title "epost"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/epost/637651> a ns1:Attribute ;
    dct:title "epost"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittforklaringendringer/771956> a ns1:Attribute ;
    dct:title "ergittforklaringendringer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittforklaringendringerforklaring/771955> a ns1:Attribute ;
    dct:title "ergittforklaringendringerforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittinngåendeutgående/771907> a ns1:Attribute ;
    dct:title "ergittinngaaendeutgaaende"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittinngåendeutgåendeforklaring/771906> a ns1:Attribute ;
    dct:title "ergittinngaaendeutgaaendeforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittopplysninger/771905> a ns1:Attribute ;
    dct:title "ergittopplysningertransaksjonsprisen"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittopplysningerforklaring/771904> a ns1:Attribute ;
    dct:title "ergittopplysningertransaksjonsprisenforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergitttilstrekkeligeopplysninger/771969> a ns1:Attribute ;
    dct:title "ergitttilstrekkeligeopplysninger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ergitttilstrekkeligeopplysningerforklaring/771968> a ns1:Attribute ;
    dct:title "ergitttilstrekkeligeopplysningerforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjordriftsinntektforklaring/771909> a ns1:Attribute ;
    dct:title "erredegjordriftsinntektforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortanvender/771908> a ns1:Attribute ;
    dct:title "erredegjortanvender"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortanvenderforklaring/771910> a ns1:Attribute ;
    dct:title "erredegjortanvenderforklaring"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortnårdriftsinntekt/771903> a ns1:Attribute ;
    dct:title "erredegjordriftsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/etablertRevisjonsutvalg/622408> a ns1:Attribute ;
    dct:title "etablertRevisjonsutvalg"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/etiskRetningslinje/445935> a ns1:Attribute ;
    dct:title "etiskRetningslinje"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsetteleieperioden/771927> a ns1:Attribute ;
    dct:title "fastsetteleieperioden"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsettelsetransaksjonspris/771898> a ns1:Attribute ;
    dct:title "fastsettelsetransaksjonspris"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsettelånerente/771925> a ns1:Attribute ;
    dct:title "fastsettelaanerente"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/feilÅrsregnskapDelårsregnskap/445984> a ns1:Attribute ;
    dct:title "feilAArsregnskapDelaarsregnskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/finansielleInstrumenterUnotert/445971> a ns1:Attribute ;
    dct:title "finansielleInstrumenterUnotert"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fondsobligasjoner/665143> a ns1:Attribute ;
    dct:title "fondsobligasjoner"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fordelingtransaksjonspris/771897> a ns1:Attribute ;
    dct:title "fordelingtransaksjonspris"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fordklarendringer/771994> a ns1:Attribute ;
    dct:title "fordklarendringer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/foretaksnavn/664848> a ns1:Attribute ;
    dct:title "foretaksnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/forsikringsbokføring/771934> a ns1:Attribute ;
    dct:title "forsikringsbokfoering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/fraveketKravIFRS/445983> a ns1:Attribute ;
    dct:title "fraveketKravIFRS"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/geografiskområde/771964> a ns1:Attribute ;
    dct:title "geografiskomraade"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/gevinstTapFinansielleInstrumenterOver25/445969> a ns1:Attribute ;
    dct:title "gevinstTapFinansielleInstrumenterOver25"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/gevinstTapFinansielleInstrumenterOver5/445970> a ns1:Attribute ;
    dct:title "gevinstTapFinansielleInstrumenterOver5"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/gjeldVirkeligVerdi/664860> a ns1:Attribute ;
    dct:title "gjeldVirkeligVerdi"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/groenneobligasjoner/665140> a ns1:Attribute ;
    dct:title "groenneobligasjoner"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/haddeias1257avesentligeffekt/771949> a ns1:Attribute ;
    dct:title "haddeias1257avesentligeffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/harleiekontrakter/771974> a ns1:Attribute ;
    dct:title "harleiekontrakter"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/identifisereleieavtale/771928> a ns1:Attribute ;
    dct:title "identifisereleieavtale"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/identifiseringleveringsforpliktelser/771899> a ns1:Attribute ;
    dct:title "identifiseringleveringsforpliktelser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ifrs16harforklartforskjeller/772063> a ns1:Attribute ;
    dct:title "ifrs16harforklartforskjeller"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ikkeaktuelt/771916> a ns1:Attribute ;
    dct:title "ikkeaktuelt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/immateriellEiendel/445945> a ns1:Attribute ;
    dct:title "immateriellEiendel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/industrioghandel/665146> a ns1:Attribute ;
    dct:title "industrioghandel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/ingeneffekt/771933> a ns1:Attribute ;
    dct:title "ingeneffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/innføringifric23vesentligeffekt/771948> a ns1:Attribute ;
    dct:title "innfoeringifric23vesentligeffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/inntektvekstOver25/445986> a ns1:Attribute ;
    dct:title "inntektvekstOver25"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/inntruffetForholdTrusselRevisorUavhengighet/622401> a ns1:Attribute ;
    dct:title "inntruffetForholdTrusselRevisorUavhengighet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/investeringerOver50/600183> a ns1:Attribute ;
    dct:title "investeringerOver50"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/investeringsaktivitetOverstigerÅrsresultat/445908> a ns1:Attribute ;
    dct:title "investeringsaktivitetOverstigerAArsresultat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kapasitetKompetanse/622395> a ns1:Attribute ;
    dct:title "kapasitetKompetanse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/klassifiseringfinansielleinstrument/771937> a ns1:Attribute ;
    dct:title "klassifiseringfinansielleinstrument"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kommuneogfylke/665149> a ns1:Attribute ;
    dct:title "kommuneogfylke"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/konsernregnskap/445938> a ns1:Attribute ;
    dct:title "konsernregnskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/konsolidertDatterselskap/600184> a ns1:Attribute ;
    dct:title "konsolidertDatterselskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kontinuitet/622392> a ns1:Attribute ;
    dct:title "kontinuitet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktensløpetid/771962> a ns1:Attribute ;
    dct:title "kontraktensloepetid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktskostnader/771892> a ns1:Attribute ;
    dct:title "kontraktskostnader"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktstype/771967> a ns1:Attribute ;
    dct:title "kontraktstype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/konvertible/665144> a ns1:Attribute ;
    dct:title "konvertible"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/korrigertNegativ/445955> a ns1:Attribute ;
    dct:title "korrigertNegativ"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kredittforetak/665147> a ns1:Attribute ;
    dct:title "kredittforetak"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kvalitetNyhetsbrev/622382> a ns1:Attribute ;
    dct:title "kvalitetNyhetsbrev"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/kvalitetPresentasjonBrev/622383> a ns1:Attribute ;
    dct:title "kvalitetPresentasjonBrev"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/lEI-nummer/771885> a ns1:Attribute ;
    dct:title "lEI-nummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/leiekontrakterinneholder/771973> a ns1:Attribute ;
    dct:title "leiekontrakterinneholder"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/leiekontrakterinneholderleiekomponenter/771979> a ns1:Attribute ;
    dct:title "harforetaketleiekontrakter"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/maalform/665679> a ns1:Attribute ;
    dct:title "maalform"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/markedkundetype/771963> a ns1:Attribute ;
    dct:title "markedkundetype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/medgåttTid/622388> a ns1:Attribute ;
    dct:title "medgaattTid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/mestkrevendevurdering/771982> a ns1:Attribute ;
    dct:title "mestkrevendevurdering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/metodebrukt/771894> a ns1:Attribute ;
    dct:title "metodebrukt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/målingandre/771935> a ns1:Attribute ;
    dct:title "maalingandre"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/målingkundefordringer/771936> a ns1:Attribute ;
    dct:title "maalingkundefordringer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/målingleiebetalinger/771926> a ns1:Attribute ;
    dct:title "maalingleiebetalinger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/navn/637645> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/navn/637650> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/nedskriving/445928> a ns1:Attribute ;
    dct:title "nedskriving"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/negativGoodwill/600182> a ns1:Attribute ;
    dct:title "negativGoodwill"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/negativtDriftsresultat/445961> a ns1:Attribute ;
    dct:title "negativtDriftsresultat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/negativtÅrsresultat/445959> a ns1:Attribute ;
    dct:title "negativtAArsresultat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/nyeAlternativeResultatmål/664863> a ns1:Attribute ;
    dct:title "nyeAlternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/obligasjonermedfortrinnsrett/665142> a ns1:Attribute ;
    dct:title "obligasjonermedfortrinnsrett"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/omarbeidelseResultatBalanseTall/600185> a ns1:Attribute ;
    dct:title "omarbeidelseResultatBalanseTall"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/oppfyllelseleveringsforpliktelsertid/771896> a ns1:Attribute ;
    dct:title "oppfyllelseleveringsforpliktelsertid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/oppfyllelseleveringsforpliktelsertidspunkt/771895> a ns1:Attribute ;
    dct:title "oppfyllelseleveringsforpliktelsertidspunkt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/organisasjonsnummer/664849> a ns1:Attribute ;
    dct:title "organisasjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/over10/445998> a ns1:Attribute ;
    dct:title "over10"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/over25FørSkatt/446010> a ns1:Attribute ;
    dct:title "over25FoerSkatt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/over50/445997> a ns1:Attribute ;
    dct:title "over50"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/over5FørSkatt/446011> a ns1:Attribute ;
    dct:title "over5FoerSkatt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/periodetype/664924> a ns1:Attribute ;
    dct:title "periodetype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/personellRevisjonsteamet/622385> a ns1:Attribute ;
    dct:title "personellRevisjonsteamet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/postnummer/660281> a ns1:Attribute ;
    dct:title "postnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/poststed/660279> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/presentererAlternativeResultatmål/664866> a ns1:Attribute ;
    dct:title "presentererAlternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/prinsipalagent/771893> a ns1:Attribute ;
    dct:title "prinsipalagent"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/pris/622397> a ns1:Attribute ;
    dct:title "pris"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/påserRevisjonsutvalgetOppfølging/622405> a ns1:Attribute ;
    dct:title "paaserRevisjonsutvalgetOppfoelging"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/rapporteringsId/660290> a ns1:Attribute ;
    dct:title "rapporteringsid"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/referanser/622380> a ns1:Attribute ;
    dct:title "referanser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/regnskapsspråk/445937> a ns1:Attribute ;
    dct:title "regnskapsspraak"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/regnskapsår/445939> a ns1:Attribute ;
    dct:title "regnskapsaar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/relasjoner/622393> a ns1:Attribute ;
    dct:title "relasjoner"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/renomme/622394> a ns1:Attribute ;
    dct:title "renomme"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/restruktureringsavsetning/446012> a ns1:Attribute ;
    dct:title "restruktureringsavsetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattNegativt/445924> a ns1:Attribute ;
    dct:title "resultatFoerSkattNegativt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattOver25/445925> a ns1:Attribute ;
    dct:title "resultatFoerSkattOver25"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattOver5/445926> a ns1:Attribute ;
    dct:title "resultatFoerSkattOver5"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetning/600180> a ns1:Attribute ;
    dct:title "revisjonsberetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetningModifisering/600178> a ns1:Attribute ;
    dct:title "revisjonsberetningModifisering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetningPresisering/600179> a ns1:Attribute ;
    dct:title "revisjonsberetningPresisering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonskvalitet/622396> a ns1:Attribute ;
    dct:title "revisjonskvalitet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsutvalgRepresentert/622402> a ns1:Attribute ;
    dct:title "revisjonsutvalgRepresentert"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/rotasjonRevisjonsselskap/622391> a ns1:Attribute ;
    dct:title "rotasjonRevisjonsselskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/salgskanaler/771960> a ns1:Attribute ;
    dct:title "salgskanaler"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/sammensetningTimeforbruk/622387> a ns1:Attribute ;
    dct:title "sammensetningTimeforbruk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/sertifikater/665151> a ns1:Attribute ;
    dct:title "sertifikater"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/sikringsbokføring/445972> a ns1:Attribute ;
    dct:title "sikringsbokfoering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/sluttetAlternativeResultatm/664864> a ns1:Attribute ;
    dct:title "sluttetAlternativeResultatm"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/spesifiser/664854> a ns1:Attribute ;
    dct:title "spesifiser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/statslaan/665152> a ns1:Attribute ;
    dct:title "statslaan"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/storlaan/665150> a ns1:Attribute ;
    dct:title "storlaan"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/styrelederToppledelseSkiftet/445934> a ns1:Attribute ;
    dct:title "styrelederToppledelseSkiftet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/sumforpliktelser/771914> a ns1:Attribute ;
    dct:title "sumforpliktelser"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/tapRettssak/445985> a ns1:Attribute ;
    dct:title "tapRettssak"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonPrefiks/637643> a ns1:Attribute ;
    dct:title "telefonprefiks"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonPrefiks/637648> a ns1:Attribute ;
    dct:title "telefonprefiks"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonnr/637644> a ns1:Attribute ;
    dct:title "telefonnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonnr/637649> a ns1:Attribute ;
    dct:title "telefonnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/tidspunktoverføring/771961> a ns1:Attribute ;
    dct:title "tidspunktoverfoering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/tidsriktigLevering/622384> a ns1:Attribute ;
    dct:title "tidsriktigLevering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/typevaretjeneste/771965> a ns1:Attribute ;
    dct:title "typevaretjeneste"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/uenighetRevisjonsutvalgetEksternRevisorInternKontroll/622404> a ns1:Attribute ;
    dct:title "uenighetRevisjonsutvalgetEksternRevisorInternKontroll"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/undersøkelserFølgeOppRevisor/622400> a ns1:Attribute ;
    dct:title "undersoekelserFoelgeOppRevisor"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendeler/445968> a ns1:Attribute ;
    dct:title "utoverFinansielleEiendeler"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendelerOver10/445967> a ns1:Attribute ;
    dct:title "utoverFinansielleEiendelerOver10"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendelerOver50/445966> a ns1:Attribute ;
    dct:title "utoverFinansielleEiendelerOver50"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordeOver5/445980> a ns1:Attribute ;
    dct:title "utsattSkattefordeOver5"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordel/445981> a ns1:Attribute ;
    dct:title "utsattSkattefordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordelOver25/445979> a ns1:Attribute ;
    dct:title "utsattSkattefordelOver25"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utstederOvertakerEllerOvertatt/445922> a ns1:Attribute ;
    dct:title "utstederOvertakerEllerOvertatt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utstedertype/445918> a ns1:Attribute ;
    dct:title "utstedertype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029> .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/åpenhetsrapport/622381> a ns1:Attribute ;
    dct:title "aapenhetsrapport"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673> .

<http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114" ;
    dct:title "KRT-1003v3_M"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/rapport>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/rapportKRT-1003>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KRT-1003v3_M/skjemainnholdKRT-1003> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/adresse/664847> a ns1:Attribute ;
    dct:title "adresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/alternativeResultatmål/664901> a ns1:Attribute ;
    dct:title "alternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/andreForhold/446000> a ns1:Attribute ;
    dct:title "andreForhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/egenkapital/446002> a ns1:Attribute ;
    dct:title "egenkapital"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/forpliktelseAvsetning/446004> a ns1:Attribute ;
    dct:title "forpliktelseAvsetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15/771902> a ns1:Attribute ;
    dct:title "ifrs15"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15kategorier/771957> a ns1:Attribute ;
    dct:title "ifrs15kategorier"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15vurderinger/771900> a ns1:Attribute ;
    dct:title "ifrs15vurderinger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16/771888> a ns1:Attribute ;
    dct:title "ifrs16"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterleietaker/771981> a ns1:Attribute ;
    dct:title "ifrs16leiekontrakterleietaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterutleiereksterne/771983> a ns1:Attribute ;
    dct:title "ifrs16leiekontrakterutleiereksterne"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurderinger/771970> a ns1:Attribute ;
    dct:title "ifrs16vurderinger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurdertikkeeffekt/771976> a ns1:Attribute ;
    dct:title "ifrs16vurdertikkeeffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs9/771947> a ns1:Attribute ;
    dct:title "ifrs9"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrsandre/771950> a ns1:Attribute ;
    dct:title "ifrsandre"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrseffekt/771942> a ns1:Attribute ;
    dct:title "ifrseffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/immatriellEiendel/446005> a ns1:Attribute ;
    dct:title "immatriellEiendel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/innsender/664852> a ns1:Attribute ;
    dct:title "innsender"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson1/664845> a ns1:Attribute ;
    dct:title "kontaktperson1"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson2/664844> a ns1:Attribute ;
    dct:title "kontaktperson2"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontantstrøm/445962> a ns1:Attribute ;
    dct:title "kontantstroem"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/markedsverdibasertEiendel/446006> a ns1:Attribute ;
    dct:title "markedsverdibasertEiendel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/nedskriving/445958> a ns1:Attribute ;
    dct:title "nedskriving"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/organisasjonsforhold/446008> a ns1:Attribute ;
    dct:title "organisasjonsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/periode/664926> a ns1:Attribute ;
    dct:title "periode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapportering/664851> a ns1:Attribute ;
    dct:title "rapportering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapporteringsregisteret/664900> a ns1:Attribute ;
    dct:title "rapporteringsregisteret"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/regnskap/445951> a ns1:Attribute ;
    dct:title "regnskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rentepapirertype/665073> a ns1:Attribute ;
    dct:title "rentepapirertype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/restruktureringsavsetning/446003> a ns1:Attribute ;
    dct:title "restruktureringsavsetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/resultatpost/446007> a ns1:Attribute ;
    dct:title "resultatpost"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsberetning/600187> a ns1:Attribute ;
    dct:title "revisjonsberetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalg/622454> a ns1:Attribute ;
    dct:title "revisjonsutvalg"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgFaktorer/622399> a ns1:Attribute ;
    dct:title "revisjonsutvalgFaktorer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgKriterier/622403> a ns1:Attribute ;
    dct:title "revisjonsutvalgKriterier"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utsattSkattefordel/445942> a ns1:Attribute ;
    dct:title "utsattSkattefordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utviklingsutgift/445941> a ns1:Attribute ;
    dct:title "utviklingsutgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/virksomhetssammenslutninger/446001> a ns1:Attribute ;
    dct:title "virksomhetssammenslutninger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:containsObjectType <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923> .

<https://altinn.fellesdatakatalog.digdir.no/models/2365-3442> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/840747972> ;
    dct:title "Report from an issuer listed on Oslo Børs/Oslo Axess (KRT-1003)"@nb ;
    ns1:containsModelElement <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1_RestriksjonAdresselinje1>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065_Heltall9-408_1>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn_RestriksjonForetaksnavn>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01_RestriksjonHeltall_1_S01>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02_RestriksjonHeltall_1_S02>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03_RestriksjonHeltall_1_S03>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04_RestriksjonHeltall_1_S04>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05_RestriksjonHeltall_1_S05>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06_RestriksjonHeltall_1_S06>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07_RestriksjonHeltall_1_S07>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08_RestriksjonHeltall_1_S08>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01_RestriksjonHeltall_2_S01>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Maalform_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Melding>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01_RestriksjonNavn>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02_RestriksjonNavn>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214_KodelisteEttValg2JaNei-4_101>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer_RestriksjonOrganisasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer_RestriksjonPostnummer>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed_RestriksjonPoststed>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid_RestriksjonRapporteringsId>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102_Ar1980AretsAr-107>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1_RestriksjonTekst_10_S1>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10_RestriksjonTekst_255_S10>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13_RestriksjonTekst_750>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01_RestriksjonTelefon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02_RestriksjonTelefon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01_RestriksjonTelefonPrefiks>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02_RestriksjonTelefonPrefiks>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100>,
        <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746_Verdirestriksjon>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658>,
        <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722>,
        <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314>,
        <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313>,
        <http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923>,
        <http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975>,
        <http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953>,
        <http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009>,
        <http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853>,
        <http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114>,
        <http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636>,
        <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588>,
        <http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150>,
        <http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170>,
        <http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128>,
        <http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133>,
        <http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215>,
        <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118>,
        <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197>,
        <http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211>,
        <http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089> .

<https://altinn.fellesdatakatalog.digdir.no/models/3906-3940> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A01 a-melding"@nb ;
    ns1:containsModelElement <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforholdstype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeskrivelseGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaatGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaretGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBoligGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EtterbetalingsperiodeGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntjeningsforholdGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LivrenteGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LoennsinntektGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiskeGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Melding>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NaeringsinntektGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NettoloennsordningGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkelGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosjiGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/RestriksjonTekstfelt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtistGruppe>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke> .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/840747972> a foaf:Agent ;
    foaf:name "Finanstilsynet"@nb .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> a foaf:Agent ;
    foaf:name "Skatteetaten"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned" ;
    dct:title "AArOgMaaned"@nb ;
    xsd:anyURI xsd:gYearMonth .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon" ;
    dct:title "AldersUfoereEtterlatteAvtalefestetOgKrigspensjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/grunnpensjonsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/heravEtterlattepensjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/pensjonsgrad>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tidsrom>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tilleggspensjonsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/ufoeregrad>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold" ;
    dct:title "Arbeidsforhold"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/antallTimerPerUkeSomEnFullStillingTilsvarer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/arbeidstidsordning>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/avloenningstype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/fartoey>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/loennsansiennitet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/loennstrinn>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/permisjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sisteDatoForStillingsprosentendring>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sisteLoennsendringsdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/sluttdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/startdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/stillingsprosent>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/typeArbeidsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/yrke> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforholdstype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforholdstype" ;
    dct:title "Arbeidsforholdstype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift" ;
    dct:title "Arbeidsgiveravgift"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForSone>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForUtenlandsk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/loennOgGodtgjoerelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/tilskuddOgPremieTilPensjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedFastAvgiftsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedSaerskiltProsentsats> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning" ;
    dct:title "Arbeidstidsordning"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype" ;
    dct:title "Avloenningstype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon" ;
    dct:title "Betalingsinformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumArbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumFinansskattLoenn>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon/sumForskuddstrekk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret" ;
    dct:title "BonusFraForsvaret"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/aaretUtbetalingenGjelderFor>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig" ;
    dct:title "DagmammaIEgenBolig"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/antallBarn>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/antallMaaneder>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid" ;
    dct:title "DatoTid"@nb ;
    xsd:anyURI xsd:dateTime .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode" ;
    dct:title "Etterbetalingsperiode"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/tidsrom>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey" ;
    dct:title "Fartoey"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/fartsomraade>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/skipsregister>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey/skipstype> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade" ;
    dct:title "Fartsomraade"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk" ;
    dct:title "Forskuddstrekk"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk/beskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse" ;
    dct:title "Forskuddstrekksbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag" ;
    dct:title "Fradrag"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag/beskrivelse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget" ;
    dct:title "FradragIGrunnlaget"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/avgiftsfradragBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/beregningskodeForArbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/prosentsatsForAvgiftsberegning>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget/sone> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk" ;
    dct:title "FradragIGrunnlagetForUtenlandsk"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk/avgiftsfradragBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk/prosentsatsForAvgiftsberegning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse" ;
    dct:title "Fradragsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske" ;
    dct:title "GrunnlagsbeloepForUtenlandske"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon" ;
    dct:title "IdentifiserendeInformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/ansattnummer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/foedselsdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon/navn> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle" ;
    dct:title "InntektAlle"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/aaretUtbetalingenGjelderFor>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallBarn>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallDager>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallKilometer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallMaaneder>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/antallReiser>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/betaltSkattebeloepIUtlandet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilregistreringsnummer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erAnnenBil>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erBilUtenforStandardregelen>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/erBilpool>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/gjelderLoennFoerste60Dager>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/grunnpensjonsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/heravAntallKilometerMellomHjemOgArbeid>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/heravEtterlattepensjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inntektsaar>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/inntjeningsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/listeprisForBil>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/oppgrossingsgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/oppgrossingstabellnummer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/pensjonsgrad>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/personklassifiseringAvBilbruker>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/persontype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tidsrom>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tilleggsinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tilleggspensjonsbeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/totaltUtbetaltBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/trukketArtistskatt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/ufoeregrad>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet" ;
    dct:title "Inntektsentitet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/alleFelter>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bilOgBaat>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bonusFraForsvaret>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/dagmammaIEgenBolig>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/etterbetalingsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntektPaaNorskKontinentalsokkel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntjeningsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/livrente>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/loennsinntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/lottOgPart>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/naeringsinntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/nettoloenn>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjonEllerTrygd>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/reiseKostOgLosji>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/tilleggsinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/utenlandskArtist>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa1>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa2>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa3>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/valgNivaa4> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker" ;
    dct:title "Inntektsmottaker"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/arbeidsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/forskuddstrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/fradrag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/identifiserendeInformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/inntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/internasjonalIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/norskIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/oppholdPaaSvalbardJanMayenOgBilandene>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/sjoefolksrelatertInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold" ;
    dct:title "Inntjeningsforhold"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/inntjeningsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator" ;
    dct:title "InternasjonalIdentifikator"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/identifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/identifikatortype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator/land> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype" ;
    dct:title "InternasjonalIdentifikatortype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet" ;
    dct:title "JuridiskEntitet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/annenBagatellmessigStoette>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/betalingsinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/virksomhet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse" ;
    dct:title "Leveranse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/kalendermaaned>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/kildesystem>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/leveringstidspunkt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/meldingsId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/oppgave>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/opplysningspliktig>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/spraakForTilbakemelding> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente" ;
    dct:title "Livrente"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/tidsrom>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/totaltUtbetaltBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt" ;
    dct:title "Loennsinntekt"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske" ;
    dct:title "LottOgPartInnenFiske"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/antallDager>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt" ;
    dct:title "Naeringsinntekt"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning" ;
    dct:title "Nettoloennsordning"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/betaltSkattebeloepIUtlandet>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/bilinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/oppgrossingstabellnummer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel" ;
    dct:title "NorskKontinentalsokkel"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/gjelderLoennFoerste60Dager>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/tidsrom>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene" ;
    dct:title "OppholdPaaSvalbardJanMayenOgBilandene"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/oppholdsId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/sluttdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene/startdato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene" ;
    dct:title "OppholdsbeskrivelseForSvalbardJanMayenOgBilandene"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig" ;
    dct:title "Opplysningspliktig"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig/norskIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd" ;
    dct:title "PensjonEllerTrygd"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon" ;
    dct:title "Permisjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/permisjonId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/permisjonsprosent>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/sluttdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon/startdato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse" ;
    dct:title "PermisjonsOgPermitteringsBeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji" ;
    dct:title "ReiseKostOgLosji"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/antallReiser>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/persontype>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon" ;
    dct:title "SjoefolksrelatertInformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon/antallDoegnOmbord>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon/antallDoegnOmbordUtenDekkedeSmaautgifter> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister" ;
    dct:title "Skipsregister"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype" ;
    dct:title "Skipstype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak" ;
    dct:title "Spraak"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist" ;
    dct:title "UtenlandskArtist"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/inntektsaar>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/oppgrossingsgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/trukketArtistskatt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep" ;
    dct:title "UtenlandskeMedFastAvgiftsbeloep"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep/antallAvgiftsgrunnlagPersoner>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep/beloepssatsForAvgiftsberegning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats" ;
    dct:title "UtenlandskeMedSaerskiltProsentsats"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats/avgiftsgrunnlagBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats/prosentsatsForAvgiftsberegning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet" ;
    dct:title "Virksomhet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/arbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/inntektsmottaker>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/norskIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke" ;
    dct:title "Yrke"@nb ;
    xsd:anyURI xsd:string .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286" ;
    dct:title "Adresselinje1"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664" ;
    dct:title "Epost_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663" ;
    dct:title "Epost_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250" ;
    dct:title "Foretaksnavn"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942" ;
    dct:title "Heltall_1_S03"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941" ;
    dct:title "Heltall_1_S04"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940" ;
    dct:title "Heltall_1_S05"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939" ;
    dct:title "Heltall_1_S06"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938" ;
    dct:title "Heltall_1_S07"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937" ;
    dct:title "Heltall_1_S08"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797" ;
    dct:title "Heltall_1_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798" ;
    dct:title "Heltall_1_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616" ;
    dct:title "Heltall_2_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277" ;
    dct:title "LEI-nummer"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674" ;
    dct:title "Maalform"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Maalform/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662" ;
    dct:title "Navn_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661" ;
    dct:title "Navn_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574" ;
    dct:title "Organisasjonsnummer"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275" ;
    dct:title "Periodetype"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288" ;
    dct:title "Postnummer"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287" ;
    dct:title "Poststed"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854" ;
    dct:title "Rapporteringsid"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631" ;
    dct:title "Tekst_10_S1"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714" ;
    dct:title "Tekst_255_S10"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952" ;
    dct:title "Tekst_750_T01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951" ;
    dct:title "Tekst_750_T02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950" ;
    dct:title "Tekst_750_T03"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949" ;
    dct:title "Tekst_750_T04"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948" ;
    dct:title "Tekst_750_T05"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947" ;
    dct:title "Tekst_750_T06"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946" ;
    dct:title "Tekst_750_T07"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945" ;
    dct:title "Tekst_750_T08"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944" ;
    dct:title "Tekst_750_T09"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943" ;
    dct:title "Tekst_750_T10"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942" ;
    dct:title "Tekst_750_T11"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941" ;
    dct:title "Tekst_750_T12"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940" ;
    dct:title "Tekst_750_T13"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660" ;
    dct:title "TelefonNummer_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659" ;
    dct:title "TelefonNummer_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658" ;
    dct:title "TelefonPrefiks_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657" ;
    dct:title "TelefonPrefiks_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705" ;
    dct:title "Boolean_S12"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701" ;
    dct:title "Boolean_S13"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697" ;
    dct:title "Boolean_S14"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693" ;
    dct:title "Boolean_S15"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689" ;
    dct:title "Boolean_S16"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685" ;
    dct:title "Boolean_S17"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677" ;
    dct:title "Boolean_S18"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681" ;
    dct:title "Boolean_S19"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673" ;
    dct:title "Boolean_S20"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462" ;
    dct:title "Boolean_S21"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458" ;
    dct:title "Boolean_S22"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322" ;
    dct:title "Boolean_S23"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318" ;
    dct:title "Boolean_S24"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252" ;
    dct:title "Boolean_S25"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248" ;
    dct:title "Boolean_S26"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244" ;
    dct:title "Boolean_S27"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232" ;
    dct:title "Boolean_S30"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228" ;
    dct:title "Boolean_S31"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224" ;
    dct:title "Boolean_S32"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089" ;
    dct:title "Boolean_S33"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085" ;
    dct:title "Boolean_S34"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081" ;
    dct:title "Boolean_S35"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077" ;
    dct:title "Boolean_S36"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068" ;
    dct:title "Ifrs16harforklartforskjeller"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985" ;
    dct:title "SvaralternativJaNei_S07"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331" ;
    dct:title "SvaralternativJaNei_S103"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327" ;
    dct:title "SvaralternativJaNei_S104"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323" ;
    dct:title "SvaralternativJaNei_S105"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319" ;
    dct:title "SvaralternativJaNei_S106"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315" ;
    dct:title "SvaralternativJaNei_S107"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999" ;
    dct:title "SvaralternativJaNei_S88"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995" ;
    dct:title "SvaralternativJaNei_S89"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003" ;
    dct:title "SvaralternativJaNei_S91"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213" ;
    dct:title "SvaralternativJaNei_S92"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209" ;
    dct:title "SvaralternativJaNei_S93"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205" ;
    dct:title "SvaralternativJaNei_S94"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734" ;
    dct:title "SvaralternativJaNei_S95"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730" ;
    dct:title "SvaralternativJaNei_S96"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726" ;
    dct:title "SvaralternativJaNei_S97"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722" ;
    dct:title "SvaralternativJaNei_S98"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718" ;
    dct:title "SvaralternativJaNei_S99"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467" ;
    dct:title "SvaralternativJaNei_S01"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475" ;
    dct:title "SvaralternativJaNei_S11"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673" ;
    dct:title "SvaralternativJaNei_S12"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672" ;
    dct:title "SvaralternativJaNei_S13"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671" ;
    dct:title "SvaralternativJaNei_S14"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670" ;
    dct:title "SvaralternativJaNei_S15"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669" ;
    dct:title "SvaralternativJaNei_S16"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668" ;
    dct:title "SvaralternativJaNei_S17"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667" ;
    dct:title "SvaralternativJaNei_S18"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666" ;
    dct:title "SvaralternativJaNei_S19"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466" ;
    dct:title "SvaralternativJaNei_S02"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665" ;
    dct:title "SvaralternativJaNei_S20"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664" ;
    dct:title "SvaralternativJaNei_S21"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663" ;
    dct:title "SvaralternativJaNei_S22"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662" ;
    dct:title "SvaralternativJaNei_S23"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465" ;
    dct:title "SvaralternativJaNei_S03"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655" ;
    dct:title "SvaralternativJaNei_S30"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654" ;
    dct:title "SvaralternativJaNei_S31"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653" ;
    dct:title "SvaralternativJaNei_S32"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652" ;
    dct:title "SvaralternativJaNei_S33"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651" ;
    dct:title "SvaralternativJaNei_S34"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646" ;
    dct:title "SvaralternativJaNei_S42"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187" ;
    dct:title "SvaralternativJaNei_S39"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464" ;
    dct:title "SvaralternativJaNei_S04"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186" ;
    dct:title "SvaralternativJaNei_S40"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185" ;
    dct:title "SvaralternativJaNei_S41"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184" ;
    dct:title "SvaralternativJaNei_S43"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183" ;
    dct:title "SvaralternativJaNei_S44"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012" ;
    dct:title "SvaralternativJaNei_S45"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011" ;
    dct:title "SvaralternativJaNei_S46"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463" ;
    dct:title "SvaralternativJaNei_S05"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007" ;
    dct:title "SvaralternativJaNei_S50"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169" ;
    dct:title "SvaralternativJaNei_S51"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168" ;
    dct:title "SvaralternativJaNei_S52"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167" ;
    dct:title "SvaralternativJaNei_S53"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166" ;
    dct:title "SvaralternativJaNei_S54"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165" ;
    dct:title "SvaralternativJaNei_S55"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164" ;
    dct:title "SvaralternativJaNei_S56"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179" ;
    dct:title "SvaralternativJaNei_S58"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178" ;
    dct:title "SvaralternativJaNei_S59"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462" ;
    dct:title "SvaralternativJaNei_S06"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176" ;
    dct:title "SvaralternativJaNei_S60"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177" ;
    dct:title "SvaralternativJaNei_S61"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161" ;
    dct:title "SvaralternativJaNei_S62"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162" ;
    dct:title "SvaralternativJaNei_S63"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160" ;
    dct:title "SvaralternativJaNei_S64"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159" ;
    dct:title "SvaralternativJaNei_S65"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175" ;
    dct:title "SvaralternativJaNei_S66"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174" ;
    dct:title "SvaralternativJaNei_S67"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314" ;
    dct:title "SvaralternativJaNei_S86"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313" ;
    dct:title "SvaralternativJaNei_S87"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87/guid> .

<http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029" ;
    dct:title "Verdipapirutsteder"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/DataTypeegenskap/aksjeutsteder/446028>,
        <http://seres.no/guid/Finanstilsynet/DataTypeegenskap/grunnfondsbevisutsteder/446026>,
        <http://seres.no/guid/Finanstilsynet/DataTypeegenskap/obligasjonsutsteder/446027> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282" ;
    dct:title "Adresse"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/adresselinje1/660280>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/postnummer/660281>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/poststed/660279> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869" ;
    dct:title "AlternativeResultatmaal"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/antallAlternativeResultatmål/664867>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/benytterAlternativeResultatmål/664868>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/endretAlternativeResultatmål/664865>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/nyeAlternativeResultatmål/664863>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/presentererAlternativeResultatmål/664866>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/sluttetAlternativeResultatm/664864> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989" ;
    dct:title "AndreForhold"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/bruddDispensasjonLånebetingelser/445987>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/endringRegnskapsprinppEndringStandard/664861>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/endringRegnskapsprinsippFrivillig/664862>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/feilÅrsregnskapDelårsregnskap/445984>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fraveketKravIFRS/445983>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/inntektvekstOver25/445986>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/investeringerOver50/600183>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/konsolidertDatterselskap/600184>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/omarbeidelseResultatBalanseTall/600185>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/tapRettssak/445985> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957" ;
    dct:title "Egenkapital"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/andelUnder10/445956>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/egenkapitalAksjeeierMorforetak/445954>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/korrigertNegativ/445955> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999" ;
    dct:title "ForpliktelseAvsetning"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/over10/445998>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/over50/445997> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887" ;
    dct:title "Ifrs15vurderinger"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771891>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklar/771890>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsettelsetransaksjonspris/771898>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fordelingtransaksjonspris/771897>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/identifiseringleveringsforpliktelser/771899>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktskostnader/771892>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/metodebrukt/771894>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/oppfyllelseleveringsforpliktelsertid/771896>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/oppfyllelseleveringsforpliktelsertidspunkt/771895>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/prinsipalagent/771893> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901" ;
    dct:title "Ifrs15"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittforklaringendringer/771956>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittforklaringendringerforklaring/771955>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittinngåendeutgående/771907>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittinngåendeutgåendeforklaring/771906>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittopplysninger/771905>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergittopplysningerforklaring/771904>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergitttilstrekkeligeopplysninger/771969>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ergitttilstrekkeligeopplysningerforklaring/771968>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjordriftsinntektforklaring/771909>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortanvender/771908>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortanvenderforklaring/771910>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/erredegjortnårdriftsinntekt/771903>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15kategorier/771957>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15vurderinger/771900> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966" ;
    dct:title "Ifrs15kategorier"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/andre/771959>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklar/771958>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/geografiskområde/771964>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktensløpetid/771962>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kontraktstype/771967>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/markedkundetype/771963>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/salgskanaler/771960>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/tidspunktoverføring/771961>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/typevaretjeneste/771965> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886" ;
    dct:title "Ifrs16"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterleietaker/771981>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterutleiereksterne/771983> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971" ;
    dct:title "Ifrs16leiekontrakterleietaker"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/ifrs16harforklartforskjeller/772063>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/leiekontrakterinneholderleiekomponenter/771979>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurderinger/771970>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurdertikkeeffekt/771976> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938" ;
    dct:title "Ifrseffekt"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/forsikringsbokføring/771934>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ingeneffekt/771933>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/klassifiseringfinansielleinstrument/771937>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/målingandre/771935>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/målingkundefordringer/771936> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917" ;
    dct:title "Ifrs16vurdertikkeeffekt"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771912>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklaring/771911>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/balansesum/771915>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ebitda/771913>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/ikkeaktuelt/771916>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/sumforpliktelser/771914> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943" ;
    dct:title "Ifrs9"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrseffekt/771942> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941" ;
    dct:title "Ifrsandre"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/anginote/771940>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/haddeias1257avesentligeffekt/771949>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/innføringifric23vesentligeffekt/771948> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929" ;
    dct:title "Ifrs16vurderinger"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/771924>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/annetforklaring/771923>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsetteleieperioden/771927>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fastsettelånerente/771925>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/identifisereleieavtale/771928>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/målingleiebetalinger/771926> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946" ;
    dct:title "ImmateriellEiendel"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver10/445944>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver50/445943>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/immateriellEiendel/445945>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utsattSkattefordel/445942>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utviklingsutgift/445941> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850" ;
    dct:title "Innsender"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/foretaksnavn/664848>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/lEI-nummer/771885>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/organisasjonsnummer/664849>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/adresse/664847> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652" ;
    dct:title "Kontaktperson1"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/epost/637651>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/navn/637650>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonPrefiks/637648>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonnr/637649> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647" ;
    dct:title "Kontaktperson2"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/epost/637646>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/navn/637645>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonPrefiks/637643>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/telefonnr/637644> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910" ;
    dct:title "Kontantstroem"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/driftsaktivitetOverstigerÅrsresultat/445909>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/investeringsaktivitetOverstigerÅrsresultat/445908> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974" ;
    dct:title "MarkedsverdibasertEiendel"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/endringGjeldOver5/664859>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/finansielleInstrumenterUnotert/445971>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/gevinstTapFinansielleInstrumenterOver25/445969>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/gevinstTapFinansielleInstrumenterOver5/445970>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/gjeldVirkeligVerdi/664860>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/sikringsbokføring/445972>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendeler/445968>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendelerOver10/445967>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utoverFinansielleEiendelerOver50/445966> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929" ;
    dct:title "Nedskriving"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/PBOver1/445927>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/nedskriving/445928>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattNegativt/445924>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattOver25/445925>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/resultatFørSkattOver5/445926> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936" ;
    dct:title "Organisasjonsforhold"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/aksjebasertInsentivordning/445930>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/eksternRevisorSkiftet/445931>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/etiskRetningslinje/445935>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/styrelederToppledelseSkiftet/445934> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925" ;
    dct:title "Periode"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/periodetype/664924> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846" ;
    dct:title "Rapportering"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson1/664845>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson2/664844>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/periode/664926>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapporteringsregisteret/664900> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291" ;
    dct:title "Rapporteringsregisteret"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/rapporteringsId/660290> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940" ;
    dct:title "Regnskap"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/konsernregnskap/445938>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/regnskapsspråk/445937>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/regnskapsår/445939>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/spesifiser/664854> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072" ;
    dct:title "RentepapirerType"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/ansvarlige/665145>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/bankogfinans/665148>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/coveredbondbenchmark/665141>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/fondsobligasjoner/665143>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/groenneobligasjoner/665140>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/industrioghandel/665146>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kommuneogfylke/665149>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/konvertible/665144>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kredittforetak/665147>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/obligasjonermedfortrinnsrett/665142>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/sertifikater/665151>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/statslaan/665152>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/storlaan/665150> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014" ;
    dct:title "Restruktureringsavsetning"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/over25FørSkatt/446010>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/over5FørSkatt/446011>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/restruktureringsavsetning/446012> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965" ;
    dct:title "Resultatpost"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/negativtDriftsresultat/445961>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/negativtÅrsresultat/445959>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontantstrøm/445962>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/nedskriving/445958> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181" ;
    dct:title "Revisjonsberetning"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetning/600180>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetningModifisering/600178>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsberetningPresisering/600179> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409" ;
    dct:title "Revisjonsutvalg"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/antallMøterRevisorOgRevisjonsutvalg/622407>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/diskutertKamAvslutning/664857>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/diskutertKamPlanlegging/664858>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/eksternRevisorPåpektSvakhetSystemKontrollRisikostyring/622406>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/etablertRevisjonsutvalg/622408>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/inntruffetForholdTrusselRevisorUavhengighet/622401>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/påserRevisjonsutvalgetOppfølging/622405>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonsutvalgRepresentert/622402>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/uenighetRevisjonsutvalgetEksternRevisorInternKontroll/622404>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/undersøkelserFølgeOppRevisor/622400>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgFaktorer/622399>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgKriterier/622403> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389" ;
    dct:title "RevisjonsutvalgFaktorer"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/annenMåte/622379>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/brukEksperterBransjeerfaring/622386>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kvalitetNyhetsbrev/622382>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kvalitetPresentasjonBrev/622383>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/medgåttTid/622388>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/personellRevisjonsteamet/622385>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/referanser/622380>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/sammensetningTimeforbruk/622387>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/tidsriktigLevering/622384>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/åpenhetsrapport/622381> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398" ;
    dct:title "RevisjonsutvalgKriterier"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/annet/622390>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kapasitetKompetanse/622395>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/kontinuitet/622392>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/pris/622397>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/relasjoner/622393>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/renomme/622394>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/revisjonskvalitet/622396>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/rotasjonRevisjonsselskap/622391> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982" ;
    dct:title "Skattefordel"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordeOver5/445980>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordel/445981>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utsattSkattefordelOver25/445979> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018" ;
    dct:title "Utviklingsutgift"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtGoodwill/600742>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver10Egenkapital/446016>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/balanseførtOver50Egenkapital/446015> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923" ;
    dct:title "Virksomhetssammenslutninger"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/bruttoEndringTotaleEiendelerOver10/445921>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/bruttoEndringTotaleEiendelerOver25/445920>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/negativGoodwill/600182>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utstederOvertakerEllerOvertatt/445922> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975" ;
    dct:title "Ifrs16leiekontrakterutleiereksterne"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/fordklarendringer/771994>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/harleiekontrakter/771974>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/leiekontrakterinneholder/771973>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/mestkrevendevurdering/771982> .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953" ;
    dct:title "RapportKRT-1003"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/OBX-utvalg/445915>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/aksjeStørstOppgangNedgang/445914>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/bransje/445917>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/børsverdiForetak/445913>,
        <http://seres.no/guid/Finanstilsynet/Dataegenskap/utstedertype/445918>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/regnskap/445951>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rentepapirertype/665073> .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009" ;
    dct:title "SkjemainnholdKRT-1003"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/alternativeResultatmål/664901>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/andreForhold/446000>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/egenkapital/446002>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/forpliktelseAvsetning/446004>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15/771902>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16/771888>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs9/771947>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrsandre/771950>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/immatriellEiendel/446005>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/markedsverdibasertEiendel/446006>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/organisasjonsforhold/446008>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/restruktureringsavsetning/446003>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/resultatpost/446007>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsberetning/600187>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalg/622454>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/virksomhetssammenslutninger/446001> .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853" ;
    dct:title "Rapport"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/maalform/665679>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/innsender/664852>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapportering/664851> .

<http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757" ;
    dct:title "RegnskapAr-17102"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494" ;
    dct:title "ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567" ;
    dct:title "ArsresultatNegativSisteToAr-23744"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529" ;
    dct:title "AvsetningRestrukturering-23767"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638" ;
    dct:title "AvsetningRestrukturering25ResultatForSkatt-23769"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495" ;
    dct:title "AvsetningRestrukturering5ResultatForSkatt-23768"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598" ;
    dct:title "AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452" ;
    dct:title "AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506" ;
    dct:title "DriftsresultatNegativSisteToAr-23742"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448" ;
    dct:title "EgenkapitalAndel10-23775"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616" ;
    dct:title "EgenkapitalKorrigertNegativ-23776"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540" ;
    dct:title "EiendelerImmaterielle10AvEgenkapital-23759"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571" ;
    dct:title "EiendelerImmaterielle50AvEgenkapital-23760"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460" ;
    dct:title "EiendelerImmaterielleAndre-23758"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485" ;
    dct:title "EnhetAksjerStorstKursoppgangKursnedgang-23724"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580" ;
    dct:title "EnhetBorsnotertOBXIndeksutvalg-23723"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572" ;
    dct:title "EnhetBransje-23719"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488" ;
    dct:title "EnhetEksternRevisorSkifteSisteToAr-23729"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602" ;
    dct:title "EnhetEtiskeRetningslinjerOffentliggjorte-23725"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570" ;
    dct:title "EnhetKonsernregnskap-23722"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611" ;
    dct:title "EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475" ;
    dct:title "FinansielleInstrumenterUnoterteEidUtstedt-23752"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532" ;
    dct:title "GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537" ;
    dct:title "GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526" ;
    dct:title "IFRSKravFraveketKravMedHensikt-31961"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590" ;
    dct:title "Inntektsvekst25SisteAr50TreSisteAr-23779"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474" ;
    dct:title "InsentivordningAksjebasert-23730"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510" ;
    dct:title "KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523" ;
    dct:title "KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610" ;
    dct:title "LanebetingelserBruddDispensasjon-23778"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478" ;
    dct:title "Nedskrivninger-23745"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484" ;
    dct:title "Nedskrivninger25ResultatForSkatt-23748"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562" ;
    dct:title "Nedskrivninger5ResultatForSkatt-23747"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560" ;
    dct:title "NedskrivningerNegativResultatForSkatt-23749"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441" ;
    dct:title "Regnskapsstandard-31959"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591" ;
    dct:title "SikringsbokfoeringFinansielleInstrumenter-23751"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453" ;
    dct:title "SkattesakerVesentligeTapteSisteToAr-23780"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473" ;
    dct:title "UtsattSkattefordel-23761"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535" ;
    dct:title "UtsattSkattefordelResultateffekt25ResultatForSkatt-23763"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490" ;
    dct:title "UtsattSkattefordelResultateffekt5ResultatForSkatt-23762"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566" ;
    dct:title "UtviklingskostnaderBalanseforte10AvEgenkapital-23773"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636" ;
    dct:title "UtviklingskostnaderBalanseforte50AvEgenkapital-23774"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588" ;
    dct:title "VerdsettelsePrisBok1-23746"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746/guid> .

<http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150" ;
    dct:title "EgenkapitalMorforetaketsAksjeeiere-34067"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067/guid> .

<http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170" ;
    dct:title "ForetakBorsverdi-34065"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065/guid> .

<http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128" ;
    dct:title "Grunnfondsbevis-34215"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215/guid> .

<http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133" ;
    dct:title "Obligasjon-34214"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214/guid> .

<http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215" ;
    dct:title "VerdipapirutstederAksje-34213"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211" ;
    dct:title "RevisjonsberetningUtenAvvik-34066"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066/guid> .

<http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089" ;
    dct:title "UtstederIdentifisertOvertakerOverdrager-34068"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068/guid> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag" ;
    dct:title "Arbeidsgiveravgiftsgrunnlag"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/avgiftsgrunnlagBeloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/beregningskodeForArbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/prosentsatsForAvgiftsberegning>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag/sone> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone" ;
    dct:title "Arbeidsgiveravgiftsone"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift" ;
    dct:title "BeregningskodeForArbeidsgiveravgift"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat" ;
    dct:title "BilOgBaat"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antall>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antallKilometer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/antallReiser>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/arbeidsforholdId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/beloep>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/beskrivelse>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/bilregistreringsnummer>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erAnnenBil>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erBilUtenforStandardregelen>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/erBilpool>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/fordel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/heravAntallKilometerMellomHjemOgArbeid>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/inngaarIGrunnlagForTrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/listeprisForBil>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/personklassifiseringAvBilbruker>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/skatteOgAvgiftsregel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/sluttdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/startdatoOpptjeningsperiode>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/utloeserArbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent" ;
    dct:title "Grunnlagsprosent"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske" ;
    dct:title "GrunnlagsprosentForUtenlandske"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold" ;
    dct:title "SpesielleInntjeningsforhold"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode" ;
    dct:title "Landkode"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse" ;
    dct:title "Naeringsinntektsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator" ;
    dct:title "NorskIdentifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall" ;
    dct:title "AArstall"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse" ;
    dct:title "PensjonEllerTrygdebeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji" ;
    dct:title "PersontypeForReiseKostLosji"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode" ;
    dct:title "Periode"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode/sluttdato>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode/startdato> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall" ;
    dct:title "BeloepSomHeltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon" ;
    dct:title "TekstMedRestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse" ;
    dct:title "Loennsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon" ;
    dct:title "Spesifikasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/erOpptjentPaaHjelpefartoey>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/erOpptjentPaaKontinentalsokkel>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/opptjeningsland>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon/skattemessigBosattILand> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall" ;
    dct:title "Desimaltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel" ;
    dct:title "Fordel"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel" ;
    dct:title "SkatteOgAvgiftsregel"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall" ;
    dct:title "Heltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator" ;
    dct:title "Identifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep" ;
    dct:title "Beloep"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk" ;
    dct:title "Boolsk"@nb ;
    xsd:anyURI xsd:boolean .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato" ;
    dct:title "Dato"@nb ;
    xsd:anyURI xsd:date .

<https://altinn.fellesdatakatalog.digdir.no#String> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#String" ;
    dct:title "String"@en ;
    xsd:anyURI xsd:string ."""
