"""Mappers to create InformationModel from altinn data."""
import os
from typing import Dict, Optional

from datacatalogtordf import Agent
from modelldcatnotordf.modelldcatno import InformationModel

from altinn_model_publisher.organizations.organizations import map_shortname_to_org


ORG_URI = os.getenv(
    "ORGANIZATION_CATALOGUE_URI",
    "https://organization-catalogue.fellesdatakatalog.digdir.no",
)
SELF_URI = os.getenv(
    "ALTINN_MODEL_PUBLISHER_URI", "https://altinn-model-publisher.digdir.no"
)


def map_model_from_dict(data: Dict) -> InformationModel:
    """Map altinn data dict to InformationModel object."""
    model = InformationModel()
    model.identifier = create_uri_identifier(data)
    model.title = extract_title(data)

    publisher = extract_publisher(data)
    if publisher:
        model.publisher = publisher

    return model


def create_uri_identifier(data: Dict) -> str:
    """Create a URI identifier for the model from relevant codes."""
    service = data["service_meta"]["ServiceCode"]
    data_format = data["forms_meta"]["DataFormatID"]
    return f"""{SELF_URI}/models/{service}-{data_format}"""


def extract_title(data: Dict) -> Dict[str, str]:
    """Extract form name as title, with service name as backup."""
    form_name = data["forms_meta"].get("FormName")
    if form_name:
        return {"nb": form_name}
    else:
        return {"nb": data["service_meta"].get("ServiceName")}


def extract_publisher(data: Dict) -> Optional[Agent]:
    """Use organization shortname to create publisher."""
    shortname = data["service_meta"].get("ServiceOwnerCode")
    if shortname:
        org = map_shortname_to_org(shortname)
        if org:
            publisher = Agent()
            publisher.identifier = f"""{ORG_URI}/organizations/{org.orgnr}"""

            publisher.name = {"nb": org.name}
            publisher.orgnr = org.orgnr
            publisher.sameas = (
                f"https://data.brreg.no/enhetsregisteret/api/enheter/{org.orgnr}"
            )

            return publisher

    return None
