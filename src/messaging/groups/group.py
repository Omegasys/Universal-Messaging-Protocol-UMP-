"""
UMP Group
"""

from dataclasses import dataclass, field


@dataclass
class Group:

    group_id: str
    name: str

    members: list[str] = field(
        default_factory=list
    )

    def add_member(self, identity_id: str):
        if identity_id not in self.members:
            self.members.append(identity_id)

    def remove_member(self, identity_id: str):
        if identity_id in self.members:
            self.members.remove(identity_id)
