"""
UMP File Integrity Verification
"""

import hashlib
import hmac


class IntegrityVerifier:

    def verify(
        self,
        data: bytes,
        expected_hash: str,
        algorithm: str = "sha256"
    ) -> bool:

        actual_hash = hashlib.new(
            algorithm,
            data
        ).hexdigest()

        return hmac.compare_digest(
            actual_hash,
            expected_hash
        )
