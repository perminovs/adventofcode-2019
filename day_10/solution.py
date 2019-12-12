from __future__ import annotations

import math
from collections import defaultdict
from itertools import cycle
from dataclasses import dataclass
from typing import List, Dict, Iterator, Iterable, Optional

INPUT = (".###..#......###..#...#\n"
         "#.#..#.##..###..#...#.#\n"
         "#.#.#.##.#..##.#.###.##\n"
         ".#..#...####.#.##..##..\n"
         "#.###.#.####.##.#######\n"
         "..#######..##..##.#.###\n"
         ".##.#...##.##.####..###\n"
         "....####.####.#########\n"
         "#.########.#...##.####.\n"
         ".#.#..#.#.#.#.##.###.##\n"
         "#..#.#..##...#..#.####.\n"
         ".###.#.#...###....###..\n"
         "###..#.###..###.#.###.#\n"
         "...###.##.#.##.#...#..#\n"
         "#......#.#.##..#...#.#.\n"
         "###.##.#..##...#..#.#.#\n"
         "###..###..##.##..##.###\n"
         "###.###.####....######.\n"
         ".###.#####.#.#.#.#####.\n"
         "##.#.###.###.##.##..##.\n"
         "##.#..#..#..#.####.#.#.\n"
         ".#.#.#.##.##########..#\n"
         "#####.##......#.#.####.")
POINT_SYMBOL = '#'
NUMBER_TO_DESTROY = 200


@dataclass
class Point:
    x: int
    y: int
    name: Optional[str] = None

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return self.name or f'<x={self.x}, y={self.y}>'

    @classmethod
    def from_raw(cls, raw: str) -> List[Point]:
        result = []
        for y, row in enumerate(raw.split('\n')):
            for x, value in enumerate(row):
                if value == POINT_SYMBOL:
                    result.append(cls(x, y))
        return result

    def dist_from(self, other: Point) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Vector:
    dx: float
    dy: float
    _ACCURACY = 6

    @classmethod
    def from_asteroids(cls, ast1: Point, ast2: Point) -> Vector:
        dx = ast1.x - ast2.x
        dy = ast1.y - ast2.y

        if dx == 0 and dy == 0:
            raise ValueError(f'got the same point twice: {ast1}')

        _len = (dx ** 2 + dy ** 2) ** 0.5

        dx = round(dx / _len, cls._ACCURACY)
        dy = round(dy / _len, cls._ACCURACY)

        return cls(dx, dy)

    @property
    def angle(self) -> float:
        # too dirty, yes
        pure = math.atan2(abs(self.dy), abs(self.dx))
        res = pure
        if self.dx >= 0 and self.dy >= 0:  # I
            res = pure
        if self.dx <= 0 and self.dy >= 0:  # II
            res = math.pi - pure
        if self.dx <= 0 and self.dy <= 0:  # III
            res = pure + math.pi
        if self.dx >= 0 and self.dy <= 0:  # IV
            res = 2 * math.pi - pure
        ans = res - 3 * math.pi / 2  # move reference system to UP direction
        while ans < 0:  # for correct ordering (first will be UP vectors)
            ans += math.pi * 2
        return ans

    def __hash__(self):
        return hash((self.dx, self.dy))


def get_asteroid_rank(asteroids: List[Point]) -> Dict[Point, int]:
    asteroid_rank = {}

    for ast1 in asteroids:
        out_vectors = {
            Vector.from_asteroids(ast1, ast2) for ast2 in asteroids
            if ast1 != ast2
        }
        asteroid_rank[ast1] = len(out_vectors)

    return asteroid_rank


def get_best_observe(asteroids: List[Point]) -> int:
    ranks = get_asteroid_rank(asteroids)
    return max(ranks.values())


def get_vector_to_points(
    asteroids: List[Point], station: Point,
) -> Dict[Vector, List[Point]]:
    vectors = defaultdict(list)
    for ast in asteroids:
        if ast == station:
            continue
        vector = Vector.from_asteroids(ast, station)
        vectors[vector].append(ast)

    for k in vectors:
        vectors[k] = list(sorted(
            vectors[k], key=lambda x: station.dist_from(x), reverse=True,
        ))
    return vectors


def sort_vectors(direction_rank: Iterable[Vector]) -> List[Vector]:
    return list(
        sorted(direction_rank, key=lambda a: a.angle)
    )


def destroy_asteroids(
    direction_rank: Dict[Vector, List[Point]],
) -> Iterator[Point]:
    vectors = sort_vectors(direction_rank)
    for vector in cycle(vectors):
        if vector not in direction_rank:
            continue

        yield direction_rank[vector].pop()

        if not direction_rank[vector]:
            direction_rank.pop(vector)

        if not direction_rank:
            return


def main():
    asteroids = Point.from_raw(INPUT)

    ranks = get_asteroid_rank(asteroids)
    visible = max(ranks.values())
    print(visible)

    station, = [a for a, c in ranks.items() if c == visible]
    rank = get_vector_to_points(asteroids, station)

    for idx, ast in enumerate(destroy_asteroids(rank), start=1):
        if idx == NUMBER_TO_DESTROY:
            print(ast.x * 100 + ast.y)
            break


if __name__ == '__main__':
    main()
