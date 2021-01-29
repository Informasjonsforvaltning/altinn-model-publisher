"""Unit test cases for the model mapper service module."""
from modelldcatnotordf.modelldcatno import (
    ObjectType,
    SimpleType,
)
import pytest
from xmlschema import XMLSchema

from altinn_model_publisher.mapper.mapper_utils import (
    extract_model_title,
    uri_safe_string,
)
from altinn_model_publisher.mapper.model_mapper import create_model_elements
from altinn_model_publisher.mapper.or_mapper import create_or_model_elements
from altinn_model_publisher.mapper.seres_mapper import create_seres_model_elements
from tests.test_data import test_xsd


@pytest.mark.unit
def test_form_name_prioritized_as_title() -> None:
    """Should return form name."""
    endpoint = extract_model_title(
        {
            "forms_meta": {"FormName": "Form name"},
            "service_meta": {"ServiceName": "Service name"},
        }
    )

    assert endpoint == {"nb": "Form name"}


@pytest.mark.unit
def test_service_name_added_as_title_when_form_name_missing() -> None:
    """Should return service name when form name missing."""
    endpoint = extract_model_title(
        {"forms_meta": {}, "service_meta": {"ServiceName": "Service name"}}
    )

    assert endpoint == {"nb": "Service name"}


@pytest.mark.unit
def test_sets_correct_class_for_different_xsd_types() -> None:
    """Should set correct class for the different types."""
    schema = XMLSchema(test_xsd)

    simple_type = create_model_elements(schema.types["Dato"], "http://namespace.no/")[0]
    complex_type = create_model_elements(
        schema.types["Tidsrom"], "http://namespace.no/"
    )[0]
    complex_list_type = create_model_elements(
        schema.types["TidsromListe"], "http://namespace.no/"
    )[0]
    extension_type = create_model_elements(
        schema.types["DatoExtension"], "http://namespace.no/"
    )[0]

    or_simple_type = create_or_model_elements(
        schema.types["Dato"], "http://namespace.no/"
    )[0]
    or_complex_type = create_or_model_elements(
        schema.types["Tidsrom"], "http://namespace.no/"
    )[0]
    or_complex_list_type = create_or_model_elements(
        schema.types["TidsromListe"], "http://namespace.no/"
    )[0]
    or_extension_type = create_or_model_elements(
        schema.types["DatoExtension"], "http://namespace.no/"
    )[0]

    seres_simple_type = create_seres_model_elements(
        schema.types["Dato"], "http://namespace.no/"
    )[0]
    seres_complex_type = create_seres_model_elements(
        schema.types["Tidsrom"], "http://namespace.no/"
    )[0]
    seres_complex_list_type = create_seres_model_elements(
        schema.types["TidsromListe"], "http://namespace.no/"
    )[0]
    seres_extension_type = create_seres_model_elements(
        schema.types["DatoExtension"], "http://namespace.no/"
    )[0]

    assert isinstance(simple_type, SimpleType)
    assert isinstance(or_simple_type, SimpleType)
    assert isinstance(seres_simple_type, SimpleType)
    assert isinstance(complex_type, ObjectType)
    assert isinstance(or_complex_type, ObjectType)
    assert isinstance(seres_complex_type, ObjectType)
    assert isinstance(complex_list_type, ObjectType)
    assert isinstance(or_complex_list_type, ObjectType)
    assert isinstance(seres_complex_list_type, ObjectType)
    assert isinstance(extension_type, ObjectType)
    assert isinstance(or_extension_type, ObjectType)
    assert isinstance(seres_extension_type, ObjectType)


@pytest.mark.unit
def test_removes_unsafe_characters() -> None:
    """Should remove unsafe characters."""
    result = uri_safe_string("Abc D%e< 12#")
    expected = "AbcDe12#"
    assert result == expected
