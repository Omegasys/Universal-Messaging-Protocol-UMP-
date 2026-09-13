"""
UMP Mesh Relay

Provides basic packet forwarding between mesh nodes.
"""


class MeshRelay:

    def __init__(self):

        self.routes = {}

    def add_route(
        self,
        destination: str,
        next_hop: str
    ):

        self.routes[destination] = next_hop

    def remove_route(
        self,
        destination: str
    ):

        self.routes.pop(
            destination,
            None
        )

    def next_hop(
        self,
        destination: str
    ) -> str | None:

        return self.routes.get(
            destination
        )

    def relay(
        self,
        destination: str,
        data: bytes
    ) -> dict | None:

        next_hop = self.next_hop(
            destination
        )

        if next_hop is None:
            return None

        return {
            "destination": destination,
            "next_hop": next_hop,
            "data": data
        }
