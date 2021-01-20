"""Service layer module for saving altinn models to a zip file."""
import gzip

from aiocache import caches
from datacatalogtordf.catalog import Catalog

from altinn_model_publisher.config import Config


caches.set_config(Config.cache_config())
cache = caches.get("default")


async def save_catalog_to_cache(catalog: Catalog, catalog_type: str) -> None:
    """Zip and save catalog to cache."""
    await cache.set(catalog_type, gzip.compress(bytes(catalog.to_rdf())))


async def read_catalog_from_cache(catalog_type: str) -> str:
    """Read zipped catalog from cache."""
    return (
        gzip.decompress(await cache.get(catalog_type)).decode()
        if await cache.exists(catalog_type)
        else ""
    )


async def save_update_status(status: str) -> None:
    """Save update status."""
    await cache.set(Config.update_status_id(), status)


async def read_update_status() -> str:
    """Read update status."""
    return (
        await cache.get(Config.update_status_id())
        if await cache.exists(Config.update_status_id())
        else "ready_to_update"
    )
