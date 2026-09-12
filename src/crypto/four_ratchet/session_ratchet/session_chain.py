"""
UMP Session Ratchet Chain

Controls conversation-level key evolution.
"""


import hashlib



class SessionChain:


    def __init__(
        self,
        session_key: bytes
    ):

        self.key = session_key
        self.counter = 0



    def next_key(self):

        self.key = hashlib.sha256(
            self.key
        ).digest()

        self.counter += 1

        return self.key



    def state(self):

        return self.counter
