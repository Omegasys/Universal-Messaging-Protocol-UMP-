"""
UMP Device Identity

Represents a device belonging to an identity.
"""


from dataclasses import dataclass


@dataclass
class Device:

    device_id: str
    device_key: str

    name: str | None = None

    status: str = "ACTIVE"


    def revoke(self):

        self.status = "REVOKED"


    def is_active(self):

        return self.status == "ACTIVE"


    def to_dict(self):

        return {
            "device_id": self.device_id,
            "device_key": self.device_key,
            "name": self.name,
            "status": self.status
        }
