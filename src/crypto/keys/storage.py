"""
UMP Key Storage

Stores and retrieves key material.

Production versions should use:
- Secure hardware storage
- OS keychains
- TPM / Secure Enclave
"""


class KeyStorage:


    def __init__(self):

        self.keys = {}



    def store(
        self,
        key_id,
        key_data
    ):

        self.keys[key_id] = key_data



    def retrieve(
        self,
        key_id
    ):

        return self.keys.get(key_id)



    def delete(
        self,
        key_id
    ):

        if key_id in self.keys:

            del self.keys[key_id]

            return True

        return False
