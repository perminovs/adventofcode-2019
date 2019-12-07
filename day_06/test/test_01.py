import pytest

from day_06.solution import (
    get_checksum, to_orbits, Orbit, build_tree, Node, set_deep, init_tree)


@pytest.mark.parametrize('orbits, expected, root', [
    (
        [Orbit('A', 'B')],
        {'A': [Node('B')]},
        'A',
    ),
    (
        [Orbit('A', 'B'), Orbit('B', 'C')],
        {'A': [Node('B')], 'B': [Node('C')]},
        'A',
    ),
    (
        [Orbit('D', 'B'), Orbit('D', 'C')],
        {'D': [Node('B'), Node('C')]},
        'D',
    ),
    (
        [Orbit('C', 'A'), Orbit('D', 'B'), Orbit('D', 'C')],
        {'D': [Node('B'), Node('C')], 'C': [Node('A')]},
        'D',
    ),
])
def test_build_tree(orbits, expected, root):
    assert build_tree(orbits) == (expected, root)


@pytest.mark.parametrize('tree, root, expected_tree', [
    (
        {'A': [Node('B')]},
        'A',
        {'A': [Node('B', 1)]},
    ),
    (
        {'D': [Node('B'), Node('C')]},
        'D',
        {'D': [Node('B', 1), Node('C', 1)]},
    ),
    (
        {'D': [Node('B'), Node('C')], 'C': [Node('A')]},
        'D',
        {'D': [Node('B', 1), Node('C', 1)], 'C': [Node('A', 2)]},
    ),
])
def test_set_deep(tree, root, expected_tree):
    set_deep(tree, root)
    assert tree == expected_tree


#
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I
#
CHECKSUMS = 42
ORBITS = [
    ('COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G',
     'G)H', 'D)I', 'E)J', 'J)K', 'K)L'),

    ('D)I', 'K)L', 'E)J', 'J)K', 'B)C', 'B)G',
     'D)E', 'E)F', 'C)D', 'G)H', 'COM)B'),

    ('J)K', 'K)L', 'B)C', 'D)I', 'G)H', 'B)G',
     'COM)B', 'D)E', 'E)J', 'C)D', 'E)F'),
]


@pytest.mark.parametrize('orbit', [*ORBITS])
def test_calc_checksum(orbit):
    tree = init_tree(orbit)
    assert get_checksum(tree) == CHECKSUMS


@pytest.mark.parametrize('raw, expected', [
    (['A)B'], [Orbit('A', 'B')]),
    (
        ['A)B', 'B)C'], [Orbit('A', 'B'), Orbit('B', 'C')],
    ),
])
def test_to_orbits(raw, expected):
    assert to_orbits(raw) == expected
