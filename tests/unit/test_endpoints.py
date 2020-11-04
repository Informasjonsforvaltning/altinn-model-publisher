"""Unit test cases for the uri endpoints service module."""
import pytest

from altinn_model_publisher.service.altinn_endpoints import forms_task_uri, xsd_uri


@pytest.mark.unit
def test_forms_task_uri() -> None:
    """Should return endpoint."""
    endpoint = forms_task_uri("1", "2")

    assert endpoint == "/api/metadata/formtask/1/2"


@pytest.mark.unit
def test_forms_task_uri_missing_service_code() -> None:
    """Should return None when service code is None."""
    endpoint = forms_task_uri(None, "1")

    assert endpoint is None


@pytest.mark.unit
def test_forms_task_uri_missing_edition() -> None:
    """Should return None when service edition code is None."""
    endpoint = forms_task_uri("1", None)

    assert endpoint is None


@pytest.mark.unit
def test_xsd_uri() -> None:
    """Should return xsd endpoint."""
    endpoint = xsd_uri("1", "2", "3", "4")

    assert endpoint == "/api/metadata/formtask/1/2/forms/3/4/xsd"


@pytest.mark.unit
def test_xsd_uri_missing_codes() -> None:
    """Should return False when not ready."""
    missing_service_code = xsd_uri(None, "2", "3", "4")
    missing_edition = xsd_uri("1", None, "3", "4")
    missing_format_id = xsd_uri("1", "2", None, "4")
    missing_version = xsd_uri("1", "2", "3", None)

    assert missing_service_code is None
    assert missing_edition is None
    assert missing_format_id is None
    assert missing_version is None
