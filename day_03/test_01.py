import pytest

from day_03.solution import (
    Point, direction_to_points, move_sequence, get_distance,
    get_sequence_crosses, closest, get_signal_delay)


@pytest.mark.parametrize(
    'point, direction, expected', [
        (Point(0, 0), 'R1', ({Point(+1, 0)}, Point(+1, 0))),
        (Point(0, 0), 'L1', ({Point(-1, 0)}, Point(-1, 0))),
        (Point(0, 0), 'U1', ({Point(0, +1)}, Point(0, +1))),
        (Point(0, 0), 'D1', ({Point(0, -1)}, Point(0, -1))),

        (Point(0, 0), 'R4', ({Point(1, 0), Point(2, 0), Point(3, 0),
                              Point(4, 0)}, Point(4, 0))),
        (Point(1, 1), 'U2', ({Point(1, 2), Point(1, 3)}, Point(1, 3))),

        (Point(0, 0), 'U10', ({
            Point(0, 1), Point(0, 2), Point(0, 3), Point(0, 4), Point(0, 5),
            Point(0, 6), Point(0, 7), Point(0, 8), Point(0, 9), Point(0, 10)
        }, Point(0, 10))),
    ],
)
def test_direction_to_points(point, direction, expected):
    assert direction_to_points(point, direction) == expected


@pytest.mark.parametrize(
    'start_point, moves, expected', [
        (Point(0, 0), 'R2,U3', {Point(1, 0), Point(2, 0), Point(2, 1),
                                Point(2, 2), Point(2, 3)}),
    ]
)
def test_move_sequence(start_point, moves, expected):
    assert move_sequence(start_point, moves) == expected


@pytest.mark.parametrize(
    'p1, p2, expected', [
        (Point(0, 0), Point(0, 0), 0),
        (Point(1, 1), Point(1, 1), 0),
        (Point(0, 0), Point(0, 1), 1),
        (Point(0, 0), Point(1, 1), 2),
        (Point(1, 1), Point(2, 3), 3),
    ]
)
def test_get_distance(p1, p2, expected):
    assert get_distance(p1, p2) == expected
    assert get_distance(p2, p1) == expected


@pytest.mark.parametrize(
    'seq1, seq2, expected', [
        ('R2', 'U4', set()),
        ('L2', 'L2', {Point(-1, 0), Point(-2, 0)}),
        ('R2,D4', 'D2,R4', {Point(2, -2)}),
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
    assert closest(seq1, seq2, to=Point(0, 0)) == expected


@pytest.mark.parametrize(
    'seq1, seq2, expected', [
        ('R8,U5,L5,D3', 'U7,R6,D4,L4', 30),
        (
            'R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83',
            610,
        ),
        (
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
            410,
        ),
    ]
)
def test_get_signal_delay(seq1, seq2, expected):
    assert get_signal_delay(seq1, seq2) == expected
