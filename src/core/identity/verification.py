"""
UMP Identity Verification

Handles trust verification between identities.
"""


class IdentityVerifier:


    def verify_key(
        self,
        identity,
        public_key
    ):

        return identity.public_key == public_key



    def verify_device(
        self,
        identity,
        device_id
    ):

        return device_id in identity.devices
