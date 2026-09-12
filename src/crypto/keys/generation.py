"""
UMP Key Generation

Creates cryptographic key material.
"""


import secrets



class KeyGenerator:


    def generate_key(
        self,
        size=32
    ):

        """
        Generate random key material.
        """

        return secrets.token_bytes(size)



    def generate_identity_keypair(self):

        """
        Creates identity key placeholders.

        Real implementation should use
        an approved asymmetric algorithm.
        """

        return {

            "public_key":
                secrets.token_hex(32),

            "private_key":
                secrets.token_hex(32)

        }
