"""
UMP Protocol Debugger

Command-line utility for inspecting and tracing UMP packets.
"""

import argparse
import json
from pathlib import Path

from logger import DebugLogger
from packet_trace import PacketTrace


def load_packet(path: str) -> dict:
    packet_path = Path(path)

    if not packet_path.exists():
        raise FileNotFoundError(
            f"Packet not found: {packet_path}"
        )

    try:
        with packet_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid packet JSON: {error}"
        ) from error


def inspect_packet(packet: dict) -> dict:
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


def print_packet(packet: dict):
    print("UMP Packet")
    print("==========")

    for key, value in packet.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(
        description="UMP Protocol Debugger"
    )

    parser.add_argument(
        "packet",
        help="Path to a UMP packet JSON file"
    )

    parser.add_argument(
        "--trace",
        action="store_true",
        help="Create a packet trace"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger = DebugLogger(
        verbose=args.verbose
    )

    try:
        packet = load_packet(
            args.packet
        )

        logger.info(
            "Loaded packet"
        )

        inspected = inspect_packet(
            packet
        )

        if args.trace:

            trace = PacketTrace()

            trace.record(
                "RECEIVED",
                inspected
            )

            inspected["trace"] = (
                trace.to_list()
            )

        if args.json:

            print(
                json.dumps(
                    inspected,
                    indent=2
                )
            )

        else:

            print_packet(
                inspected
            )

    except (
        FileNotFoundError,
        ValueError
    ) as error:

        parser.error(
            str(error)
        )


if __name__ == "__main__":
    main()
