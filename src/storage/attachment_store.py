"""
UMP Attachment Store
"""

from .database import Database


class AttachmentStore:

    TABLE = "attachments"

    def __init__(
        self,
        database: Database | None = None
    ):

        self.database = database or Database()

    def save(
        self,
        attachment_id: str,
        attachment
    ):

        self.database.insert(
            self.TABLE,
            attachment_id,
            attachment
        )

    def get(
        self,
        attachment_id: str
    ):

        return self.database.get(
            self.TABLE,
            attachment_id
        )

    def delete(
        self,
        attachment_id: str
    ) -> bool:

        return self.database.delete(
            self.TABLE,
            attachment_id
        )

    def all(self) -> list:

        return self.database.all(
            self.TABLE
        )
