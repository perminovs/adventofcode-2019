import pytest

from day_03.solution import (
    direction_to_points, move_sequence, get_distance,
    get_sequence_crosses, closest)


@pytest.mark.parametrize(
    'point, direction, expected', [
        ((0, 0), 'R1', ({(+1, 0)}, (+1, 0))),
        ((0, 0), 'L1', ({(-1, 0)}, (-1, 0))),
        ((0, 0), 'U1', ({(0, +1)}, (0, +1))),
        ((0, 0), 'D1', ({(0, -1)}, (0, -1))),

        ((0, 0), 'R4', ({(1, 0), (2, 0), (3, 0), (4, 0)}, (4, 0))),
        ((1, 1), 'U2', ({(1, 2), (1, 3)}, (1, 3))),

        ((0, 0), 'U10', ({
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)
        }, (0, 10))),
    ],
)
def test_direction_to_points(point, direction, expected):
    assert direction_to_points(point, direction) == expected


@pytest.mark.parametrize(
    'start_point, moves, expected', [
        ((0, 0), 'R2,U3', {(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)}),
    ]
)
def test_move_sequence(start_point, moves, expected):
    assert move_sequence(start_point, moves) == expected


@pytest.mark.parametrize(
    'p1, p2, expected', [
        ((0, 0), (0, 0), 0),
        ((1, 1), (1, 1), 0),
        ((0, 0), (0, 1), 1),
        ((0, 0), (1, 1), 2),
        ((1, 1), (2, 3), 3),
    ]
)
def test_get_distance(p1, p2, expected):
    assert get_distance(p1, p2) == expected
    assert get_distance(p2, p1) == expected


@pytest.mark.parametrize(
    'seq1, seq2, expected', [
        ('R2', 'U4', set()),
        ('L2', 'L2', {(-1, 0), (-2, 0)}),
        ('R2,D4', 'D2,R4', {(2, -2)}),
    ]
)
def test_get_sequence_crosses(seq1, seq2, expected):
    assert get_sequence_crosses(seq1, seq2) == expected
    assert get_sequence_crosses(seq2, seq1) == expected


@pytest.mark.parametrize(
    'seq1, seq2, expected', [
        ('R8,U5,L5,D3', 'U7,R6,D4,L4', 6),
        (
            'R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83',
            159,
        ),
        (
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
            135,
        ),
    ]
)
def test_closest(seq1, seq2, expected):
    assert closest(seq1, seq2, to=(0, 0)) == expected
