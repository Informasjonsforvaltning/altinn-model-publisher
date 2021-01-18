"""Resource module for update."""
import asyncio

from aiohttp.web import Response, View

from altinn_model_publisher.config import Config
from altinn_model_publisher.service.altinn_service import update_altinn_models


class Update(View):
    """Class representing update resource."""

    @staticmethod
    async def post() -> Response:
        """Update file with altinn models."""
        update_status = await asyncio.create_task(update_altinn_models())

        if update_status == Config.update_in_progress():
            return Response(text="Too Many Requests", status=429)
        else:
            return Response(text="OK")
