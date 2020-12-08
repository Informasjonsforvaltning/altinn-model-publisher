"""Integration test cases for the ready route."""
from unittest.mock import Mock

from flask import Flask
import pytest
from rdflib import Graph

from ..test_data import create_altinn_test_catalog


@pytest.mark.integration
@pytest.mark.docker
def test_update(
    client: Flask,
    docker_service: str,
    mock_save_to_mongo: Mock,
    mock_models_exist_in_db: Mock,
) -> None:
    """Saved models are updated on post request to /update."""
    response = client.post("/update")

    assert response.status_code == 200
    assert response.data.decode() == "OK"

    mock_save_to_mongo.assert_called_once()

    expected = create_altinn_test_catalog()
    saved = mock_save_to_mongo.call_args_list.pop()[0][0]

    expected_graph = Graph().parse(data=expected.to_rdf(), format="turtle")
    saved_graph = Graph().parse(data=saved.to_rdf(), format="turtle")

    assert expected_graph.isomorphic(saved_graph)


@pytest.mark.integration
@pytest.mark.docker
def test_update_on_startup(
    client: Flask,
    docker_service: str,
    mock_save_to_mongo: Mock,
    mock_no_models_in_db: Mock,
) -> None:
    """Saved models are updated on startup."""
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.data.decode() == "OK"

    mock_save_to_mongo.assert_called_once()

    expected = create_altinn_test_catalog()
    saved = mock_save_to_mongo.call_args_list.pop()[0][0]

    expected_graph = Graph().parse(data=expected.to_rdf(), format="turtle")
    saved_graph = Graph().parse(data=saved.to_rdf(), format="turtle")

    assert expected_graph.isomorphic(saved_graph)
