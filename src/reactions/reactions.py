"""
UMP Message Reactions
"""

from dataclasses import dataclass


@dataclass
class Reaction:

    message_id: str
    sender: str
    reaction: str

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "sender": self.sender,
            "reaction": self.reaction
        }


class ReactionManager:

    def __init__(self):
        self.reactions = []

    def add(self, reaction: Reaction):
        self.reactions.append(reaction)

    def remove(
        self,
        message_id: str,
        sender: str
    ):
        self.reactions = [
            r for r in self.reactions
            if not (
                r.message_id == message_id
                and r.sender == sender
            )
        ]
