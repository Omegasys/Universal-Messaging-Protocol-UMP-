"""
UMP SMS Codec

Encodes UMP data for SMS-compatible transport.
"""


class SMSCodec:

    MAX_PAYLOAD = 140

    def encode(self, data: bytes) -> bytes:

        if len(data) > self.MAX_PAYLOAD:
            raise ValueError(
                "Data exceeds single SMS payload size"
            )

        return data

    def decode(self, data: bytes) -> bytes:

        return data
