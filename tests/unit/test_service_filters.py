"""Unit test cases for meta data filters in the service module."""
import pytest

from altinn_model_publisher.service.altinn_service import (
    filter_form_tasks_by_edition,
    filter_forms_meta_data,
)


@pytest.mark.unit
def test_filter_form_tasks_by_edition() -> None:
    """Should filter service meta data by highest edition."""
    filtered = filter_form_tasks_by_edition(
        [
            {"ServiceCode": "1", "ServiceEditionCode": "1"},
            {"ServiceCode": "1", "ServiceEditionCode": "not a number"},
            {"ServiceCode": "1", "ServiceEditionCode": "56"},
        ]
    )

    assert filtered == {"1": {"ServiceCode": "1", "ServiceEditionCode": "56"}}


@pytest.mark.unit
def test_filter_forms_meta_data() -> None:
    """Should filter forms meta data by highest version."""
    filtered = filter_forms_meta_data(
        [
            {"DataFormatID": "34", "DataFormatVersion": "1"},
            {"DataFormatID": "34", "DataFormatVersion": "not a number"},
            {"DataFormatID": "34", "DataFormatVersion": "13"},
        ]
    )

    assert filtered == {"34": {"DataFormatID": "34", "DataFormatVersion": "13"}}
