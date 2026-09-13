"""
UMP Message Receipts
"""

from enum import Enum


class ReceiptStatus(Enum):

    SENT = "SENT"
    DELIVERED = "DELIVERED"
    READ = "READ"
    FAILED = "FAILED"


class Receipt:

    def __init__(
        self,
        message_id: str,
        status: ReceiptStatus
    ):
        self.message_id = message_id
        self.status = status

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "status": self.status.value
        }
