"""Test data module."""
from datacatalogtordf import Agent, Catalog
from modelldcatnotordf.modelldcatno import InformationModel


def create_altinn_test_catalog() -> Catalog:
    """Catalog object that should be saved in an update."""
    altinn_test_catalog = Catalog()

    altinn_test_catalog.identifier = "https://www.altinn.no/models/catalog"
    altinn_test_catalog.title = {"nb": "Altinn informasjonsmodellkatalog"}
    altinn_test_catalog.publisher = "https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827"

    model_publisher = Agent()
    model_publisher.identifier = "https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076"
    model_publisher.name = {"nb": "Skatteetaten"}
    model_publisher.orgnr = "974761076"
    model_publisher.sameas = (
        "https://data.brreg.no/enhetsregisteret/api/enheter/974761076"
    )

    model_0 = InformationModel()
    model_0.identifier = "https://altinn.fellesdatakatalog.digdir.no/models/3314-245"
    model_0.title = {"nb": "Sensitive role Reporting"}

    model_1 = InformationModel()
    model_1.identifier = "https://altinn.fellesdatakatalog.digdir.no/models/3357-4166"
    model_1.title = {"nb": "A02 a-melding submission from system"}
    model_1.publisher = model_publisher

    altinn_test_catalog.models = [model_0, model_1]

    return altinn_test_catalog


