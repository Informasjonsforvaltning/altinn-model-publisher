"""Resource module for update."""
from flask import Response
from flask_restful import Resource

from altinn_model_publisher.service.altinn_service import update_altinn_models_file


class Update(Resource):
    """Class representing update resource."""

    @staticmethod
    def post() -> Response:
        """Update file with altinn models."""
        update_altinn_models_file()
        return Response("OK")
