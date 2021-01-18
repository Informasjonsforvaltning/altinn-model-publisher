"""Security module with authorization middleware."""
import logging
from typing import Awaitable, Callable

from aiohttp import web

from altinn_model_publisher.config import Config


def request_is_protected(request: web.Request) -> bool:
    """Return true when route is protected for method."""
    protected_methods = Config.protected_routes().get(request.path)
    return request.method in protected_methods if protected_methods else False


@web.middleware
async def auth_middleware(
    request: web.Request,
    handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
) -> web.StreamResponse:
    """Middleware that raises HTTPForbidden for unauthorized requests to protected routes."""
    if request_is_protected(request):
        auth_header = request.headers.get("X-API-KEY")
        if not auth_header or Config.api_key() not in auth_header:
            logging.error("Unauthorized update request")
            raise web.HTTPForbidden
    return await handler(request)
