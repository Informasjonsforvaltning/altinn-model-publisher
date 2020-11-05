"""Service layer module for modelldcat-ap-no compliant information models from altinn."""
import logging
import os
from typing import Dict, List, Optional

from datacatalogtordf.catalog import Catalog
from modelldcatnotordf.informationmodel import InformationModel

from .altinn_client import (
    fetch_altinn_metadata,
    fetch_metadata_with_task_forms,
    get_xsd_data,
)
from .altinn_file_service import (
    CATALOG_FILE_PATH,
    read_catalog_zip_file,
    save_catalog_to_zip_file,
)
from .altinn_model_mapper import map_model_from_dict


def is_ready() -> bool:
    """Check if altinn models file is available."""
    return os.path.isfile(CATALOG_FILE_PATH)


def service_meta_data_filtered_by_type_form_task() -> List[Dict]:
    """Fetch service metadata from Altinn, filter by type FormTask."""
    form_tasks = [
        metadata
        for metadata in fetch_altinn_metadata()
        if metadata.get("ServiceType") == "FormTask"
    ]

    return form_tasks


def filter_form_tasks_by_edition(form_tasks: List[Dict]) -> Dict:
    """Filter form task meta data by highest edition."""
    filtered_tasks: Dict = {}

    for form_task in form_tasks:
        service_code = form_task.get("ServiceCode")
        edition = form_task.get("ServiceEditionCode")
        if service_code and edition:
            current_highest = filtered_tasks.get(service_code)
            current_highest = (
                current_highest if current_highest else {"ServiceEditionCode": "0"}
            )
            try:
                if int(edition) > int(current_highest["ServiceEditionCode"]):
                    filtered_tasks[service_code] = form_task
            except ValueError:
                logging.error(
                    f"ServiceCode {service_code} or ServiceEditionCode {edition} was not a valid integer."
                )

    return filtered_tasks


def filter_forms_meta_data(data_formats: Optional[List[Dict]]) -> Dict:
    """Filter by unique data format id and highest corresponding version."""
    data_formats_with_highest_version: Dict = {}
    data_formats = data_formats if data_formats else []

    for data_format in data_formats:
        format_id = data_format.get("DataFormatID")
        version = data_format.get("DataFormatVersion")
        if format_id and version:
            current_highest = data_formats_with_highest_version.get(format_id)
            current_highest = (
                current_highest if current_highest else {"DataFormatVersion": "0"}
            )
            try:
                if int(version) > int(current_highest["DataFormatVersion"]):
                    data_formats_with_highest_version[format_id] = data_format
            except ValueError:
                logging.error(
                    f"DataFormatID {format_id} or DataFormatVersion {version} was not a valid integer."
                )

    return data_formats_with_highest_version


def create_altinn_models_catalog(altinn_models: List[InformationModel]) -> Catalog:
    """Create turtle representation of catalog with models."""
    catalog = Catalog()
    catalog.identifier = "https://www.altinn.no/models/catalog"
    catalog.title = {"nb": "Altinn informasjonsmodellkatalog"}
    catalog.publisher = f"""{os.getenv("ORG_URI")}/organizations/991825827"""

    catalog.models = altinn_models

    return catalog


def update_altinn_models_file() -> None:
    """Update content of altinn models file."""
    all_form_tasks = service_meta_data_filtered_by_type_form_task()
    form_tasks = filter_form_tasks_by_edition(all_form_tasks)
    combined_meta_data = []

    for service_code in form_tasks:
        metadata = fetch_metadata_with_task_forms(
            service_code, form_tasks[service_code].get("ServiceEditionCode")
        )

        forms_meta = filter_forms_meta_data(metadata.get("FormsMetaData"))

        for format_id in forms_meta:
            combined_meta_data.append(
                {
                    "service_meta": form_tasks[service_code],
                    "forms_meta": forms_meta[format_id],
                }
            )

    models_data = []

    for data in combined_meta_data:
        parsed_response = get_xsd_data(
            data["service_meta"].get("ServiceCode"),
            data["service_meta"].get("ServiceEditionCode"),
            data["forms_meta"].get("DataFormatID"),
            data["forms_meta"].get("DataFormatVersion"),
        )
        if parsed_response:
            data["elements"] = parsed_response
            models_data.append(data)

    altinn_models = [map_model_from_dict(model_dict) for model_dict in models_data]
    altinn_catalog = create_altinn_models_catalog(altinn_models)
    save_catalog_to_zip_file(altinn_catalog)

    logging.info("Altinn model catalog successfully updated")


def all_altinn_models() -> str:
    """Return content of altinn models file."""
    return read_catalog_zip_file()
