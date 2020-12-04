"""Unit test cases for meta data filters in the service module."""
from unittest.mock import Mock

import pytest

from altinn_model_publisher.service.altinn_mongo_service import (
    no_altinn_models_in_database,
    read_catalog_from_mongo,
    save_catalog_to_mongo,
)
from ..test_data import create_altinn_test_catalog, test_altinn_catalog_turtle


@pytest.mark.unit
def test_models_exist_in_database(mock_find_one: Mock) -> None:
    """Should return true."""
    assert no_altinn_models_in_database() is False


@pytest.mark.unit
def test_models_does_not_exist_in_database(mock_find_one_no_data: Mock) -> None:
    """Should return true."""
    assert no_altinn_models_in_database() is True


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
