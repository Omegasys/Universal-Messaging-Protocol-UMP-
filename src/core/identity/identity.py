"""
UMP Identity System

Represents a user's cryptographic identity.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Identity:

    identity_id: str
    public_key: str

    username: str | None = None
    phone_number: str | None = None

    devices: List[str] = field(default_factory=list)

    active: bool = True


    def add_device(self, device_id: str):
        if device_id not in self.devices:
            self.devices.append(device_id)


    def remove_device(self, device_id: str):
        if device_id in self.devices:
            self.devices.remove(device_id)


    def to_dict(self):

        return {
            "identity_id": self.identity_id,
            "public_key": self.public_key,
            "username": self.username,
            "phone_number": self.phone_number,
            "devices": self.devices,
            "active": self.active
        }
