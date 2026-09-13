"""
UMP Chunk Manager

Splits and reassembles file attachments.
"""

import uuid

from .chunk import Chunk


class ChunkManager:

    def __init__(self, chunk_size: int = 1024 * 1024):
        self.chunk_size = chunk_size

    def split(
        self,
        attachment_id: str,
        data: bytes
    ) -> list[Chunk]:

        if not data:
            return []

        total = (
            len(data) + self.chunk_size - 1
        ) // self.chunk_size

        chunks = []

        for index in range(total):

            start = index * self.chunk_size
            end = start + self.chunk_size

            chunks.append(
                Chunk(
                    chunk_id=str(uuid.uuid4()),
                    attachment_id=attachment_id,
                    index=index,
                    total=total,
                    data=data[start:end]
                )
            )

        return chunks

    def reassemble(
        self,
        chunks: list[Chunk]
    ) -> bytes:

        chunks = sorted(
            chunks,
            key=lambda chunk: chunk.index
        )

        return b"".join(
            chunk.data
            for chunk in chunks
        )
