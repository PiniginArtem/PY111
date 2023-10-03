from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    n = len(stairway)
    list_min_cost = [0, stairway[0]] + [0] * (n - 1)
    for i in range(2, n + 1):
        list_min_cost[i] = stairway[i - 1] + min(list_min_cost[i - 1], list_min_cost[i - 2])
    print(list_min_cost)
    return list_min_cost[n]


if __name__ == '__main__':
    print(stairway_path([5, 11, 43, 2, 23, 43, 22, 12, 6, 8]))  # 72
    print(stairway_path([100000, 5]))  # 5
