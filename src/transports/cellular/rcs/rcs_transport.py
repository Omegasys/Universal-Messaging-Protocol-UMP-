"""
UMP RCS Transport

RCS compatibility transport.
"""

from ...transport_core.transport import Transport
from .rcs_adapter import RCSAdapter


class RCSTransport(Transport):

    name = "RCS"

    def __init__(self):
        self.adapter = RCSAdapter()
        self.inbox = []

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        message = self.adapter.encode(
            destination,
            data
        )

        self.inbox.append(message)

        return True

    def receive(self) -> bytes | None:

        if not self.inbox:
            return None

        message = self.inbox.pop(0)

        return self.adapter.decode(message)
