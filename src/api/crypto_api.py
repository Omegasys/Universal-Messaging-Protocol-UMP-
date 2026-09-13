"""
UMP Crypto API

High-level interface to cryptographic components.
"""


class CryptoAPI:

    def __init__(
        self,
        encryptor=None,
        decryptor=None,
        key_generator=None,
        signer=None,
        verifier=None
    ):

        self.encryptor = encryptor
        self.decryptor = decryptor
        self.key_generator = key_generator
        self.signer = signer
        self.verifier = verifier

    def generate_key(
        self,
        size: int = 32
    ):

        if self.key_generator is None:
            raise RuntimeError(
                "Key generator is not configured"
            )

        return self.key_generator.generate_key(
            size
        )

    def encrypt(
        self,
        data: bytes,
        key: bytes
    ):

        if self.encryptor is None:
            raise RuntimeError(
                "Encryptor is not configured"
            )

        return self.encryptor.encrypt(
            data,
            key
        )

    def decrypt(
        self,
        data: bytes,
        key: bytes
    ):

        if self.decryptor is None:
            raise RuntimeError(
                "Decryptor is not configured"
            )

        return self.decryptor.decrypt(
            data,
            key
        )

    def sign(
        self,
        data: bytes,
        private_key: str
    ):

        if self.signer is None:
            raise RuntimeError(
                "Signer is not configured"
            )

        return self.signer.sign(
            data,
            private_key
        )

    def verify(
        self,
        data: bytes,
        signature: str,
        public_key: str
    ) -> bool:

        if self.verifier is None:
            return False

        return self.verifier.verify(
            data,
            signature,
            public_key
        )
