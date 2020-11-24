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
    model_0.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3314-1212-245-10980"
    )
    model_0.title = {"nb": "Sensitive role Reporting"}

    model_1 = InformationModel()
    model_1.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3357-130429-4166-35895"
    )
    model_1.title = {"nb": "A02 a-melding submission from system"}
    model_1.publisher = model_publisher

    model_2 = InformationModel()
    model_2.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3736-170607-4685-1706091129"
    )
    model_2.title = {
        "nb": "A06 a-melding version 3.1.0 order reconciliation information"
    }
    model_2.publisher = model_publisher

    model_3 = InformationModel()
    model_3.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3743-140516-4444-32407"
    )
    model_3.title = {
        "nb": "A04 Declaration of paid work at home where a private individual is the employer"
    }
    model_3.publisher = model_publisher

    model_4 = InformationModel()
    model_4.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3814-140602-4445-32408"
    )
    model_4.title = {
        "nb": "A05 Simplified a-melding for charitable and non-profit organisations"
    }
    model_4.publisher = model_publisher

    model_5 = InformationModel()
    model_5.identifier = (
        "https://altinn.fellesdatakatalog.digdir.no/models/3906-141205-3940-20161021"
    )
    model_5.title = {"nb": "A01 a-melding"}
    model_5.publisher = model_publisher

    altinn_test_catalog.models = [model_0, model_1, model_2, model_3, model_4, model_5]

    return altinn_test_catalog


test_altinn_catalog_turtle = """
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix ns2: <http://www.w3.org/2002/07/owl#> .

<https://www.altinn.no/models/catalog> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/991825827> ;
    dct:title "Altinn informasjonsmodellkatalog"@nb ;
    ns1:model <https://altinn.fellesdatakatalog.digdir.no/models/3314-1212-245-10980>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3357-130429-4166-35895>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3736-170607-4685-1706091129>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3743-140516-4444-32407>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3814-140602-4445-32408>,
        <https://altinn.fellesdatakatalog.digdir.no/models/3906-141205-3940-20161021> .

<https://altinn.fellesdatakatalog.digdir.no/models/3314-1212-245-10980> a ns1:InformationModel ;
    dct:title "Sensitive role Reporting"@nb .

<https://altinn.fellesdatakatalog.digdir.no/models/3357-130429-4166-35895> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A02 a-melding submission from system"@nb .

<https://altinn.fellesdatakatalog.digdir.no/models/3736-170607-4685-1706091129> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A06 a-melding version 3.1.0 order reconciliation information"@nb .

<https://altinn.fellesdatakatalog.digdir.no/models/3743-140516-4444-32407> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A04 Declaration of paid work at home where a private individual is the employer"@nb .

<https://altinn.fellesdatakatalog.digdir.no/models/3814-140602-4445-32408> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A05 Simplified a-melding for charitable and non-profit organisations"@nb .

<https://altinn.fellesdatakatalog.digdir.no/models/3906-141205-3940-20161021> a ns1:InformationModel ;
    dct:publisher <https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> ;
    dct:title "A01 a-melding"@nb .

<https://organization-catalogue.staging.fellesdatakatalog.digdir.no/organizations/974761076> a foaf:Agent ;
    dct:identifier "974761076" ;
    ns2:sameAs <https://data.brreg.no/enhetsregisteret/api/enheter/974761076> ;
    foaf:name "{'nb': 'Skatteetaten'}" ."""
