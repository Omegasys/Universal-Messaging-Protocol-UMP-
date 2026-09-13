"""
UMP Packet Decoder
"""


def decode_packet(packet: dict) -> dict:

    header = packet.get(
        "header",
        {}
    )

    fragments = packet.get(
        "fragments",
        {}
    )

    security = packet.get(
        "security",
        {}
    )

    return {
        "version": packet.get(
            "version",
            header.get("version")
        ),

        "packet_id": packet.get(
            "packet_id",
            header.get("packet_id")
        ),

        "message_id": packet.get(
            "message_id",
            header.get("message_id")
        ),

        "packet_type": packet.get(
            "packet_type",
            header.get(
                "packet_type",
                "DATA"
            )
        ),

        "transport": packet.get(
            "transport"
        ),

        "fragment_number": fragments.get(
            "number",
            packet.get(
                "fragment_number",
                0
            )
        ),

        "total_fragments": fragments.get(
            "total",
            packet.get(
                "total_fragments",
                1
            )
        ),

        "encrypted": security.get(
            "encrypted",
            packet.get(
                "encrypted",
                False
            )
        ),

        "ratchet": security.get(
            "ratchet"
        ),

        "payload_size": packet.get(
            "payload_size",
            0
        )
    }
