"""Integration test cases for the ready route."""
from unittest.mock import Mock

from aiohttp.test_utils import TestClient
import pytest

from ..test_data import test_altinn_catalog_turtle


@pytest.mark.integration
async def test_models(client: TestClient, mock_load_rdf_from_cache: Mock) -> None:
    """Should return OK."""
    response = await client.get("/models")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == test_altinn_catalog_turtle
