import pytest

from day_14.main import count_fuel
from day_14.solution.models import Reaction, Element, TRILLION
from day_14.solution.via_recursion import calc_ore as rec_calc_ore
from day_14.solution.via_queue import calc_ore as queue_calc_ore


@pytest.mark.parametrize('raw, expected', [
    (
        '10 ORE => 10 A',
        Reaction(output=Element('A', 10), input=[Element('ORE', 10)]),
    ),
    (
        '7 A, 1 E => 1 FUEL',
        Reaction(
            output=Element('FUEL', 1),
            input=[Element('A', 7), Element('E', 1)],
        ),
    ),
])
def test_from_raw(raw, expected):
    assert Reaction.from_raw(raw) == expected


@pytest.mark.parametrize('raw, expected', [
    ('1 ORE => 1 FUEL', 1),
    ('2 ORE => 1 FUEL', 2),
    ('3 ORE => 2 FUEL', 3),
    ('1 ORE => 2 FUEL', 1),

    ('10 ORE => 10 A\n7 A => 1 FUEL', 10),

    (
        "10 ORE => 10 A\n"
        "1 ORE => 1 B\n"
        "7 A, 1 B => 1 C\n"
        "7 A, 1 C => 1 D\n"
        "7 A, 1 D => 1 E\n"
        "7 A, 1 E => 1 FUEL",
        31,
    ),
    (
        "9 ORE => 2 A\n"
        "8 ORE => 3 B\n"
        "7 ORE => 5 C\n"
        "3 A, 4 B => 1 AB\n"
        "5 B, 7 C => 1 BC\n"
        "4 C, 1 A => 1 CA\n"
        "2 AB, 3 BC, 4 CA => 1 FUEL",
        165,
    ),
    (
        "171 ORE => 8 CNZTR\n"
        "7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL\n"
        "114 ORE => 4 BHXH\n"
        "14 VRPVC => 6 BMBT\n"
        "6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL\n"
        "6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT\n"
        "15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW\n"
        "13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW\n"
        "5 BMBT => 4 WPTQ\n"
        "189 ORE => 9 KTJDG\n"
        "1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP\n"
        "12 VRPVC, 27 CNZTR => 2 XDBXC\n"
        "15 KTJDG, 12 BHXH => 5 XCVML\n"
        "3 BHXH, 2 VRPVC => 7 MZWV\n"
        "121 ORE => 7 VRPVC\n"
        "7 XCVML => 6 RJRHP\n"
        "5 BHXH, 4 VRPVC => 5 LTCX",
        2210736,
    ),
])
def test_calc_ore(raw, expected):
    reactions = Reaction.from_multi_raw(raw)
    q = queue_calc_ore(reactions)
    r = rec_calc_ore(reactions)
    assert q == r == expected


@pytest.mark.parametrize('raw, ore_cnt, fuel', [
    (
        "157 ORE => 5 NZVS\n"
        "165 ORE => 6 DCFZ\n"
        "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n"
        "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n"
        "179 ORE => 7 PSHF\n"
        "177 ORE => 5 HKGWZ\n"
        "7 DCFZ, 7 PSHF => 2 XJWVT\n"
        "165 ORE => 2 GPVTF\n"
        "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT",
        TRILLION,
        82892753,
    ),
])
def test_count_fuel(raw, ore_cnt, fuel):
    reactions = [Reaction.from_raw(r) for r in raw.split('\n')]
    assert count_fuel(reactions, ore_cnt) == fuel
