"""Resource module for models."""
import asyncio

from aiohttp import hdrs
from aiohttp.web import Response, View

from altinn_model_publisher.service.altinn_service import all_altinn_models


MODELS_ROUTE = "/models"


class Models(View):
    """Class representing models resource."""

    @staticmethod
    async def get() -> Response:
        """Get all altinn models."""
        altinn_models = await asyncio.create_task(all_altinn_models())
        return Response(
            text=altinn_models,
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )
