"""Integration test cases for the ready route."""
from unittest.mock import Mock

from aiohttp.test_utils import TestClient
import pytest

from tests.test_data import (
    altinn_catalog_turtle,
    or_catalog_turtle,
    seres_catalog_turtle,
)


@pytest.mark.integration
async def test_altinn(client: TestClient, mock_load_altinn_from_cache: Mock) -> None:
    """Should return OK."""
    response = await client.get("/altinn")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == altinn_catalog_turtle


@pytest.mark.integration
async def test_or(client: TestClient, mock_load_or_from_cache: Mock) -> None:
    """Should return OK."""
    response = await client.get("/or")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == or_catalog_turtle


@pytest.mark.integration
async def test_seres(client: TestClient, mock_load_seres_from_cache: Mock) -> None:
    """Should return OK."""
    response = await client.get("/seres")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == seres_catalog_turtle
