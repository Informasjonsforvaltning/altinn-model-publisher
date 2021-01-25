"""Service layer module for modelldcat-ap-no compliant information models from altinn."""
import logging
from typing import Dict, List, Optional

from datacatalogtordf.catalog import Catalog
from modelldcatnotordf.modelldcatno import InformationModel

from altinn_model_publisher.config import Config
from altinn_model_publisher.mapper.model_mapper import map_model_from_dict
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


def catalog_type_corresponds_with_data_format_provider(
    meta_data: Dict, catalog_type: str
) -> bool:
    """Check that DataFormatProviderType corresponds with catalog type."""
    if catalog_type == Config.catalog_types()["SERES"]:
        return meta_data["forms_meta"]["DataFormatProviderType"] == "Seres"
    elif catalog_type == Config.catalog_types()["OR"]:
        return meta_data["forms_meta"]["DataFormatProviderType"] == "OR"
    else:
        return (
            meta_data["forms_meta"]["DataFormatProviderType"] != "Seres"
            and meta_data["forms_meta"]["DataFormatProviderType"] != "OR"
        )


def create_catalog(altinn_models: List[InformationModel], catalog_type: str) -> Catalog:
    """Create turtle representation of catalog with models."""
    catalog = Catalog()
    catalog.publisher = f"""{Config.organizations_uri()}/organizations/991825827"""

    if catalog_type == Config.catalog_types()["SERES"]:
        catalog.identifier = "https://www.altinn.no/models/seres"
        catalog.title = {"nb": "Seres informasjonsmodellkatalog"}
    elif catalog_type == Config.catalog_types()["OR"]:
        catalog.identifier = "https://www.altinn.no/models/or"
        catalog.title = {"nb": "OR informasjonsmodellkatalog"}
    else:
        catalog.identifier = "https://www.altinn.no/models/altinn"
        catalog.title = {"nb": "Altinn informasjonsmodellkatalog"}

    catalog.models = altinn_models

    return catalog


async def update_altinn_catalog() -> str:
    """Update Altinn catalog."""
    if await read_update_status() == Config.update_in_progress():
        logging.info("Update already in progress, new update run is cancelled")
        return Config.update_in_progress()
    else:
        await save_update_status(Config.update_in_progress())
        await fetch_altinn_models_and_update_database(Config.catalog_types()["ALTINN"])
        await save_update_status(Config.ready_to_update())
        return "updated"


async def update_seres_catalog() -> str:
    """Update Seres catalog."""
    if await read_update_status() == Config.update_in_progress():
        logging.info("Update already in progress, new update run is cancelled")
        return Config.update_in_progress()
    else:
        await save_update_status(Config.update_in_progress())
        await fetch_altinn_models_and_update_database(Config.catalog_types()["SERES"])
        await save_update_status(Config.ready_to_update())
        return "updated"


async def update_or_catalog() -> str:
    """Update OR catalog."""
    if await read_update_status() == Config.update_in_progress():
        logging.info("Update already in progress, new update run is cancelled")
        return Config.update_in_progress()
    else:
        await save_update_status(Config.update_in_progress())
        await fetch_altinn_models_and_update_database(Config.catalog_types()["OR"])
        await save_update_status(Config.ready_to_update())
        return "updated"


async def fetch_altinn_models_and_update_database(catalog_type: str) -> None:
    """Fetch information models from Altinn and update database."""
    logging.info(f"Starting update of {catalog_type} from Altinn")
    try:
        all_form_tasks = service_meta_data_filtered_by_type_form_task()
        form_tasks = filter_form_tasks_by_edition(all_form_tasks)
        logging.info("Form tasks metadata fetched from Altinn")

        combined_meta_data_all_types = []
        for service_code in form_tasks:
            metadata = fetch_metadata_with_task_forms(
                service_code, form_tasks[service_code].get("ServiceEditionCode")
            )

            forms_meta = filter_forms_meta_data(metadata.get("FormsMetaData"))

            for format_id in forms_meta:
                combined_meta_data_all_types.append(
                    {
                        "service_meta": form_tasks[service_code],
                        "forms_meta": forms_meta[format_id],
                    }
                )
        logging.info("Form task services metadata fetched from Altinn")

        combined_meta_data = [
            meta_data
            for meta_data in combined_meta_data_all_types
            if catalog_type_corresponds_with_data_format_provider(
                meta_data, catalog_type
            )
        ]

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
        altinn_catalog = create_catalog(altinn_models, catalog_type)
        await save_catalog_to_cache(altinn_catalog, catalog_type)

        logging.info(f"Completed update of {catalog_type} catalog")
    except BaseException as err:
        logging.error(f"Exception occured when updating {catalog_type}, {err}")


async def altinn_catalog() -> str:
    """Return Altinn models from database."""
    logging.info("Fetching Altinn catalog from database")
    return await read_catalog_from_cache(Config.catalog_types()["ALTINN"])


async def seres_catalog() -> str:
    """Return Seres models from database."""
    logging.info("Fetching Seres catalog from database")
    return await read_catalog_from_cache(Config.catalog_types()["SERES"])


async def or_catalog() -> str:
    """Return OR models from database."""
    logging.info("Fetching OR catalog from database")
    return await read_catalog_from_cache(Config.catalog_types()["OR"])
