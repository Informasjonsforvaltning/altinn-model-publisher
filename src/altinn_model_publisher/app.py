"""Module for starting an aiohttp API."""
import logging

from aiohttp import web

from .resources.models import Models
from .resources.ping import Ping
from .resources.ready import Ready
from .resources.update import Update


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
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    return app
