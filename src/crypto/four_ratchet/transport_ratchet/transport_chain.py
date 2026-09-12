"""
UMP Transport Ratchet Chain

Protects changing network connections.
"""


import hashlib



class TransportChain:


    def __init__(
        self,
        transport_key: bytes
    ):

        self.key = transport_key
        self.transport_version = 0



    def rotate_transport(self):

        self.key = hashlib.sha256(
            self.key
        ).digest()

        self.transport_version += 1

        return self.key
