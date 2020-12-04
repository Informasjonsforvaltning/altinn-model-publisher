"""Service layer module for saving altinn models to a zip file."""
import gzip
import os

from datacatalogtordf.catalog import Catalog
from pymongo import MongoClient


ALTINN_MODELS_MONGO_ID = "altinn-models"
MONGO_COLLECTION = "models"
MONGO_DATABASE = "altinnModelPublisher"
MONGO_CONNECTION_STRING = f"""mongodb://{os.environ['MONGO_USERNAME']}:{os.environ['MONGO_PASSWORD']}@mongodb:27017"""


def save_catalog_to_mongo(catalog: Catalog) -> None:
    """Zip and save catalog to mongo."""
    connection = MongoClient(MONGO_CONNECTION_STRING)
    mongo_collection = connection.altinnModelPublisher.models

    mongo_object = {
        "_id": ALTINN_MODELS_MONGO_ID,
        "catalog": gzip.compress(bytes(catalog.to_rdf())),
    }
    mongo_collection.replace_one(
        filter={"_id": ALTINN_MODELS_MONGO_ID}, replacement=mongo_object, upsert=True
    )


def read_catalog_from_mongo() -> str:
    """Read zipped catalog from mongo."""
    connection = MongoClient(MONGO_CONNECTION_STRING)
    mongo_collection = connection.altinnModelPublisher.models

    mongo_object = mongo_collection.find_one({"_id": ALTINN_MODELS_MONGO_ID})
    return gzip.decompress(mongo_object["catalog"]).decode() if mongo_object else ""


def no_altinn_models_in_database() -> bool:
    """Check if altinn catalog is saved to database."""
    connection = MongoClient(MONGO_CONNECTION_STRING)
    mongo_collection = connection.altinnModelPublisher.models

    mongo_object = mongo_collection.find_one({"_id": ALTINN_MODELS_MONGO_ID})
    return False if mongo_object else True
