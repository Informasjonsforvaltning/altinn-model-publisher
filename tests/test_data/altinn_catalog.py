"""Altinn catalog test data."""
altinn_catalog_turtle = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix ns2: <http://rdf-vocabulary.ddialliance.org/xkos#> .
@prefix ns3: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.altinn.no/models/altinn> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "Altinn informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/4711-5466>,
        <https://altinn.fellesdatakatalog.digdir.no/models/4942-sofus> .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Melding> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Melding" ;
    dct:title "Melding"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer/husbokstav> a ns1:Attribute ;
    dct:title "husbokstav"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer/husnummer> a ns1:Attribute ;
    dct:title "husnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ankomstdatoTilNorge> a ns1:Attribute ;
    dct:title "ankomstdatoTilNorge"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/antallArbeidsdager> a ns1:Attribute ;
    dct:title "antallArbeidsdager"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/arbeidsstedsbeliggenhet> a ns1:Attribute ;
    dct:title "arbeidsstedsbeliggenhet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/erDagEllerUkependler> a ns1:Attribute ;
    dct:title "erDagEllerUkependler"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/foersteArbeidsdag> a ns1:Attribute ;
    dct:title "foersteArbeidsdag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/foersteOppholdskommune> a ns1:Attribute ;
    dct:title "foersteOppholdskommune"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker> a ns1:Attribute ;
    dct:title "oppholdSomArbeidstaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende> a ns1:Attribute ;
    dct:title "oppholdSomSelvstendigNaeringsdrivende"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/planlagtUtreisedatoFraNorge> a ns1:Attribute ;
    dct:title "planlagtUtreisedatoFraNorge"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgiverDekkerKostLosjiBesoeksreise> a ns1:Attribute ;
    dct:title "arbeidsgiverDekkerKostLosjiBesoeksreise"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgivernavn> a ns1:Attribute ;
    dct:title "arbeidsgivernavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgiversOrganisasjonsnummer> a ns1:Attribute ;
    dct:title "arbeidsgiversOrganisasjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse> a ns1:Attribute ;
    dct:title "arbeidskontraktreferanse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/forventetLoennsinntekt> a ns1:Attribute ;
    dct:title "forventetLoennsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende/enkeltpersonforetaketsOrganisasjonsnummer> a ns1:Attribute ;
    dct:title "enkeltpersonforetaketsOrganisasjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende/forventetNaeringsinntekt> a ns1:Attribute ;
    dct:title "forventetNaeringsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/partsnummer> a ns1:Attribute ;
    dct:title "partsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> a ns1:Attribute ;
    dct:title "referanseTilIdentifikasjonsdokument"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument/identifikasjonsdokumentMangler> a ns1:Attribute ;
    dct:title "identifikasjonsdokumentMangler"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/bekreftersLand> a ns1:Attribute ;
    dct:title "bekreftersLand"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/identitetErBekreftet> a ns1:Attribute ;
    dct:title "identitetErBekreftet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/organisasjonsidentifikator> a ns1:Attribute ;
    dct:title "organisasjonsidentifikator"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/organisasjonsnavn> a ns1:Attribute ;
    dct:title "organisasjonsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedeland> a ns1:Attribute ;
    dct:title "foedeland"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedested> a ns1:Attribute ;
    dct:title "foedested"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedselsdato> a ns1:Attribute ;
    dct:title "foedselsdato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedselsdatoErKjent> a ns1:Attribute ;
    dct:title "foedselsdatoErKjent"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/harUkjentOppholdsadresse> a ns1:Attribute ;
    dct:title "harUkjentOppholdsadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/kjoenn> a ns1:Attribute ;
    dct:title "kjoenn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/statsborgerskap> a ns1:Attribute ;
    dct:title "statsborgerskap"@nb ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi> a ns1:Attribute ;
    dct:title "dokumentkopi"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/gyldigFra> a ns1:Attribute ;
    dct:title "gyldigFra"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/gyldigTil> a ns1:Attribute ;
    dct:title "gyldigTil"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/identifikasjonsdokumentnummer> a ns1:Attribute ;
    dct:title "identifikasjonsdokumentnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/identifikasjonsdokumenttype> a ns1:Attribute ;
    dct:title "identifikasjonsdokumenttype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/utstederland> a ns1:Attribute ;
    dct:title "utstederland"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/utstedernavn> a ns1:Attribute ;
    dct:title "utstedernavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/rettkjentKopiBekreftet> a ns1:Attribute ;
    dct:title "rettkjentKopiBekreftet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/skannetDokument> a ns1:Attribute ;
    dct:title "skannetDokument"@nb ;
    xsd:maxOccurs 1 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/administrativEnhet> a ns1:Attribute ;
    dct:title "administrativEnhet"@nb ;
    xsd:maxOccurs 6 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressebrukskategori> a ns1:Attribute ;
    dct:title "adressebrukskategori"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressenavn> a ns1:Attribute ;
    dct:title "adressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressenummer> a ns1:Attribute ;
    dct:title "adressenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/boenhet> a ns1:Attribute ;
    dct:title "boenhet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/byEllerStedsnavn> a ns1:Attribute ;
    dct:title "byEllerStedsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/bygning> a ns1:Attribute ;
    dct:title "bygning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/coAdressenavn> a ns1:Attribute ;
    dct:title "coAdressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/distriktsnavn> a ns1:Attribute ;
    dct:title "distriktsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/etasjenummer> a ns1:Attribute ;
    dct:title "etasjenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/landkode> a ns1:Attribute ;
    dct:title "landkode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/postboks> a ns1:Attribute ;
    dct:title "postboks"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/postkode> a ns1:Attribute ;
    dct:title "postkode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/erKlientadresse> a ns1:Attribute ;
    dct:title "erKlientadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/epostadresse> a ns1:Attribute ;
    dct:title "epostadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Epostadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/mobiltelefonummer> a ns1:Attribute ;
    dct:title "mobiltelefonummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/navn> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/smsNummer> a ns1:Attribute ;
    dct:title "smsNummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/telefonnummer> a ns1:Attribute ;
    dct:title "telefonnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/adressetilleggsnavn> a ns1:Attribute ;
    dct:title "adressetilleggsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/bruksenhetsnummer> a ns1:Attribute ;
    dct:title "bruksenhetsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/coAdressenavn> a ns1:Attribute ;
    dct:title "coAdressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkeladressenavn> a ns1:Attribute ;
    dct:title "matrikkeladressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer> a ns1:Attribute ;
    dct:title "matrikkelnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/undernummer> a ns1:Attribute ;
    dct:title "undernummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/bruksnummer> a ns1:Attribute ;
    dct:title "bruksnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/festenummer> a ns1:Attribute ;
    dct:title "festenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/gaardsnummer> a ns1:Attribute ;
    dct:title "gaardsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/kommunenummer> a ns1:Attribute ;
    dct:title "kommunenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/seksjonsnummer> a ns1:Attribute ;
    dct:title "seksjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/erKlientadresse> a ns1:Attribute ;
    dct:title "erKlientadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse> a ns1:Attribute ;
    dct:title "matrikkeladresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/oppholdsadressedato> a ns1:Attribute ;
    dct:title "oppholdsadressedato"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> a ns1:Attribute ;
    dct:title "vegadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag> a ns1:Attribute ;
    dct:title "dokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identifikasjonsnummer> a ns1:Attribute ;
    dct:title "identifikasjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identifikasjonsnummertype> a ns1:Attribute ;
    dct:title "identifikasjonsnummertype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse> a ns1:Attribute ;
    dct:title "identitetsbekreftelse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag> a ns1:Attribute ;
    dct:title "manglendeDokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/utstederland> a ns1:Attribute ;
    dct:title "utstederland"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/utstedernavn> a ns1:Attribute ;
    dct:title "utstedernavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator/dnummer> a ns1:Attribute ;
    dct:title "dnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator/foedselsnummer> a ns1:Attribute ;
    dct:title "foedselsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Foedselsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/etternavn> a ns1:Attribute ;
    dct:title "etternavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/fornavn> a ns1:Attribute ;
    dct:title "fornavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/mellomnavn> a ns1:Attribute ;
    dct:title "mellomnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/postboksnummer> a ns1:Attribute ;
    dct:title "postboksnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed/postnummer> a ns1:Attribute ;
    dct:title "postnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed/poststedsnavn> a ns1:Attribute ;
    dct:title "poststedsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger" ;
    dct:title "SoeknadOmSkattekortForUtenlandskBorger"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/arbeidstakerinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersKontaktinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersOrganisasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersPartsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendingsreferanse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/inntektsaar> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersOrganisasjonsnummer> a ns1:Attribute ;
    dct:title "innsendersOrganisasjonsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersPartsnummer> a ns1:Attribute ;
    dct:title "innsendersPartsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendingsreferanse> a ns1:Attribute ;
    dct:title "innsendingsreferanse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/inntektsaar> a ns1:Attribute ;
    dct:title "inntektsaar"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/filnavn> a ns1:Attribute ;
    dct:title "filnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/filtype> a ns1:Attribute ;
    dct:title "filtype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Filtype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/innsendersFilnavn> a ns1:Attribute ;
    dct:title "innsendersFilnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenavn> a ns1:Attribute ;
    dct:title "adressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer> a ns1:Attribute ;
    dct:title "adressenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressetilleggsnavn> a ns1:Attribute ;
    dct:title "adressetilleggsnavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/bruksenhetsnummer> a ns1:Attribute ;
    dct:title "bruksenhetsnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/coAdressenavn> a ns1:Attribute ;
    dct:title "coAdressenavn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/gatenummer> a ns1:Attribute ;
    dct:title "gatenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/kommunenummer> a ns1:Attribute ;
    dct:title "kommunenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> .

