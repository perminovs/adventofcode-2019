import pytest

from day_22.solution import (
    stack_shuffle, cut_shuffle, increment_shuffle, parse_instruction, shuffle)


@pytest.mark.parametrize('cards, expected', [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
])
def test_stack_shuffle(cards, expected):
    assert stack_shuffle(cards) == expected


@pytest.mark.parametrize('cards, expected, n', [
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
        3,
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
        -4,
    ),
])
def test_cut_shuffle(cards, expected, n):
    assert cut_shuffle(cards, n) == expected


@pytest.mark.parametrize('cards, expected, n', [
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 7, 4, 1, 8, 5, 2, 9, 6, 3],
        3,
    ),
])
def test_increment_shuffle(cards, expected, n):
    assert increment_shuffle(cards, n) == expected


@pytest.mark.parametrize('instruction, parsed', [
    ('deal with increment 7', (increment_shuffle, (7, ))),
    ('deal with increment 5', (increment_shuffle, (5, ))),
    ('deal into new stack', (stack_shuffle, ())),
    ('cut 6', (cut_shuffle, (6, ))),
    ('cut -2', (cut_shuffle, (-2, ))),
])
def test_parse_instruction(instruction, parsed):
    assert parse_instruction(instruction) == parsed


@pytest.mark.parametrize('cards, instructions, expected', [
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "deal with increment 7\n"
        "deal into new stack\n"
        "deal into new stack".split('\n'),
        [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cut 6\n"
        "deal with increment 7\n"
        "deal into new stack".split('\n'),
        [3, 0, 7, 4, 1, 8, 5, 2, 9, 6],
    ),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "deal into new stack\n"
        "cut -2\n"
        "deal with increment 7\n"
        "cut 8\n"
        "cut -4\n"
        "deal with increment 7\n"
        "cut 3\n"
        "deal with increment 9\n"
        "deal with increment 3\n"
        "cut -1".split('\n'),
        [9, 2, 5, 8, 1, 4, 7, 0, 3, 6],
    ),
])
def test_shuffle(cards, instructions, expected):
    assert shuffle(cards, instructions) == expected
