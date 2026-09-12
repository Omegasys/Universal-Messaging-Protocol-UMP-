"""
UMP Packet Reassembly

Combines fragmented packets back into data.
"""


class Reassembler:


    def assemble(self, packets):

        packets = sorted(
            packets,
            key=lambda x: x.fragment_number
        )

        data = b""

        for packet in packets:
            data += packet.data


        return data
