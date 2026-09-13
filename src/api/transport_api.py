"""
UMP Transport API

High-level interface to registered transports.
"""


class TransportAPI:

    def __init__(
        self,
        transport_manager=None,
        transport_selector=None
    ):

        self.manager = transport_manager
        self.selector = transport_selector

    def register(
        self,
        transport
    ):

        if self.manager is None:
            raise RuntimeError(
                "Transport manager is not configured"
            )

        self.manager.register(
            transport
        )

    def available(self) -> list:

        if self.manager is None:
            return []

        return self.manager.available()

    def select(
        self,
        preferred: list[str] | None = None
    ):

        if self.manager is None:
            return None

        if self.selector is None:
            return None

        return self.selector.select(
            self.manager.available(),
            preferred
        )

    def send(
        self,
        transport_name: str,
        destination: str,
        data: bytes
    ) -> bool:

        transport = self.manager.get(
            transport_name
        )

        if transport is None:
            return False

        if not transport.available():
            return False

        return transport.send(
            destination,
            data
        )
