"""Unit test cases for startup tasks."""
from unittest.mock import Mock

from aiohttp.web import Application
import pytest

from altinn_model_publisher.app import set_ready_to_update_on_startup


@pytest.mark.unit
async def test_set_ready_update_status_on_startup(
    mock_replace_one: Mock, mock_non_test_environment: Mock
) -> None:
    """Should set ready to update in non test environment."""
    await set_ready_to_update_on_startup(Application())
    mock_replace_one.assert_called_once()


@pytest.mark.unit
async def test_do_not_set_update_status_in_startup_in_test_environment(
    mock_replace_one: Mock,
) -> None:
    """Should not set ready to update in test environment."""
    await set_ready_to_update_on_startup(Application())
    mock_replace_one.assert_not_called()
