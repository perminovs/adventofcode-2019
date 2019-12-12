import pytest

from day_10.solution import (
    Vector, Point, get_asteroid_rank, get_vector_to_points, sort_vectors,
    destroy_asteroids, NUMBER_TO_DESTROY)

SAMPLE = (
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
    "###.##.####.##.#..##\n"
)


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
        SAMPLE,
        Point(11, 13),
        210,
    )
])
def test_get_best_observe(raw, expected_asteroid, expected_count):
    asteroids = Point.from_raw(raw)
    rank = get_asteroid_rank(asteroids)
    assert max(rank.values()) == expected_count
    assert rank[expected_asteroid] == expected_count


@pytest.mark.parametrize('raw, station, expected', [
    (
        "#\n"
        ".\n"
        "#\n"
        "#\n",
        Point(0, 0),
        {
            Vector(0, 1): [Point(0, 3), Point(0, 2)],
        },
    ),
    (
        "#..\n"
        ".##\n"
        "#.#\n"
        "#..\n",
        Point(0, 0),
        {
            Vector(0, 1): [Point(0, 3), Point(0, 2)],
            Vector(0.707107, 0.707107): [Point(2, 2), Point(1, 1)],
            Vector(0.894427, 0.447214): [Point(2, 1)],
        },
    ),
])
def test_direction_rank(raw, station: Point, expected):
    asteroids = Point.from_raw(raw)
    assert get_vector_to_points(asteroids, station) == expected


@pytest.mark.parametrize('vectors, expected', [
    (
        {
            Vector(0, 1),
            Vector(0.707107, 0.707107),
            Vector(0.894427, 0.447214),
        },
        [
            Vector(0.894427, 0.447214),
            Vector(0.707107, 0.707107),
            Vector(0, 1),
        ]
    ),
])
def test_sort_directions(vectors, expected):
    assert sort_vectors(vectors) == expected


def test_sort_from_points():
    station = Point(3, 2)
    p1 = Point(3, 1, 'p1')  # ....2..
    p2 = Point(4, 0, 'p2')  # .5.13..
    p3 = Point(4, 1, 'p3')  # ...X...
    p4 = Point(2, 4, 'p4')  # .......
    p5 = Point(1, 1, 'p5')  # ..4....

    asteroids = [station, p1, p2, p3, p4, p5]

    vectors = get_vector_to_points(asteroids, station)
    assert all(len(points) == 1 for points in vectors.values())
    vector_order = sort_vectors(vectors)
    points_rank = []
    point_to_vectors = {}
    for v in vector_order:
        point = vectors[v][0]
        points_rank.append(point)
        point_to_vectors[point] = v, v.angle
    assert points_rank == [p1, p2, p3, p4, p5], point_to_vectors


@pytest.mark.parametrize('raw, station, last, number_to_destroy', [
    (
        "#..\n"
        ".##\n"
        "#.#\n"
        "#..\n",
        Point(0, 0),
        Point(0, 2),
        3,
    ),
    (
        "...###.\n"
        ".#####.\n"
        "..##.#.\n"
        "..#..#.\n"
        "...#.#.\n",
        Point(3, 2),
        Point(3, 1),
        1,
    ),
    (
        "...###.\n"
        ".#####.\n"
        "..##.#.\n"
        "..#..#.\n"
        "...#.#.\n",
        Point(3, 2),
        Point(5, 1),
        4,
    ),
    (SAMPLE, Point(11, 13), Point(11, 12), 1),
    (SAMPLE, Point(11, 13), Point(12, 1), 2),
    (SAMPLE, Point(11, 13), Point(12, 2), 3),
    (SAMPLE, Point(11, 13), Point(12, 8), 10),
    (SAMPLE, Point(11, 13), Point(8, 2), NUMBER_TO_DESTROY),
])
def test_destroy_asteroids(raw, station, last, number_to_destroy):
    asteroids = Point.from_raw(raw)
    rank = get_vector_to_points(asteroids, station)
    destroyed = list(destroy_asteroids(rank))
    assert destroyed[number_to_destroy - 1] == last

