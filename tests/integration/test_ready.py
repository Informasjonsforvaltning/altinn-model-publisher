"""Integration test cases for the ready route."""
from unittest.mock import Mock

from flask import Flask
import pytest


@pytest.mark.integration
def test_ready(client: Flask, mock_ready: Mock) -> None:
    """Should return OK."""
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.data.decode() == "OK"


@pytest.mark.integration
def test_not_ready(client: Flask, mock_not_ready: Mock) -> None:
    """Should return Service Unavailable."""
    response = client.get("/ready")

    assert response.status_code == 503
