"""Security module with authorization middleware."""
import logging
import os
from typing import Awaitable, Callable

from aiohttp import web


API_KEY = os.getenv("API_KEY", "secret-key")


@web.middleware
async def auth_middleware(
    request: web.Request,
    handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
) -> web.StreamResponse:
    """Middleware that raises HTTPForbidden for unauthorized POST requests."""
    if "POST" in request.method:
        auth_header = request.headers.get("X-API-KEY")
        if not auth_header or API_KEY not in auth_header:
            logging.error("Unauthorized update request")
            raise web.HTTPForbidden
    return await handler(request)
