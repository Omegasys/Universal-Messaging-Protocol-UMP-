"""
UMP Text Message
"""

from dataclasses import dataclass


@dataclass
class TextMessage:

    text: str

    def to_payload(self) -> dict:
        return {
            "type": "TEXT",
            "text": self.text
        }
