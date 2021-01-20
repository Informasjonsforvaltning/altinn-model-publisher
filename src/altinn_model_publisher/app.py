"""Module for starting an aiohttp API."""
import logging

from aiohttp import web

from altinn_model_publisher.config import Config
from altinn_model_publisher.security.auth import auth_middleware
from altinn_model_publisher.service.altinn_cache_service import save_update_status
from .resources.catalogs import Altinn, OR, Seres
from .resources.ping import Ping
from .resources.ready import Ready


async def set_ready_to_update_on_startup(app: web.Application) -> None:
    """Set ready to update status on startup in non test environments."""
    if not Config.is_test():
        await save_update_status(Config.ready_to_update())


def setup_routes(app: web.Application) -> None:
    """Add active routes to application."""
    app.add_routes(
        [
            web.view(Config.routes()["ALTINN"], Altinn),
            web.view(Config.routes()["OR"], OR),
            web.get(Config.routes()["PING"], Ping),
            web.get(Config.routes()["READY"], Ready),
            web.view(Config.routes()["SERES"], Seres),
        ]
    )


async def create_app() -> web.Application:
    """Create aiohttp application."""
    app = web.Application(middlewares=[auth_middleware])
    app.on_startup.append(set_ready_to_update_on_startup)
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    return app
