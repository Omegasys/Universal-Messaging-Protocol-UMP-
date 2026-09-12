"""
UMP Message Parser

Converts serialized data into Message objects.
"""

from .message import Message


class MessageParser:

    def parse(self, data: dict) -> Message:

        security = data.get("security", {})

        return Message(
            version=data["version"],
            message_id=data["id"],
            message_type=data["type"],
            sender=data["sender"],
            recipient=data.get("recipient"),
            timestamp=data.get("timestamp"),
            payload=data.get("payload", {}),
            metadata=data.get("metadata", {}),
            encrypted=security.get("encrypted", False),
            ratchet=security.get("ratchet")
        )
