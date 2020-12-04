"""Integration test cases for the ready route."""
from unittest.mock import Mock

from flask import Flask
import pytest


@pytest.mark.integration
def test_ready(client: Flask, mock_update_on_startup: Mock) -> None:
    """Should return OK."""
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.data.decode() == "OK"
