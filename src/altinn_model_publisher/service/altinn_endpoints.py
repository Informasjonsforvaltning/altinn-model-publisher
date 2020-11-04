"""Relevant altinn endpoints."""
from typing import Optional


API_METADATA_ENDPOINT = "/api/metadata"


def forms_task_uri(
    service_code: Optional[str], service_edition_code: Optional[str]
) -> Optional[str]:
    """Create endpoint for service edition metadata from service code and edition."""
    if service_code and service_edition_code:
        return f"{API_METADATA_ENDPOINT}/formtask/{service_code}/{service_edition_code}"

    return None


def xsd_uri(
    service_code: Optional[str],
    service_edition_code: Optional[str],
    data_format_id: Optional[str],
    data_format_version: Optional[str],
) -> Optional[str]:
    """Create endpoint for xsd model from service code, service edition, data format id and version."""
    if service_code and service_edition_code and data_format_id and data_format_version:
        return f"{forms_task_uri(service_code, service_edition_code)}/forms/{data_format_id}/{data_format_version}/xsd"

    return None
