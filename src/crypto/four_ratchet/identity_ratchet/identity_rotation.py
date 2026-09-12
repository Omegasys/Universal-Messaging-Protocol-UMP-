"""
UMP Identity Key Rotation
"""


from .identity_chain import IdentityChain



class IdentityRotation:


    def rotate(
        self,
        chain: IdentityChain
    ):

        new_key = chain.advance()

        return {
            "version": chain.version,
            "key": new_key
        }
