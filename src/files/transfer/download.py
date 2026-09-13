"""
UMP File Download
"""

from dataclasses import dataclass


@dataclass
class Download:

    attachment_id: str

    total_size: int

    downloaded: int = 0

    completed: bool = False

    def update(self, amount: int):

        self.downloaded = min(
            self.downloaded + amount,
            self.total_size
        )

        if self.downloaded >= self.total_size:
            self.completed = True

    def progress(self) -> float:

        if self.total_size <= 0:
            return 0.0

        return self.downloaded / self.total_size
