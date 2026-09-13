"""
UMP File Hashing
"""

import hashlib


class FileHasher:

    def __init__(
        self,
        algorithm: str = "sha256"
    ):

        self.algorithm = algorithm

    def hash(
        self,
        data: bytes
    ) -> str:

        hasher = hashlib.new(
            self.algorithm
        )

        hasher.update(data)

        return hasher.hexdigest()
