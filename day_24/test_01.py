import pytest

from day_24.solution import Board, step_while_unique


def __eq__(self, other):
    return self._array == other._array


def __repr__(self):
    return "\n{}\n".format(
        "\n".join(
            ' '.join(row)
            for row in self._array
        )
    )


Board.__repr__ = __repr__
Board.__eq__ = __eq__


@pytest.mark.parametrize('initial, expected', [
    (
        "....#\n"
        "#..#.\n"
        "#..##\n"
        "..#..\n"
        "#....",

        "#..#.\n"
        "####.\n"
        "###.#\n"
        "##.##\n"
        ".##..",
    ),
])
def test_step(initial, expected):
    board = Board.from_raw(initial)
    board.make_step()
    expected_board = Board.from_raw(expected)
    assert board == expected_board


@pytest.mark.parametrize('raw_board, expected', [
    (
        ".....\n"
        ".....\n"
        ".....\n"
        "#....\n"
        ".#...",
        2129920,
    )
])
def test_energy(raw_board, expected):
    board = Board.from_raw(raw_board)
    assert board.energy == expected


@pytest.mark.parametrize('raw, expected', [
    (
        "....#\n"
        "#..#.\n"
        "#..##\n"
        "..#..\n"
        "#....",
        2129920,
    ),
])
def test_find_duplicate(raw, expected):
    board = Board.from_raw(raw)
    assert step_while_unique(board) == expected
