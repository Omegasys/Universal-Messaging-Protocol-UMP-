"""
UMP Message Ratchet Chain

Creates a new key state for every message.
"""


import hashlib



class MessageChain:


    def __init__(
        self,
        chain_key: bytes
    ):

        self.chain_key = chain_key
        self.message_number = 0



    def advance(self):

        self.chain_key = hashlib.sha256(
            self.chain_key
        ).digest()

        self.message_number += 1

        return self.chain_key
