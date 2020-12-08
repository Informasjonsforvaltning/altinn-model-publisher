"""Unit test cases for meta data filters in the service module."""
from unittest.mock import Mock

import pytest

from altinn_model_publisher.service.altinn_mongo_service import (
    read_catalog_from_mongo,
    read_update_status,
    save_catalog_to_mongo,
    save_update_status,
)
from ..test_data import create_altinn_test_catalog, test_altinn_catalog_turtle


@pytest.mark.unit
def test_models_read_from_database(mock_find_one: Mock) -> None:
    """Should return models from database."""
    expected = test_altinn_catalog_turtle
    assert read_catalog_from_mongo() == expected


@pytest.mark.unit
def test_models_saved_to_mongo(mock_replace_one: Mock) -> None:
    """Should save catalog to database."""
    to_save = create_altinn_test_catalog()
    save_catalog_to_mongo(to_save)
    mock_replace_one.assert_called_once()


@pytest.mark.unit
def test_read_update_status(mock_find_one_update_status: Mock) -> None:
    """Should return models from database."""
    expected = "ready_to_update"
    assert read_update_status() == expected


@pytest.mark.unit
def test_set_update_status(mock_replace_one_update_status: Mock) -> None:
    """Should save catalog to database."""
    save_update_status("ready_to_update")
    mock_replace_one_update_status.assert_called_once()
