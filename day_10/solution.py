from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

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


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    @classmethod
    def from_raw(cls, raw: str) -> List[Point]:
        result = []
        for y, row in enumerate(raw.split('\n')):
            for x, value in enumerate(row):
                if value == POINT_SYMBOL:
                    result.append(cls(x, y))
        return result


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


def main():
    asteroids = Point.from_raw(INPUT)
    print(get_best_observe(asteroids))


if __name__ == '__main__':
    main()
