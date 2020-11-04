"""Resource module for models."""
from flask import Response
from flask_restful import Resource

from altinn_model_publisher.service.altinn_service import all_altinn_models


class Models(Resource):
    """Class representing models resource."""

    @staticmethod
    def get() -> Response:
        """Get all altinn models."""
        return Response(
            all_altinn_models(),
            mimetype="text/turtle",
        )
