"""Unit test cases for the model mapper service module."""
import pytest

from altinn_model_publisher.service.altinn_model_mapper import extract_title


@pytest.mark.unit
def test_form_name_prioritized_as_title() -> None:
    """Should return form name."""
    endpoint = extract_title(
        {
            "forms_meta": {"FormName": "Form name"},
            "service_meta": {"ServiceName": "Service name"},
        }
    )

    assert endpoint == {"nb": "Form name"}


@pytest.mark.unit
def test_service_name_added_as_title_when_form_name_missing() -> None:
    """Should return service name when form name missing."""
    endpoint = extract_title(
        {"forms_meta": {}, "service_meta": {"ServiceName": "Service name"}}
    )

    assert endpoint == {"nb": "Service name"}
