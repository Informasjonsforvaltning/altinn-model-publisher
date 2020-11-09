"""Unit test cases for the client module."""
from unittest.mock import Mock

import pytest

from altinn_model_publisher.service.altinn_client import (
    altinn_get_request,
    fetch_altinn_metadata,
    fetch_metadata_with_task_forms,
    get_xsd_data,
)


@pytest.mark.unit
def test_altinn_http_error(mock_altinn_client_http_error: Mock) -> None:
    """Should return None when http error occurs."""
    _result = altinn_get_request("endpoint", {"Accept": "text/plain"})

    assert _result is None


@pytest.mark.unit
def test_altinn_request_no_endpoint() -> None:
    """Should return None when no endpoint given."""
    _result = altinn_get_request(None, {"Accept": "text/plain"})

    assert _result is None


@pytest.mark.unit
def test_fetch_altinn_metadata(mock_altinn_client: Mock) -> None:
    """Should return json parsed as dict."""
    _result = fetch_altinn_metadata()

    assert _result == [{"test": "test"}]


@pytest.mark.unit
def test_fetch_altinn_metadata_parse_error(
    mock_altinn_client_json_parse_error: Mock,
) -> None:
    """Should return empty dict when parse failed."""
    _result = fetch_altinn_metadata()

    assert _result == []


@pytest.mark.unit
def test_fetch_metadata_with_task_forms_parse_error(
    mock_altinn_client_json_parse_error: Mock,
) -> None:
    """Should return empty dict when parse failed."""
    _result = fetch_metadata_with_task_forms("1", "2")

    assert _result == {}


@pytest.mark.unit
def test_get_xsd_data_parse_error(mock_altinn_client_xml_parse_error: Mock) -> None:
    """Should return empty dict when parse failed."""
    _result = get_xsd_data("1", "2", "3", "4")

    assert _result == {}
