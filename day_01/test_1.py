import pytest

from day_01.solution import _calc_fuel, calc_fuel


@pytest.mark.parametrize(
    'mass, fuel',
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ]
)
def test_01(mass, fuel):
    assert _calc_fuel(mass) == fuel


@pytest.mark.parametrize(
    'mass, fuel',
    [
        (14, 2),
        (1969, 966),
        (100756, 50346),
    ]
)
def test_02(mass, fuel):
    assert calc_fuel(mass) == fuel
