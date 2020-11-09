"""Integration test cases for the ready route."""
from unittest.mock import Mock

from flask import Flask
import pytest


@pytest.mark.integration
def test_models(client: Flask, mock_load_rdf_from_file: Mock) -> None:
    """Should return OK."""
    response = client.get("/models")

    assert response.status_code == 200
