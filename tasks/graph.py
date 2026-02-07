from collections import deque
from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self, received_nodes: list[Node] | None = None) -> list[Node]:
        if received_nodes is None:
            received_nodes = []
        
        if self._root not in received_nodes:
            received_nodes.append(self._root)
            for node in self._root.outbound:
                temp_graph = Graph(node)
                temp_graph.dfs(received_nodes=received_nodes)
        return received_nodes
        

    def bfs(self) -> list[Node]:
        received_nodes = [self._root]
        queue = deque(self._root.outbound)
        while queue:
            node = queue.popleft()
            if node not in received_nodes:
                received_nodes.append(node)
                for new_node in node.outbound:
                    if new_node not in queue:
                        queue.append(new_node)
        return received_nodes
