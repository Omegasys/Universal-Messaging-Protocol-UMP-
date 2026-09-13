"""
UMP MMS Media Handler
"""


class MediaHandler:

    def create(
        self,
        data: bytes,
        mime_type: str
    ) -> dict:

        return {
            "mime_type": mime_type,
            "size": len(data),
            "data": data
        }

    def extract(
        self,
        media: dict
    ) -> bytes:

        return media["data"]
