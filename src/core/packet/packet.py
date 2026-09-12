"""
UMP Packet Object
"""

from dataclasses import dataclass


@dataclass
class Packet:

    packet_id: str
    message_id: str
    version: str

    data: bytes

    transport: str | None = None

    checksum: str | None = None

    fragment_number: int = 0
    total_fragments: int = 1


    def is_fragmented(self):

        return self.total_fragments > 1
