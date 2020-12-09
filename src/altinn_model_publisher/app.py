"""Module for starting an aiohttp API."""
import logging
import os

from aiohttp import web

from altinn_model_publisher.service.altinn_mongo_service import save_update_status
from .resources.models import Models
from .resources.ping import Ping
from .resources.ready import Ready
from .resources.update import Update


async def set_ready_to_update_on_startup(app: web.Application) -> None:
    """Set ready to update status on startup in non test environments."""
    if os.getenv("IS_TEST") != "is_test":
        save_update_status("ready_to_update")


def setup_routes(app: web.Application) -> None:
    """Add active routes to application."""
    app.add_routes(
        [
            web.get("/models", Models),
            web.get("/ping", Ping),
            web.get("/ready", Ready),
            web.view("/update", Update),
        ]
    )


async def create_app() -> web.Application:
    """Create aiohttp application."""
    app = web.Application()
    app.on_startup.append(set_ready_to_update_on_startup)
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    return app
