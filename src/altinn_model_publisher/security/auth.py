"""Security module with authorization middleware."""
import logging
import os
from typing import Awaitable, Callable

from aiohttp import web

from altinn_model_publisher.resources.update import UPDATE_ROUTE


API_KEY = os.getenv("API_KEY", "secret-key")
PROTECTED_ROUTE_METHODS = {UPDATE_ROUTE: {"POST"}}


def request_is_protected(request: web.Request) -> bool:
    """Return true when route is protected for method."""
    protected_methods = PROTECTED_ROUTE_METHODS.get(request.path)
    return request.method in protected_methods if protected_methods else False


@web.middleware
async def auth_middleware(
    request: web.Request,
    handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
) -> web.StreamResponse:
    """Middleware that raises HTTPForbidden for unauthorized requests to protected routes."""
    if request_is_protected(request):
        auth_header = request.headers.get("X-API-KEY")
        if not auth_header or API_KEY not in auth_header:
            logging.error("Unauthorized update request")
            raise web.HTTPForbidden
    return await handler(request)
