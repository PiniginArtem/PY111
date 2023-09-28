from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    if not isinstance(count_stairs, int):
        raise ValueError
    if count_stairs < 0:
        raise ValueError
    if not count_stairs:
        return [0]
    list_path = [0, 1] + [0] * (count_stairs - 1)
    for i in range(2, count_stairs + 1):
        list_path[i] = list_path[i - 1] + list_path[i - 2]
    return list_path


if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
