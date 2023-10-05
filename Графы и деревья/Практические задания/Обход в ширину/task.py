from typing import Hashable, List
from collections import deque

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    visited = {node: False for node in g.nodes}
    d = deque()
    path = []

    d.append(start_node)
    visited[start_node] = True

    while d:
        current_node = d.popleft()
        path.append(current_node)
        for neig in g.neighbors(current_node):
            if not visited[neig]:
                d.append(neig)
                visited[neig] = True
    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ("A", "B"),
        ("A", "F"),
        ("B", "G"),
        ("F", "G"),
        ("G", "C"),
        ("G", "H"),
        ("G", "I"),
        ("C", "H"),
        ("I", "H"),
        ("H", "D"),
        ("H", "E"),
        ("H", "J"),
        ("E", "D")
    ])
    print(bfs(graph, "A"))
