"""Resource module for ready."""
from typing import Any

from flask import abort, request, Response
from flask_restful import Resource

from altinn_model_publisher.service.altinn_service import is_ready


class Ready(Resource):
    """Class representing ready resource."""

    @staticmethod
    def get() -> Any:
        """Ready route function."""
        if is_ready(request.headers.get("Accept")):
            return Response("OK")
        else:
            abort(503)
