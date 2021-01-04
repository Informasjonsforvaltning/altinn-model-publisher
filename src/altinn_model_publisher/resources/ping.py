"""Resource module for ping."""
from aiohttp.web import Response, View


PING_ROUTE = "/ping"


class Ping(View):
    """Class representing ping resource."""

    @staticmethod
    async def get() -> Response:
        """Ping route function."""
        return Response(text="OK")
