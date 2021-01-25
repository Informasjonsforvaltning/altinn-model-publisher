"""Altinn catalog test data."""
altinn_catalog_turtle = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.altinn.no/models/altinn> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "Altinn informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/4711-5466>,
        <https://altinn.fellesdatakatalog.digdir.no/models/4942-sofus> .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid" ;
    dct:title "DatoTid"@nb ;
    xsd:anyURI xsd:dateTime .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator" ;
    dct:title "Identifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Melding> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Melding" ;
    dct:title "Melding"@nb .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall" ;
    dct:title "Aarstall"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori" ;
    dct:title "Adressebrukskategori"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall" ;
    dct:title "Antall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker> a ns1:Attribute ;
    dct:title "oppholdSomArbeidstaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende> a ns1:Attribute ;
    dct:title "oppholdSomSelvstendigNaeringsdrivende"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse> a ns1:Attribute ;
    dct:title "arbeidskontraktreferanse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet" ;
    dct:title "Arbeidsstedsbeliggenhet"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidsopphold> a ns1:Attribute ;
    dct:title "arbeidsopphold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidstaker> a ns1:Attribute ;
    dct:title "arbeidstaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/identifikasjon> a ns1:Attribute ;
    dct:title "identifikasjon"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/kontaktinformasjon> a ns1:Attribute ;
    dct:title "kontaktinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/norskPersonidentifikator> a ns1:Attribute ;
    dct:title "norskPersonidentifikator"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> a ns1:Attribute ;
    dct:title "referanseTilIdentifikasjonsdokument"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall" ;
    dct:title "BeloepSomHeltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk" ;
    dct:title "Boolsk"@nb ;
    xsd:anyURI xsd:boolean .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato" ;
    dct:title "Dato"@nb ;
    xsd:anyURI xsd:date .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dnummer" ;
    dct:title "Dnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Epostadresse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Epostadresse" ;
    dct:title "Epostadresse"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 254 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Filtype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Filtype" ;
    dct:title "Filtype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Foedselsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Foedselsnummer" ;
    dct:title "Foedselsnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/navn> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/oppholdsadresse> a ns1:Attribute ;
    dct:title "oppholdsadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresse> a ns1:Attribute ;
    dct:title "postadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresseIUtlandet> a ns1:Attribute ;
    dct:title "postadresseIUtlandet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall" ;
    dct:title "Heltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi> a ns1:Attribute ;
    dct:title "dokumentkopi"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/skannetDokument> a ns1:Attribute ;
    dct:title "skannetDokument"@nb ;
    xsd:maxOccurs 1 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype" ;
    dct:title "Identifikasjonsdokumenttype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype" ;
    dct:title "Identifikatortype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn" ;
    dct:title "Kjoenn"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer" ;
    dct:title "Kommunenummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/matrikkeladresse> a ns1:Attribute ;
    dct:title "matrikkeladresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/postboksadresse> a ns1:Attribute ;
    dct:title "postboksadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/utenlandskPostadresse> a ns1:Attribute ;
    dct:title "utenlandskPostadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/vegadresse> a ns1:Attribute ;
    dct:title "vegadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode" ;
    dct:title "Landkode"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3" ;
    dct:title "LandkodeISOAlpha3"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 3 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer> a ns1:Attribute ;
    dct:title "matrikkelnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn" ;
    dct:title "Navn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 200 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse> a ns1:Attribute ;
    dct:title "matrikkeladresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> a ns1:Attribute ;
    dct:title "vegadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn" ;
    dct:title "Organisasjonsnavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 175 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer" ;
    dct:title "Organisasjonsnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer" ;
    dct:title "Partsnummer"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag> a ns1:Attribute ;
    dct:title "dokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse> a ns1:Attribute ;
    dct:title "identitetsbekreftelse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag> a ns1:Attribute ;
    dct:title "manglendeDokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype" ;
    dct:title "Personidentifikatortype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer" ;
    dct:title "Postnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger" ;
    dct:title "SoeknadOmSkattekortForUtenlandskBorger"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/arbeidstakerinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersKontaktinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/arbeidstakerinformasjon> a ns1:Attribute ;
    dct:title "arbeidstakerinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersKontaktinformasjon> a ns1:Attribute ;
    dct:title "innsendersKontaktinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4000 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer" ;
    dct:title "Telefonnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer> a ns1:Attribute ;
    dct:title "adressenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> .

