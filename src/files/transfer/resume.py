"""
UMP Transfer Resume

Tracks the point from which a transfer can continue.
"""


class ResumeManager:

    def __init__(self):
        self.positions = {}

    def save(
        self,
        attachment_id: str,
        offset: int
    ):

        self.positions[attachment_id] = offset

    def get(
        self,
        attachment_id: str
    ) -> int:

        return self.positions.get(
            attachment_id,
            0
        )

    def clear(
        self,
        attachment_id: str
    ):

        self.positions.pop(
            attachment_id,
            None
        )
