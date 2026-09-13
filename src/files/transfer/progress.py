"""
UMP Transfer Progress
"""


class TransferProgress:

    def __init__(
        self,
        total: int = 0
    ):

        self.total = total
        self.current = 0

    def update(self, amount: int):

        self.current = min(
            self.current + amount,
            self.total
        )

    def percentage(self) -> float:

        if self.total <= 0:
            return 0.0

        return (
            self.current /
            self.total
        ) * 100

    def complete(self) -> bool:

        return self.current >= self.total
