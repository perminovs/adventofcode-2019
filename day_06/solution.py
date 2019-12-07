from __future__ import annotations

from itertools import chain
from queue import Queue
from collections import defaultdict
from dataclasses import dataclass
from typing import NamedTuple, List, Dict, Tuple, Sequence

from day_06.data import RAW_DATA

YOU = 'YOU'
SAN = 'SAN'


class Orbit(NamedTuple):
    center: str
    rotating: str


@dataclass
class Node:
    name: str
    deep: int = 0

    def __hash__(self):
        return hash(self.name)


NodeTree = Dict[str, List[Node]]


def to_orbits(raw: Sequence[str]) -> List[Orbit]:
    return [Orbit(*r.split(')')) for r in raw]


def build_tree(orbits: Sequence[Orbit]) -> Tuple[NodeTree, str]:
    tree = defaultdict(list)
    children = set()
    for orbit in orbits:
        tree[orbit.center].append(Node(orbit.rotating))
        children.add(orbit.rotating)
    root, = tuple(tree.keys() - children)
    return tree, root


def set_deep(tree: NodeTree, root: str):
    q = Queue()
    q.put(tree[root])
    deep = 1
    while not q.empty():
        nodes: List[Node] = q.get()
        next_nodes = []
        for node in nodes:
            node.deep = deep
            if node.name in tree:
                next_nodes.extend(tree[node.name])
        if next_nodes:
            q.put(next_nodes)
        deep += 1


def reverse_tree(tree: NodeTree) -> Dict[str, Node]:
    return {
        node.name: Node(parent, node.deep - 1)
        for parent in tree for node in tree[parent]
    }


def get_checksum(tree: NodeTree) -> int:
    return sum(node.deep for nodes in chain(tree.values()) for node in nodes)


def init_tree(raw_nodes: Sequence[str]) -> NodeTree:
    orbits = to_orbits(raw_nodes)
    tree, root = build_tree(orbits)
    set_deep(tree, root)
    return tree


def get_path_len(p1: str, p2: str, child_to_parent: Dict[str, Node]) -> int:
    pnode1 = child_to_parent[p1]
    pnode2 = child_to_parent[p2]
    path = 0
    while pnode1 != pnode2:
        path += 1
        if pnode1.deep > pnode2.deep:
            pnode1 = child_to_parent[pnode1.name]
        else:
            pnode2 = child_to_parent[pnode2.name]
    return path


def main():
    raw_nodes = RAW_DATA.split('\n')

    tree = init_tree(raw_nodes)
    checksum = get_checksum(tree)
    print(checksum)

    reversed_tree = reverse_tree(tree)
    path_len = get_path_len(YOU, SAN, reversed_tree)
    print(path_len)


if __name__ == '__main__':
    main()
