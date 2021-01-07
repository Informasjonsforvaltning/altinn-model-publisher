"""Integration test cases for the ready route."""
from unittest.mock import call, Mock

from aiohttp.test_utils import TestClient
import pytest
from rdflib import Graph

from ..test_data import test_altinn_catalog_turtle


@pytest.mark.integration
@pytest.mark.docker
async def test_update(
    client: TestClient,
    docker_service: str,
    mock_save_to_cache: Mock,
    mock_save_update_status: Mock,
    mock_not_running_update_status: Mock,
) -> None:
    """Saved models are updated on post request to /update."""
    response = await client.post("/update", headers={"X-API-KEY": "api-test-secret"})
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"

    set_update_status_calls = [call("update_in_progress"), call("ready_to_update")]
    mock_save_update_status.assert_has_calls(set_update_status_calls)

    mock_save_to_cache.assert_called_once()
    saved = mock_save_to_cache.call_args_list.pop()[0][0]
    saved_rdf = saved.to_rdf().decode()

    expected_graph = Graph().parse(data=test_altinn_catalog_turtle, format="turtle")
    saved_graph = Graph().parse(data=saved_rdf, format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
async def test_update_cancelled_if_other_update_running(
    client: TestClient,
    mock_running_update_status: Mock,
) -> None:
    """Update is cancelled when already running."""
    response = await client.post("/update", headers={"X-API-KEY": "api-test-secret"})
    response_content = await response.content.read()

    assert response.status == 429
    assert response_content.decode() == "Too Many Requests"


@pytest.mark.integration
async def test_update_forbidden_when_key_header_missing(client: TestClient) -> None:
    """Forbidden when header X-API-KEY is missing."""
    response = await client.post("/update")
    response_content = await response.content.read()

    assert response.status == 403
    assert "Forbidden" in response_content.decode()


@pytest.mark.integration
async def test_update_forbidden_when_key_header_wrong(client: TestClient) -> None:
    """Forbidden when header X-API-KEY is wrong."""
    response = await client.post("/update", headers={"X-API-KEY": "wrong-secret"})
    response_content = await response.content.read()

    assert response.status == 403
    assert "Forbidden" in response_content.decode()
