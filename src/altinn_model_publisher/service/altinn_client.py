"""Service layer module for http connections to altinn."""
import logging
from typing import Dict, List, Optional

import requests
from xmlschema import XMLSchema

from altinn_model_publisher.config import Config
from .altinn_endpoints import API_METADATA_ENDPOINT, forms_task_uri, xsd_uri


def fetch_altinn_metadata() -> List[Dict]:
    """Fetch Altinn metadata."""
    try:
        response = altinn_get_request(
            API_METADATA_ENDPOINT, headers={"Accept": "application/json"}
        )

        return response.json() if response else []

    except Exception as err:
        logging.error(f"Error occurred when parsing altinn metadata: {err}")

    return []


def fetch_metadata_with_task_forms(
    service_code: Optional[str], service_edition_code: Optional[str]
) -> Dict:
    """Fetch Altinn metadata with task forms for specific service edition."""
    uri = forms_task_uri(service_code, service_edition_code)
    if uri:
        try:
            response = altinn_get_request(uri, headers={"Accept": "application/json"})
            meta_data_with_forms = response.json() if response else None

            return meta_data_with_forms if meta_data_with_forms else {}
        except Exception as err:
            logging.error(f"Error occurred when parsing forms task from {uri}: {err}")

    return {}


def get_xsd_data(
    service_code: str,
    service_edition_code: str,
    data_format_id: str,
    data_format_version: str,
) -> Optional[XMLSchema]:
    """Fetch Altinn model in xsd format."""
    xsd_endpoint = xsd_uri(
        service_code, service_edition_code, data_format_id, data_format_version
    )
    if xsd_endpoint:
        try:
            return XMLSchema(f"{Config.altinn_uri()}{xsd_endpoint}")
        except Exception as err:
            logging.error(f"Error occurred when parsing xsd from {xsd_endpoint}: {err}")

    return None


def altinn_get_request(
    endpoint: Optional[str], headers: Dict
) -> Optional[requests.Response]:
    """Altinn GET request for specified endpoint and headers."""
    if endpoint:
        try:
            response = requests.get(
                f"""{Config.altinn_uri()}{endpoint}""", headers=headers
            )

            response.raise_for_status()

            return response

        except requests.HTTPError as err:
            logging.error(f"Http error response from altinn ({err})")

    return None
