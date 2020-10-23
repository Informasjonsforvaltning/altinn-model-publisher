import pytest

from altinn_model_publisher.service.altinn_service import is_ready


@pytest.mark.unit
def test_is_ready() -> None:
    _result = is_ready(None)

    assert _result is True


@pytest.mark.unit
def test_not_ready() -> None:
    _result = is_ready("application/json")

    assert _result is False
