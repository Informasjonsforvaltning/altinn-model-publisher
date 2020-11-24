"""Mappers to create InformationModel from altinn data."""
import os
from typing import Dict, Optional

from datacatalogtordf import Agent
from modelldcatnotordf.modelldcatno import InformationModel

from altinn_model_publisher.organizations.organizations import map_shortname_to_org


BRREG_ORG_URI = "https://data.brreg.no/enhetsregisteret/api/enheter/"


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
    edition = data["service_meta"]["ServiceEditionCode"]
    data_format = data["forms_meta"]["DataFormatID"]
    version = data["forms_meta"]["DataFormatVersion"]
    return f"""{os.getenv("SELF_URI")}/models/{service}-{edition}-{data_format}-{version}"""


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
            publisher.identifier = (
                f"""{os.getenv("ORG_URI")}/organizations/{org.orgnr}"""
            )

            publisher.name = {"nb": org.name}
            publisher.orgnr = org.orgnr
            publisher.sameas = (
                f"https://data.brreg.no/enhetsregisteret/api/enheter/{org.orgnr}"
            )

            return publisher

    return None
