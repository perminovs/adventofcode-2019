from collections import defaultdict
from typing import Dict, List, TypeVar, Tuple

Node = TypeVar('Node')


def build_graph(
    raw_data: str, start_point: str, end_point: str
) -> Tuple[Dict[Node, List[Node]], Node, Node]:
    # I'm sorry for that all, but it works
    rows = raw_data.split('\n')[1:-1]

    # <shit>
    dots = set()
    portals = defaultdict(list)

    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] == '.':
                dots.add((x, y))

            if not rows[y][x].isalpha():
                continue

            first_letter = rows[y][x]
            second_letter = None
            entrance = None
            for dy in (-1, 0, +1):
                for dx in (-1, 0, +1):
                    if abs(dx) + abs(dy) != 1:
                        continue
                    _y = y + dy
                    _x = x + dx

                    _y = max(0, _y)
                    _x = max(0, _x)

                    _y = min(_y, len(rows) - 1)
                    _x = min(_x, len(rows[y]) - 1)

                    if rows[_y][_x].isalpha():
                        second_letter = rows[_y][_x]
                    if rows[_y][_x] == '.':
                        entrance = _x, _y

            if entrance is not None:
                p = tuple(sorted(f'{first_letter}{second_letter}'))
                portals[p].append(entrance)

    graph = defaultdict(list)
    for node in dots:
        for dy in (-1, 0, +1):
            for dx in (-1, 0, +1):
                if abs(dx) + abs(dy) != 1:
                    continue
                neighbor = (node[0] + dy, node[1] + dx)
                if neighbor in dots:
                    graph[node].append(neighbor)

    start, end = None, None

    for letters, dots in portals.items():
        if len(dots) == 1:
            if letters == tuple(start_point):
                start = dots[0]
            if letters == tuple(end_point):
                end = dots[0]
        if len(dots) == 2:
            d1, d2 = dots
            graph[d1].append(d2)
            graph[d2].append(d1)

    # </shit>
    return graph, start, end
