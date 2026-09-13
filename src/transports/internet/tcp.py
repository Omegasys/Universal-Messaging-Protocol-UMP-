"""
UMP TCP Transport
"""

import socket

from ..transport_core.transport import Transport


class TCPTransport(Transport):

    name = "TCP"

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None
    ):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):

        if self.host is None or self.port is None:
            raise ValueError(
                "TCP host and port are required"
            )

        self.socket = socket.create_connection(
            (self.host, self.port)
        )

    def send(
        self,
        destination: str,
        data: bytes
    ) -> bool:

        if self.socket is None:
            return False

        self.socket.sendall(data)

        return True

    def receive(self) -> bytes | None:

        if self.socket is None:
            return None

        return self.socket.recv(65535)

    def close(self):

        if self.socket:
            self.socket.close()
            self.socket = None
