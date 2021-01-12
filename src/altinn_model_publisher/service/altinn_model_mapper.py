"""Mappers to create InformationModel from altinn data."""
import os
import re
from typing import Dict, List, Optional

from datacatalogtordf import Agent
from modelldcatnotordf.modelldcatno import (
    Attribute,
    InformationModel,
    ModelElement,
    ModelProperty,
    ObjectType,
    SimpleType,
)
from xmlschema import XMLSchema
from xmlschema.validators import (
    XsdAttribute,
    XsdComplexType,
    XsdElement,
    XsdGroup,
)

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
    model_namespace = f"{data['schema'].base_url}/"

    for model_element_key in data["schema"].elements:
        model_element = create_model_element(
            data["schema"].elements[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    for model_element_key in data["schema"].types:
        model_element = create_model_element(
            data["schema"].types[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    for model_element_key in data["schema"].groups:
        model_element = create_model_element(
            data["schema"].groups[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    model.identifier = create_model_uri_identifier(data)
    model.title = extract_title(data)

    publisher = extract_publisher(data)
    if publisher:
        model.publisher = publisher
    return model


def create_model_uri_identifier(data: Dict) -> str:
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


def uri_safe_string(input: str) -> str:
    """Remove unsafe characters from input."""
    match_non_safe = "[^-\]_.~!*'();:@&=+$,/?%#[A-z0-9]"  # noqa: W605
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


def uri_identifier(data: XMLSchema, model_namespace: str) -> Optional[str]:
    """Create URI-identifier from namespace and name."""
    identifier = None
    seres_guid = extract_seres_guid(data)

    if seres_guid:
        identifier = seres_guid
    elif hasattr(data, "prefixed_name") and data.prefixed_name:
        if "xs:" in data.prefixed_name or "xsd:" in data.prefixed_name:
            identifier = xsd_uri_identifier(data)
        else:
            identifier = f"{model_namespace}{uri_safe_string(data.prefixed_name)}"
    elif (
        hasattr(data, "base_type")
        and hasattr(data.base_type, "prefixed_name")
        and data.base_type.prefixed_name
    ):
        identifier = f"{model_namespace}{uri_safe_string(data.base_type.prefixed_name)}"

    return identifier


def create_simple_type(data: XMLSchema) -> SimpleType:
    """Create Model Element - Simple Type."""
    simple_type = SimpleType()
    simple_type.type_definition_reference = (
        f"{data.primitive_type.target_namespace}#{data.primitive_type.id}"
    )
    simple_type.min_length = data.min_length
    simple_type.max_length = data.max_length

    if data.patterns and len(data.patterns.patterns) > 0:
        simple_type.pattern = data.patterns.patterns[0].pattern

    return simple_type


def model_properties_from_content(
    content_data: Optional[XMLSchema], model_namespace: str
) -> List[ModelProperty]:
    """Create list of properties from element content."""
    model_properties = []
    if content_data:
        if isinstance(content_data, XsdGroup):
            for group_data in content_data:
                model_properties.extend(
                    model_properties_from_content(group_data, model_namespace)
                )
        elif hasattr(content_data, "prefixed_name"):
            prop = create_model_property(content_data, model_namespace)
            if prop:
                model_properties.append(prop)

    return model_properties


def create_model_element(
    data: XMLSchema, model_namespace: str
) -> Optional[ModelElement]:
    """Create Model Element."""
    model_element = None
    identifier = uri_identifier(data, model_namespace)
    if identifier:
        if isinstance(data, XsdComplexType):
            model_element = ObjectType()
        elif hasattr(data, "primitive_type"):
            model_element = create_simple_type(data)
        else:
            model_element = ObjectType()

        model_element.identifier = identifier
        model_element.dct_identifier = identifier
        model_element.title = {"nb": data.prefixed_name}

        if hasattr(data, "attributes"):
            for attribute_key in data.attributes:
                if attribute_key:
                    model_property = create_model_property(
                        data.attributes[attribute_key], f"{identifier}/"
                    )
                    if model_property:
                        model_element.has_property.append(model_property)

        if hasattr(data, "content"):
            content_properties = model_properties_from_content(
                data.content, f"{identifier}/"
            )
            model_element.has_property.extend(content_properties)
    return model_element


def create_model_property(
    data: XMLSchema, model_namespace: str
) -> Optional[ModelProperty]:
    """Create Model Property."""
    model_property = None
    if isinstance(data, XsdAttribute):
        model_property = Attribute()
    elif isinstance(data, XsdElement):
        model_property = Attribute()

    if model_property and hasattr(data, "prefixed_name") and data.prefixed_name:
        identifier = uri_identifier(data, model_namespace)
        if identifier:
            model_property.identifier = identifier
            model_property.title = {"nb": data.prefixed_name}

            type_ref_data = None
            if hasattr(data, "type") and data.type is not None:
                type_ref_data = data.type
            elif hasattr(data, "ref") and data.ref is not None:
                type_ref_data = data.ref

            if hasattr(type_ref_data, "primitive_type"):
                type_ref = SimpleType()
                type_ref.identifier = uri_identifier(type_ref_data, model_namespace)
                if type_ref.identifier:
                    model_property.has_simple_type = type_ref
            elif type_ref_data and type_ref_data.prefixed_name:
                type_ref = ObjectType()
                type_ref.identifier = uri_identifier(type_ref_data, model_namespace)
                if type_ref.identifier:
                    model_property.has_type.append(type_ref)

            if hasattr(data, "occurs"):
                model_property.min_occurs = data.occurs[0]
                model_property.max_occurs = data.occurs[1]
    return model_property
