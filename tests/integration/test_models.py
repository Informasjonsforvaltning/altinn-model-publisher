"""Integration test cases for the ready route."""
from unittest.mock import Mock

from flask import Flask
import pytest


@pytest.mark.integration
def test_models(
    client: Flask, mock_load_rdf_from_mongo: Mock, mock_update_on_startup: Mock
) -> None:
    """Should return OK."""
    response = client.get("/models")

    assert response.status_code == 200
