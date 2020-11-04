"""Integration test cases for the ready route."""
from flask import Flask
import pytest


@pytest.mark.integration
@pytest.mark.docker
def test_update(client: Flask, docker_service: str) -> None:
    """Should return OK."""
    response = client.post("/update")

    assert response.status_code == 200
    assert response.data.decode() == "OK"
