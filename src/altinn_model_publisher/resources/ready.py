"""Resource module for ready."""
from flask import Response
from flask_restful import Resource


class Ready(Resource):
    """Class representing ready resource."""

    @staticmethod
    def get() -> Response:
        """Ready route function."""
        return Response("OK")
