"""
UMP SMS Transport

SMS compatibility transport.

The actual cellular/modem integration should be
provided by the platform or carrier interface.
"""

from ...transport_core.transport import Transport
from .sms_codec import SMSCodec


class SMSTransport(Transport):

    name = "SMS"

    def __init__(self):
        self.codec = SMSCodec()
        self.inbox = []

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        encoded = self.codec.encode(data)

        self.inbox.append(
            {
                "destination": destination,
                "data": encoded
            }
        )

        return True

    def receive(self) -> bytes | None:

        if not self.inbox:
            return None

        message = self.inbox.pop(0)

        return self.codec.decode(
            message["data"]
        )
