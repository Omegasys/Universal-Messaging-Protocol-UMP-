"""
UMP Message Store
"""

from .database import Database


class MessageStore:

    TABLE = "messages"

    def __init__(
        self,
        database: Database | None = None
    ):

        self.database = database or Database()

    def save(
        self,
        message_id: str,
        message
    ):

        self.database.insert(
            self.TABLE,
            message_id,
            message
        )

    def get(
        self,
        message_id: str
    ):

        return self.database.get(
            self.TABLE,
            message_id
        )

    def delete(
        self,
        message_id: str
    ) -> bool:

        return self.database.delete(
            self.TABLE,
            message_id
        )

    def all(self) -> list:

        return self.database.all(
            self.TABLE
        )
