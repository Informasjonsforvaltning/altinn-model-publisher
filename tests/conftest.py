"""Conftest module."""
import json
import os
from os import environ as env
import time
from typing import Any, Generator
from unittest.mock import Mock

from dotenv import load_dotenv
from flask import Flask
from flask.testing import FlaskClient
import pytest
from pytest_mock import MockFixture
import requests
from requests.exceptions import ConnectionError

from altinn_model_publisher import create_app
from .test_data import test_altinn_catalog_turtle

load_dotenv()
HOST_PORT = int(env.get("HOST_PORT", "8080"))


def is_responsive(url: Any) -> Any:
    """Return true if response from service is 200."""
    url = f"{url}/ready"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            time.sleep(2)  # sleep extra 2 sec
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def docker_service(docker_ip: Any, docker_services: Any) -> Any:
    """Ensure that HTTP service is up and responsive."""
    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("altinn-model-publisher", HOST_PORT)
    url = "http://{}:{}".format(docker_ip, port)
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: Any) -> Any:
    """Override default location of docker-compose.yml file."""
    return os.path.join(str(pytestconfig.rootdir), "./", "docker-compose.yml")


@pytest.mark.unit
@pytest.fixture
def app() -> Generator:
    """Return a Flask app for unit testing."""
    app = create_app({"TESTING": True})

    yield app


@pytest.mark.unit
@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Return a client for unit testing."""
    return app.test_client()


@pytest.fixture
def mock_altinn_client_http_error(mocker: MockFixture) -> Mock:
    """Mock https error from altinn."""
    mock = mocker.patch("requests.get")
    mock.side_effect = requests.HTTPError(
        "altinn-not-found",
        404,
        "Not Found",
        {},
        None,
    )
    return mock


@pytest.fixture
def mock_altinn_client_json_parse_error(mocker: MockFixture) -> Mock:
    """Mock decode error for json."""
    mock = mocker.patch("requests.get")
    mock.side_effect = json.JSONDecodeError(msg="altinn-parse-error", doc="", pos=0)
    return mock


def altinn_effect_xml_error(*args: Any, **kwargs: Any) -> Mock:
    """Create mocked altinn response."""
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None
    rsp.content.read.return_value = (
        """<?xml version="1.0" encoding="UTF-8" ?><test """.encode()
    )
    return rsp


@pytest.fixture
def mock_altinn_client_xml_parse_error(mocker: MockFixture) -> Mock:
    """Mock OK GET with xml error."""
    mock = mocker.patch("requests.get")
    mock.side_effect = altinn_effect_xml_error
    return mock


def altinn_effect(*args: Any, **kwargs: Any) -> Mock:
    """Create mocked altinn response."""
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None
    rsp.json.return_value = json.loads("""[{"test": "test"}]""")
    return rsp


@pytest.fixture
def mock_altinn_client(mocker: MockFixture) -> Mock:
    """Mock OK GET from altinn."""
    mock = mocker.patch("requests.get")
    mock.side_effect = altinn_effect
    return mock


@pytest.fixture
def mock_orgs_file(mocker: MockFixture) -> Mock:
    """Mock file with orgs shortname map."""
    mock = mocker.patch("os.path.isfile")
    mock.return_value = True
    return mock


@pytest.fixture
def mock_ready(mocker: MockFixture) -> Mock:
    """Mock check models file is present."""
    mock = mocker.patch("os.path.isfile")
    mock.return_value = True
    return mock


@pytest.fixture
def mock_not_ready(mocker: MockFixture) -> Mock:
    """Mock check models file is missing."""
    mock = mocker.patch("os.path.isfile")
    mock.return_value = False
    return mock


@pytest.fixture
def mock_save_to_file(mocker: MockFixture) -> Mock:
    """Mock save catalog to file."""
    mock = mocker.patch(
        "altinn_model_publisher.service.altinn_service.save_catalog_to_zip_file"
    )
    return mock


@pytest.fixture
def mock_load_rdf_from_file(mocker: MockFixture) -> Mock:
    """Mock save catalog to file."""
    mock = mocker.patch(
        "altinn_model_publisher.service.altinn_service.read_catalog_zip_file"
    )
    mock.return_value = test_altinn_catalog_turtle
    return mock
