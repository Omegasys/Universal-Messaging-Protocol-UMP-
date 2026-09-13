"""
UMP Router

Coordinates route selection and packet delivery.
"""

from .route_selection import RouteSelector
from .direct import DirectRouter
from .relay import RelayRouter
from .mesh import MeshRouter
from .fallback import FallbackRouter


class Router:

    def __init__(self):

        self.selector = RouteSelector()

        self.direct = DirectRouter()
        self.relay = RelayRouter()
        self.mesh = MeshRouter()
        self.fallback = FallbackRouter()

    def route(
        self,
        destination: str,
        data: bytes,
        routes: list[dict]
    ):

        route = self.selector.select(routes)

        if route is None:
            return None

        route_type = route.get("type")

        if route_type == "DIRECT":
            return self.direct.send(
                destination,
                data
            )

        if route_type == "RELAY":
            return self.relay.send(
                destination,
                data,
                route.get("next_hop")
            )

        if route_type == "MESH":
            return self.mesh.send(
                destination,
                data,
                route.get("path", [])
            )

        return self.fallback.send(
            destination,
            data,
            routes
        )
