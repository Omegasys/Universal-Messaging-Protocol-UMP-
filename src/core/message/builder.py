"""
UMP Message Builder

Creates messages using the UMP format.
"""

import uuid

from .message import Message


class MessageBuilder:

    def __init__(self):
        self.version = "1.0"


    def create(
        self,
        message_type,
        sender,
        recipient,
        payload
    ):

        return Message(
            version=self.version,
            message_id=str(uuid.uuid4()),
            message_type=message_type,
            sender=sender,
            recipient=recipient,
            payload=payload
        )
