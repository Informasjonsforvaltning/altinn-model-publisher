"""Resource module for ready."""
from flask import abort, Response
from flask_restful import Resource

from altinn_model_publisher.service.altinn_service import is_ready


class Ready(Resource):
    """Class representing ready resource."""

    @staticmethod
    def get() -> Response:
        """Ready route function."""
        if is_ready():
            return Response("OK")
        else:
            abort(503)
