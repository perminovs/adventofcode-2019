from day_20.data import DATA
from day_20.graphs import bfs
from day_20.parsing import build_graph


def get_shortest_path(graph: str, start_point, end_point) -> int:
    graph, n1, n2 = build_graph(graph, start_point, end_point)
    return bfs(graph, n1, n2)


def main():
    path_len = get_shortest_path(DATA, 'AA', 'ZZ')
    print(path_len)


if __name__ == '__main__':
    main()
