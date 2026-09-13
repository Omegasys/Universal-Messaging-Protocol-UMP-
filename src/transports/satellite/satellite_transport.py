"""
UMP Satellite Transport

Provides an interface for satellite-based
UMP communication.
"""

from ..transport_core.transport import Transport


class SatelliteTransport(Transport):

    name = "SATELLITE"

    def __init__(
        self,
        max_payload: int = 1024
    ):

        self.max_payload = max_payload
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

        if len(data) > self.max_payload:
            raise ValueError(
                "Data exceeds satellite transport payload size"
            )

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
