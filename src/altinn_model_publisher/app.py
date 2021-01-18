"""Module for starting an aiohttp API."""
import logging

from aiohttp import web

from altinn_model_publisher.config import Config
from altinn_model_publisher.security.auth import auth_middleware
from altinn_model_publisher.service.altinn_cache_service import save_update_status
from .resources.models import Models
from .resources.ping import Ping
from .resources.ready import Ready
from .resources.update import Update


async def set_ready_to_update_on_startup(app: web.Application) -> None:
    """Set ready to update status on startup in non test environments."""
    if not Config.is_test():
        await save_update_status(Config.ready_to_update())


def setup_routes(app: web.Application) -> None:
    """Add active routes to application."""
    app.add_routes(
        [
            web.get(Config.routes()["MODELS"], Models),
            web.get(Config.routes()["PING"], Ping),
            web.get(Config.routes()["READY"], Ready),
            web.view(Config.routes()["UPDATE"], Update),
        ]
    )


async def create_app() -> web.Application:
    """Create aiohttp application."""
    app = web.Application(middlewares=[auth_middleware])
    app.on_startup.append(set_ready_to_update_on_startup)
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    return app