<http://seres.no/guid/NAV/DataTypeegenskap/data/634499> a ns1:Attribute ;
    dct:title "data"@nb ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/data/634511> .

<http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> a ns1:Attribute ;
    dct:title "indikatordata"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500> .

<http://seres.no/guid/NAV/Dataegenskap/dato/634644> a ns1:Attribute ;
    dct:title "dato"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/dato/634507> .

<http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643> a ns1:Attribute ;
    dct:title "geografiskOmraadeMedIndikatordata"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503> .

<http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513" ;
    dct:title "Maalekort_M"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513/skjema> .

<http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513/skjema> a ns1:Attribute ;
    dct:title "skjema"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Meldingsdel/skjema/634646> .

<http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> a ns1:Attribute ;
    dct:title "fagsystem"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498> .

<https://altinn.fellesdatakatalog.digdir.no/models/4711-5466> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/889640782> ;
    dct:title "Målekortskjema "@nb ;
    ns1:containsModelElement <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid>,
        <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator>,
        <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Melding>,
        <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst>,
        <http://seres.no/guid/NAV/Datakomplekstype/data/634511>,
        <http://seres.no/guid/NAV/Datakomplekstype/dato/634507>,
        <http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503>,
        <http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500>,
        <http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498>,
        <http://seres.no/guid/NAV/Meldingsdel/skjema/634646>,
        <http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513> .

<https://altinn.fellesdatakatalog.digdir.no/models/4942-sofus> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "RF-1209  Søknad om skattekort for utenlandske borgere"@nb ;
    ns1:containsModelElement <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Epostadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Filtype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Foedselsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/889640782> a foaf:Agent ;
    foaf:name "Arbeids- og velferdsetaten"@nb .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> a foaf:Agent ;
    foaf:name "Skatteetaten"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer" ;
    dct:title "Adressenummer"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge" ;
    dct:title "ArbeidsoppholdINorge"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker" ;
    dct:title "ArbeidsoppholdSomArbeidstaker"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende" ;
    dct:title "ArbeidsoppholdSomSelvstendigNaeringsdrivende"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon" ;
    dct:title "Arbeidstakerinformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidsopphold>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/identifikasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/kontaktinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/norskPersonidentifikator>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument" ;
    dct:title "BekreftelsePaaManglendeIdentifikasjonsdokument"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet" ;
    dct:title "BekreftetIdentitet"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat" ;
    dct:title "Folkeregisterkandidat"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/navn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/oppholdsadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresseIUtlandet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument" ;
    dct:title "Identifikasjonsdokument"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi" ;
    dct:title "Identifikasjonsdokumentkopi"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/skannetDokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse" ;
    dct:title "InternasjonalAdresse"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer" ;
    dct:title "Matrikkelnummer"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse" ;
    dct:title "OffisiellOppholdsadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon" ;
    dct:title "Personidentifikasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator" ;
    dct:title "Personidentifikator"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn" ;
    dct:title "Personnavn"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse" ;
    dct:title "Postboksadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> .

<http://seres.no/guid/NAV/Datakomplekstype/data/634511> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/data/634511" ;
    dct:title "Data"@nb .

<http://seres.no/guid/NAV/Datakomplekstype/dato/634507> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/dato/634507" ;
    dct:title "Dato"@nb .

<http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503" ;
    dct:title "GeografiskOmraadeMedIndikatordata"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> .

<http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500" ;
    dct:title "Indikatordata"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/data/634499> .

<http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498" ;
    dct:title "Fagsystem"@nb .

<http://seres.no/guid/NAV/Meldingsdel/skjema/634646> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Meldingsdel/skjema/634646" ;
    dct:title "Skjema"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/Dataegenskap/dato/634644>,
        <http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643>,
        <http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse" ;
    dct:title "Kontaktadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/postboksadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/utenlandskPostadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon" ;
    dct:title "Kontaktinformasjon"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse" ;
    dct:title "Matrikkeladresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed" ;
    dct:title "Poststed"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse" ;
    dct:title "Vedleggsreferanse"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse" ;
    dct:title "Vegadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> .

<https://altinn.fellesdatakatalog.digdir.no#String> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#String" ;
    dct:title "String"@en ;
    xsd:anyURI xsd:string ."""
