"""Utility methods for mapping process."""
import os
import re
from typing import Dict, Optional

from datacatalogtordf import Agent
from modelldcatnotordf.modelldcatno import SimpleType
from xmlschema import XMLSchema

from altinn_model_publisher.organizations.organizations import map_shortname_to_org

ORG_URI = os.getenv(
    "ORGANIZATION_CATALOGUE_URI",
    "https://organization-catalogue.fellesdatakatalog.digdir.no",
)
SELF_URI = os.getenv(
    "ALTINN_MODEL_PUBLISHER_URI", "https://altinn-model-publisher.digdir.no"
)


def create_model_uri_identifier(data: Dict) -> str:
    """Create a URI identifier for the model from relevant codes."""
    service = data["service_meta"]["ServiceCode"]
    data_format = data["forms_meta"]["DataFormatID"]
    return f"""{SELF_URI}/models/{service}-{data_format}"""


def extract_model_title(data: Dict) -> Dict[str, str]:
    """Extract form name as title, with service name as backup."""
    form_name = data["forms_meta"].get("FormName")
    if form_name:
        return {"nb": form_name}
    else:
        return {"nb": data["service_meta"].get("ServiceName")}


def extract_model_publisher(data: Dict) -> Optional[Agent]:
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


def uri_safe_string(input: str) -> str:
    """Remove unsafe characters from input."""
    match_non_safe = "[^-\]_.~!*'();:@&=+$,/?%#[A-z0-9æÆøØåÅ]"  # noqa: W605
    return re.sub(match_non_safe, "", input) if isinstance(input, str) else ""


def xsd_uri_identifier(data: XMLSchema) -> str:
    """Create URI-identifier for XSD-types."""
    if data.content_type_label and "simple" in data.content_type_label:
        return f"{data.primitive_type.target_namespace}#{uri_safe_string(data.primitive_type.id)}"
    else:
        return f"{data.target_namespace}#{uri_safe_string(data.id)}"


def extract_seres_guid(data: XMLSchema) -> Optional[str]:
    """Extract seres GUID from xsd-data."""
    if (
        hasattr(data, "schema_elem")
        and hasattr(data.schema_elem, "attrib")
        and data.schema_elem.attrib
    ):
        for attrib_key in data.schema_elem.attrib:
            if "seres" in attrib_key and "guid" in attrib_key:
                return uri_safe_string(data.schema_elem.attrib[attrib_key])
    return None


def uri_identifier(
    data: XMLSchema, model_namespace: str, capitalize: bool
) -> Optional[str]:
    """Create URI-identifier from namespace and name."""
    identifier = None

    if hasattr(data, "prefixed_name") and data.prefixed_name:
        if "xs:" in data.prefixed_name or "xsd:" in data.prefixed_name:
            identifier = xsd_uri_identifier(data)
        else:
            safe_name = uri_safe_string(data.prefixed_name)
            capitalized_name = (
                first_character_upper_case(safe_name)
                if capitalize
                else first_character_lower_case(safe_name)
            )
            identifier = f"{model_namespace}{capitalized_name}"
    elif (
        hasattr(data, "base_type")
        and hasattr(data.base_type, "prefixed_name")
        and data.base_type.prefixed_name
    ):
        if (
            "xs:" in data.base_type.prefixed_name
            or "xsd:" in data.base_type.prefixed_name
        ):
            identifier = xsd_uri_identifier(data.base_type)
        else:
            safe_name = uri_safe_string(data.base_type.prefixed_name)
            capitalized_name = (
                first_character_upper_case(safe_name)
                if capitalize
                else first_character_lower_case(safe_name)
            )
            identifier = f"{model_namespace}{capitalized_name}"

    return identifier


def create_simple_type(input_data: XMLSchema, model_namespace: str) -> SimpleType:
    """Create Model Element - Simple Type."""
    simple_type = SimpleType()
    if (
        hasattr(input_data, "base_type")
        and hasattr(input_data.base_type, "prefixed_name")
        and input_data.base_type.prefixed_name
        and (
            not hasattr(input_data, "prefixed_name") or input_data.prefixed_name is None
        )
    ):
        data = input_data.base_type
    else:
        data = input_data

    identifier = uri_identifier(data, model_namespace, True)
    if identifier and "http://www.w3.org/2001/XMLSchema#" in identifier:
        simple_type_name = first_character_upper_case(data.id)
        simple_type.identifier = f"{SELF_URI}#{simple_type_name}"
        simple_type.dct_identifier = f"{SELF_URI}#{simple_type_name}"
        simple_type.title = {"en": simple_type_name}
        simple_type.type_definition_reference = identifier
    else:
        simple_type.identifier = identifier
        simple_type.dct_identifier = identifier
        simple_type.title = {"nb": first_character_upper_case(data.prefixed_name)}
        simple_type.type_definition_reference = (
            f"{data.primitive_type.target_namespace}#{data.primitive_type.id}"
        )
    simple_type.min_length = data.min_length
    simple_type.max_length = data.max_length

    if data.patterns and len(data.patterns.patterns) > 0:
        simple_type.pattern = data.patterns.patterns[0].pattern

    return simple_type


def first_character_lower_case(input: str) -> str:
    """Ensure that the first character of the input string is lower case."""
    if len(input) > 2:
        return input[0].lower() + input[1:]
    if len(input) == 1:
        return input[0].lower()
    return input


def first_character_upper_case(input: str) -> str:
    """Ensure that the first character of the input string is upper case."""
    if len(input) > 2:
        return input[0].upper() + input[1:]
    if len(input) == 1:
        return input[0].upper()
    return input
