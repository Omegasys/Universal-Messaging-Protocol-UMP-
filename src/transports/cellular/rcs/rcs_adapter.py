"""
UMP RCS Adapter

Provides the interface between UMP and an
RCS implementation.
"""


class RCSAdapter:

    def encode(
        self,
        destination: str,
        data: bytes
    ) -> dict:

        return {
            "destination": destination,
            "data": data,
            "content_type": "application/ump"
        }

    def decode(
        self,
        message: dict
    ) -> bytes:

        return message["data"]
