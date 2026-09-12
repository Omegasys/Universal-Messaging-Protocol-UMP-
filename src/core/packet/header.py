"""
UMP Packet Header
"""

from dataclasses import dataclass


@dataclass
class PacketHeader:

    version: str
    packet_id: str
    message_id: str
    packet_type: str = "DATA"


    def to_dict(self):

        return {
            "version": self.version,
            "packet_id": self.packet_id,
            "message_id": self.message_id,
            "packet_type": self.packet_type
        }
