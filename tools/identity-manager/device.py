"""
UMP Device Manager

Manages devices belonging to UMP identities.
"""

import argparse
import json

from identity import identities


def add_device(
    identity_id: str,
    device_id: str,
    device_key: str
) -> dict:

    identity = identities.get(
        identity_id
    )

    if identity is None:
        raise ValueError(
            "Identity not found"
        )

    device = {
        "device_id": device_id,
        "device_key": device_key,
        "status": "ACTIVE"
    }

    identity["devices"].append(
        device
    )

    return device


def list_devices(
    identity_id: str
) -> list:

    identity = identities.get(
        identity_id
    )

    if identity is None:
        raise ValueError(
            "Identity not found"
        )

    return identity["devices"]


def main():

    parser = argparse.ArgumentParser(
        description="UMP Device Manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add = subparsers.add_parser(
        "add"
    )

    add.add_argument(
        "identity_id"
    )

    add.add_argument(
        "device_id"
    )

    add.add_argument(
        "device_key"
    )

    listing = subparsers.add_parser(
        "list"
    )

    listing.add_argument(
        "identity_id"
    )

    args = parser.parse_args()

    try:

        if args.command == "add":

            device = add_device(
                args.identity_id,
                args.device_id,
                args.device_key
            )

            print(
                json.dumps(
                    device,
                    indent=2
                )
            )

        elif args.command == "list":

            devices = list_devices(
                args.identity_id
            )

            print(
                json.dumps(
                    devices,
                    indent=2
                )
            )

    except ValueError as error:

        parser.error(str(error))


if __name__ == "__main__":
    main()
