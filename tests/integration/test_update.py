"""Integration test cases for the ready route."""
from unittest.mock import call, Mock

from aiohttp.test_utils import TestClient
import pytest
from rdflib import Graph

from tests.test_data import (
    altinn_catalog_turtle,
    or_catalog_turtle,
    seres_catalog_turtle,
)


@pytest.mark.integration
@pytest.mark.docker
async def test_altinn_update(
    client: TestClient,
    docker_service: str,
    mock_save_to_cache: Mock,
    mock_save_update_status: Mock,
    mock_not_running_update_status: Mock,
) -> None:
    """Saved Altinn catalog are updated on post request to /altinn."""
    response = await client.post("/altinn", headers={"X-API-KEY": "api-test-secret"})
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"

    set_update_status_calls = [call("update_in_progress"), call("ready_to_update")]
    mock_save_update_status.assert_has_calls(set_update_status_calls)

    mock_save_to_cache.assert_called_once()
    saved = mock_save_to_cache.call_args_list.pop()[0][0]
    saved_rdf = saved.decode()

    expected_graph = Graph().parse(data=altinn_catalog_turtle, format="turtle")
    saved_graph = Graph().parse(data=saved_rdf, format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
@pytest.mark.docker
async def test_or_update(
    client: TestClient,
    docker_service: str,
    mock_save_to_cache: Mock,
    mock_save_update_status: Mock,
    mock_not_running_update_status: Mock,
) -> None:
    """Saved OR catalog are updated on post request to /or."""
    response = await client.post("/or", headers={"X-API-KEY": "api-test-secret"})
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"

    set_update_status_calls = [call("update_in_progress"), call("ready_to_update")]
    mock_save_update_status.assert_has_calls(set_update_status_calls)

    mock_save_to_cache.assert_called_once()
    saved = mock_save_to_cache.call_args_list.pop()[0][0]
    saved_rdf = saved.decode()

    expected_graph = Graph().parse(data=or_catalog_turtle, format="turtle")
    saved_graph = Graph().parse(data=saved_rdf, format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
@pytest.mark.docker
async def test_seres_update(
    client: TestClient,
    docker_service: str,
    mock_save_to_cache: Mock,
    mock_save_update_status: Mock,
    mock_not_running_update_status: Mock,
) -> None:
    """Saved Seres catalog are updated on post request to /seres."""
    response = await client.post("/seres", headers={"X-API-KEY": "api-test-secret"})
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"

    set_update_status_calls = [call("update_in_progress"), call("ready_to_update")]
    mock_save_update_status.assert_has_calls(set_update_status_calls)

    mock_save_to_cache.assert_called_once()
    saved = mock_save_to_cache.call_args_list.pop()[0][0]
    saved_rdf = saved.decode()

    expected_graph = Graph().parse(data=seres_catalog_turtle, format="turtle")
    saved_graph = Graph().parse(data=saved_rdf, format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
async def test_update_cancelled_if_other_update_running(
    client: TestClient,
    mock_running_update_status: Mock,
) -> None:
    """Update is cancelled when already running."""
    response_altinn = await client.post(
        "/altinn", headers={"X-API-KEY": "api-test-secret"}
    )
    response_or = await client.post("/or", headers={"X-API-KEY": "api-test-secret"})
    response_seres = await client.post(
        "/seres", headers={"X-API-KEY": "api-test-secret"}
    )

    altinn_content = await response_altinn.content.read()
    or_content = await response_or.content.read()
    seres_content = await response_seres.content.read()

    assert response_altinn.status == 429
    assert altinn_content.decode() == "Too Many Requests"
    assert response_or.status == 429
    assert or_content.decode() == "Too Many Requests"
    assert response_seres.status == 429
    assert seres_content.decode() == "Too Many Requests"


@pytest.mark.integration
async def test_update_forbidden_when_key_header_missing(client: TestClient) -> None:
    """Forbidden when header X-API-KEY is missing."""
    response_altinn = await client.post("/altinn")
    response_or = await client.post("/or")
    response_seres = await client.post("/seres")

    altinn_content = await response_altinn.content.read()
    or_content = await response_or.content.read()
    seres_content = await response_seres.content.read()

    assert response_altinn.status == 403
    assert "Forbidden" in altinn_content.decode()
    assert response_or.status == 403
    assert "Forbidden" in or_content.decode()
    assert response_seres.status == 403
    assert "Forbidden" in seres_content.decode()


@pytest.mark.integration
async def test_update_forbidden_when_key_header_wrong(client: TestClient) -> None:
    """Forbidden when header X-API-KEY is wrong."""
    response_altinn = await client.post(
        "/altinn", headers={"X-API-KEY": "api-wrong-secret"}
    )
    response_or = await client.post("/or", headers={"X-API-KEY": "api-wrong-secret"})
    response_seres = await client.post(
        "/seres", headers={"X-API-KEY": "api-wrong-secret"}
    )

    altinn_content = await response_altinn.content.read()
    or_content = await response_or.content.read()
    seres_content = await response_seres.content.read()

    assert response_altinn.status == 403
    assert "Forbidden" in altinn_content.decode()
    assert response_or.status == 403
    assert "Forbidden" in or_content.decode()
    assert response_seres.status == 403
    assert "Forbidden" in seres_content.decode()
