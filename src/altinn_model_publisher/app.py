"""Module for starting an aiohttp API."""
import logging
import os

from aiohttp import web

from altinn_model_publisher.security.auth import auth_middleware
from altinn_model_publisher.service.altinn_cache_service import save_update_status
from .resources.models import Models, MODELS_ROUTE
from .resources.ping import Ping, PING_ROUTE
from .resources.ready import Ready, READY_ROUTE
from .resources.update import Update, UPDATE_ROUTE


async def set_ready_to_update_on_startup(app: web.Application) -> None:
    """Set ready to update status on startup in non test environments."""
    if os.getenv("IS_TEST") != "is_test":
        await save_update_status("ready_to_update")


def setup_routes(app: web.Application) -> None:
    """Add active routes to application."""
    app.add_routes(
        [
            web.get(MODELS_ROUTE, Models),
            web.get(PING_ROUTE, Ping),
            web.get(READY_ROUTE, Ready),
            web.view(UPDATE_ROUTE, Update),
        ]
    )


async def create_app() -> web.Application:
    """Create aiohttp application."""
    app = web.Application(middlewares=[auth_middleware])
    app.on_startup.append(set_ready_to_update_on_startup)
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    return app
