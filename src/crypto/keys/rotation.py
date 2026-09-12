"""
UMP Key Rotation

Handles replacement of expired keys.
"""


from .generation import KeyGenerator



class KeyRotation:


    def __init__(self):

        self.generator = KeyGenerator()



    def rotate(
        self,
        old_key
    ):

        """
        Replace an old key with a new key.
        """

        new_key = self.generator.generate_key()

        return new_key
