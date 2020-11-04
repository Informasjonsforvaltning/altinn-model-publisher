"""Integration test cases for the ready route."""
from flask import Flask
import pytest


@pytest.mark.integration
def test_update(client: Flask) -> None:
    """Should return OK."""
    response = client.get("/models")

    assert response.status_code == 200
