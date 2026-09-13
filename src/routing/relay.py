"""
UMP Relay Routing
"""


class RelayRouter:

    def send(
        self,
        destination: str,
        data: bytes,
        next_hop: str | None = None
    ) -> dict:

        return {
            "type": "RELAY",
            "destination": destination,
            "next_hop": next_hop,
            "data": data
        }