<http://seres.no/guid/NAV/DataTypeegenskap/aar/634506> a ns1:Attribute ;
    dct:title "aar"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

<http://seres.no/guid/NAV/DataTypeegenskap/data/634499> a ns1:Attribute ;
    dct:title "data"@nb ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/data/634511> .

<http://seres.no/guid/NAV/DataTypeegenskap/datafangst/634504> a ns1:Attribute ;
    dct:title "datafangst"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid> .

<http://seres.no/guid/NAV/DataTypeegenskap/geografiskOmraadeId/634502> a ns1:Attribute ;
    dct:title "geografiskOmraadeId"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator> .

<http://seres.no/guid/NAV/DataTypeegenskap/identifikator/634510> a ns1:Attribute ;
    dct:title "indikatorId"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator> .

<http://seres.no/guid/NAV/DataTypeegenskap/identikatorNavn/634509> a ns1:Attribute ;
    dct:title "indikatorNavn"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

<http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> a ns1:Attribute ;
    dct:title "indikatordata"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500> .

<http://seres.no/guid/NAV/DataTypeegenskap/mnd/634505> a ns1:Attribute ;
    dct:title "mnd"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

<http://seres.no/guid/NAV/DataTypeegenskap/verdi/634508> a ns1:Attribute ;
    dct:title "verdi"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

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

