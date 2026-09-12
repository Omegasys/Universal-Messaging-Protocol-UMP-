"""
UMP Packet Fragmentation

Splits large messages into smaller packets.
"""


from .packet import Packet
import uuid


class Fragmenter:


    def __init__(self, chunk_size=4096):

        self.chunk_size = chunk_size



    def fragment(
        self,
        message_id,
        data: bytes
    ):

        packets = []

        total = (
            len(data) + self.chunk_size - 1
        ) // self.chunk_size


        for index in range(total):

            start = index * self.chunk_size

            end = start + self.chunk_size


            packets.append(
                Packet(
                    packet_id=str(uuid.uuid4()),
                    message_id=message_id,
                    version="1.0",
                    data=data[start:end],
                    fragment_number=index,
                    total_fragments=total
                )
            )

        return packets
