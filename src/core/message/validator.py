"""
UMP Message Validator
"""


class MessageValidator:


    REQUIRED_FIELDS = [
        "version",
        "id",
        "type",
        "sender",
        "payload"
    ]


    def validate(self, message: dict):

        for field in self.REQUIRED_FIELDS:
            if field not in message:
                return False

        return True