<http://seres.no/guid/NAV/Dataegenskap/navn/634497> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

<http://seres.no/guid/NAV/Dataegenskap/versjon/634496> a ns1:Attribute ;
    dct:title "versjon"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasSimpleType <http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> .

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
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#bosted>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#leveranse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellForretning>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellPost>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#post>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#ukjent>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#virksomhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#fastland>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#kontinentalsokkel>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#sjoe>,
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
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#annet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#diplomatpass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#foedselsmelding>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nasjonaltIdentitetskort>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#noedpass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nordiskFoererkort>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#norskUtlendingspass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#pass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#passerbrev>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#reisebevisForFlyktninger>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#schengenStandardisertOppholdskortFraNorge>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#servicePass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#spesialpass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tiltroddTredjepart>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tjenestepass>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#socialSecurityNumber>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#taxidentificationNumber>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utenlandskIdentifikasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utlendingsmyndighetenesIdentifikasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#kvinne>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#mann>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#ukjentEllerUspesifisert>,
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
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#DUFNummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#TINNummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskDnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskFoedselsnummer>,
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

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/DatoTid" ;
    dct:title "DatoTid"@nb ;
    xsd:anyURI xsd:dateTime .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Aarstall" ;
    dct:title "Aarstall"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellForretning> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellForretning" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellPost> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "offisiellForretning" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#ukjent> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#ukjent" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#leveranse> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "ukjent" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer" ;
    dct:title "Adressenummer"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer/husbokstav>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer/husnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall" ;
    dct:title "Antall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge" ;
    dct:title "ArbeidsoppholdINorge"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ankomstdatoTilNorge>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/antallArbeidsdager>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/arbeidsstedsbeliggenhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/erDagEllerUkependler>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/foersteArbeidsdag>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/foersteOppholdskommune>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/planlagtUtreisedatoFraNorge> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker" ;
    dct:title "ArbeidsoppholdSomArbeidstaker"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgiverDekkerKostLosjiBesoeksreise>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgivernavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidsgiversOrganisasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/forventetLoennsinntekt> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende" ;
    dct:title "ArbeidsoppholdSomSelvstendigNaeringsdrivende"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende/enkeltpersonforetaketsOrganisasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende/forventetNaeringsinntekt> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#fastland> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#fastland" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#kontinentalsokkel> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> ;
    ns3:notation "fastland" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#sjoe> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#sjoe" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#kontinentalsokkel> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> ;
    ns3:notation "sjoe" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon" ;
    dct:title "Arbeidstakerinformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidsopphold>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/identifikasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/kontaktinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/norskPersonidentifikator>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/partsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument" ;
    dct:title "BekreftelsePaaManglendeIdentifikasjonsdokument"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument/identifikasjonsdokumentMangler> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet" ;
    dct:title "BekreftetIdentitet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/bekreftersLand>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/identitetErBekreftet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/organisasjonsidentifikator>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet/organisasjonsnavn> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat" ;
    dct:title "Folkeregisterkandidat"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedeland>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedested>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedselsdato>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/foedselsdatoErKjent>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/harUkjentOppholdsadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/kjoenn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/navn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/oppholdsadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresseIUtlandet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/statsborgerskap> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument" ;
    dct:title "Identifikasjonsdokument"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/gyldigFra>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/gyldigTil>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/identifikasjonsdokumentnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/identifikasjonsdokumenttype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/utstederland>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/utstedernavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi" ;
    dct:title "Identifikasjonsdokumentkopi"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/rettkjentKopiBekreftet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/skannetDokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#annet> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#annet" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tiltroddTredjepart> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "annet" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#pass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#pass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#servicePass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "pass" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utenlandskIdentifikasjonsnummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utenlandskIdentifikasjonsnummer" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#socialSecurityNumber> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> ;
    ns3:notation "utenlandskIdentifikasjonsnummer" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utlendingsmyndighetenesIdentifikasjonsnummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utlendingsmyndighetenesIdentifikasjonsnummer" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#taxidentificationNumber> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> ;
    ns3:notation "utlendingsmyndighetenesIdentifikasjonsnummer" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse" ;
    dct:title "InternasjonalAdresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/administrativEnhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressebrukskategori>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/boenhet>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/byEllerStedsnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/bygning>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/coAdressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/distriktsnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/etasjenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/landkode>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/postboks>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse/postkode> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#kvinne> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#kvinne" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#mann> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> ;
    ns3:notation "kvinne" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#ukjentEllerUspesifisert> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#ukjentEllerUspesifisert" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#mann> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> ;
    ns3:notation "ukjentEllerUspesifisert" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode" ;
    dct:title "Landkode"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer" ;
    dct:title "Matrikkelnummer"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/bruksnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/festenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/gaardsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/kommunenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer/seksjonsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse" ;
    dct:title "OffisiellOppholdsadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/erKlientadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/oppholdsadressedato>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnavn" ;
    dct:title "Organisasjonsnavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 175 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon" ;
    dct:title "Personidentifikasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identifikasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identifikasjonsnummertype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/utstederland>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/utstedernavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator" ;
    dct:title "Personidentifikator"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator/dnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator/foedselsnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#TINNummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#TINNummer" ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#DUFNummer> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> ;
    ns3:notation "TINNummer" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskFoedselsnummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskFoedselsnummer" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskDnummer> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> ;
    ns3:notation "norskFoedselsnummer" ;
    ns3:topConceptOf <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn" ;
    dct:title "Personnavn"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/etternavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/fornavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn/mellomnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse" ;
    dct:title "Postboksadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/postboksnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer" ;
    dct:title "Postnummer"@nb ;
    xsd:anyURI xsd:string .

