"""
UMP Decryption Module
"""


class Decryptor:


    def __init__(self, algorithm="AEAD"):

        self.algorithm = algorithm



    def decrypt(
        self,
        encrypted_data: bytes,
        key: bytes
    ):

        """
        Decrypt encrypted data.
        """

        # Placeholder decryption interface

        decrypted = encrypted_data

        return decrypted
