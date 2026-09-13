"""
UMP Key Formats

Serialization helpers for development key material.
"""

import json


def key_to_hex(
    key: bytes
) -> str:

    return key.hex()


def key_to_json(
    key: bytes
) -> str:

    return json.dumps(
        {
            "type": "symmetric",
            "encoding": "hex",
            "key": key_to_hex(key)
        },
        indent=2
    )


def identity_to_json(
    identity: dict
) -> str:

    return json.dumps(
        {
            "type": "development_identity",
            "public_key": identity[
                "public_key"
            ],
            "private_key": identity[
                "private_key"
            ]
        },
        indent=2
    )