<http://seres.no/guid/NAV/Datakomplekstype/data/634511> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/data/634511" ;
    dct:title "Data"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/identifikator/634510>,
        <http://seres.no/guid/NAV/DataTypeegenskap/identikatorNavn/634509>,
        <http://seres.no/guid/NAV/DataTypeegenskap/verdi/634508> .

<http://seres.no/guid/NAV/Datakomplekstype/dato/634507> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/dato/634507" ;
    dct:title "Dato"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/aar/634506>,
        <http://seres.no/guid/NAV/DataTypeegenskap/datafangst/634504>,
        <http://seres.no/guid/NAV/DataTypeegenskap/mnd/634505> .

<http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/geografiskOmraadeMedIndikatordata/634503" ;
    dct:title "GeografiskOmraadeMedIndikatordata"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/geografiskOmraadeId/634502>,
        <http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> .

<http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Datakomplekstype/identikatordata/634500" ;
    dct:title "Indikatordata"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/DataTypeegenskap/data/634499> .

<http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Dataobjekttype/fagsystem/634498" ;
    dct:title "Fagsystem"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/Dataegenskap/navn/634497>,
        <http://seres.no/guid/NAV/Dataegenskap/versjon/634496> .

<http://seres.no/guid/NAV/Meldingsdel/skjema/634646> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Meldingsdel/skjema/634646" ;
    dct:title "Skjema"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/Dataegenskap/dato/634644>,
        <http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643>,
        <http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Identifikator" ;
    dct:title "Identifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#bosted> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#bosted" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#post> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#virksomhet> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "bosted" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#leveranse> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#leveranse" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#ukjent> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#post> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "leveranse" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellPost> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellPost" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#virksomhet> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellForretning> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "offisiellPost" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#post> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#post" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#leveranse> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#bosted> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "post" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#virksomhet> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#virksomhet" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#bosted> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori#offisiellPost> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> ;
    ns3:notation "virksomhet" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#kontinentalsokkel> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#kontinentalsokkel" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#sjoe> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet#fastland> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> ;
    ns3:notation "kontinentalsokkel" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BeloepSomHeltall" ;
    dct:title "BeloepSomHeltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#diplomatpass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#diplomatpass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#norskUtlendingspass> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#spesialpass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "diplomatpass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#foedselsmelding> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#foedselsmelding" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tiltroddTredjepart> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nordiskFoererkort> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "foedselsmelding" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nasjonaltIdentitetskort> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nasjonaltIdentitetskort" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#reisebevisForFlyktninger> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#passerbrev> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "nasjonaltIdentitetskort" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#noedpass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#noedpass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#passerbrev> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#norskUtlendingspass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "noedpass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nordiskFoererkort> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nordiskFoererkort" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#foedselsmelding> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#schengenStandardisertOppholdskortFraNorge> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "nordiskFoererkort" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#norskUtlendingspass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#norskUtlendingspass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#noedpass> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#diplomatpass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "norskUtlendingspass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#passerbrev> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#passerbrev" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nasjonaltIdentitetskort> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#noedpass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "passerbrev" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#reisebevisForFlyktninger> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#reisebevisForFlyktninger" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#schengenStandardisertOppholdskortFraNorge> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nasjonaltIdentitetskort> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "reisebevisForFlyktninger" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#schengenStandardisertOppholdskortFraNorge> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#schengenStandardisertOppholdskortFraNorge" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#nordiskFoererkort> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#reisebevisForFlyktninger> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "schengenStandardisertOppholdskortFraNorge" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#servicePass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#servicePass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tjenestepass> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#pass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "servicePass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#spesialpass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#spesialpass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#diplomatpass> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tjenestepass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "spesialpass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tiltroddTredjepart> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tiltroddTredjepart" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#annet> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#foedselsmelding> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "tiltroddTredjepart" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tjenestepass> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#tjenestepass" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#spesialpass> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype#servicePass> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> ;
    ns3:notation "tjenestepass" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#socialSecurityNumber> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#socialSecurityNumber" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utenlandskIdentifikasjonsnummer> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#taxidentificationNumber> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> ;
    ns3:notation "socialSecurityNumber" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#taxidentificationNumber> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#taxidentificationNumber" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#socialSecurityNumber> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype#utlendingsmyndighetenesIdentifikasjonsnummer> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> ;
    ns3:notation "taxidentificationNumber" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#mann> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#mann" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#ukjentEllerUspesifisert> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn#kvinne> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> ;
    ns3:notation "mann" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer" ;
    dct:title "Kommunenummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse" ;
    dct:title "Kontaktadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/erKlientadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/postboksadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/utenlandskPostadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon" ;
    dct:title "Kontaktinformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/epostadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/mobiltelefonummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/navn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/smsNummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon/telefonnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse" ;
    dct:title "Matrikkeladresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/adressetilleggsnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/bruksenhetsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/coAdressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkeladressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/undernummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Partsnummer" ;
    dct:title "Partsnummer"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#DUFNummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#DUFNummer" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#TINNummer> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskDnummer> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> ;
    ns3:notation "DUFNummer" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskDnummer> a ns1:CodeElement ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskDnummer" ;
    ns2:next <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#DUFNummer> ;
    ns2:previous <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype#norskFoedselsnummer> ;
    ns3:inScheme <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> ;
    ns3:notation "norskDnummer" .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed" ;
    dct:title "Poststed"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed/postnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed/poststedsnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse" ;
    dct:title "Vedleggsreferanse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/filnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/filtype>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse/innsendersFilnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse" ;
    dct:title "Vegadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressetilleggsnavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/bruksenhetsnummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/coAdressenavn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/gatenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/kommunenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> .

<https://altinn.fellesdatakatalog.digdir.no#String> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#String" ;
    dct:title "String"@en ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Telefonnummer" ;
    dct:title "Telefonnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Organisasjonsnummer" ;
    dct:title "Organisasjonsnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet" ;
    dct:title "Arbeidsstedsbeliggenhet"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall" ;
    dct:title "Heltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn" ;
    dct:title "Kjoenn"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3" ;
    dct:title "LandkodeISOAlpha3"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 3 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype" ;
    dct:title "Personidentifikatortype"@nb .

<http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4711/1/forms/5466/41779/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikatortype" ;
    dct:title "Identifikatortype"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Dato" ;
    dct:title "Dato"@nb ;
    xsd:anyURI xsd:date .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn" ;
    dct:title "Navn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 200 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Boolsk" ;
    dct:title "Boolsk"@nb ;
    xsd:anyURI xsd:boolean .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressebrukskategori" ;
    dct:title "Adressebrukskategori"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype> a ns1:CodeList ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumenttype" ;
    dct:title "Identifikasjonsdokumenttype"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4000 ."""
