"""
UMP Packet Inspector

Command-line utility for inspecting UMP packets.
"""

import argparse
import json
from pathlib import Path

from decode import decode_packet


def main():

    parser = argparse.ArgumentParser(
        description="Inspect a UMP packet"
    )

    parser.add_argument(
        "packet",
        help="Path to packet JSON file"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON"
    )

    parser.add_argument(
        "--header",
        action="store_true",
        help="Show packet header only"
    )

    args = parser.parse_args()

    path = Path(args.packet)

    if not path.exists():
        parser.error(
            f"Packet not found: {path}"
        )

    try:
        with path.open(
            "r",
            encoding="utf-8"
        ) as file:

            packet = json.load(file)

    except json.JSONDecodeError as error:
        parser.error(
            f"Invalid JSON: {error}"
        )

    decoded = decode_packet(packet)

    if args.header:

        decoded = {
            "version": decoded.get("version"),
            "packet_id": decoded.get("packet_id"),
            "message_id": decoded.get("message_id"),
            "packet_type": decoded.get("packet_type")
        }

    if args.json:

        print(
            json.dumps(
                decoded,
                indent=2
            )
        )

        return

    print("UMP Packet")
    print("==========")

    for key, value in decoded.items():

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()
