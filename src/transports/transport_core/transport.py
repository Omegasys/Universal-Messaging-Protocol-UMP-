"""
UMP Transport Interface
"""

from abc import ABC, abstractmethod


class Transport(ABC):

    name: str = "UNKNOWN"

    @abstractmethod
    def send(self, destination: str, data: bytes) -> bool:
        """Send data through the transport."""
        raise NotImplementedError

    @abstractmethod
    def receive(self) -> bytes | None:
        """Receive data from the transport."""
        raise NotImplementedError

    def available(self) -> bool:
        """Return whether the transport is currently available."""
        return True
