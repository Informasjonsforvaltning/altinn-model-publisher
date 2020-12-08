"""Integration test cases for the ready route."""
from unittest.mock import call, Mock

from aiohttp.test_utils import TestClient
import pytest
from rdflib import Graph

from ..test_data import create_altinn_test_catalog


@pytest.mark.integration
@pytest.mark.docker
async def test_update(
    client: TestClient,
    docker_service: str,
    mock_save_to_mongo: Mock,
    mock_save_update_status: Mock,
    mock_not_running_update_status: Mock,
) -> None:
    """Saved models are updated on post request to /update."""
    response = await client.post("/update")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"

    set_update_status_calls = [call("update_in_progress"), call("ready_to_update")]
    mock_save_update_status.assert_has_calls(set_update_status_calls)

    mock_save_to_mongo.assert_called_once()

    expected = create_altinn_test_catalog()
    saved = mock_save_to_mongo.call_args_list.pop()[0][0]

    expected_graph = Graph().parse(data=expected.to_rdf(), format="turtle")
    saved_graph = Graph().parse(data=saved.to_rdf(), format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
async def test_update_cancelled_if_other_update_running(
    client: TestClient,
    docker_service: str,
    mock_running_update_status: Mock,
) -> None:
    """Saved models are updated on startup."""
    response = await client.post("/update")
    response_content = await response.content.read()

    assert response.status == 429
    assert response_content.decode() == "Too Many Requests"
