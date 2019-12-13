import pytest

from day_12.solution import Moon, make_step, find_restate


@pytest.mark.parametrize('ganymede, callisto, g_vx, c_vx', [
    (Moon([3, 0, 0], [0, 0, 0]), Moon([5, 0, 0], [0, 0, 0]), +1, -1)
])
def test_velocity_step(ganymede, callisto, g_vx, c_vx):
    ganymede.apply_gravity(callisto, 0)
    callisto.apply_gravity(ganymede, 0)
    assert ganymede.velocity[0] == g_vx
    assert callisto.velocity[0] == c_vx


@pytest.mark.parametrize('raw, moon', [
    ('<x=-16, y=15, z=-9>', Moon([-16, 15, -9], [0, 0, 0])),
    (
        'pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>',
        Moon([+2, -1, +1], [+3, -1, -1]),
    ),
])
def test_from_raw(raw, moon):
    assert Moon.from_raw(raw) == moon


@pytest.mark.parametrize('raw_moons, raw_expected, step_cnt', [
    (
        "<x=-1, y=0, z=2>\n"
        "<x=2, y=-10, z=-7>\n"
        "<x=4, y=-8, z=8>\n"
        "<x=3, y=5, z=-1>",

        "pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>\n"
        "pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>\n"
        "pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>\n"
        "pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>",

        1,
    ),

    (
        "<x=-1, y=0, z=2>\n"
        "<x=2, y=-10, z=-7>\n"
        "<x=4, y=-8, z=8>\n"
        "<x=3, y=5, z=-1>",

        "pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>\n"
        "pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>\n"
        "pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>\n"
        "pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>",

        10,
    )
])
def test_step(raw_moons, raw_expected, step_cnt):
    moons = [Moon.from_raw(raw) for raw in raw_moons.split('\n')]
    expected = [Moon.from_raw(raw) for raw in raw_expected.split('\n')]
    for _ in range(step_cnt):
        make_step(moons)
    assert moons == expected


@pytest.mark.parametrize('raw, expected', [
    ("pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>", 36)
])
def test_energy(raw, expected):
    assert Moon.from_raw(raw).energy == expected


@pytest.mark.parametrize('raw, idx', [
    (
        "pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>\n"
        "pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>\n"
        "pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>\n"
        "pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>",
        2772,
    ),
])
def test_find_restate(raw, idx):
    moons = [Moon.from_raw(r) for r in raw.split('\n')]
    assert find_restate(moons) == idx
