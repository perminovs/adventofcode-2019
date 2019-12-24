from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterator, Iterable
from copy import deepcopy


class CeilState(str, Enum):
    DEAD = '.'
    ALIVE = '#'


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class Board:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._array = [
            [CeilState.DEAD for _ in range(width)]
            for _ in range(height)
        ]

    @classmethod
    def from_raw(cls, raw: str) -> Board:
        rows = raw.split('\n')
        height = len(rows)
        width = len(rows[0])
        self = cls(width, height)
        for y in range(height):
            for x in range(width):
                self._array[y][x] = CeilState(rows[y][x])
        return self

    def get(self, point: Point) -> CeilState:
        return self._array[point.y][point.x]

    def get_neighbors(self, point: Point) -> Iterator[CeilState]:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if abs(dx) + abs(dy) != 1:
                    continue
                _p = Point(point.x + dx, point.y + dy)
                if 0 <= _p.y < self._height and 0 <= _p.x < self._width:
                    yield self._array[_p.y][_p.x]

    @property
    def energy(self) -> int:
        return sum(
            2 ** i for i, point in enumerate(self.iter_points())
            if self.get(point) is CeilState.ALIVE
        )

    def iter_points(self) -> Iterator[Point]:
        for y in range(self._height):
            for x in range(self._width):
                yield Point(x=x, y=y)

    def make_step(self):
        array = deepcopy(self._array)

        for point in self.iter_points():
            count_neighbors = len(filter_alive(self.get_neighbors(point)))

            if self.get(point) is CeilState.DEAD and count_neighbors in (1, 2):
                array[point.y][point.x] = CeilState.ALIVE
            elif self.get(point) is CeilState.ALIVE and count_neighbors != 1:
                array[point.y][point.x] = CeilState.DEAD

        self._array = array


def filter_alive(state_seq: Iterable[CeilState]):
    return list(filter(lambda i: i is CeilState.ALIVE, state_seq))


def step_while_unique(board: Board) -> int:
    energies = {board.energy}
    while True:
        board.make_step()
        energy = board.energy
        if energy in energies:
            return energy
        energies.add(energy)


def main():
    raw = (
        "..#.#\n"
        ".#.##\n"
        "##...\n"
        ".#.#.\n"
        "###.."
    )
    board = Board.from_raw(raw)
    energy = step_while_unique(board)
    print(energy)


if __name__ == '__main__':
    main()
