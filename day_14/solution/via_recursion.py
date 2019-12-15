import math
from collections import defaultdict
from typing import List, Dict, DefaultDict

from day_14.solution.models import Reaction, Element, ORE, FUEL


def calc_ore(reactions: List[Reaction], cnt: int = 1) -> int:
    """ How many ORE we need to produce <cnt> FUEL?
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
