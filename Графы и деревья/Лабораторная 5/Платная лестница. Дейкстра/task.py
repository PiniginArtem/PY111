from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> int:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    return nx.shortest_path_length(graph, source=0, target=(len(graph.nodes) - 1), weight='weight')


def do_graph_from_stairway(stairway: Union[list[int], tuple[int]]) -> nx.DiGraph:
    """
    Функция, которая преобразует лестницу со стоимостью ступеней во взвешанный направленный граф

    :param stairway: Последовательность стоимости ступеней, где элемент с индексом 0 - это стоимость наступить на
    1ую ступень, элемент с индексом 0 - стоимость 2ой ступени и т.д.
    :return: взвешанный направленный граф
    """
    graph = nx.DiGraph()
    for i in range(len(stairway)):
        graph.add_edge(i, i + 1, weight=stairway[i])
        if i != len(stairway) - 1:
            graph.add_edge(i, i + 2, weight=stairway[i + 1])

    # Дальнейший кусок кода печатает направленный взвешанный граф в удобном виде (от узла, к узлу, вес)
    # for (n, nbr, wt) in graph.edges.data('weight'):
    #     print(f"({n}, {nbr}, {wt})")

    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = do_graph_from_stairway(stairway)
    print(stairway_path(stairway_graph))  # 72
