import pytest

from day_06.solution import Node, reverse_tree, get_path_len
from day_06.solution import (
    get_checksum, to_orbits, Orbit, build_tree, Node, set_deep)


#
#                          YOU
#                          /
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I - SAN
#
PATH_LEN = 4
FROM = 'YOU'
TO = 'SAN'
ORBITS = [
    ('COM)B', 'B)C', 'C)D', 'K)YOU', 'D)E', 'E)F', 'B)G',
     'G)H', 'D)I', 'E)J', 'I)SAN', 'J)K', 'K)L'),

    ('K)YOU', 'D)I', 'K)L', 'I)SAN', 'E)J', 'J)K', 'B)C', 'B)G',
     'D)E', 'E)F', 'C)D', 'G)H', 'COM)B'),

    ('J)K', 'K)L', 'I)SAN', 'B)C', 'D)I', 'G)H', 'B)G',
     'COM)B', 'D)E', 'E)J', 'C)D', 'E)F', 'K)YOU'),
]


@pytest.mark.parametrize('raw', [*ORBITS])
def test_get_path_len(raw):
    orbits = to_orbits(raw)
    tree, root = build_tree(orbits)
    set_deep(tree, root)
    child_to_parent = reverse_tree(tree)
    assert get_path_len(FROM, TO, child_to_parent) == PATH_LEN


@pytest.mark.parametrize('tree, expected', [
    (
        {'A': [Node('B', 1)]},
        {'B': Node('A', 0)},
    ),
    (
        {'D': [Node('B', 1), Node('C', 1)], 'C': [Node('A', 2)]},
        {
            'B': Node('D', 0),
            'C': Node('D', 0),
            'A': Node('C', 1)
        },
    ),
])
def test_reverse_tree(tree, expected):
    assert reverse_tree(tree) == expected
