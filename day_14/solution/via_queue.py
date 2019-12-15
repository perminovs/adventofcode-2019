import math
from collections import defaultdict
from queue import Queue
from typing import List

from day_14.solution.models import Reaction, Element, ORE, FUEL


def calc_ore(reactions: List[Reaction], cnt: int = 1) -> int:
    """ How many ORE we need to produce <cnt> FUEL?
    """
    name_to_reaction = {r.output.name: r for r in reactions}
    name_to_reaction[ORE] = Reaction(output=Element(ORE, 1), input=[])

    needs = defaultdict(int)
    needs[FUEL] += cnt

    extra = defaultdict(int)
    produced = defaultdict(int)

    q = Queue()
    q.put(name_to_reaction[FUEL])

    while not q.empty():
        reaction = q.get()

        need_to_produce = needs[reaction.output.name]
        repeat_cnt = math.ceil(need_to_produce / reaction.output.cnt)

        amount_produced = reaction.output.cnt * repeat_cnt
        produced[reaction.output.name] += amount_produced

        if amount_produced > need_to_produce:
            extra[reaction.output.name] += amount_produced - need_to_produce

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
