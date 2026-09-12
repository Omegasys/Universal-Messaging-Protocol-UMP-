"""
UMP Transport Keys

Manages keys for different transports.
"""


class TransportKeyManager:


    def __init__(self):

        self.transports = {}



    def add_transport(
        self,
        name,
        key
    ):

        self.transports[name] = key



    def get_transport_key(
        self,
        name
    ):

        return self.transports.get(name)



    def remove_transport(
        self,
        name
    ):

        if name in self.transports:

            del self.transports[name]
