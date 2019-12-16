import pytest

from day_16.solution import phase, get_pattern_for_round


@pytest.mark.parametrize('iteration, expected', [
    (2, [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1]),
    (3, [0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1]),
])
def test_get_pattern_for_round(iteration, expected):
    nums = []
    for i in get_pattern_for_round(iteration):
        nums.append(i)
        if len(nums) == len(expected):
            break
    assert nums == expected


@pytest.mark.parametrize('numbers, expected', [
    ('12345678', '48226158'),
    ('48226158', '34040438'),
])
def test_one_phase(numbers, expected):
    assert phase(numbers, 1) == expected


@pytest.mark.parametrize('numbers, expected, repeat', [
    ('12345678', '34040438', 2),
])
def test_phase(numbers, expected, repeat):
    assert phase(numbers, repeat) == expected
