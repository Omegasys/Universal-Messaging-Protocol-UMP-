"""
UMP Transport Selector

Selects an appropriate available transport.
"""


class TransportSelector:

    def select(
        self,
        transports,
        preferred: list[str] | None = None
    ):

        available = [
            transport
            for transport in transports
            if transport.available()
        ]

        if preferred:

            for name in preferred:

                for transport in available:

                    if transport.name == name:
                        return transport

        return available[0] if available else None
