"""
UMP Identity and Device Revocation
"""

import argparse

from identity import identities


def revoke_device(
    identity_id: str,
    device_id: str
) -> bool:

    identity = identities.get(
        identity_id
    )

    if identity is None:
        return False

    for device in identity["devices"]:

        if device["device_id"] == device_id:

            device["status"] = "REVOKED"

            return True

    return False


def revoke_identity(
    identity_id: str
) -> bool:

    identity = identities.get(
        identity_id
    )

    if identity is None:
        return False

    identity["active"] = False

    return True


def main():

    parser = argparse.ArgumentParser(
        description="UMP Revocation Manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    device = subparsers.add_parser(
        "device"
    )

    device.add_argument(
        "identity_id"
    )

    device.add_argument(
        "device_id"
    )

    identity = subparsers.add_parser(
        "identity"
    )

    identity.add_argument(
        "identity_id"
    )

    args = parser.parse_args()

    if args.command == "device":

        if not revoke_device(
            args.identity_id,
            args.device_id
        ):

            parser.error(
                "Identity or device not found"
            )

        print(
            f"Device '{args.device_id}' revoked"
        )

    elif args.command == "identity":

        if not revoke_identity(
            args.identity_id
        ):

            parser.error(
                "Identity not found"
            )

        print(
            f"Identity '{args.identity_id}' revoked"
        )


if __name__ == "__main__":
    main()
