import pytest

from day_02.solution import solve, get_packet


@pytest.mark.parametrize(
    'encounters, idx, expected', [
        ([1, 0, 0, 0, 99], 0, [1, 0, 0, 0]),
        ([1, 0, 0, 0, 99], 1, None),
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 0, [1, 9, 10, 3]),
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 1, [2, 3, 11, 0]),
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 2, None),
    ])
def test_get_pack(encounters, idx, expected):
    assert get_packet(idx, encounters) == expected


@pytest.mark.parametrize(
    'encounters, expected', [
        (
            [1, 0, 0, 0, 99],
            [2, 0, 0, 0, 99],
        ),
        (
            [2, 3, 0, 3, 99],
            [2, 3, 0, 6, 99],
        ),
        (
            [2, 4, 4, 5, 99, 0],
            [2, 4, 4, 5, 99, 9801],
        ),
        (
            [1, 1, 1, 4, 99, 5, 6, 0, 99],
            [30, 1, 1, 4, 2, 5, 6, 0, 99],
        ),
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        )
    ])
def test_solve(encounters, expected):
    solve(encounters)
    assert encounters == expected
