"""Resource module for update."""
import asyncio

from aiohttp.web import Response, View

from altinn_model_publisher.service.altinn_service import (
    update_altinn_models,
    UPDATE_IN_PROGRESS,
)


UPDATE_ROUTE = "/update"


class Update(View):
    """Class representing update resource."""

    @staticmethod
    async def post() -> Response:
        """Update file with altinn models."""
        update_status = await asyncio.create_task(update_altinn_models())

        if update_status == UPDATE_IN_PROGRESS:
            return Response(text="Too Many Requests", status=429)
        else:
            return Response(text="OK")
