"""Service layer module for saving altinn models to a zip file."""
import gzip
import os

from datacatalogtordf.catalog import Catalog
from pymongo import MongoClient


UPDATE_STATUS_ID = "update-status"
ALTINN_MODELS_MONGO_ID = "altinn-models"
MONGO_COLLECTION = "models"
MONGO_DATABASE = "altinnModelPublisher"
MONGO_CONNECTION_STRING = f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017"""

mongo_connection = MongoClient(MONGO_CONNECTION_STRING)
mongo_collection = mongo_connection.altinnModelPublisher.models


def save_catalog_to_mongo(catalog: Catalog) -> None:
    """Zip and save catalog to mongo."""
    mongo_object = {
        "_id": ALTINN_MODELS_MONGO_ID,
        "catalog": gzip.compress(bytes(catalog.to_rdf())),
    }
    mongo_collection.replace_one(
        filter={"_id": ALTINN_MODELS_MONGO_ID}, replacement=mongo_object, upsert=True
    )


def read_catalog_from_mongo() -> str:
    """Read zipped catalog from mongo."""
    mongo_object = mongo_collection.find_one({"_id": ALTINN_MODELS_MONGO_ID})
    return gzip.decompress(mongo_object["catalog"]).decode() if mongo_object else ""


def save_update_status(status: str) -> None:
    """Save update status."""
    mongo_object = {
        "_id": UPDATE_STATUS_ID,
        "value": status,
    }
    mongo_collection.replace_one(
        filter={"_id": UPDATE_STATUS_ID}, replacement=mongo_object, upsert=True
    )


def read_update_status() -> str:
    """Read update status."""
    update_status = mongo_collection.find_one({"_id": UPDATE_STATUS_ID})
    return update_status["value"] if update_status else "ready_to_update"
