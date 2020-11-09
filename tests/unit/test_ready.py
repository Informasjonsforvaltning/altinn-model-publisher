"""Unit test cases for the model service module."""
from unittest.mock import Mock

import pytest

from altinn_model_publisher.service.altinn_service import is_ready


@pytest.mark.unit
def test_is_ready(mock_ready: Mock) -> None:
    """Should return True when ready."""
    _result = is_ready()

    assert _result is True


@pytest.mark.unit
def test_not_ready(mock_not_ready: Mock) -> None:
    """Should return False when not ready."""
    _result = is_ready()

    assert _result is False
