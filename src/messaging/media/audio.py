"""
UMP Audio Message
"""

from dataclasses import dataclass


@dataclass
class Audio:

    attachment_id: str
    mime_type: str = "audio/mpeg"

    def to_payload(self) -> dict:
        return {
            "type": "AUDIO",
            "attachment_id": self.attachment_id,
            "mime_type": self.mime_type
        }
