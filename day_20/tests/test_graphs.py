import pytest

from day_20.graphs import dijkstra, bfs


@pytest.mark.parametrize('graph, n1, n2, path_len', [
    (
        {
            #
            #            _----(5)---- _
            #           /              \
            #         9                  6
            #       /                      \
            #     (6)---2------(3)----11----(4)
            #       \        /    \         /
            #       14      9      10     15
            #         \   /           \  /
            #           (1)-----7-----(2)
            #
            1: [(6, 14), (3, 9), (2, 7)],
            2: [(1, 7), (3, 10), (4, 15)],
            3: [(2, 10), (1, 9), (6, 2), (4, 11)],
            4: [(2, 15), (3, 11), (5, 6)],
            5: [(4, 6), (6, 9)],
            6: [(1, 14), (3, 2), (5, 9)],
        },
        1,
        5,
        20,
    ),
])
def test_dijkstra(graph, n1, n2, path_len):
    assert dijkstra(graph, n1, n2) == path_len


GRAPH = {
    #
    #            _----(5)---- _
    #           /              \
    #         /                  \
    #       /                      \
    #     (6)----------(3)----------(4)
    #       \        /    \         /
    #        \      /       \     /
    #         \   /           \  /
    #           (1)-----------(2)
    #
    1: [2, 3, 6],
    2: [1, 3, 4],
    3: [1, 6, 4, 2],
    4: [3, 2, 5],
    5: [6, 4],
    6: [5, 1, 3],
}


@pytest.mark.parametrize('graph, n1, n2, path_len', [
    (GRAPH, 1, 1, 0),
    (GRAPH, 1, 6, 1),
    (GRAPH, 1, 5, 2),
    (GRAPH, 5, 1, 2),
    (GRAPH, 5, 3, 2),
    (GRAPH, 5, 2, 2),
    (GRAPH, 6, 4, 2),
])
def test_bfs(graph, n1, n2, path_len):
    assert bfs(graph, n1, n2) == path_len
