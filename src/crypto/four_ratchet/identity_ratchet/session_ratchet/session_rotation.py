"""
UMP Session Rotation
"""


class SessionRotation:


    def rotate(
        self,
        session_chain
    ):

        return session_chain.next_key()
