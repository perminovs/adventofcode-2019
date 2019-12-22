from heapq import heappop, heappush
from queue import Queue
from typing import Dict, Tuple, Sequence, TypeVar

Node = TypeVar('Node')
Vertex = Tuple[Node, int]


# dijkstra is unused here :(
def dijkstra(graph: Dict[Node, Sequence[Vertex]], n1: Node, n2: Node):
    path_len = {n1: 0}

    heap = []
    heappush(heap, (0, n1))
    seen = {n1}

    while heap:
        _, node = heappop(heap)
        for neighbor, weight in graph[node]:
            if neighbor in seen:
                continue

            if (
                neighbor not in path_len
                or path_len[neighbor] > path_len[node] + weight
            ):
                path_len[neighbor] = path_len[node] + weight

            heappush(heap, (weight, neighbor))
        seen.add(node)

    return path_len[n2]


def bfs(graph: Dict[Node, Sequence[Node]], n1: Node, n2: Node):
    ranks = {n1: 0}
    q = Queue()
    q.put(n1)

    while not q.empty():
        node = q.get()
        for neighbor in graph[node]:
            if neighbor in ranks:
                continue
            q.put(neighbor)
            ranks[neighbor] = ranks[node] + 1

    return ranks[n2]
