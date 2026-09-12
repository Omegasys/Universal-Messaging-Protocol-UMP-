"""
UMP Address System

Defines how users are reached.
"""

from dataclasses import dataclass


@dataclass
class Address:

    address_type: str
    value: str


    def to_string(self):

        return f"{self.address_type}:{self.value}"
