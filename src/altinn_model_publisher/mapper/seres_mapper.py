"""Mappers to create InformationModel from Seres data."""
from typing import List, Optional

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
    XsdElement,
    XsdGroup,
)

from .mapper_utils import (
    create_simple_type,
    extract_seres_guid,
    first_character_lower_case,
    first_character_upper_case,
    uri_identifier,
)


def create_model_from_seres_xsd(xsd_data: XMLSchema) -> InformationModel:
    """Create InformationModel object from Seres xsd."""
    model = InformationModel()
    model_namespace = f"{xsd_data.base_url}/"

    for model_element_key in xsd_data.elements:
        model_element = create_seres_model_element(
            xsd_data.elements[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    for model_element_key in xsd_data.types:
        model_element = create_seres_model_element(
            xsd_data.types[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    for model_element_key in xsd_data.groups:
        model_element = create_seres_model_element(
            xsd_data.groups[model_element_key], model_namespace
        )
        model.modelelements.append(model_element)

    return model


def seres_model_properties_from_content(
    content_data: Optional[XMLSchema], model_namespace: str
) -> List[ModelProperty]:
    """Create list of properties from element content."""
    model_properties = []
    if content_data:
        if isinstance(content_data, XsdGroup):
            for group_data in content_data:
                model_properties.extend(
                    seres_model_properties_from_content(group_data, model_namespace)
                )
        elif hasattr(content_data, "prefixed_name"):
            prop = create_seres_model_property(content_data, model_namespace)
            if prop:
                model_properties.append(prop)

    return model_properties


def create_seres_model_element(
    data: XMLSchema, model_namespace: str
) -> Optional[ModelElement]:
    """Create Model Element."""
    model_element = None
    seres_guid = extract_seres_guid(data)
    identifier = (
        seres_guid if seres_guid else uri_identifier(data, model_namespace, True)
    )
    if identifier:
        if hasattr(data, "primitive_type"):
            model_element = create_simple_type(data, model_namespace)
        else:
            model_element = ObjectType()
            model_element.identifier = identifier
            model_element.dct_identifier = identifier
            model_element.title = {"nb": first_character_upper_case(data.prefixed_name)}

        if hasattr(data, "attributes"):
            for attribute_key in data.attributes:
                if attribute_key:
                    model_property = create_seres_model_property(
                        data.attributes[attribute_key], f"{identifier}/"
                    )
                    if model_property:
                        model_element.has_property.append(model_property)

        if hasattr(data, "content"):
            content_properties = seres_model_properties_from_content(
                data.content, f"{identifier}/"
            )
            model_element.has_property.extend(content_properties)
    return model_element


def create_seres_model_property(
    data: XMLSchema, model_namespace: str
) -> Optional[ModelProperty]:
    """Create Model Property."""
    model_property = None
    if isinstance(data, XsdAttribute):
        model_property = Attribute()
    elif isinstance(data, XsdElement):
        model_property = Attribute()

    if model_property and hasattr(data, "prefixed_name") and data.prefixed_name:
        seres_guid = extract_seres_guid(data)
        identifier = (
            seres_guid if seres_guid else uri_identifier(data, model_namespace, False)
        )
        if identifier:
            model_property.identifier = identifier
            model_property.title = {
                "nb": first_character_lower_case(data.prefixed_name)
            }

            type_ref_data = None
            if hasattr(data, "type") and data.type is not None:
                type_ref_data = data.type
            elif hasattr(data, "ref") and data.ref is not None:
                type_ref_data = data.ref

            if hasattr(type_ref_data, "primitive_type"):
                seres_guid = extract_seres_guid(data)
                type_ref_identifier = (
                    seres_guid
                    if seres_guid
                    else uri_identifier(type_ref_data, model_namespace, True)
                )
                if type_ref_identifier:
                    if "http://www.w3.org/2001/XMLSchema#" in type_ref_identifier:
                        type_ref = create_simple_type(type_ref_data, model_namespace)
                    else:
                        type_ref = SimpleType()
                        type_ref.identifier = type_ref_identifier
                    model_property.has_simple_type = type_ref
            elif type_ref_data and type_ref_data.prefixed_name:
                type_ref = ObjectType()
                seres_guid = extract_seres_guid(data)
                type_ref.identifier = (
                    seres_guid
                    if seres_guid
                    else uri_identifier(type_ref_data, model_namespace, True)
                )
                if type_ref.identifier:
                    model_property.has_type.append(type_ref)

            if hasattr(data, "occurs"):
                model_property.min_occurs = data.occurs[0]
                model_property.max_occurs = data.occurs[1]
    return model_property
