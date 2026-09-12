"""
UMP Message Object

Defines the core message structure.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class Message:
    version: str
    message_id: str
    message_type: str
    sender: str
    recipient: str
    payload: Dict[str, Any]

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    metadata: Dict[str, Any] = field(default_factory=dict)

    encrypted: bool = False
    ratchet: str | None = None


    def to_dict(self):
        return {
            "version": self.version,
            "id": self.message_id,
            "type": self.message_type,
            "sender": self.sender,
            "recipient": self.recipient,
            "timestamp": self.timestamp,
            "payload": self.payload,
            "metadata": self.metadata,
            "security": {
                "encrypted": self.encrypted,
                "ratchet": self.ratchet
            }
        }
