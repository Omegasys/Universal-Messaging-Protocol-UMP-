"""
UMP LoRa Transport

Low-bandwidth long-range transport interface.
"""

from ..transport_core.transport import Transport


class LoRaTransport(Transport):

    name = "LORA"

    def __init__(
        self,
        max_payload: int = 255
    ):

        self.max_payload = max_payload
        self.inbox = []

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        if len(data) > self.max_payload:
            raise ValueError(
                "Data exceeds LoRa payload size"
            )

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
