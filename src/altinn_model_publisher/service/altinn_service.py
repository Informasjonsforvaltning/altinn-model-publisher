"""Service layer module for modelldcat-ap-no compliant information models from altinn."""
import logging
import os
from typing import Dict, List, Optional

from datacatalogtordf.catalog import Catalog
from modelldcatnotordf.modelldcatno import InformationModel

from .altinn_cache_service import (
    read_catalog_from_cache,
    read_update_status,
    save_catalog_to_cache,
    save_update_status,
)
from .altinn_client import (
    fetch_altinn_metadata,
    fetch_metadata_with_task_forms,
    get_xsd_data,
)
from .altinn_model_mapper import map_model_from_dict


UPDATE_IN_PROGRESS = "update_in_progress"
ORG_URI = os.getenv(
    "ORGANIZATION_CATALOGUE_URI",
    "https://organization-catalogue.fellesdatakatalog.digdir.no",
)


def service_meta_data_filtered_by_type_form_task() -> List[Dict]:
    """Fetch service metadata from Altinn, filter by type FormTask."""
    return [
        metadata
        for metadata in fetch_altinn_metadata()
        if metadata.get("ServiceType") == "FormTask"
    ]


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
    catalog.publisher = f"""{ORG_URI}/organizations/991825827"""

    catalog.models = altinn_models

    return catalog


async def update_altinn_models() -> str:
    """Update altinn models catalog."""
    if await read_update_status() == UPDATE_IN_PROGRESS:
        logging.info("Update already in progress, new update run is cancelled")
        return UPDATE_IN_PROGRESS
    else:
        await save_update_status(UPDATE_IN_PROGRESS)
        await fetch_altinn_models_and_update_database()
        await save_update_status("ready_to_update")
        return "updated"


async def fetch_altinn_models_and_update_database() -> None:
    """Fetch information models from Altinn and update database."""
    logging.info("Starting update from Altinn")
    all_form_tasks = service_meta_data_filtered_by_type_form_task()
    form_tasks = filter_form_tasks_by_edition(all_form_tasks)
    logging.info("Form tasks metadata fetched from Altinn")

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
    logging.info("Form task services metadata fetched from Altinn")

    models_data = []

    for data in combined_meta_data:
        xml_schema = get_xsd_data(
            data["service_meta"].get("ServiceCode"),
            data["service_meta"].get("ServiceEditionCode"),
            data["forms_meta"].get("DataFormatID"),
            data["forms_meta"].get("DataFormatVersion"),
        )
        if xml_schema:
            data["schema"] = xml_schema
            models_data.append(data)
    logging.info("Form task services xsd data fetched from Altinn")

    altinn_models = [map_model_from_dict(model_dict) for model_dict in models_data]
    altinn_catalog = create_altinn_models_catalog(altinn_models)
    await save_catalog_to_cache(altinn_catalog)

    logging.info("Altinn model catalog successfully updated")


async def all_altinn_models() -> str:
    """Return altinn models from database."""
    logging.info("Fetching models catalog from database")
    return await read_catalog_from_cache()
