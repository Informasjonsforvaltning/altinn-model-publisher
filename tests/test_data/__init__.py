"""Test data module."""
from datacatalogtordf import Agent, Catalog
from modelldcatnotordf.modelldcatno import InformationModel

from .altinn_catalog import altinn_catalog_turtle
from .or_catalog import or_catalog_turtle
from .seres_catalog import seres_catalog_turtle


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
