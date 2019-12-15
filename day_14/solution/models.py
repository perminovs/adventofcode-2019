from __future__ import annotations

from dataclasses import dataclass
from typing import List

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

    @classmethod
    def from_multi_raw(cls, raws: str) -> List[Reaction]:
        return [cls.from_raw(raw) for raw in raws.split('\n')]
