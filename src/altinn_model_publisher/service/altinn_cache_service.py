"""Service layer module for saving altinn models to a zip file."""
import gzip
import os

from aiocache import caches
from datacatalogtordf.catalog import Catalog

PUBLISHER_REDIS = "publisher_redis"
UPDATE_STATUS_ID = "update-status"
ALTINN_MODELS_CACHE_ID = "altinn-models"

caches.set_config(
    {
        "default": {
            "cache": "aiocache.RedisCache",
            "endpoint": "publishers-cache",
            "port": 6379,
            "password": os.getenv("CACHE_PASSWORD", None),
            "serializer": {"class": "aiocache.serializers.PickleSerializer"},
            "plugins": [
                {"class": "aiocache.plugins.HitMissRatioPlugin"},
                {"class": "aiocache.plugins.TimingPlugin"},
            ],
        },
    }
)
cache = caches.get("default")


async def save_catalog_to_cache(catalog: Catalog) -> None:
    """Zip and save catalog to cache."""
    await cache.set(ALTINN_MODELS_CACHE_ID, gzip.compress(bytes(catalog.to_rdf())))


async def read_catalog_from_cache() -> str:
    """Read zipped catalog from cache."""
    return (
        gzip.decompress(await cache.get(ALTINN_MODELS_CACHE_ID)).decode()
        if await cache.exists(ALTINN_MODELS_CACHE_ID)
        else ""
    )


async def save_update_status(status: str) -> None:
    """Save update status."""
    await cache.set(UPDATE_STATUS_ID, status)


async def read_update_status() -> str:
    """Read update status."""
    return (
        await cache.get(UPDATE_STATUS_ID)
        if await cache.exists(UPDATE_STATUS_ID)
        else "ready_to_update"
    )
