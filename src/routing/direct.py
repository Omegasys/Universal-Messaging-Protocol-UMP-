"""
UMP Direct Routing
"""


class DirectRouter:

    def send(
        self,
        destination: str,
        data: bytes
    ) -> dict:

        return {
            "type": "DIRECT",
            "destination": destination,
            "data": data
        }
