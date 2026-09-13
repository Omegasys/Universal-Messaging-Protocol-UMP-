"""
UMP Mesh Routing
"""


class MeshRouter:

    def send(
        self,
        destination: str,
        data: bytes,
        path: list[str]
    ) -> dict:

        return {
            "type": "MESH",
            "destination": destination,
            "path": path,
            "hops": len(path),
            "data": data
        }

    def next_hop(
        self,
        path: list[str]
    ) -> str | None:

        if not path:
            return None

        return path[0]

    def remaining_path(
        self,
        path: list[str]
    ) -> list[str]:

        return path[1:]
