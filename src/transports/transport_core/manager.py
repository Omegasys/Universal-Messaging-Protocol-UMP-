"""
UMP Transport Manager
"""

from .transport import Transport


class TransportManager:

    def __init__(self):
        self.transports: dict[str, Transport] = {}

    def register(self, transport: Transport):

        self.transports[transport.name] = transport

    def unregister(self, name: str):

        self.transports.pop(name, None)

    def get(self, name: str) -> Transport | None:

        return self.transports.get(name)

    def available(self) -> list[Transport]:

        return [
            transport
            for transport in self.transports.values()
            if transport.available()
        ]
