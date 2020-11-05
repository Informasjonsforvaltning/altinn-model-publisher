"""Service layer module for saving altinn models to a zip file."""
import gzip
import os

from datacatalogtordf.catalog import Catalog


CATALOG_FILE_PATH = os.getenv("CATALOG_FILE_PATH", "/app/altinn_catalog.ttl.gz")


def save_catalog_to_zip_file(catalog: Catalog) -> None:
    """Zip and save catalog to file."""
    rdf_catalog = bytes(catalog.to_rdf())
    with gzip.open(CATALOG_FILE_PATH, "wb") as zip_file:
        zip_file.write(rdf_catalog)


def read_catalog_zip_file() -> str:
    """Read zipped catalog from file."""
    with gzip.open(CATALOG_FILE_PATH, "rb") as zip_file:
        return zip_file.read().decode()
