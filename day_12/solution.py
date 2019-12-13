from __future__ import annotations, print_function

import math
from dataclasses import dataclass
from itertools import cycle
from typing import Sequence, List

INPUT = (
    "<x=-16, y=15, z=-9>\n"
    "<x=-14, y=5, z=4>\n"
    "<x=2, y=0, z=6>\n"
    "<x=-3, y=18, z=9>"
)
STEPS = 1000


def _abs_sum(iterable):
    return sum(map(abs, iterable))


@dataclass
class Moon:
    position: List[int]
    velocity: List[int]

    @classmethod
    def from_raw(cls, raw: str) -> Moon:
        for symbol in ('<', '>', '=', 'x', 'y', 'z', 'pos', 'vel'):
            raw = raw.replace(symbol, '')
        values = list(map(int, raw.split(',')))
        if len(values) == 3:
            return cls(values, [0, 0, 0])
        return cls(values[:3], values[3:])

    def move(self, dim):
        self.position[dim] += self.velocity[dim]

    def apply_gravity(self, other: Moon, dim):
        a = self.position[dim]
        b = other.position[dim]
        if a != b:
            self.velocity[dim] += (b - a) / abs(b - a)

    @property
    def energy(self):
        return _abs_sum(self.position) * _abs_sum(self.velocity)


def make_step(moons: Sequence[Moon]):
    for dim in (0, 1, 2):
        _make_step(moons, dim)


def _make_step(moons: Sequence[Moon], dim):
    for m1 in moons:
        for m2 in moons:
            if m1 == m2:
                continue
            m1.apply_gravity(m2, dim)

    for moon in moons:
        moon.move(dim)


def find_restate(moons: List[Moon]):
    x = _find_restate(moons, 0)
    print(f'found x: {x}')

    y = _find_restate(moons, 1)
    print(f'found y: {y}')

    z = _find_restate(moons, 2)
    print(f'found z: {z}')

    return lcm(x, y, z)


def _find_restate(moons: List[Moon], dim):
    def _get_state():
        return tuple((m.position[dim], m.velocity[dim]) for m in moons)

    initial_state = _get_state()
    for idx, _ in enumerate(cycle([0]), start=1):
        _make_step(moons, dim)
        if initial_state == _get_state():
            return idx


def lcm(x, y, z):
    xy = x * y // math.gcd(x, y)
    return z * xy // math.gcd(z, xy)


def main_p1():
    moons = [Moon.from_raw(raw) for raw in INPUT.split('\n')]
    for _ in range(STEPS):
        make_step(moons)
    energy = sum(moon.energy for moon in moons)
    print(energy)


def main_p2():
    moons = [Moon.from_raw(raw) for raw in INPUT.split('\n')]
    idx = find_restate(moons)
    print(idx)


if __name__ == '__main__':
    main_p1()
    main_p2()
