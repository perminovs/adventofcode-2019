import pytest

from day_04.solution import (
    has_decrease, has_duplicate, good_password_v1, additional_criteria)


@pytest.mark.parametrize(
    'digits, expected', [
        ('111123', False),
        ('135679', False),
        ('111111', False),
        ('223450', True),
    ]
)
def test_is_not_decrease(digits, expected):
    assert has_decrease(digits) == expected


@pytest.mark.parametrize(
    'digits, expected', [
        ('122345', True),
        ('111123', True),
        ('111111', True),
        ('213455', True),
        ('223450', True),
        ('123789', False),
    ]
)
def test_has_duplicate(digits, expected):
    assert has_duplicate(digits) == expected


@pytest.mark.parametrize(
    'number, expected', [
        (111111, True),
        (223450, False),
        (123789, False),
    ]
)
def test_good_password(number, expected):
    assert good_password_v1(number) == expected


@pytest.mark.parametrize(
    'digits, expected', [
        ('112233', True),
        ('123444', False),
        ('111122', True),
        ('111222', False),
    ]
)
def test_additional_criteria(digits, expected):
    assert additional_criteria(digits) == expected
