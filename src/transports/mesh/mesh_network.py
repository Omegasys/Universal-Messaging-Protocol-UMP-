"""
UMP Mesh Network
"""

from dataclasses import dataclass, field


@dataclass
class MeshNode:

    node_id: str
    neighbors: list[str] = field(
        default_factory=list
    )


class MeshNetwork:

    def __init__(self):

        self.nodes: dict[str, MeshNode] = {}

    def add_node(
        self,
        node_id: str
    ):

        if node_id not in self.nodes:

            self.nodes[node_id] = MeshNode(
                node_id=node_id
            )

    def remove_node(
        self,
        node_id: str
    ):

        self.nodes.pop(
            node_id,
            None
        )

    def connect_nodes(
        self,
        first: str,
        second: str
    ):

        self.add_node(first)
        self.add_node(second)

        if second not in self.nodes[first].neighbors:
            self.nodes[first].neighbors.append(second)

        if first not in self.nodes[second].neighbors:
            self.nodes[second].neighbors.append(first)

    def neighbors(
        self,
        node_id: str
    ) -> list[str]:

        node = self.nodes.get(node_id)

        if node is None:
            return []

        return list(node.neighbors)
