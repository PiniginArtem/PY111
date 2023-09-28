from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError

    if n < 1 or m < 1:
        return [[0]]

    count_paths = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, (n + 1)):
        for j in range(1, (m + 1)):
            if i == 1 and j == 1:
                count_paths[i][j] = 1
            else:
                count_paths[i][j] = count_paths[i - 1][j] + count_paths[i][j - 1] + count_paths[i - 1][j - 1]

    return count_paths


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
