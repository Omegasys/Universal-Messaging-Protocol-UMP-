"""
UMP Signature Verification
"""


class SignatureVerifier:


    def verify(
        self,
        data: bytes,
        signature: str,
        public_key: str
    ):

        """
        Verify a digital signature.

        Placeholder implementation.
        """

        expected = str(hash(data))


        return signature == expected
