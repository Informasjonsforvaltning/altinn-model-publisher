"""Integration test cases for the ready route."""
from aiohttp.test_utils import TestClient
import pytest


@pytest.mark.integration
async def test_ready(client: TestClient) -> None:
    """Should return OK."""
    response = await client.get("/ready")
    response_content = await response.content.read()

    assert response.status == 200
    assert response_content.decode() == "OK"