test_xsd = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<xsd:schema targetNamespace="http://seres.no/xsd/StatistiskSentralbyrå/TEST" elementFormDefault="qualified" attributeFormDefault="unqualified" xmlns="http://seres.no/xsd/StatistiskSentralbyrå/TEST" xmlns:seres="http://seres.no/xsd/forvaltningsdata" xmlns:kodebib="http://kodebibliotek.brreg.no/xsd/kodebibliotek" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:import namespace="http://seres.no/xsd/forvaltningsdata" schemaLocation="seres.xsd" />
    <xsd:import namespace="http://kodebibliotek.brreg.no/xsd/kodebibliotek" schemaLocation="kodebibliotek.xsd" />
    <xsd:complexType name="Tidsrom">
        <xsd:sequence>
            <xsd:element name="uoppgittType" nillable="true" minOccurs="0" />
            <xsd:element name="fomDato" type="Dato" nillable="true" minOccurs="0" />
            <xsd:element name="tomDato" type="Dato" nillable="true" minOccurs="0" />
        </xsd:sequence>
    </xsd:complexType>
    <xsd:simpleType name="Dato">
        <xsd:restriction base="xsd:date" />
    </xsd:simpleType>
    <xsd:simpleType name="Kodeliste">
        <xsd:list itemType="Kodeliste-item" />
    </xsd:simpleType>
    <xsd:simpleType name="Kodeliste-item">
        <xsd:restriction base="xsd:string">
            <xsd:minLength value="1" />
            <xsd:maxLength value="1000" />
            <xsd:enumeration value="ITEM_0" />
            <xsd:enumeration value="ITEM_1" />
        </xsd:restriction>
    </xsd:simpleType>
    <xsd:group name="DatoGruppe">
        <xsd:sequence>
            <xsd:element name="startdato" type="Dato" nillable="true" minOccurs="0" />
        </xsd:sequence>
    </xsd:group>
    <xsd:complexType name="TidsromListe">
        <xsd:sequence>
            <xsd:element name="tidsrom" nillable="true" minOccurs="0" maxOccurs="unbounded">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="Tidsrom">
                            <xsd:anyAttribute />
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="DatoExtension">
        <xsd:simpleContent>
            <xsd:extension base="Dato">
                <xsd:attribute name="guid" type="xsd:string" use="required" fixed="http://seres.no/guid/34213/374215" />
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
</xsd:schema>"""


test_altinn_catalog_turtle = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.altinn.no/models/catalog> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "Altinn informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/2365-3442>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3314-245>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3906-3940>,
        <https://altinn.fellesdatakatalog.digdir.no/models/4711-5466>,
        <https://altinn.fellesdatakatalog.digdir.no/models/4942-sofus> .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1_RestriksjonAdresselinje1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Adresselinje1_RestriksjonAdresselinje1" ;
    dct:title "Adresselinje1_RestriksjonAdresselinje1"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 175 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon" ;
    dct:title "ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ArsresultatNegativSisteToAr-23744_Verdirestriksjon" ;
    dct:title "ArsresultatNegativSisteToAr-23744_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering-23767_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering-23767_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering25ResultatForSkatt-23769_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon" ;
    dct:title "AvsetningRestrukturering5ResultatForSkatt-23768_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon" ;
    dct:title "AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon" ;
    dct:title "AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S12_Verdirestriksjon" ;
    dct:title "Boolean_S12_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S13_Verdirestriksjon" ;
    dct:title "Boolean_S13_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S14_Verdirestriksjon" ;
    dct:title "Boolean_S14_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S15_Verdirestriksjon" ;
    dct:title "Boolean_S15_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S16_Verdirestriksjon" ;
    dct:title "Boolean_S16_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S17_Verdirestriksjon" ;
    dct:title "Boolean_S17_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S18_Verdirestriksjon" ;
    dct:title "Boolean_S18_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S19_Verdirestriksjon" ;
    dct:title "Boolean_S19_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S20_Verdirestriksjon" ;
    dct:title "Boolean_S20_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S21_Verdirestriksjon" ;
    dct:title "Boolean_S21_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S22_Verdirestriksjon" ;
    dct:title "Boolean_S22_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S23_Verdirestriksjon" ;
    dct:title "Boolean_S23_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S24_Verdirestriksjon" ;
    dct:title "Boolean_S24_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S25_Verdirestriksjon" ;
    dct:title "Boolean_S25_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S26_Verdirestriksjon" ;
    dct:title "Boolean_S26_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S27_Verdirestriksjon" ;
    dct:title "Boolean_S27_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S30_Verdirestriksjon" ;
    dct:title "Boolean_S30_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S31_Verdirestriksjon" ;
    dct:title "Boolean_S31_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S32_Verdirestriksjon" ;
    dct:title "Boolean_S32_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S33_Verdirestriksjon" ;
    dct:title "Boolean_S33_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S34_Verdirestriksjon" ;
    dct:title "Boolean_S34_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S35_Verdirestriksjon" ;
    dct:title "Boolean_S35_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Boolean_S36_Verdirestriksjon" ;
    dct:title "Boolean_S36_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/DriftsresultatNegativSisteToAr-23742_Verdirestriksjon" ;
    dct:title "DriftsresultatNegativSisteToAr-23742_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalAndel10-23775_Verdirestriksjon" ;
    dct:title "EgenkapitalAndel10-23775_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalKorrigertNegativ-23776_Verdirestriksjon" ;
    dct:title "EgenkapitalKorrigertNegativ-23776_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2" ;
    dct:title "EgenkapitalMorforetaketsAksjeeiere-34067_Heltall9-408_2"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielle10AvEgenkapital-23759_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielle50AvEgenkapital-23760_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EiendelerImmaterielleAndre-23758_Verdirestriksjon" ;
    dct:title "EiendelerImmaterielleAndre-23758_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon" ;
    dct:title "EnhetAksjerStorstKursoppgangKursnedgang-23724_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon" ;
    dct:title "EnhetBorsnotertOBXIndeksutvalg-23723_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetBransje-23719_Verdirestriksjon" ;
    dct:title "EnhetBransje-23719_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon" ;
    dct:title "EnhetEksternRevisorSkifteSisteToAr-23729_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon" ;
    dct:title "EnhetEtiskeRetningslinjerOffentliggjorte-23725_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetKonsernregnskap-23722_Verdirestriksjon" ;
    dct:title "EnhetKonsernregnskap-23722_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon" ;
    dct:title "EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S01_Verdirestriksjon" ;
    dct:title "Epost_S01_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Epost_S02_Verdirestriksjon" ;
    dct:title "Epost_S02_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon" ;
    dct:title "FinansielleInstrumenterUnoterteEidUtstedt-23752_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065_Heltall9-408_1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/ForetakBorsverdi-34065_Heltall9-408_1" ;
    dct:title "ForetakBorsverdi-34065_Heltall9-408_1"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn_RestriksjonForetaksnavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Foretaksnavn_RestriksjonForetaksnavn" ;
    dct:title "Foretaksnavn_RestriksjonForetaksnavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon" ;
    dct:title "GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon" ;
    dct:title "GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102" ;
    dct:title "Grunnfondsbevis-34215_KodelisteEttValg2Janei-4_102"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 24 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01_RestriksjonHeltall_1_S01> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S01_RestriksjonHeltall_1_S01" ;
    dct:title "Heltall_1_S01_RestriksjonHeltall_1_S01"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02_RestriksjonHeltall_1_S02> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S02_RestriksjonHeltall_1_S02" ;
    dct:title "Heltall_1_S02_RestriksjonHeltall_1_S02"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03_RestriksjonHeltall_1_S03> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S03_RestriksjonHeltall_1_S03" ;
    dct:title "Heltall_1_S03_RestriksjonHeltall_1_S03"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04_RestriksjonHeltall_1_S04> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S04_RestriksjonHeltall_1_S04" ;
    dct:title "Heltall_1_S04_RestriksjonHeltall_1_S04"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05_RestriksjonHeltall_1_S05> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S05_RestriksjonHeltall_1_S05" ;
    dct:title "Heltall_1_S05_RestriksjonHeltall_1_S05"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06_RestriksjonHeltall_1_S06> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S06_RestriksjonHeltall_1_S06" ;
    dct:title "Heltall_1_S06_RestriksjonHeltall_1_S06"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07_RestriksjonHeltall_1_S07> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S07_RestriksjonHeltall_1_S07" ;
    dct:title "Heltall_1_S07_RestriksjonHeltall_1_S07"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08_RestriksjonHeltall_1_S08> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_1_S08_RestriksjonHeltall_1_S08" ;
    dct:title "Heltall_1_S08_RestriksjonHeltall_1_S08"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01_RestriksjonHeltall_2_S01> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Heltall_2_S01_RestriksjonHeltall_2_S01" ;
    dct:title "Heltall_2_S01_RestriksjonHeltall_2_S01"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon" ;
    dct:title "IFRSKravFraveketKravMedHensikt-31961_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Ifrs16harforklartforskjeller_Verdirestriksjon" ;
    dct:title "Ifrs16harforklartforskjeller_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon" ;
    dct:title "Inntektsvekst25SisteAr50TreSisteAr-23779_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/InsentivordningAksjebasert-23730_Verdirestriksjon" ;
    dct:title "InsentivordningAksjebasert-23730_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon" ;
    dct:title "KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon" ;
    dct:title "KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LEI-nummer_Verdirestriksjon" ;
    dct:title "LEI-nummer_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/LanebetingelserBruddDispensasjon-23778_Verdirestriksjon" ;
    dct:title "LanebetingelserBruddDispensasjon-23778_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

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

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01_RestriksjonNavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S01_RestriksjonNavn" ;
    dct:title "Navn_S01_RestriksjonNavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02_RestriksjonNavn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Navn_S02_RestriksjonNavn" ;
    dct:title "Navn_S02_RestriksjonNavn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger-23745_Verdirestriksjon" ;
    dct:title "Nedskrivninger-23745_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon" ;
    dct:title "Nedskrivninger25ResultatForSkatt-23748_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon" ;
    dct:title "Nedskrivninger5ResultatForSkatt-23747_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon" ;
    dct:title "NedskrivningerNegativResultatForSkatt-23749_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214_KodelisteEttValg2JaNei-4_101> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Obligasjon-34214_KodelisteEttValg2JaNei-4_101" ;
    dct:title "Obligasjon-34214_KodelisteEttValg2JaNei-4_101"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 19 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer_RestriksjonOrganisasjonsnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Organisasjonsnummer_RestriksjonOrganisasjonsnummer" ;
    dct:title "Organisasjonsnummer_RestriksjonOrganisasjonsnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 9 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Periodetype_Verdirestriksjon" ;
    dct:title "Periodetype_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer_RestriksjonPostnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Postnummer_RestriksjonPostnummer" ;
    dct:title "Postnummer_RestriksjonPostnummer"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed_RestriksjonPoststed> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Poststed_RestriksjonPoststed" ;
    dct:title "Poststed_RestriksjonPoststed"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 35 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid_RestriksjonRapporteringsId> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Rapporteringsid_RestriksjonRapporteringsId" ;
    dct:title "Rapporteringsid_RestriksjonRapporteringsId"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 50 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102_Ar1980AretsAr-107> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapAr-17102_Ar1980AretsAr-107" ;
    dct:title "RegnskapAr-17102_Ar1980AretsAr-107"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Regnskapsstandard-31959_Verdirestriksjon" ;
    dct:title "Regnskapsstandard-31959_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/RevisjonsberetningUtenAvvik-34066_Verdirestriksjon" ;
    dct:title "RevisjonsberetningUtenAvvik-34066_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon" ;
    dct:title "SikringsbokfoeringFinansielleInstrumenter-23751_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon" ;
    dct:title "SkattesakerVesentligeTapteSisteToAr-23780_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S01_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S01_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S02_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S02_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S03_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S03_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S04_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S04_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S05_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S05_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S06_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S06_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S07_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S07_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S103_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S103_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S104_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S104_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S105_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S105_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S106_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S106_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S107_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S107_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S11_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S11_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S12_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S12_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S13_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S13_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S14_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S14_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S15_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S15_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S16_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S16_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S17_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S17_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S18_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S18_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S19_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S19_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S20_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S20_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S21_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S21_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S22_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S22_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S23_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S23_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S30_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S30_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S31_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S31_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S32_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S32_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S33_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S33_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S34_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S34_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S39_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S39_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S40_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S40_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S41_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S41_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S42_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S42_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S43_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S43_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S44_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S44_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S45_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S45_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S46_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S46_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S50_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S50_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S51_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S51_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S52_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S52_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S53_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S53_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S54_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S54_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S55_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S55_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S56_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S56_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S58_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S58_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S59_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S59_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S60_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S60_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S61_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S61_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S62_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S62_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S63_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S63_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S64_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S64_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S65_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S65_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S66_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S66_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S67_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S67_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S86_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S86_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S87_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S87_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S88_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S88_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S89_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S89_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S91_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S91_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S92_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S92_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S93_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S93_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S94_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S94_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S95_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S95_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S96_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S96_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S97_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S97_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S98_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S98_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/SvaralternativJaNei_S99_Verdirestriksjon" ;
    dct:title "SvaralternativJaNei_S99_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1_RestriksjonTekst_10_S1> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_10_S1_RestriksjonTekst_10_S1" ;
    dct:title "Tekst_10_S1_RestriksjonTekst_10_S1"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 10 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10_RestriksjonTekst_255_S10> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_255_S10_RestriksjonTekst_255_S10" ;
    dct:title "Tekst_255_S10_RestriksjonTekst_255_S10"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 255 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T01_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T01_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T02_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T02_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T03_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T03_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T04_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T04_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T05_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T05_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T06_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T06_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T07_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T07_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T08_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T08_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T09_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T09_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T10_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T10_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T11_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T11_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T12_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T12_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13_RestriksjonTekst_750> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/Tekst_750_T13_RestriksjonTekst_750" ;
    dct:title "Tekst_750_T13_RestriksjonTekst_750"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 750 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01_RestriksjonTelefon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S01_RestriksjonTelefon" ;
    dct:title "TelefonNummer_S01_RestriksjonTelefon"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02_RestriksjonTelefon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonNummer_S02_RestriksjonTelefon" ;
    dct:title "TelefonNummer_S02_RestriksjonTelefon"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 20 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01_RestriksjonTelefonPrefiks> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S01_RestriksjonTelefonPrefiks" ;
    dct:title "TelefonPrefiks_S01_RestriksjonTelefonPrefiks"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02_RestriksjonTelefonPrefiks> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/TelefonPrefiks_S02_RestriksjonTelefonPrefiks" ;
    dct:title "TelefonPrefiks_S02_RestriksjonTelefonPrefiks"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 4 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordel-23761_Verdirestriksjon" ;
    dct:title "UtsattSkattefordel-23761_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon" ;
    dct:title "UtsattSkattefordelResultateffekt25ResultatForSkatt-23763_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon" ;
    dct:title "UtsattSkattefordelResultateffekt5ResultatForSkatt-23762_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon" ;
    dct:title "UtstederIdentifisertOvertakerOverdrager-34068_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon" ;
    dct:title "UtviklingskostnaderBalanseforte10AvEgenkapital-23773_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon" ;
    dct:title "UtviklingskostnaderBalanseforte50AvEgenkapital-23774_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100" ;
    dct:title "VerdipapirutstederAksje-34213_KodelisteEttValg2JaNei-4_100"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 13 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746_Verdirestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/2365/6/forms/3442/45350/VerdsettelsePrisBok1-23746_Verdirestriksjon" ;
    dct:title "VerdsettelsePrisBok1-23746_Verdirestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Ar44-repformat-6> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Ar44-repformat-6" ;
    dct:title "Ar44-repformat-6"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125" ;
    dct:title "Avgiver-grp-1125"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Avgiver-grp-1125/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BelopHeltall15-repformat-37> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BelopHeltall15-repformat-37" ;
    dct:title "BelopHeltall15-repformat-37"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560" ;
    dct:title "BilArsmodellSpesifisertBil-datadef-30560"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilArsmodellSpesifisertBil-datadef-30560/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587" ;
    dct:title "BilBrukerAdresseSpesifisertBil-datadef-7587"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerAdresseSpesifisertBil-datadef-7587/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586" ;
    dct:title "BilBrukerFodselsnummerSpesifisertBil-datadef-7586"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerFodselsnummerSpesifisertBil-datadef-7586/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585" ;
    dct:title "BilBrukerNavnSpesifisertBil-datadef-7585"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerNavnSpesifisertBil-datadef-7585/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588" ;
    dct:title "BilBrukerPostnummerSpesifisertBil-datadef-7588"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPostnummerSpesifisertBil-datadef-7588/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589" ;
    dct:title "BilBrukerPoststedSpesifisertBil-datadef-7589"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBrukerPoststedSpesifisertBil-datadef-7589/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584" ;
    dct:title "BilBruksomradeSpesifisertBil-datadef-7584"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilBruksomradeSpesifisertBil-datadef-7584/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582" ;
    dct:title "BilKilometerstandFjoraretSpesifisertBil-datadef-7582"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandFjoraretSpesifisertBil-datadef-7582/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581" ;
    dct:title "BilKilometerstandSpesifisertBil-datadef-7581"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKilometerstandSpesifisertBil-datadef-7581/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118" ;
    dct:title "BilKjorebokSpesifisertBil-datadef-3118"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorebokSpesifisertBil-datadef-3118/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116" ;
    dct:title "BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilKjorelengdeYrkesmessigSpesifisertBil-datadef-3116/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114" ;
    dct:title "BilListeprisSpesifisertBil-datadef-3114"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilListeprisSpesifisertBil-datadef-3114/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580" ;
    dct:title "BilMerkeTypeSpesifisertBil-datadef-7580"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilMerkeTypeSpesifisertBil-datadef-7580/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405" ;
    dct:title "BilParkeringAdresseSpesifisertBil-datadef-30405"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAdresseSpesifisertBil-datadef-30405/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667" ;
    dct:title "BilParkeringAnnetStedSpesifisertBil-datadef-7667"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringAnnetStedSpesifisertBil-datadef-7667/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406" ;
    dct:title "BilParkeringVarierendeStedSpesifisertBil-datadef-30406"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilParkeringVarierendeStedSpesifisertBil-datadef-30406/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579" ;
    dct:title "BilRegistreringsnummerSpesifisertBil-datadef-7579"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilRegistreringsnummerSpesifisertBil-datadef-7579/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115" ;
    dct:title "BilgodtgjorelseMottattSpesifisertBil-datadef-3115"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilgodtgjorelseMottattSpesifisertBil-datadef-3115/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576" ;
    dct:title "BilkategoriSpesifisertBil-datadef-7576"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkategoriSpesifisertBil-datadef-7576/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591" ;
    dct:title "BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderPrivatTilbakefortSpesifisertBil-datadef-7591/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250" ;
    dct:title "BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderTilbakeforingsgrunnlagSamletKostnadSpesifisertBil-datadef-11250/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249" ;
    dct:title "BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/BilkostnaderVerdiforringelseSaldoSpesifisertBil-datadef-11249/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596" ;
    dct:title "DriftskostnaderDrivstoffSpesifisertBil-datadef-7596"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderDrivstoffSpesifisertBil-datadef-7596/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590" ;
    dct:title "DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderForsikringAvgifterSpesifisertBil-datadef-7590/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252" ;
    dct:title "DriftskostnaderLeasingleieSpesifisertBil-datadef-11252"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderLeasingleieSpesifisertBil-datadef-11252/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594" ;
    dct:title "DriftskostnaderOverskuddSpesifisertBil-datadef-7594"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderOverskuddSpesifisertBil-datadef-7594/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484" ;
    dct:title "DriftskostnaderSpesifisertBil-datadef-34484"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-34484/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578" ;
    dct:title "DriftskostnaderSpesifisertBil-datadef-7578"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderSpesifisertBil-datadef-7578/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595" ;
    dct:title "DriftskostnaderUnderskuddSpesifisertBil-datadef-7595"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderUnderskuddSpesifisertBil-datadef-7595/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251" ;
    dct:title "DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderVedlikeholdSpesifisertBil-datadef-11251/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254" ;
    dct:title "DriftskostnaderYrketSpesifisertBil-datadef-11254"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/DriftskostnaderYrketSpesifisertBil-datadef-11254/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15" ;
    dct:title "EnhetAdresse-datadef-15"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetAdresse-datadef-15/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1" ;
    dct:title "EnhetNavn-datadef-1"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetNavn-datadef-1/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18" ;
    dct:title "EnhetOrganisasjonsnummer-datadef-18"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetOrganisasjonsnummer-datadef-18/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673" ;
    dct:title "EnhetPostnummer-datadef-6673"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPostnummer-datadef-6673/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674" ;
    dct:title "EnhetPoststed-datadef-6674"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/EnhetPoststed-datadef-6674/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124" ;
    dct:title "GenerellInformasjon-grp-1124"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/GenerellInformasjon-grp-1124/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Heltall7-repformat-116> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Heltall7-repformat-116" ;
    dct:title "Heltall7-repformat-116"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139" ;
    dct:title "HvemBrukerBilenUtenomArbeidstiden-grp-1139"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/HvemBrukerBilenUtenomArbeidstiden-grp-1139/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497" ;
    dct:title "InformasjonOmBil-grp-3497"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBil-grp-3497/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771" ;
    dct:title "InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/InformasjonOmBilOgSpesifikasjonAvDriftskostnader-grp-2771/gruppeid> .

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

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667" ;
    dct:title "OmBil-grp-5667"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OmBil-grp-5667/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26" ;
    dct:title "OppgavegiverFodselsnummer-datadef-26"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/OppgavegiverFodselsnummer-datadef-26/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633" ;
    dct:title "Regnskapsforer-grp-2633"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Regnskapsforer-grp-2633/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281" ;
    dct:title "RegnskapsforerAdresse-datadef-281"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerAdresse-datadef-281/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280" ;
    dct:title "RegnskapsforerNavn-datadef-280"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerNavn-datadef-280/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678" ;
    dct:title "RegnskapsforerPostnummer-datadef-6678"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPostnummer-datadef-6678/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679" ;
    dct:title "RegnskapsforerPoststed-datadef-6679"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/RegnskapsforerPoststed-datadef-6679/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253" ;
    dct:title "SaldoavskrivningSpesifisertBil-datadef-11253"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SaldoavskrivningSpesifisertBil-datadef-11253/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema" ;
    dct:title "Skjema"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/blankettnummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/etatid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/gruppeid>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/skjemanummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/spesifikasjonsnummer>,
        <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/tittel> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/blankettnummer> a ns1:Attribute ;
    dct:title "blankettnummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/etatid> a ns1:Attribute ;
    dct:title "etatid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/skjemanummer> a ns1:Attribute ;
    dct:title "skjemanummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#Integer> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/spesifikasjonsnummer> a ns1:Attribute ;
    dct:title "spesifikasjonsnummer"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#Integer> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/Skjema/tittel> a ns1:Attribute ;
    dct:title "tittel"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404" ;
    dct:title "SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404/orid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SkjemaVedleggTilSelvangivelseNaringsoppgave-datadef-30404/orid> a ns1:Attribute ;
    dct:title "orid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150" ;
    dct:title "SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/gruppeid> .

<http://localhost:8000/api/metadata/formtask/3314/1212/forms/245/10980/SpesifikasjonAvDriftskostnaderForPrivatBrukAvYrkesbil-grp-1150/gruppeid> a ns1:Attribute ;
    dct:title "gruppeid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArOgMaaned" ;
    dct:title "AArOgMaaned"@nb ;
    xsd:anyURI xsd:gYearMonth .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AArstall" ;
    dct:title "AArstall"@nb ;
    xsd:anyURI xsd:gYear .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon" ;
    dct:title "AldersUfoereEtterlatteAvtalefestetOgKrigspensjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tidsrom> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/Periode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe" ;
    dct:title "AldersUfoereEtterlatteAvtalefestetOgKrigspensjonGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold" ;
    dct:title "Arbeidsforhold"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/fartoey>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/permisjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/Fartoey> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/Permisjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/fartoey> a ns1:Attribute ;
    dct:title "fartoey"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/Fartoey> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/permisjon> a ns1:Attribute ;
    dct:title "permisjon"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsforhold/Permisjon> .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/FradragIGrunnlaget> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/FradragIGrunnlagetForUtenlandsk> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/UtenlandskeMedFastAvgiftsbeloep> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/UtenlandskeMedSaerskiltProsentsats> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForSone> a ns1:Attribute ;
    dct:title "fradragIGrunnlagetForSone"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/FradragIGrunnlaget> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/fradragIGrunnlagetForUtenlandsk> a ns1:Attribute ;
    dct:title "fradragIGrunnlagetForUtenlandsk"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/FradragIGrunnlagetForUtenlandsk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/loennOgGodtgjoerelse> a ns1:Attribute ;
    dct:title "loennOgGodtgjoerelse"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/Arbeidsgiveravgiftsgrunnlag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/tilskuddOgPremieTilPensjon> a ns1:Attribute ;
    dct:title "tilskuddOgPremieTilPensjon"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/Arbeidsgiveravgiftsgrunnlag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedFastAvgiftsbeloep> a ns1:Attribute ;
    dct:title "utenlandskeMedFastAvgiftsbeloep"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/UtenlandskeMedFastAvgiftsbeloep> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/utenlandskeMedSaerskiltProsentsats> a ns1:Attribute ;
    dct:title "utenlandskeMedSaerskiltProsentsats"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/UtenlandskeMedSaerskiltProsentsats> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsgrunnlag" ;
    dct:title "Arbeidsgiveravgiftsgrunnlag"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgiftsone" ;
    dct:title "Arbeidsgiveravgiftsone"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidstidsordning" ;
    dct:title "Arbeidstidsordning"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Avloenningstype" ;
    dct:title "Avloenningstype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Beloep" ;
    dct:title "Beloep"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeloepSomHeltall" ;
    dct:title "BeloepSomHeltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeregningskodeForArbeidsgiveravgift" ;
    dct:title "BeregningskodeForArbeidsgiveravgift"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeskrivelseGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BeskrivelseGruppe" ;
    dct:title "BeskrivelseGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Betalingsinformasjon" ;
    dct:title "Betalingsinformasjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat" ;
    dct:title "BilOgBaat"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaat/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaatGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BilOgBaatGruppe" ;
    dct:title "BilOgBaatGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret" ;
    dct:title "BonusFraForsvaret"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaret/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaretGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/BonusFraForsvaretGruppe" ;
    dct:title "BonusFraForsvaretGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Boolsk" ;
    dct:title "Boolsk"@nb ;
    xsd:anyURI xsd:boolean .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBolig" ;
    dct:title "DagmammaIEgenBolig"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBoligGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DagmammaIEgenBoligGruppe" ;
    dct:title "DagmammaIEgenBoligGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Dato" ;
    dct:title "Dato"@nb ;
    xsd:anyURI xsd:date .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/DatoTid" ;
    dct:title "DatoTid"@nb ;
    xsd:anyURI xsd:dateTime .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Desimaltall" ;
    dct:title "Desimaltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M" ;
    dct:title "EDAG_M"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/leveranse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/Leveranse> a ns1:ObjectType .

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
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EDAG_M/Leveranse> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode" ;
    dct:title "Etterbetalingsperiode"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/tidsrom> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/Periode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Etterbetalingsperiode/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EtterbetalingsperiodeGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/EtterbetalingsperiodeGruppe" ;
    dct:title "EtterbetalingsperiodeGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartoey" ;
    dct:title "Fartoey"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fartsomraade" ;
    dct:title "Fartsomraade"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fordel" ;
    dct:title "Fordel"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekk" ;
    dct:title "Forskuddstrekk"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Forskuddstrekksbeskrivelse" ;
    dct:title "Forskuddstrekksbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradrag" ;
    dct:title "Fradrag"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlaget" ;
    dct:title "FradragIGrunnlaget"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/FradragIGrunnlagetForUtenlandsk" ;
    dct:title "FradragIGrunnlagetForUtenlandsk"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Fradragsbeskrivelse" ;
    dct:title "Fradragsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsbeloepForUtenlandske" ;
    dct:title "GrunnlagsbeloepForUtenlandske"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Grunnlagsprosent" ;
    dct:title "Grunnlagsprosent"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/GrunnlagsprosentForUtenlandske" ;
    dct:title "GrunnlagsprosentForUtenlandske"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Heltall" ;
    dct:title "Heltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Identifikator" ;
    dct:title "Identifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/IdentifiserendeInformasjon" ;
    dct:title "IdentifiserendeInformasjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntekt" ;
    dct:title "Inntekt"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle" ;
    dct:title "InntektAlle"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tidsrom> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/Periode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/bilinformasjon> a ns1:Attribute ;
    dct:title "bilinformasjon"@nb ;
    xsd:maxOccurs 1 .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektAlle/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntektGruppe" ;
    dct:title "InntektGruppe"@nb .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/BilOgBaat> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/BonusFraForsvaret> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/DagmammaIEgenBolig> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Etterbetalingsperiode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/InntektAlle> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Inntjeningsforhold> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Livrente> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Loennsinntekt> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/LottOgPartInnenFiske> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Naeringsinntekt> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Nettoloennsordning> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/NorskKontinentalsokkel> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/PensjonEllerTrygd> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/ReiseKostOgLosji> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/UtenlandskArtist> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/alleFelter> a ns1:Attribute ;
    dct:title "alleFelter"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/InntektAlle> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bilOgBaat> a ns1:Attribute ;
    dct:title "bilOgBaat"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/BilOgBaat> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/bonusFraForsvaret> a ns1:Attribute ;
    dct:title "bonusFraForsvaret"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/BonusFraForsvaret> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/dagmammaIEgenBolig> a ns1:Attribute ;
    dct:title "dagmammaIEgenBolig"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/DagmammaIEgenBolig> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/etterbetalingsperiode> a ns1:Attribute ;
    dct:title "etterbetalingsperiode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Etterbetalingsperiode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntektPaaNorskKontinentalsokkel> a ns1:Attribute ;
    dct:title "inntektPaaNorskKontinentalsokkel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/NorskKontinentalsokkel> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/inntjeningsforhold> a ns1:Attribute ;
    dct:title "inntjeningsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Inntjeningsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/livrente> a ns1:Attribute ;
    dct:title "livrente"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Livrente> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/loennsinntekt> a ns1:Attribute ;
    dct:title "loennsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Loennsinntekt> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/lottOgPart> a ns1:Attribute ;
    dct:title "lottOgPart"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/LottOgPartInnenFiske> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/naeringsinntekt> a ns1:Attribute ;
    dct:title "naeringsinntekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Naeringsinntekt> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/nettoloenn> a ns1:Attribute ;
    dct:title "nettoloenn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/Nettoloennsordning> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjon> a ns1:Attribute ;
    dct:title "pensjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/AldersUfoereEtterlatteAvtalefestetOgKrigspensjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/pensjonEllerTrygd> a ns1:Attribute ;
    dct:title "pensjonEllerTrygd"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/PensjonEllerTrygd> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/reiseKostOgLosji> a ns1:Attribute ;
    dct:title "reiseKostOgLosji"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/ReiseKostOgLosji> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/tilleggsinformasjon> a ns1:Attribute ;
    dct:title "tilleggsinformasjon"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/utenlandskArtist> a ns1:Attribute ;
    dct:title "utenlandskArtist"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsentitet/UtenlandskArtist> .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker" ;
    dct:title "Inntektsmottaker"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/arbeidsforhold>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/forskuddstrekk>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/fradrag>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/identifiserendeInformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/inntekt>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/internasjonalIdentifikator>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/oppholdPaaSvalbardJanMayenOgBilandene>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/sjoefolksrelatertInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Arbeidsforhold> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Forskuddstrekk> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Fradrag> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/IdentifiserendeInformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Inntektsentitet> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/InternasjonalIdentifikator> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/OppholdPaaSvalbardJanMayenOgBilandene> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/SjoefolksrelatertInformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/arbeidsforhold> a ns1:Attribute ;
    dct:title "arbeidsforhold"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Arbeidsforhold> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/forskuddstrekk> a ns1:Attribute ;
    dct:title "forskuddstrekk"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Forskuddstrekk> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/fradrag> a ns1:Attribute ;
    dct:title "fradrag"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Fradrag> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/identifiserendeInformasjon> a ns1:Attribute ;
    dct:title "identifiserendeInformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/IdentifiserendeInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/inntekt> a ns1:Attribute ;
    dct:title "inntekt"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/Inntektsentitet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/internasjonalIdentifikator> a ns1:Attribute ;
    dct:title "internasjonalIdentifikator"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/InternasjonalIdentifikator> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/oppholdPaaSvalbardJanMayenOgBilandene> a ns1:Attribute ;
    dct:title "oppholdPaaSvalbardJanMayenOgBilandene"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/OppholdPaaSvalbardJanMayenOgBilandene> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/sjoefolksrelatertInformasjon> a ns1:Attribute ;
    dct:title "sjoefolksrelatertInformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntektsmottaker/SjoefolksrelatertInformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold" ;
    dct:title "Inntjeningsforhold"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Inntjeningsforhold/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntjeningsforholdGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InntjeningsforholdGruppe" ;
    dct:title "InntjeningsforholdGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikator" ;
    dct:title "InternasjonalIdentifikator"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/InternasjonalIdentifikatortype" ;
    dct:title "InternasjonalIdentifikatortype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet" ;
    dct:title "JuridiskEntitet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/betalingsinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/virksomhet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/Betalingsinformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/Virksomhet> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/betalingsinformasjon> a ns1:Attribute ;
    dct:title "betalingsinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/Betalingsinformasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/virksomhet> a ns1:Attribute ;
    dct:title "virksomhet"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/JuridiskEntitet/Virksomhet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Landkode" ;
    dct:title "Landkode"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse" ;
    dct:title "Leveranse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/oppgave>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/opplysningspliktig> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/JuridiskEntitet> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/Opplysningspliktig> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/oppgave> a ns1:Attribute ;
    dct:title "oppgave"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/JuridiskEntitet> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/opplysningspliktig> a ns1:Attribute ;
    dct:title "opplysningspliktig"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Leveranse/Opplysningspliktig> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente" ;
    dct:title "Livrente"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/tidsrom> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/Periode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Livrente/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LivrenteGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LivrenteGruppe" ;
    dct:title "LivrenteGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsbeskrivelse" ;
    dct:title "Loennsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt" ;
    dct:title "Loennsinntekt"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Loennsinntekt/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LoennsinntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LoennsinntektGruppe" ;
    dct:title "LoennsinntektGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/LottOgPartInnenFiske" ;
    dct:title "LottOgPartInnenFiske"@nb .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntekt" ;
    dct:title "Naeringsinntekt"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NaeringsinntektGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NaeringsinntektGruppe" ;
    dct:title "NaeringsinntektGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Naeringsinntektsbeskrivelse" ;
    dct:title "Naeringsinntektsbeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning" ;
    dct:title "Nettoloennsordning"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/bilinformasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/BilOgBaat> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/bilinformasjon> a ns1:Attribute ;
    dct:title "bilinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/BilOgBaat> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Nettoloennsordning/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NettoloennsordningGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NettoloennsordningGruppe" ;
    dct:title "NettoloennsordningGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskIdentifikator" ;
    dct:title "NorskIdentifikator"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel" ;
    dct:title "NorskKontinentalsokkel"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/spesifikasjon>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/tidsrom> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/Periode> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/tidsrom> a ns1:Attribute ;
    dct:title "tidsrom"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkel/Periode> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkelGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/NorskKontinentalsokkelGruppe" ;
    dct:title "NorskKontinentalsokkelGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdPaaSvalbardJanMayenOgBilandene" ;
    dct:title "OppholdPaaSvalbardJanMayenOgBilandene"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/OppholdsbeskrivelseForSvalbardJanMayenOgBilandene" ;
    dct:title "OppholdsbeskrivelseForSvalbardJanMayenOgBilandene"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Opplysningspliktig" ;
    dct:title "Opplysningspliktig"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygd" ;
    dct:title "PensjonEllerTrygd"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdGruppe" ;
    dct:title "PensjonEllerTrygdGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PensjonEllerTrygdebeskrivelse" ;
    dct:title "PensjonEllerTrygdebeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Periode" ;
    dct:title "Periode"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Permisjon" ;
    dct:title "Permisjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PermisjonsOgPermitteringsBeskrivelse" ;
    dct:title "PermisjonsOgPermitteringsBeskrivelse"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/PersontypeForReiseKostLosji" ;
    dct:title "PersontypeForReiseKostLosji"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji" ;
    dct:title "ReiseKostOgLosji"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/ReiseKostOgLosji/Spesifikasjon> .

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

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SjoefolksrelatertInformasjon" ;
    dct:title "SjoefolksrelatertInformasjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SkatteOgAvgiftsregel" ;
    dct:title "SkatteOgAvgiftsregel"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipsregister" ;
    dct:title "Skipsregister"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Skipstype" ;
    dct:title "Skipstype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/SpesielleInntjeningsforhold" ;
    dct:title "SpesielleInntjeningsforhold"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spesifikasjon" ;
    dct:title "Spesifikasjon"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Spraak" ;
    dct:title "Spraak"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Tekst" ;
    dct:title "Tekst"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/TekstMedRestriksjon" ;
    dct:title "TekstMedRestriksjon"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist" ;
    dct:title "UtenlandskArtist"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/Spesifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/spesifikasjon> a ns1:Attribute ;
    dct:title "spesifikasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtist/Spesifikasjon> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtistGruppe> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskArtistGruppe" ;
    dct:title "UtenlandskArtistGruppe"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedFastAvgiftsbeloep" ;
    dct:title "UtenlandskeMedFastAvgiftsbeloep"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/UtenlandskeMedSaerskiltProsentsats" ;
    dct:title "UtenlandskeMedSaerskiltProsentsats"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet" ;
    dct:title "Virksomhet"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/arbeidsgiveravgift>,
        <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/inntektsmottaker> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/Arbeidsgiveravgift> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/Inntektsmottaker> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/arbeidsgiveravgift> a ns1:Attribute ;
    dct:title "arbeidsgiveravgift"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/Arbeidsgiveravgift> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/inntektsmottaker> a ns1:Attribute ;
    dct:title "inntektsmottaker"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Virksomhet/Inntektsmottaker> .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Yrke" ;
    dct:title "Yrke"@nb ;
    xsd:anyURI xsd:string .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Adressenummer" ;
    dct:title "Adressenummer"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Antall" ;
    dct:title "Antall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge" ;
    dct:title "ArbeidsoppholdINorge"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ArbeidsoppholdSomArbeidstaker> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ArbeidsoppholdSomSelvstendigNaeringsdrivende> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomArbeidstaker> a ns1:Attribute ;
    dct:title "oppholdSomArbeidstaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ArbeidsoppholdSomArbeidstaker> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/oppholdSomSelvstendigNaeringsdrivende> a ns1:Attribute ;
    dct:title "oppholdSomSelvstendigNaeringsdrivende"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdINorge/ArbeidsoppholdSomSelvstendigNaeringsdrivende> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker" ;
    dct:title "ArbeidsoppholdSomArbeidstaker"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/Vedleggsreferanse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/arbeidskontraktreferanse> a ns1:Attribute ;
    dct:title "arbeidskontraktreferanse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomArbeidstaker/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/ArbeidsoppholdSomSelvstendigNaeringsdrivende" ;
    dct:title "ArbeidsoppholdSomSelvstendigNaeringsdrivende"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidsstedsbeliggenhet" ;
    dct:title "Arbeidsstedsbeliggenhet"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon" ;
    dct:title "Arbeidstakerinformasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidsopphold>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidstaker>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/identifikasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/kontaktinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/norskPersonidentifikator>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/ArbeidsoppholdINorge> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Folkeregisterkandidat> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Kontaktinformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Personidentifikasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Personidentifikator> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Vedleggsreferanse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidsopphold> a ns1:Attribute ;
    dct:title "arbeidsopphold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/ArbeidsoppholdINorge> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/arbeidstaker> a ns1:Attribute ;
    dct:title "arbeidstaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Folkeregisterkandidat> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/identifikasjon> a ns1:Attribute ;
    dct:title "identifikasjon"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Personidentifikasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/kontaktinformasjon> a ns1:Attribute ;
    dct:title "kontaktinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Kontaktinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/norskPersonidentifikator> a ns1:Attribute ;
    dct:title "norskPersonidentifikator"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Personidentifikator> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/referanseTilIdentifikasjonsdokument> a ns1:Attribute ;
    dct:title "referanseTilIdentifikasjonsdokument"@nb ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Arbeidstakerinformasjon/Vedleggsreferanse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftelsePaaManglendeIdentifikasjonsdokument" ;
    dct:title "BekreftelsePaaManglendeIdentifikasjonsdokument"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/BekreftetIdentitet" ;
    dct:title "BekreftetIdentitet"@nb .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat" ;
    dct:title "Folkeregisterkandidat"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/navn>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/oppholdsadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresseIUtlandet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/OffisiellOppholdsadresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/Personnavn> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/navn> a ns1:Attribute ;
    dct:title "navn"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/Personnavn> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/oppholdsadresse> a ns1:Attribute ;
    dct:title "oppholdsadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/OffisiellOppholdsadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresse> a ns1:Attribute ;
    dct:title "postadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/Kontaktadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/postadresseIUtlandet> a ns1:Attribute ;
    dct:title "postadresseIUtlandet"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/Kontaktadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Heltall" ;
    dct:title "Heltall"@nb ;
    xsd:anyURI xsd:decimal .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument" ;
    dct:title "Identifikasjonsdokument"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/Identifikasjonsdokumentkopi> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/dokumentkopi> a ns1:Attribute ;
    dct:title "dokumentkopi"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokument/Identifikasjonsdokumentkopi> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi" ;
    dct:title "Identifikasjonsdokumentkopi"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Identifikasjonsdokumentkopi/skannetDokument> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/InternasjonalAdresse" ;
    dct:title "InternasjonalAdresse"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kjoenn" ;
    dct:title "Kjoenn"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kommunenummer" ;
    dct:title "Kommunenummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse" ;
    dct:title "Kontaktadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/postboksadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/utenlandskPostadresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/InternasjonalAdresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Matrikkeladresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Postboksadresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Vegadresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/matrikkeladresse> a ns1:Attribute ;
    dct:title "matrikkeladresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Matrikkeladresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/postboksadresse> a ns1:Attribute ;
    dct:title "postboksadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Postboksadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/utenlandskPostadresse> a ns1:Attribute ;
    dct:title "utenlandskPostadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/InternasjonalAdresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/vegadresse> a ns1:Attribute ;
    dct:title "vegadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktadresse/Vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Kontaktinformasjon" ;
    dct:title "Kontaktinformasjon"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Landkode" ;
    dct:title "Landkode"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/LandkodeISOAlpha3" ;
    dct:title "LandkodeISOAlpha3"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 3 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse" ;
    dct:title "Matrikkeladresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/Matrikkelnummer> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/matrikkelnummer> a ns1:Attribute ;
    dct:title "matrikkelnummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkeladresse/Matrikkelnummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Matrikkelnummer" ;
    dct:title "Matrikkelnummer"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Navn" ;
    dct:title "Navn"@nb ;
    xsd:anyURI xsd:string ;
    xsd:maxLength 200 ;
    xsd:minLength 1 .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse" ;
    dct:title "OffisiellOppholdsadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/Matrikkeladresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/Vegadresse> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/matrikkeladresse> a ns1:Attribute ;
    dct:title "matrikkeladresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/Matrikkeladresse> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/vegadresse> a ns1:Attribute ;
    dct:title "vegadresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/OffisiellOppholdsadresse/Vegadresse> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon" ;
    dct:title "Personidentifikasjon"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/BekreftelsePaaManglendeIdentifikasjonsdokument> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/BekreftetIdentitet> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/Identifikasjonsdokument> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/dokumentgrunnlag> a ns1:Attribute ;
    dct:title "dokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/Identifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/identitetsbekreftelse> a ns1:Attribute ;
    dct:title "identitetsbekreftelse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/BekreftetIdentitet> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/manglendeDokumentgrunnlag> a ns1:Attribute ;
    dct:title "manglendeDokumentgrunnlag"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikasjon/BekreftelsePaaManglendeIdentifikasjonsdokument> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikator" ;
    dct:title "Personidentifikator"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personidentifikatortype" ;
    dct:title "Personidentifikatortype"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Personnavn" ;
    dct:title "Personnavn"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse" ;
    dct:title "Postboksadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/Poststed> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postboksadresse/Poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer> a ns1:SimpleType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Postnummer" ;
    dct:title "Postnummer"@nb ;
    xsd:anyURI xsd:string .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Poststed" ;
    dct:title "Poststed"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger" ;
    dct:title "SoeknadOmSkattekortForUtenlandskBorger"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/arbeidstakerinformasjon>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatId>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatProvider>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/dataFormatVersion>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/innsendersKontaktinformasjon> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/Arbeidstakerinformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/Kontaktinformasjon> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/arbeidstakerinformasjon> a ns1:Attribute ;
    dct:title "arbeidstakerinformasjon"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/Arbeidstakerinformasjon> .

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
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/SoeknadOmSkattekortForUtenlandskBorger/Kontaktinformasjon> .

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

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vedleggsreferanse" ;
    dct:title "Vedleggsreferanse"@nb .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse> a ns1:ObjectType ;
    dct:identifier "http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse" ;
    dct:title "Vegadresse"@nb ;
    ns1:hasProperty <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer>,
        <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/Adressenummer> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/Poststed> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/adressenummer> a ns1:Attribute ;
    dct:title "adressenummer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/Adressenummer> .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/poststed> a ns1:Attribute ;
    dct:title "poststed"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Vegadresse/Poststed> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286" ;
    dct:title "Adresselinje1"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Adresselinje1/660286/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664" ;
    dct:title "Epost_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S01/637664/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663" ;
    dct:title "Epost_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Epost_S02/637663/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250" ;
    dct:title "Foretaksnavn"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Foretaksnavn/639250/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942" ;
    dct:title "Heltall_1_S03"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S03/602942/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941" ;
    dct:title "Heltall_1_S04"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S04/602941/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940" ;
    dct:title "Heltall_1_S05"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S05/602940/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939" ;
    dct:title "Heltall_1_S06"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S06/602939/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938" ;
    dct:title "Heltall_1_S07"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S07/602938/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937" ;
    dct:title "Heltall_1_S08"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S08/602937/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797" ;
    dct:title "Heltall_1_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S1/488797/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798" ;
    dct:title "Heltall_1_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_1_S2/488798/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616" ;
    dct:title "Heltall_2_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Heltall_2_S01/493616/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277" ;
    dct:title "LEI-nummer"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/LEI-nummer/660277/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674" ;
    dct:title "Maalform"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Målform/660674/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662" ;
    dct:title "Navn_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S01/637662/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661" ;
    dct:title "Navn_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Navn_S02/637661/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574" ;
    dct:title "Organisasjonsnummer"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Organisasjonsnummer/638574/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275" ;
    dct:title "Periodetype"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Periodetype/660275/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288" ;
    dct:title "Postnummer"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Postnummer/660288/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287" ;
    dct:title "Poststed"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Poststed/660287/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854" ;
    dct:title "Rapporteringsid"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/RapporteringsId/636854/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631" ;
    dct:title "Tekst_10_S1"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_10_S1/488631/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714" ;
    dct:title "Tekst_255_S10"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_255_S10/600714/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952" ;
    dct:title "Tekst_750_T01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T01/658952/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951" ;
    dct:title "Tekst_750_T02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T02/658951/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950" ;
    dct:title "Tekst_750_T03"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T03/658950/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949" ;
    dct:title "Tekst_750_T04"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T04/658949/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948" ;
    dct:title "Tekst_750_T05"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T05/658948/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947" ;
    dct:title "Tekst_750_T06"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T06/658947/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946" ;
    dct:title "Tekst_750_T07"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T07/658946/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945" ;
    dct:title "Tekst_750_T08"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T08/658945/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944" ;
    dct:title "Tekst_750_T09"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T09/658944/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943" ;
    dct:title "Tekst_750_T10"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T10/658943/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942" ;
    dct:title "Tekst_750_T11"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T11/658942/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941" ;
    dct:title "Tekst_750_T12"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T12/658941/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940" ;
    dct:title "Tekst_750_T13"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/Tekst_750_T13/658940/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660" ;
    dct:title "TelefonNummer_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S01/637660/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659" ;
    dct:title "TelefonNummer_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonNummer_S02/637659/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658" ;
    dct:title "TelefonPrefiks_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S01/637658/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657" ;
    dct:title "TelefonPrefiks_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657/guid> .

<http://seres.no/guid/Finanstilsynet/Dataenkeltype/TelefonPrefiks_S02/637657/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705" ;
    dct:title "Boolean_S12"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S12/602705/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701" ;
    dct:title "Boolean_S13"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S13/602701/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697" ;
    dct:title "Boolean_S14"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S14/602697/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693" ;
    dct:title "Boolean_S15"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S15/602693/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689" ;
    dct:title "Boolean_S16"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S16/602689/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685" ;
    dct:title "Boolean_S17"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S17/602685/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677" ;
    dct:title "Boolean_S18"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S18/602677/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681" ;
    dct:title "Boolean_S19"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S19/602681/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673" ;
    dct:title "Boolean_S20"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S20/602673/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462" ;
    dct:title "Boolean_S21"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S21/622462/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458" ;
    dct:title "Boolean_S22"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S22/622458/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322" ;
    dct:title "Boolean_S23"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S23/632322/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318" ;
    dct:title "Boolean_S24"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S24/632318/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252" ;
    dct:title "Boolean_S25"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S25/634252/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248" ;
    dct:title "Boolean_S26"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S26/634248/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244" ;
    dct:title "Boolean_S27"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S27/634244/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232" ;
    dct:title "Boolean_S30"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S30/634232/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228" ;
    dct:title "Boolean_S31"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S31/634228/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224" ;
    dct:title "Boolean_S32"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S32/634224/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089" ;
    dct:title "Boolean_S33"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S33/665089/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085" ;
    dct:title "Boolean_S34"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S34/665085/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081" ;
    dct:title "Boolean_S35"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S35/665081/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077" ;
    dct:title "Boolean_S36"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Boolean_S36/665077/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068" ;
    dct:title "Ifrs16harforklartforskjeller"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/Ifrs16harforklartforskjeller/772068/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985" ;
    dct:title "SvaralternativJaNei_S07"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S07/517985/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331" ;
    dct:title "SvaralternativJaNei_S103"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S103/639331/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327" ;
    dct:title "SvaralternativJaNei_S104"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S104/639327/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323" ;
    dct:title "SvaralternativJaNei_S105"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S105/639323/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319" ;
    dct:title "SvaralternativJaNei_S106"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S106/639319/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315" ;
    dct:title "SvaralternativJaNei_S107"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S107/639315/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999" ;
    dct:title "SvaralternativJaNei_S88"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S88/517999/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995" ;
    dct:title "SvaralternativJaNei_S89"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S89/517995/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003" ;
    dct:title "SvaralternativJaNei_S91"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S91/518003/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213" ;
    dct:title "SvaralternativJaNei_S92"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S92/508213/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209" ;
    dct:title "SvaralternativJaNei_S93"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S93/508209/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205" ;
    dct:title "SvaralternativJaNei_S94"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S94/508205/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734" ;
    dct:title "SvaralternativJaNei_S95"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S95/600734/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730" ;
    dct:title "SvaralternativJaNei_S96"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S96/600730/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726" ;
    dct:title "SvaralternativJaNei_S97"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S97/600726/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722" ;
    dct:title "SvaralternativJaNei_S98"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S98/600722/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718" ;
    dct:title "SvaralternativJaNei_S99"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeliste/SvaralternativJaNei_S99/600718/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467" ;
    dct:title "SvaralternativJaNei_S01"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S1/487467/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475" ;
    dct:title "SvaralternativJaNei_S11"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S11/488475/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673" ;
    dct:title "SvaralternativJaNei_S12"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S12/488673/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672" ;
    dct:title "SvaralternativJaNei_S13"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S13/488672/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671" ;
    dct:title "SvaralternativJaNei_S14"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S14/488671/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670" ;
    dct:title "SvaralternativJaNei_S15"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S15/488670/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669" ;
    dct:title "SvaralternativJaNei_S16"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S16/488669/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668" ;
    dct:title "SvaralternativJaNei_S17"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S17/488668/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667" ;
    dct:title "SvaralternativJaNei_S18"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S18/488667/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666" ;
    dct:title "SvaralternativJaNei_S19"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S19/488666/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466" ;
    dct:title "SvaralternativJaNei_S02"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S2/487466/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665" ;
    dct:title "SvaralternativJaNei_S20"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S20/488665/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664" ;
    dct:title "SvaralternativJaNei_S21"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S21/488664/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663" ;
    dct:title "SvaralternativJaNei_S22"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S22/488663/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662" ;
    dct:title "SvaralternativJaNei_S23"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S23/488662/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465" ;
    dct:title "SvaralternativJaNei_S03"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S3/487465/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655" ;
    dct:title "SvaralternativJaNei_S30"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S30/488655/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654" ;
    dct:title "SvaralternativJaNei_S31"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S31/488654/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653" ;
    dct:title "SvaralternativJaNei_S32"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S32/488653/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652" ;
    dct:title "SvaralternativJaNei_S33"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S33/488652/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651" ;
    dct:title "SvaralternativJaNei_S34"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S34/488651/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646" ;
    dct:title "SvaralternativJaNei_S42"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/488646/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187" ;
    dct:title "SvaralternativJaNei_S39"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S39/493187/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464" ;
    dct:title "SvaralternativJaNei_S04"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S4/487464/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186" ;
    dct:title "SvaralternativJaNei_S40"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S40/493186/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185" ;
    dct:title "SvaralternativJaNei_S41"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S41/493185/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184" ;
    dct:title "SvaralternativJaNei_S43"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S43/493184/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183" ;
    dct:title "SvaralternativJaNei_S44"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S44/493183/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012" ;
    dct:title "SvaralternativJaNei_S45"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S45/494012/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011" ;
    dct:title "SvaralternativJaNei_S46"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S46/494011/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463" ;
    dct:title "SvaralternativJaNei_S05"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S5/487463/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007" ;
    dct:title "SvaralternativJaNei_S50"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S50/494007/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169" ;
    dct:title "SvaralternativJaNei_S51"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S51/493169/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168" ;
    dct:title "SvaralternativJaNei_S52"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S52/493168/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167" ;
    dct:title "SvaralternativJaNei_S53"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S53/493167/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166" ;
    dct:title "SvaralternativJaNei_S54"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S54/493166/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165" ;
    dct:title "SvaralternativJaNei_S55"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S55/493165/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164" ;
    dct:title "SvaralternativJaNei_S56"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S56/493164/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179" ;
    dct:title "SvaralternativJaNei_S58"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S58/493179/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178" ;
    dct:title "SvaralternativJaNei_S59"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S59/493178/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462" ;
    dct:title "SvaralternativJaNei_S06"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S6/487462/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176" ;
    dct:title "SvaralternativJaNei_S60"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S60/493176/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177" ;
    dct:title "SvaralternativJaNei_S61"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S61/493177/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161" ;
    dct:title "SvaralternativJaNei_S62"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S62/493161/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162" ;
    dct:title "SvaralternativJaNei_S63"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S63/493162/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160" ;
    dct:title "SvaralternativJaNei_S64"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S64/493160/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159" ;
    dct:title "SvaralternativJaNei_S65"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S65/493159/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175" ;
    dct:title "SvaralternativJaNei_S66"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S66/493175/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174" ;
    dct:title "SvaralternativJaNei_S67"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S67/493174/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314" ;
    dct:title "SvaralternativJaNei_S86"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S86/494314/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313" ;
    dct:title "SvaralternativJaNei_S87"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313/guid> .

<http://seres.no/guid/Finanstilsynet/Datakodeutvalg/SvaralternativJaNei_S87/494313/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Datakomplekstype/Verdipapirutsteder/446029" ;
    dct:title "Verdipapirutsteder"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Adresse/660282" ;
    dct:title "Adresse"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/AlternativeResultatmål/664869" ;
    dct:title "AlternativeResultatmaal"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/AndreForhold/445989" ;
    dct:title "AndreForhold"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Egenkapital/445957" ;
    dct:title "Egenkapital"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ForpliktelseAvsetning/445999" ;
    dct:title "ForpliktelseAvsetning"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771887" ;
    dct:title "Ifrs15vurderinger"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15/771901" ;
    dct:title "Ifrs15"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15kategorier/771957>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15vurderinger/771900> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs15kategorier/771966" ;
    dct:title "Ifrs15kategorier"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16/771886" ;
    dct:title "Ifrs16"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterleietaker/771981>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterutleiereksterne/771983> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16leiekontrakterleietaker/771971" ;
    dct:title "Ifrs16leiekontrakterleietaker"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurderinger/771970>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurdertikkeeffekt/771976> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16utleiereksterne/771938" ;
    dct:title "Ifrseffekt"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs16vurdertikkeeffekt/771917" ;
    dct:title "Ifrs16vurdertikkeeffekt"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrs9/771943" ;
    dct:title "Ifrs9"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrseffekt/771942> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifrsandre/771941" ;
    dct:title "Ifrsandre"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Ifsr16vurderinger/771929" ;
    dct:title "Ifrs16vurderinger"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ImmateriellEiendel/445946" ;
    dct:title "ImmateriellEiendel"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utsattSkattefordel/445942>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utviklingsutgift/445941> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Innsender/664850" ;
    dct:title "Innsender"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/adresse/664847> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson1/637652" ;
    dct:title "Kontaktperson1"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontaktperson2/637647" ;
    dct:title "Kontaktperson2"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Kontantstrøm/445910" ;
    dct:title "Kontantstroem"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/MarkedsverdibasertEiendel/445974" ;
    dct:title "MarkedsverdibasertEiendel"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Nedskriving/445929" ;
    dct:title "Nedskriving"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Organisasjonsforhold/445936" ;
    dct:title "Organisasjonsforhold"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Periode/664925" ;
    dct:title "Periode"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapportering/664846" ;
    dct:title "Rapportering"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson1/664845>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson2/664844>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/periode/664926>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapporteringsregisteret/664900> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Rapporteringsregsregisteret/660291" ;
    dct:title "Rapporteringsregisteret"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Regnskap/445940" ;
    dct:title "Regnskap"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RentepapirerType/665072" ;
    dct:title "RentepapirerType"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Restruktureringsavsetning/446014" ;
    dct:title "Restruktureringsavsetning"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Resultatpost/445965" ;
    dct:title "Resultatpost"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontantstrøm/445962>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/nedskriving/445958> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsberetning/600181" ;
    dct:title "Revisjonsberetning"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Revisjonsutvalg/622409" ;
    dct:title "Revisjonsutvalg"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgFaktorer/622399>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgKriterier/622403> .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgFaktorer/622389" ;
    dct:title "RevisjonsutvalgFaktorer"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/RevisjonsutvalgKriterier/622398" ;
    dct:title "RevisjonsutvalgKriterier"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Skattefordel/445982" ;
    dct:title "Skattefordel"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Utviklingsutgift/446018" ;
    dct:title "Utviklingsutgift"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/Virksomhetssammenslutninger/445923" ;
    dct:title "Virksomhetssammenslutninger"@nb .

<http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Dataobjekttype/ifrs16leiekontrakterutleiereksterne/771975" ;
    dct:title "Ifrs16leiekontrakterutleiereksterne"@nb .

<http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114" ;
    dct:title "KRT-1003v3_M"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953>,
        <http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009>,
        <http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853>,
        <http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatId>,
        <http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatProvider>,
        <http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatVersion> .

<http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatId> a ns1:Attribute ;
    dct:title "dataFormatId"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatProvider> a ns1:Attribute ;
    dct:title "dataFormatProvider"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/Meldingsmodell/KRT-1003v3_M/446114/dataFormatVersion> a ns1:Attribute ;
    dct:title "dataFormatVersion"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757" ;
    dct:title "RegnskapAr-17102"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757/guid> .

<http://seres.no/guid/Finanstilsynet/ORDataenkeltype/RegnskapAr-17102/10757/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494" ;
    dct:title "ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsregnskapDelarsregnskapTidligereArsAvdeketVesentligeFeil-31960/11494/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567" ;
    dct:title "ArsresultatNegativSisteToAr-23744"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/ArsresultatNegativSisteToAr-23744/11567/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529" ;
    dct:title "AvsetningRestrukturering-23767"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering-23767/11529/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638" ;
    dct:title "AvsetningRestrukturering25ResultatForSkatt-23769"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering25ResultatForSkatt-23769/11638/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495" ;
    dct:title "AvsetningRestrukturering5ResultatForSkatt-23768"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningRestrukturering5ResultatForSkatt-23768/11495/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598" ;
    dct:title "AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig10AvEgenkapital-23764/11598/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452" ;
    dct:title "AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/AvsetningerForpliktelserKortsiktig50AvEgenkapital-23765/11452/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506" ;
    dct:title "DriftsresultatNegativSisteToAr-23742"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/DriftsresultatNegativSisteToAr-23742/11506/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448" ;
    dct:title "EgenkapitalAndel10-23775"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalAndel10-23775/11448/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616" ;
    dct:title "EgenkapitalKorrigertNegativ-23776"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EgenkapitalKorrigertNegativ-23776/11616/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler-23755/11609/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler10EK-23756/11527/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539" ;
    dct:title "EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelMarkedsverdibasertUtoverFinansielleEiendeler50EK-23757/11539/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540" ;
    dct:title "EiendelerImmaterielle10AvEgenkapital-23759"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle10AvEgenkapital-23759/11540/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571" ;
    dct:title "EiendelerImmaterielle50AvEgenkapital-23760"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielle50AvEgenkapital-23760/11571/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460" ;
    dct:title "EiendelerImmaterielleAndre-23758"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EiendelerImmaterielleAndre-23758/11460/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485" ;
    dct:title "EnhetAksjerStorstKursoppgangKursnedgang-23724"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetAksjerStorstKursoppgangKursnedgang-23724/11485/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580" ;
    dct:title "EnhetBorsnotertOBXIndeksutvalg-23723"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBorsnotertOBXIndeksutvalg-23723/11580/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572" ;
    dct:title "EnhetBransje-23719"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetBransje-23719/11572/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488" ;
    dct:title "EnhetEksternRevisorSkifteSisteToAr-23729"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEksternRevisorSkifteSisteToAr-23729/11488/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602" ;
    dct:title "EnhetEtiskeRetningslinjerOffentliggjorte-23725"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetEtiskeRetningslinjerOffentliggjorte-23725/11602/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570" ;
    dct:title "EnhetKonsernregnskap-23722"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetKonsernregnskap-23722/11570/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611" ;
    dct:title "EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/EnhetStyrelederToppledelseEkstraordinartSkifteSisteTreAr-23726/11611/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475" ;
    dct:title "FinansielleInstrumenterUnoterteEidUtstedt-23752"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/FinansielleInstrumenterUnoterteEidUtstedt-23752/11475/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532" ;
    dct:title "GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter25ResultatForSkatt-23754/11532/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537" ;
    dct:title "GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/GevinstTapFinansielleInstrumenter5ResultatForSkatt-23753/11537/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526" ;
    dct:title "IFRSKravFraveketKravMedHensikt-31961"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/IFRSKravFraveketKravMedHensikt-31961/11526/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590" ;
    dct:title "Inntektsvekst25SisteAr50TreSisteAr-23779"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Inntektsvekst25SisteAr50TreSisteAr-23779/11590/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474" ;
    dct:title "InsentivordningAksjebasert-23730"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/InsentivordningAksjebasert-23730/11474/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510" ;
    dct:title "KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjDriftInvesteringerOverstigerArsresultat-23740/11510/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523" ;
    dct:title "KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/KontantstromOperasjonelleDriftsaktiviteterOverstigerArsresultat-23739/11523/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610" ;
    dct:title "LanebetingelserBruddDispensasjon-23778"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/LanebetingelserBruddDispensasjon-23778/11610/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478" ;
    dct:title "Nedskrivninger-23745"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger-23745/11478/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484" ;
    dct:title "Nedskrivninger25ResultatForSkatt-23748"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger25ResultatForSkatt-23748/11484/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562" ;
    dct:title "Nedskrivninger5ResultatForSkatt-23747"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Nedskrivninger5ResultatForSkatt-23747/11562/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560" ;
    dct:title "NedskrivningerNegativResultatForSkatt-23749"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/NedskrivningerNegativResultatForSkatt-23749/11560/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441" ;
    dct:title "Regnskapsstandard-31959"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/Regnskapsstandard-31959/11441/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591" ;
    dct:title "SikringsbokfoeringFinansielleInstrumenter-23751"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SikringsbokføringFinansielleInstrumenter-23751/11591/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453" ;
    dct:title "SkattesakerVesentligeTapteSisteToAr-23780"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/SkattesakerVesentligeTapteSisteToAr-23780/11453/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473" ;
    dct:title "UtsattSkattefordel-23761"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordel-23761/11473/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535" ;
    dct:title "UtsattSkattefordelResultateffekt25ResultatForSkatt-23763"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt25ResultatForSkatt-23763/11535/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490" ;
    dct:title "UtsattSkattefordelResultateffekt5ResultatForSkatt-23762"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtsattSkattefordelResultateffekt5ResultatForSkatt-23762/11490/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566" ;
    dct:title "UtviklingskostnaderBalanseforte10AvEgenkapital-23773"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte10AvEgenkapital-23773/11566/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636" ;
    dct:title "UtviklingskostnaderBalanseforte50AvEgenkapital-23774"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/UtviklingskostnaderBalanseforte50AvEgenkapital-23774/11636/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588" ;
    dct:title "VerdsettelsePrisBok1-23746"@nb ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588/guid> .

<http://seres.no/guid/Finanstilsynet/ORDatakodeutvalg/VerdsettelsePrisBok1-23746/11588/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

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

<http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Meldingsmodell/Maalekort_M/634513" ;
    dct:title "Maalekort_M"@nb ;
    ns1:hasProperty <http://seres.no/guid/NAV/Meldingsdel/skjema/634646> .

<http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150" ;
    dct:title "EgenkapitalMorforetaketsAksjeeiere-34067"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150/guid> .

<http://seres.no/guid/ORDataenkeltype/EgenkapitalMorforetaketsAksjeeiere-34067/374150/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170" ;
    dct:title "ForetakBorsverdi-34065"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170/guid> .

<http://seres.no/guid/ORDataenkeltype/ForetakBorsverdi-34065/374170/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128" ;
    dct:title "Grunnfondsbevis-34215"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128/guid> .

<http://seres.no/guid/ORDataenkeltype/Grunnfondsbevis-34215/374128/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133" ;
    dct:title "Obligasjon-34214"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133/guid> .

<http://seres.no/guid/ORDataenkeltype/Obligasjon-34214/374133/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215" ;
    dct:title "VerdipapirutstederAksje-34213"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215/guid> .

<http://seres.no/guid/ORDataenkeltype/VerdipapirutstederAksje-34213/374215/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler10-34069/374118/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197" ;
    dct:title "RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RegnskapsforingVirksomhetssammenslutningEndringEiendeler25-34070/374197/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211" ;
    dct:title "RevisjonsberetningUtenAvvik-34066"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211/guid> .

<http://seres.no/guid/ORDatakodeutvalg/RevisjonsberetningUtenAvvik-34066/374211/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

<http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089> a ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089" ;
    dct:title "UtstederIdentifisertOvertakerOverdrager-34068"@nb ;
    ns1:hasProperty <http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089/guid> .

<http://seres.no/guid/ORDatakodeutvalg/UtstederIdentifisertOvertakerOverdrager-34068/374089/guid> a ns1:Attribute ;
    dct:title "guid"@nb ;
    ns1:hasSimpleType <https://altinn.fellesdatakatalog.digdir.no#String> .

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

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/840747972> a foaf:Agent ;
    foaf:name "Finanstilsynet"@nb .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/889640782> a foaf:Agent ;
    foaf:name "Arbeids- og velferdsetaten"@nb .

<http://localhost:8000/api/metadata/formtask/3906/141205/forms/3940/20161021/Arbeidsgiveravgift/Arbeidsgiveravgiftsgrunnlag> a ns1:ObjectType .

<http://localhost:8000/api/metadata/formtask/4942/2017/forms/sofus/17091115/Folkeregisterkandidat/Kontaktadresse> a ns1:ObjectType .

<http://seres.no/guid/Finanstilsynet/Dataegenskap/utstedertype/445918> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "utstedertype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Dataegenskap/utstedertype/445918> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/adresse/664847> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "adresse"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/adresse/664847> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/alternativeResultatmål/664901> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "alternativeResultatmaal"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/alternativeResultatmål/664901> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/andreForhold/446000> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "andreForhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/andreForhold/446000> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/egenkapital/446002> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "egenkapital"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/egenkapital/446002> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/forpliktelseAvsetning/446004> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "forpliktelseAvsetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/forpliktelseAvsetning/446004> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15/771902> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs15"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15/771902> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15kategorier/771957> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs15kategorier"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15kategorier/771957> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15vurderinger/771900> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs15vurderinger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs15vurderinger/771900> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16/771888> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs16"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16/771888> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterleietaker/771981> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs16leiekontrakterleietaker"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterleietaker/771981> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterutleiereksterne/771983> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs16leiekontrakterutleiereksterne"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16leiekontrakterutleiereksterne/771983> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurderinger/771970> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs16vurderinger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurderinger/771970> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurdertikkeeffekt/771976> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs16vurdertikkeeffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs16vurdertikkeeffekt/771976> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs9/771947> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrs9"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrs9/771947> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrsandre/771950> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrsandre"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrsandre/771950> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrseffekt/771942> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "ifrseffekt"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/ifrseffekt/771942> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/immatriellEiendel/446005> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "immatriellEiendel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/immatriellEiendel/446005> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/innsender/664852> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "innsender"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/innsender/664852> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson1/664845> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "kontaktperson1"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson1/664845> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson2/664844> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "kontaktperson2"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontaktperson2/664844> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontantstrøm/445962> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "kontantstroem"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/kontantstrøm/445962> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/markedsverdibasertEiendel/446006> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "markedsverdibasertEiendel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/markedsverdibasertEiendel/446006> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/nedskriving/445958> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "nedskriving"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/nedskriving/445958> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/organisasjonsforhold/446008> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "organisasjonsforhold"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/organisasjonsforhold/446008> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/periode/664926> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "periode"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/periode/664926> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapportering/664851> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "rapportering"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapportering/664851> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapporteringsregisteret/664900> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "rapporteringsregisteret"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapporteringsregisteret/664900> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/regnskap/445951> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "regnskap"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/regnskap/445951> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rentepapirertype/665073> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "rentepapirertype"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rentepapirertype/665073> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/restruktureringsavsetning/446003> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "restruktureringsavsetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/restruktureringsavsetning/446003> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/resultatpost/446007> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "resultatpost"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/resultatpost/446007> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsberetning/600187> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "revisjonsberetning"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsberetning/600187> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalg/622454> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "revisjonsutvalg"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalg/622454> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgFaktorer/622399> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "revisjonsutvalgFaktorer"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgFaktorer/622399> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgKriterier/622403> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "revisjonsutvalgKriterier"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/revisjonsutvalgKriterier/622403> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utsattSkattefordel/445942> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "utsattSkattefordel"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utsattSkattefordel/445942> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utviklingsutgift/445941> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "utviklingsutgift"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/utviklingsutgift/445941> .

<http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/virksomhetssammenslutninger/446001> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "virksomhetssammenslutninger"@nb ;
    xsd:maxOccurs 1 ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/virksomhetssammenslutninger/446001> .

<http://seres.no/guid/NAV/DataTypeegenskap/data/634499> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "data"@nb ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/DataTypeegenskap/data/634499> .

<http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "indikatordata"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/DataTypeegenskap/identikatordata/634501> .

<http://seres.no/guid/NAV/Dataegenskap/dato/634644> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "dato"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Dataegenskap/dato/634644> .

<http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "geografiskOmraadeMedIndikatordata"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643> .

<http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> a ns1:Attribute,
        ns1:ObjectType ;
    dct:title "fagsystem"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasType <http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> .

<https://altinn.fellesdatakatalog.digdir.no#Integer> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#Integer" ;
    dct:title "Integer"@en ;
    xsd:anyURI xsd:decimal .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> a foaf:Agent ;
    foaf:name "Skatteetaten"@nb .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953> a ns1:Attribute,
        ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953" ;
    dct:title "RapportKRT-1003"@nb,
        "rapportKRT-1003"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Dataegenskap/utstedertype/445918>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/regnskap/445951>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rentepapirertype/665073> ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Meldingsdel/RapportKRT-1003/445953> .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009> a ns1:Attribute,
        ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009" ;
    dct:title "SkjemainnholdKRT-1003"@nb,
        "skjemainnholdKRT-1003"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
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
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/virksomhetssammenslutninger/446001> ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Meldingsdel/SkjemainnholdKRT-1003/446009> .

<http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853> a ns1:Attribute,
        ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853" ;
    dct:title "Rapport"@nb,
        "rapport"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasProperty <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/innsender/664852>,
        <http://seres.no/guid/Finanstilsynet/Relasjonsegenskap/rapportering/664851> ;
    ns1:hasType <http://seres.no/guid/Finanstilsynet/Meldingsdel/rapport/664853> .

<http://seres.no/guid/NAV/Meldingsdel/skjema/634646> a ns1:Attribute,
        ns1:ObjectType ;
    dct:identifier "http://seres.no/guid/NAV/Meldingsdel/skjema/634646" ;
    dct:title "Skjema"@nb,
        "skjema"@nb ;
    xsd:maxOccurs 1 ;
    xsd:minOccurs 1 ;
    ns1:hasProperty <http://seres.no/guid/NAV/Dataegenskap/dato/634644>,
        <http://seres.no/guid/NAV/Dataegenskap/geografiskOmraadeMedIndikatordata/634643>,
        <http://seres.no/guid/NAV/Relasjonsegenskap/fagsystem/634645> ;
    ns1:hasType <http://seres.no/guid/NAV/Meldingsdel/skjema/634646> .

<https://altinn.fellesdatakatalog.digdir.no#PositiveInteger> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#PositiveInteger" ;
    dct:title "PositiveInteger"@en ;
    xsd:anyURI xsd:decimal .

<https://altinn.fellesdatakatalog.digdir.no#String> a ns1:SimpleType ;
    dct:identifier "https://altinn.fellesdatakatalog.digdir.no#String" ;
    dct:title "String"@en ;
    xsd:anyURI xsd:string ."""
