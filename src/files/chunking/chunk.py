"""
UMP File Chunk
"""

from dataclasses import dataclass


@dataclass
class Chunk:

    chunk_id: str
    attachment_id: str

    index: int
    total: int

    data: bytes

    def is_last(self) -> bool:
        return self.index == self.total - 1

    def size(self) -> int:
        return len(self.data)

    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "attachment_id": self.attachment_id,
            "index": self.index,
            "total": self.total,
            "size": len(self.data)
        }
