"""
UMP Image Message
"""

from dataclasses import dataclass


@dataclass
class Image:

    attachment_id: str
    mime_type: str = "image/jpeg"

    def to_payload(self) -> dict:
        return {
            "type": "IMAGE",
            "attachment_id": self.attachment_id,
            "mime_type": self.mime_type
        }
