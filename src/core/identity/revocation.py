"""
UMP Identity Revocation

Handles compromised identities and devices.
"""


class RevocationManager:


    def revoke_device(
        self,
        identity,
        device_id
    ):

        if device_id in identity.devices:

            identity.devices.remove(device_id)

            return True

        return False



    def revoke_identity(
        self,
        identity
    ):

        identity.active = False

        return True
