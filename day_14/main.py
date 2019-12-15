from typing import List

from day_14.data import RAW
from day_14.solution.models import Reaction, TRILLION
from day_14.solution.via_queue import calc_ore as queue_calc_ore
from day_14.solution.via_recursion import calc_ore as recursion_calc_ore


def count_fuel(reactions: List[Reaction], ore_cnt: int) -> int:
    """ PART 2: what amount of fuel we can produce with <ore_cnt> or ORE?
    """
    left = 0
    right = ore_cnt  # Just suppose. It's not correct for arbitrary case.
    mid = -1
    ore = -1

    while left <= right:
        mid = (right + left) // 2
        ore = queue_calc_ore(reactions, mid)

        if ore < TRILLION:
            left = mid + 1
        elif ore > TRILLION:
            right = mid - 1
        else:
            break

    if ore > ore_cnt:  # one fuel is extra, because we have just ore_cnt ORE
        mid -= 1

    return mid


def main_p1_rec():
    reactions = Reaction.from_multi_raw(RAW)
    ore = recursion_calc_ore(reactions)
    print(ore)


def main_p1_queue():
    reactions = Reaction.from_multi_raw(RAW)
    ore = queue_calc_ore(reactions)
    print(ore)


def main_p2():
    reactions = Reaction.from_multi_raw(RAW)
    fuel = count_fuel(reactions, TRILLION)
    print(fuel)


if __name__ == '__main__':
    main_p1_rec()
    main_p1_queue()
    main_p2()
