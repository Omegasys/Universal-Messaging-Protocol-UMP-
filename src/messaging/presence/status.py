"""
UMP Presence Status
"""

from enum import Enum


class PresenceStatus(Enum):

    ONLINE = "ONLINE"
    AWAY = "AWAY"
    BUSY = "BUSY"
    OFFLINE = "OFFLINE"


class Presence:

    def __init__(
        self,
        status=PresenceStatus.OFFLINE
    ):
        self.status = status

    def set_status(self, status):
        self.status = status
