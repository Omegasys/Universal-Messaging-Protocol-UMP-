"""
UMP Address Resolver

Maps addresses to identities.
"""


class AddressResolver:


    def __init__(self):

        self.registry = {}



    def register(
        self,
        address,
        identity_id
    ):

        self.registry[
            address.to_string()
        ] = identity_id



    def resolve(
        self,
        address
    ):

        return self.registry.get(
            address.to_string()
        )
