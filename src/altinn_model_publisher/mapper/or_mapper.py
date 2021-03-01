"""Mappers to create InformationModel from OR data."""
from typing import Optional

from modelldcatnotordf.modelldcatno import (
    Attribute,
    CodeList,
    Composition,
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
)

from .mapper_utils import (
    create_simple_type,
    first_character_lower_case,
    first_character_upper_case,
    is_code_list,
    uri_identifier,
)


def create_model_from_or_xsd(xsd_data: XMLSchema) -> InformationModel:
    """Create InformationModel object from OR xsd."""
    model = InformationModel()
    model_namespace = f"{xsd_data.base_url}/"

    for model_element_key in xsd_data.elements:
        model_element = create_or_model_element(
            xsd_data.elements[model_element_key], model_namespace
        )
        if model_element:
            model.modelelements.append(model_element)

    for model_element_key in xsd_data.types:
        model_element = create_or_model_element(
            xsd_data.types[model_element_key], model_namespace
        )
        if model_element:
            model.modelelements.append(model_element)

    for model_element_key in xsd_data.groups:
        model_element = create_or_model_element(
            xsd_data.groups[model_element_key], model_namespace
        )
        if model_element:
            model.modelelements.append(model_element)

    return model


def create_or_model_element(
    data: XMLSchema, model_namespace: str
) -> Optional[ModelElement]:
    """Create Model Element."""
    model_element = None
    identifier = uri_identifier(data, model_namespace, True)
    if identifier:
        if is_code_list(data):
            model_element = CodeList()
            model_element.identifier = identifier
            model_element.dct_identifier = identifier
            model_element.title = {"nb": first_character_upper_case(data.prefixed_name)}
        elif hasattr(data, "primitive_type"):
            model_element = create_simple_type(data, model_namespace)
        else:
            model_element = ObjectType()
            model_element.identifier = identifier
            model_element.dct_identifier = identifier
            model_element.title = {"nb": first_character_upper_case(data.prefixed_name)}

        if hasattr(data, "attributes"):
            for attribute_key in data.attributes:
                if attribute_key:
                    model_property = create_or_model_property(
                        data.attributes[attribute_key],
                        model_namespace,
                        f"{identifier}/",
                    )
                    if model_property:
                        model_element.has_property.append(model_property)

        if (
            hasattr(data, "type")
            and hasattr(data.type, "model_group")
            and data.type.model_group
        ):
            for model_group_data in data.type.model_group:
                model_property = create_or_group_model_property(
                    model_group_data, model_namespace, f"{identifier}/"
                )
                if model_property:
                    model_element.has_property.append(model_property)

    return model_element


def create_or_model_property(
    data: XMLSchema, model_namespace: str, element_namespace: str
) -> Optional[ModelProperty]:
    """Create Model Property."""
    model_property = None
    if isinstance(data, XsdAttribute):
        model_property = Attribute()
    elif isinstance(data, XsdElement):
        model_property = Attribute()

    if model_property and hasattr(data, "prefixed_name") and data.prefixed_name:
        identifier = uri_identifier(data, element_namespace, False)
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

            if is_code_list(type_ref_data):
                type_ref = CodeList()
                type_ref_identifier = uri_identifier(
                    type_ref_data, model_namespace, True
                )
                if type_ref_identifier:
                    type_ref.identifier = type_ref_identifier
                    model_property.has_value_from = type_ref
            elif hasattr(type_ref_data, "primitive_type"):
                type_ref_identifier = uri_identifier(
                    type_ref_data, model_namespace, True
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
                type_ref_identifier = uri_identifier(
                    type_ref_data, model_namespace, True
                )
                if type_ref_identifier:
                    type_ref.identifier = type_ref_identifier
                    model_property.contains_object_type = type_ref

            if hasattr(data, "occurs"):
                model_property.min_occurs = data.occurs[0]
                model_property.max_occurs = data.occurs[1]
    return model_property


def create_or_group_model_property(
    data: XMLSchema, model_namespace: str, element_namespace: str
) -> Optional[ModelProperty]:
    """Create group Model Property."""
    model_property = None
    if hasattr(data, "prefixed_name") and data.prefixed_name:
        if "-grp-" in data.prefixed_name:
            model_property = Composition()
        elif "-datadef-" in data.prefixed_name:
            model_property = Attribute()

        if model_property:
            identifier = uri_identifier(data, element_namespace, False)
            if identifier:
                model_property.identifier = identifier
                model_property.title = {
                    "nb": first_character_lower_case(data.prefixed_name)
                }

                if hasattr(data, "primitive_type"):
                    type_ref = SimpleType()
                else:
                    type_ref = ObjectType()
                type_ref.identifier = uri_identifier(data, model_namespace, True)
                model_property.has_type.append(type_ref)
    return model_property
