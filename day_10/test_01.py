import pytest

from day_10.solution import Vector, Point, get_asteroid_rank, get_best_observe


@pytest.mark.parametrize('a1, a2, expected_line', [
    (Point(3, 1), Point(2, 1), Vector(1.0, 0.0)),
    (Point(2, 7), Point(2, 5), Vector(0.0, 1.0)),
    (Point(1, 1), Point(4, 2), Vector(-0.948683, -0.316228)),
])
def test_from_asteroids(a1, a2, expected_line):
    real = Vector.from_asteroids(a1, a2)
    assert real == expected_line


@pytest.mark.parametrize('raw, expected', [
    (".#.#.#", [Point(1, 0), Point(3, 0), Point(5, 0)]),
    (
        ".#..#\n"
        ".....\n"
        "#####\n"
        "....#\n"
        "...##\n",
        [
            Point(1, 0), Point(4, 0),

            Point(0, 2), Point(1, 2), Point(2, 2),
            Point(3, 2), Point(4, 2),

            Point(4, 3),

            Point(3, 4), Point(4, 4),
        ],
    ),
])
def test_from_raw(raw, expected):
    real = Point.from_raw(raw)
    assert len(real) == len(expected)
    assert set(real) == set(expected)


@pytest.mark.parametrize('raw, expected', [
    (
        ".#.#.#",
        {
            Point(1, 0): 1,
            Point(3, 0): 2,
            Point(5, 0): 1,
        },
    ),
    (
        ".#..#\n"
        ".....\n"
        "#####\n"
        "....#\n"
        "...##\n",
        {
            Point(1, 0): 7,
            Point(4, 0): 7,

            Point(0, 2): 6,
            Point(1, 2): 7,
            Point(2, 2): 7,
            Point(3, 2): 7,
            Point(4, 2): 5,

            Point(4, 3): 7,

            Point(3, 4): 8,
            Point(4, 4): 7,
        }
    ),
])
def test_get_asteroid_rank(raw, expected):
    asteroids = Point.from_raw(raw)
    real = get_asteroid_rank(asteroids)
    for r_ast, r_value in real.items():
        expected_value = expected[r_ast]
        if expected_value != r_value:
            print(f'{r_ast}: expected {expected_value}, got {r_value}')
    assert real == expected


@pytest.mark.parametrize('raw, expected_asteroid, expected_count', [
    (
        ".#..#\n"
        ".....\n"
        "#####\n"
        "....#\n"
        "...##\n",
        Point(3, 4),
        8,
    ),
    (
        "......#.#.\n"
        "#..#.#....\n"
        "..#######.\n"
        ".#.#.###..\n"
        ".#..#.....\n"
        "..#....#.#\n"
        "#..#....#.\n"
        ".##.#..###\n"
        "##...#..#.\n"
        ".#....####\n",
        Point(5, 8),
        33,
    ),
    (
        "#.#...#.#.\n"
        ".###....#.\n"
        ".#....#...\n"
        "##.#.#.#.#\n"
        "....#.#.#.\n"
        ".##..###.#\n"
        "..#...##..\n"
        "..##....##\n"
        "......#...\n"
        ".####.###.\n",
        Point(1, 2),
        35,
    ),
    (
        ".#..##.###...#######\n"
        "##.############..##.\n"
        ".#.######.########.#\n"
        ".###.#######.####.#.\n"
        "#####.##.#.##.###.##\n"
        "..#####..#.#########\n"
        "####################\n"
        "#.####....###.#.#.##\n"
        "##.#################\n"
        "#####.##.###..####..\n"
        "..######..##.#######\n"
        "####.##.####...##..#\n"
        ".#####..#.######.###\n"
        "##...#.##########...\n"
        "#.##########.#######\n"
        ".####.#.###.###.#.##\n"
        "....##.##.###..#####\n"
        ".#.#.###########.###\n"
        "#.#.#.#####.####.###\n"
        "###.##.####.##.#..##\n",
        Point(11, 13),
        210,
    )
])
def test_get_best_observe(raw, expected_asteroid, expected_count):
    asteroids = Point.from_raw(raw)
    rank = get_asteroid_rank(asteroids)
    assert max(rank.values()) == expected_count
    assert rank[expected_asteroid] == expected_count
