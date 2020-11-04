"""Contract test cases for models."""
import pytest
import requests


@pytest.mark.contract
@pytest.mark.docker
def test_models(docker_service: str) -> None:
    """Should return content of zipped ttl-file."""
    url = f"{docker_service}/models"
    response = requests.get(url)

    assert response.status_code == 200
