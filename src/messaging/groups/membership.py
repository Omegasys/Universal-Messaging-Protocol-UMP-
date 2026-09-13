"""
UMP Group Membership
"""


class MembershipManager:

    def add(self, group, identity_id):
        group.add_member(identity_id)

    def remove(self, group, identity_id):
        group.remove_member(identity_id)

    def is_member(self, group, identity_id):
        return identity_id in group.members
