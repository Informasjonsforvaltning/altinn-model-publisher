"""Contract test cases for models."""
import pytest
import requests


@pytest.mark.contract
@pytest.mark.docker
def test_altinn(docker_service: str) -> None:
    """Should return Altinn catalog."""
    url = f"{docker_service}/altinn"
    response = requests.get(url)

    assert response.status_code == 200


@pytest.mark.contract
@pytest.mark.docker
def test_or(docker_service: str) -> None:
    """Should return OR catalog."""
    url = f"{docker_service}/or"
    response = requests.get(url)

    assert response.status_code == 200


@pytest.mark.contract
@pytest.mark.docker
def test_seres(docker_service: str) -> None:
    """Should return Seres catalog."""
    url = f"{docker_service}/seres"
    response = requests.get(url)

    assert response.status_code == 200
