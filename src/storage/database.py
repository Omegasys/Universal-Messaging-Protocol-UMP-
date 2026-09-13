"""
UMP Database

Lightweight in-memory database abstraction.
A persistent backend can be added later.
"""


class Database:

    def __init__(self):

        self.tables = {}

    def create_table(
        self,
        name: str
    ):

        if name not in self.tables:
            self.tables[name] = {}

    def insert(
        self,
        table: str,
        key: str,
        value
    ):

        self.create_table(table)

        self.tables[table][key] = value

    def get(
        self,
        table: str,
        key: str
    ):

        return self.tables.get(
            table,
            {}
        ).get(key)

    def delete(
        self,
        table: str,
        key: str
    ) -> bool:

        if (
            table in self.tables
            and key in self.tables[table]
        ):

            del self.tables[table][key]
            return True

        return False

    def all(
        self,
        table: str
    ) -> list:

        return list(
            self.tables.get(
                table,
                {}
            ).values()
        )
