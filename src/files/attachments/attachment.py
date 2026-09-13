"""
UMP File Attachment
"""

from dataclasses import dataclass


MAX_FILE_SIZE = 10 * 1024 * 1024 * 1024


@dataclass
class Attachment:

    attachment_id: str
    filename: str
    size: int
    mime_type: str

    checksum: str | None = None

    def is_valid_size(self) -> bool:
        return 0 <= self.size <= MAX_FILE_SIZE

    def to_dict(self) -> dict:
        return {
            "attachment_id": self.attachment_id,
            "filename": self.filename,
            "size": self.size,
            "mime_type": self.mime_type,
            "checksum": self.checksum
        }
