"""
UMP MMS Transport

MMS compatibility transport.
"""

from ...transport_core.transport import Transport
from .media_handler import MediaHandler


class MMSTransport(Transport):

    name = "MMS"

    def __init__(self):
        self.media_handler = MediaHandler()
        self.inbox = []

    def send(
        self,
        destination: str,
        data: bytes,
        mime_type: str = "application/octet-stream"
    ) -> bool:

        media = self.media_handler.create(
            data,
            mime_type
        )

        self.inbox.append(
            {
                "destination": destination,
                "media": media
            }
        )

        return True

    def receive(self) -> bytes | None:

        if not self.inbox:
            return None

        message = self.inbox.pop(0)

        return message["media"]["data"]
