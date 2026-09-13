"""
UMP Wi-Fi Transport
"""

from ..transport_core.transport import Transport


class WiFiTransport(Transport):

    name = "WIFI"

    def __init__(self):

        self.connected = False
        self.inbox = []

    def connect(self):

        self.connected = True

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        if not self.connected:
            return False

        self.inbox.append(
            {
                "destination": destination,
                "data": data
            }
        )

        return True

    def receive(self) -> bytes | None:

        if not self.inbox:
            return None

        return self.inbox.pop(0)["data"]

    def available(self) -> bool:

        return self.connected
