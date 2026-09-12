"""
UMP Message Keys

Creates individual message keys.
"""


class MessageKeyManager:


    def __init__(
        self,
        chain
    ):

        self.chain = chain



    def create_key(self):

        return {
            "message_number":
                self.chain.message_number,

            "key":
                self.chain.advance()
        }
