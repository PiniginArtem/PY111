from collections import deque
import networkx as nx


"""
3
Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине. 
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой. 
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов. 
"""


def connect_graph(g: nx.Graph) -> int:
    """
    Функция выполняет обход в ширину и возвращает кол-во не соединенных между собой графов.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :return: Кол-во не соединенных между собой графов

    >>> graph = nx.Graph()
    >>> connect_graph(graph)
    0
    >>> graph.add_edges_from([('A', 'C'), ('C', 'F'), ('B', 'E'), ('B', 'D'), ('E', 'G')])
    >>> connect_graph(graph)
    2
    """
    if not isinstance(g, nx.Graph):
        raise TypeError("на входе должен быть nx.Graph")

    visited = {node: False for node in g.nodes}
    d = deque()
    all_paths = []

    for node in visited.keys():
        if not visited[node]:

            path = []
            d.append(node)
            visited[node] = True

            while d:
                current_node = d.popleft()
                path.append(current_node)
                for neig in g.neighbors(current_node):
                    if not visited[neig]:
                        d.append(neig)
                        visited[neig] = True
            all_paths.append(path)

    # print(all_paths)
    return len(all_paths)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
