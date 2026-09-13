"""
UMP Bluetooth Transport
"""

from ..transport_core.transport import Transport


class BluetoothTransport(Transport):

    name = "BLUETOOTH"

    def __init__(self):

        self.connected_devices = {}
        self.inbox = []

    def connect(
        self,
        device_id: str
    ):

        self.connected_devices[
            device_id
        ] = True

    def disconnect(
        self,
        device_id: str
    ):

        self.connected_devices.pop(
            device_id,
            None
        )

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        if destination not in self.connected_devices:
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

        return bool(self.connected_devices)
