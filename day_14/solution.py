from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import List
from queue import Queue

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
    name_to_reaction[ORE] = Reaction(output=Element(ORE, 1), input=[])

    needs = defaultdict(int)
    needs[FUEL] += 1

    extra = defaultdict(int)
    produced = defaultdict(int)
    used = defaultdict(int)

    q = Queue()
    q.put(name_to_reaction[FUEL])

    while not q.empty():
        reaction = q.get()

        to_produce = needs[reaction.output.name]
        repeat_cnt = math.ceil(to_produce / reaction.output.cnt)
        produced[reaction.output.name] += reaction.output.cnt * repeat_cnt

        used[reaction.output.name] += needs[reaction.output.name] + extra[reaction.output.name]

        e = produced[reaction.output.name] - used[reaction.output.name]
        extra[reaction.output.name] = e

        needs[reaction.output.name] = 0

        for inp in reaction.input:

            diff = extra[inp.name] - needs[inp.name]

            if diff > inp.cnt:
                extra[inp.name] -= inp.cnt
                used[inp.name] += inp.cnt
                needs[inp.name] = 0
                continue
            to_produce = inp.cnt - diff
            needs[inp.name] += to_produce
            q.put(name_to_reaction[inp.name])

    return produced[ORE]