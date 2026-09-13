"""
UMP Route Selection
"""


class RouteSelector:

    def select(
        self,
        routes: list[dict]
    ) -> dict | None:

        available = [
            route
            for route in routes
            if route.get("available", True)
        ]

        if not available:
            return None

        return min(
            available,
            key=lambda route: route.get(
                "cost",
                0
            )
        )
