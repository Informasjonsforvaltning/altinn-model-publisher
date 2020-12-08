"""Resource module for update."""
import asyncio

from flask import Response
from flask_restful import Resource

from altinn_model_publisher.service.altinn_service import update_altinn_models


class Update(Resource):
    """Class representing update resource."""

    @staticmethod
    def post() -> Response:
        """Update file with altinn models."""
        asyncio.run(update_altinn_models())
        return Response("OK")
