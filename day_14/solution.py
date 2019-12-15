from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import List
from queue import Queue

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


def calc_ore(reactions: List[Reaction]) -> int:
    name_to_reaction = {r.output.name: r for r in reactions}
    name_to_reaction[ORE] = Reaction(output=Element(ORE, 1), input=[])

    needs = defaultdict(int)
    needs[FUEL] += 1

    extra = defaultdict(int)
    produced = defaultdict(int)

    q = Queue()
    q.put(name_to_reaction[FUEL])

    while not q.empty():
        reaction = q.get()

        to_produce = needs[reaction.output.name]
        repeat_cnt = math.ceil(to_produce / reaction.output.cnt)

        amount = reaction.output.cnt * repeat_cnt
        produced[reaction.output.name] += amount

        if amount > to_produce:
            extra[reaction.output.name] += amount - to_produce

        needs[reaction.output.name] = 0

        for inp in reaction.input:
            needed_amount = repeat_cnt * inp.cnt
            if extra[inp.name] > needed_amount:
                extra[inp.name] -= needed_amount
                continue
            else:
                needed_amount -= extra[inp.name]
                needs[inp.name] += needed_amount
                extra[inp.name] = 0
            q.put(name_to_reaction[inp.name])

    return produced[ORE]


def main_p1():
    reactions = [Reaction.from_raw(raw) for raw in RAW.split('\n')]
    ore = calc_ore(reactions)
    print(ore)


if __name__ == '__main__':
    main_p1()
