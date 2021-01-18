"""Configure altinn-model-publisher."""
import os
from typing import Dict, Set, Type, TypeVar


T = TypeVar("T", bound="Config")


class Config:
    """Configuration class."""

    _ALTINN_URI: str = os.getenv("ALTINN_URI", "https://www.altinn.no")
    _API_KEY = os.getenv("API_KEY", "secret-key")
    _CACHE_PASSWORD = os.getenv("CACHE_PASSWORD", None)
    _IS_TEST: str = os.getenv("IS_TEST", "not_test")
    _ORGANIZATION_CATALOGUE_URI = os.getenv(
        "ORGANIZATION_CATALOGUE_URI",
        "https://organization-catalogue.fellesdatakatalog.digdir.no",
    )
    _ALTINN_MODEL_PUBLISHER_URI = os.getenv(
        "ALTINN_MODEL_PUBLISHER_URI", "https://altinn-model-publisher.digdir.no"
    )
    _CACHE_VALUES = {
        "ALTINN_MODELS_ID": "altinn-models",
        "READY_TO_UPDATE": "ready_to_update",
        "UPDATE_IN_PROGRESS": "update_in_progress",
        "UPDATE_STATUS_ID": "update-status",
    }
    _ROUTES = {
        "MODELS": "/models",
        "PING": "/ping",
        "READY": "/ready",
        "UPDATE": "/update",
    }
    _PROTECTED_ROUTE_METHODS = {_ROUTES["UPDATE"]: {"POST"}}

    @classmethod
    def altinn_uri(cls: Type[T]) -> str:
        """Altinn URI."""
        return cls._ALTINN_URI

    @classmethod
    def api_key(cls: Type[T]) -> str:
        """API-key."""
        return cls._API_KEY

    @classmethod
    def is_test(cls: Type[T]) -> bool:
        """Is True when run in test environment."""
        return cls._IS_TEST == "is_test"

    @classmethod
    def organizations_uri(cls: Type[T]) -> str:
        """URI for organization-catalogue."""
        return cls._ORGANIZATION_CATALOGUE_URI

    @classmethod
    def self_uri(cls: Type[T]) -> str:
        """URI for altinn-model-publisher."""
        return cls._ALTINN_MODEL_PUBLISHER_URI

    @classmethod
    def routes(cls: Type[T]) -> Dict[str, str]:
        """Return a dict with route-value for available views."""
        return cls._ROUTES

    @classmethod
    def protected_routes(cls: Type[T]) -> Dict[str, Set[str]]:
        """Return a dict where request methods are keys and value is a list of protected routes for the method."""
        return cls._PROTECTED_ROUTE_METHODS

    @classmethod
    def cache_config(cls: Type[T]) -> Dict:
        """Configure cache."""
        config = {
            "default": {
                "cache": "aiocache.RedisCache",
                "endpoint": "publishers-cache",
                "port": 6379,
                "serializer": {"class": "aiocache.serializers.PickleSerializer"},
                "plugins": [
                    {"class": "aiocache.plugins.HitMissRatioPlugin"},
                    {"class": "aiocache.plugins.TimingPlugin"},
                ],
            },
        }
        if cls._CACHE_PASSWORD:
            config["default"]["password"] = cls._CACHE_PASSWORD

        return config

    @classmethod
    def altinn_models_id(cls: Type[T]) -> str:
        """Cache id for Altinn models."""
        return cls._CACHE_VALUES["ALTINN_MODELS_ID"]

    @classmethod
    def update_status_id(cls: Type[T]) -> str:
        """Cache id for current update status."""
        return cls._CACHE_VALUES["UPDATE_STATUS_ID"]

    @classmethod
    def ready_to_update(cls: Type[T]) -> str:
        """Update status value when ready to update."""
        return cls._CACHE_VALUES["READY_TO_UPDATE"]

    @classmethod
    def update_in_progress(cls: Type[T]) -> str:
        """Update status value when update in progress."""
        return cls._CACHE_VALUES["UPDATE_IN_PROGRESS"]
