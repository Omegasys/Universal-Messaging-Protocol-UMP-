"""
UMP Video Message
"""

from dataclasses import dataclass


@dataclass
class Video:

    attachment_id: str
    mime_type: str = "video/mp4"

    def to_payload(self) -> dict:
        return {
            "type": "VIDEO",
            "attachment_id": self.attachment_id,
            "mime_type": self.mime_type
        }
