"""
UMP Extension API

Provides a simple interface for optional protocol extensions.
"""


class ExtensionAPI:

    def __init__(self):

        self.extensions = {}

    def register(
        self,
        name: str,
        extension
    ):

        self.extensions[name] = extension

    def unregister(
        self,
        name: str
    ):

        self.extensions.pop(
            name,
            None
        )

    def get(
        self,
        name: str
    ):

        return self.extensions.get(
            name
        )

    def list(self) -> list[str]:

        return list(
            self.extensions.keys()
        )

    def has(
        self,
        name: str
    ) -> bool:

        return name in self.extensions
