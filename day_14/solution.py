from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, DefaultDict

from day_14.data import RAW

FUEL = 'FUEL'
ORE = 'ORE'
TRILLION = 1000000000000


@dataclass
class Element:
    name: str
    cnt: int

    def __str__(self):
        return f'{self.cnt} {self.name}'


@dataclass
class Reaction:
    output: Element
    input: List[Element]

    def __str__(self):
        inp = ', '.join(str(e) for e in self.input)
        return f'{inp} => {self.output}'

    @classmethod
    def from_raw(cls, raw: str) -> Reaction:
        def _parse_input(inp: str):
            c, n = inp.strip().split(' ')
            return n, int(c)

        left, right = raw.split('=>')
        left_elements = left.split(',')
        inputs = [Element(*_parse_input(i)) for i in left_elements]
        return cls(Element(*_parse_input(right)), inputs)


def calc_ore(reactions: List[Reaction], cnt: int = 1) -> int:
    """ How many ORE we need to produce one FUEL?
    """
    name_to_reaction = {r.output.name: r for r in reactions}
    return _calc_ore(Element(FUEL, cnt), name_to_reaction, defaultdict(int))


def _calc_ore(
    needed: Element,
    name_to_reaction: Dict[str, Reaction],
    extra: DefaultDict[str, int],
) -> int:
    if needed.name == ORE:
        return needed.cnt

    reaction = name_to_reaction[needed.name]

    repeat_cnt = math.ceil(needed.cnt / reaction.output.cnt)
    produced = repeat_cnt * reaction.output.cnt
    _extra = produced - needed.cnt
    if _extra > 0:
        extra[needed.name] += _extra

    ore_needed = 0
    for element in reaction.input:
        to_produce = element.cnt * repeat_cnt
        if extra[element.name] > to_produce:
            extra[element.name] -= to_produce
            continue
        to_produce -= extra[element.name]
        extra[element.name] = 0

        what_produce = Element(element.name, to_produce)
        ore_needed += _calc_ore(what_produce, name_to_reaction, extra)

    return ore_needed


def main_p1():
    reactions = [Reaction.from_raw(raw) for raw in RAW.split('\n')]
    ore = calc_ore(reactions)
    print(ore)


def count_fuel(reactions: List[Reaction], ore_cnt: int) -> int:
    """ What amount of fuel we can produce with <ore_cnt> or ORE?
    """
    left = 0
    right = ore_cnt  # Just suppose. It's not correct for arbitrary case.
    mid = -1
    ore = -1

    while left <= right:
        mid = (right + left) // 2
        ore = calc_ore(reactions, mid)

        if ore < TRILLION:
            left = mid + 1
        elif ore > TRILLION:
            right = mid - 1
        else:
            break

    if ore > ore_cnt:  # one fuel is extra, because we have just ore_cnt ORE
        mid -= 1

    return mid


def main_p2():
    reactions = [Reaction.from_raw(raw) for raw in RAW.split('\n')]
    fuel = count_fuel(reactions, TRILLION)
    print(fuel)


if __name__ == '__main__':
    main_p1()
    main_p2()
