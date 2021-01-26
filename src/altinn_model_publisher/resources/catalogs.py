"""Resource module for catalog views."""
import asyncio
import gc

from aiohttp import hdrs
from aiohttp.web import Response, View

from altinn_model_publisher.config import Config
from altinn_model_publisher.service.altinn_service import (
    altinn_catalog,
    or_catalog,
    seres_catalog,
    update_altinn_catalog,
    update_or_catalog,
    update_seres_catalog,
)


class Altinn(View):
    """Class representing Altinn catalog resource."""

    @staticmethod
    async def get() -> Response:
        """Get Altinn catalog."""
        altinn_models = await asyncio.create_task(altinn_catalog())
        return Response(
            text=altinn_models,
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )

    @staticmethod
    async def post() -> Response:
        """Update Altinn catalog."""
        update_status = await asyncio.create_task(update_altinn_catalog())
        gc.collect()

        if update_status == Config.update_in_progress():
            return Response(text="Too Many Requests", status=429)
        else:
            return Response(text="OK")


class OR(View):
    """Class representing OR catalog resource."""

    @staticmethod
    async def get() -> Response:
        """Get OR catalog."""
        altinn_models = await asyncio.create_task(or_catalog())
        return Response(
            text=altinn_models,
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )

    @staticmethod
    async def post() -> Response:
        """Update OR catalog."""
        update_status = await asyncio.create_task(update_or_catalog())
        gc.collect()

        if update_status == Config.update_in_progress():
            return Response(text="Too Many Requests", status=429)
        else:
            return Response(text="OK")


class Seres(View):
    """Class representing Seres catalog resource."""

    @staticmethod
    async def get() -> Response:
        """Get Seres catalog."""
        altinn_models = await asyncio.create_task(seres_catalog())
        return Response(
            text=altinn_models,
            headers={hdrs.CONTENT_TYPE: "text/turtle"},
        )

    @staticmethod
    async def post() -> Response:
        """Update Seres catalog."""
        update_status = await asyncio.create_task(update_seres_catalog())
        gc.collect()

        if update_status == Config.update_in_progress():
            return Response(text="Too Many Requests", status=429)
        else:
            return Response(text="OK")
