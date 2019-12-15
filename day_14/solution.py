from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, DefaultDict

from day_14.data import RAW

FUEL = 'FUEL'
ORE = 'ORE'


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


def calc_need(reactions: List[Reaction]) -> int:
    name_to_reaction = {r.output.name: r for r in reactions}
    return _calc_need(Element(FUEL, 1), name_to_reaction, defaultdict(int))


def _calc_need(
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
        ore_needed += _calc_need(what_produce, name_to_reaction, extra)

    return ore_needed


def main():
    reactions = [Reaction.from_raw(raw) for raw in RAW.split('\n')]
    ore = calc_need(reactions)
    print(ore)


if __name__ == '__main__':
    main()
