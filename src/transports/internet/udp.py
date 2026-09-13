"""
UMP UDP Transport
"""

import socket

from ..transport_core.transport import Transport


class UDPTransport(Transport):

    name = "UDP"

    def __init__(self):

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        host, port = destination.rsplit(
            ":",
            1
        )

        self.socket.sendto(
            data,
            (host, int(port))
        )

        return True

    def receive(self) -> bytes | None:

        data, _ = self.socket.recvfrom(
            65535
        )

        return data

    def close(self):

        self.socket.close()
