"""
UMP File Upload
"""

from dataclasses import dataclass


@dataclass
class Upload:

    attachment_id: str

    total_size: int

    uploaded: int = 0

    completed: bool = False

    def update(self, amount: int):

        self.uploaded = min(
            self.uploaded + amount,
            self.total_size
        )

        if self.uploaded >= self.total_size:
            self.completed = True

    def progress(self) -> float:

        if self.total_size <= 0:
            return 0.0

        return self.uploaded / self.total_size
