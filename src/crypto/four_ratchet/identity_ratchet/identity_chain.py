"""
UMP Identity Ratchet Chain

Maintains long-term identity key evolution.
"""


import hashlib


class IdentityChain:


    def __init__(self, root_key: bytes):

        self.current_key = root_key
        self.version = 0



    def advance(self):

        self.current_key = hashlib.sha256(
            self.current_key
        ).digest()

        self.version += 1

        return self.current_key



    def get_version(self):

        return self.version
