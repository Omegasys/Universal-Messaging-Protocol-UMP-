"""
UMP Fallback Routing

Attempts routes in priority order until an
available route is found.
"""


class FallbackRouter:

    def send(
        self,
        destination: str,
        data: bytes,
        routes: list[dict]
    ) -> dict | None:

        ordered = sorted(
            routes,
            key=lambda route: route.get(
                "priority",
                0
            )
        )

        for route in ordered:

            if not route.get(
                "available",
                True
            ):
                continue

            return {
                "type": "FALLBACK",
                "route": route,
                "destination": destination,
                "data": data
            }

        return None
