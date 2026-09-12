"""
UMP Digital Signatures

Creates message signatures.
"""


class Signer:


    def sign(
        self,
        data: bytes,
        private_key: str
    ):

        """
        Create a digital signature.

        Placeholder implementation.
        """

        signature = (
            str(hash(data))
        )

        return signature
