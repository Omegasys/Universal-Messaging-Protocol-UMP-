"""
UMP Tor Transport

Provides a transport interface for routing UMP
traffic through the Tor network.
"""

from ..transport_core.transport import Transport


class TorTransport(Transport):

    name = "TOR"

    def __init__(self):

        self.connection = None
        self.connected = False

    def connect(self, connection):

        self.connection = connection
        self.connected = True

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        if not self.connected:
            return False

        self.connection.send(
            destination,
            data
        )

        return True

    def receive(self) -> bytes | None:

        if not self.connected:
            return None

        return self.connection.receive()

    def close(self):

        if self.connection:
            self.connection.close()

        self.connection = None
        self.connected = False

    def available(self) -> bool:

        return self.connected
