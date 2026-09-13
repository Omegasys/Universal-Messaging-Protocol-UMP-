"""
UMP Protocol API

High-level interface to the UMP messaging protocol.
"""


class ProtocolAPI:

    def __init__(
        self,
        message_builder=None,
        message_validator=None
    ):

        self.message_builder = message_builder
        self.message_validator = message_validator

    def create_message(
        self,
        message_type: str,
        sender: str,
        recipient: str,
        payload: dict
    ):

        if self.message_builder is None:
            raise RuntimeError(
                "Message builder is not configured"
            )

        return self.message_builder.create(
            message_type,
            sender,
            recipient,
            payload
        )

    def validate(
        self,
        message: dict
    ) -> bool:

        if self.message_validator is None:
            return False

        return self.message_validator.validate(
            message
        )
