import networkx as nx


"""4.	Навигатор на сетке. 
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
(все стоимости положительные). 
Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
"""


def min_cost_path(graph: nx.DiGraph, start: tuple[int, int], stop: tuple[int, int]) -> list[tuple[int]]:
    """
    Функция, которая находит путь минимальной стоимости из стартовой ячейки в конечную

    :param graph: Граф типа nx.DiGraph
    :param start: Стартовая точка
    :param stop: Конечная точка

    :return: Список ячеек пути минимальной стоимости для прохода из стартовой в конечную точку.
    Стартовая и конечная точка включены в список.
    """
    if not isinstance(graph, nx.DiGraph):
        raise TypeError("Граф должен быть типа 'nx.DiGraph'")
    if not isinstance(start, tuple) or not isinstance(stop, tuple):
        raise TypeError("Старт и стоп должен быть кортежами целых чисел")

    return nx.shortest_path(graph, source=start, target=stop, weight='weight')


def do_graph_from_array(arr) -> nx.DiGraph:
    """
    Функция преобразующая двумерную матрицу в граф. В графе узлы связаны таким образом, что мы можем перейти только
    в соседнюю клетку по вертикали или горизонтали исходной матрицы

    :param arr: двумерная сетка, на которой определена стоимость захода в каждую ячейку

    :return: направленный граф связанных ячеек, с весом ребер равным стоимости захода в данные ячейки
    """
    graph = nx.DiGraph()
    for i in range(len(arr)):
        for j in range(len(arr[i])):  # Пробегаем по каждому значению двумерной сетки
            if 0 <= i-1 < len(arr[i]) and 0 <= j < len(arr[j]):  # Проверяем существует ли ячейка со смещением
                graph.add_edge((i, j), (i-1, j), weight=arr[i-1][j])  # Добавляем связь в граф с весом захода в ячейку
            if 0 <= i < len(arr[i]) and 0 <= j-1 < len(arr[j]):
                graph.add_edge((i, j), (i, j-1), weight=arr[i][j-1])
            if 0 <= i+1 < len(arr[i]) and 0 <= j < len(arr[j]):
                graph.add_edge((i, j), (i+1, j), weight=arr[i+1][j])
            if 0 <= i < len(arr[i]) and 0 <= j+1 < len(arr[j]):
                graph.add_edge((i, j), (i, j+1), weight=arr[i][j+1])
    return graph


if __name__ == "__main__":
    array_1 = [[5, 10, 3, 6, 8],
               [1, 9, 20, 2, 11],
               [2, 7, 4, 12, 3],
               [3, 13, 7, 8, 1],
               [1, 1, 1, 1, 1]
               ]
    print(min_cost_path(do_graph_from_array(array_1), (0, 0), (4, 4)))
    # [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    print(min_cost_path(do_graph_from_array(array_1), (1, 1), (3, 1)))
    # [(1, 1), (1, 0), (2, 0), (3, 0), (3, 1)]

