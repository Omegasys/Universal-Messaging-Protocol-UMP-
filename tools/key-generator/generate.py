"""
UMP Key Generator

Generates development/test key material.
"""

import argparse
import json

from formats import (
    key_to_hex,
    key_to_json,
    identity_to_json
)

from secrets import token_bytes


def generate_key(size: int) -> bytes:

    if size <= 0:
        raise ValueError(
            "Key size must be greater than zero"
        )

    return token_bytes(size)


def generate_identity() -> dict:

    return {
        "public_key": key_to_hex(
            generate_key(32)
        ),

        "private_key": key_to_hex(
            generate_key(32)
        )
    }


def main():

    parser = argparse.ArgumentParser(
        description="Generate UMP development key material"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    key_parser = subparsers.add_parser(
        "key",
        help="Generate a random key"
    )

    key_parser.add_argument(
        "--size",
        type=int,
        default=32,
        help="Key size in bytes"
    )

    key_parser.add_argument(
        "--format",
        choices=[
            "hex",
            "json"
        ],
        default="hex"
    )

    subparsers.add_parser(
        "identity",
        help="Generate development identity material"
    )

    args = parser.parse_args()

    if args.command == "key":

        key = generate_key(
            args.size
        )

        if args.format == "json":

            print(
                key_to_json(key)
            )

        else:

            print(
                key_to_hex(key)
            )

    elif args.command == "identity":

        identity = generate_identity()

        print(
            identity_to_json(identity)
        )


if __name__ == "__main__":
    main()
