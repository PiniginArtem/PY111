from typing import Tuple
from functools import lru_cache


@lru_cache
def calculate_paths(shape: Tuple[int, int], i: int = None, j: int = None) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :param i: индекс строки
    :param j: индекс столбца
    :return: количество путей согласно заданным условиям
    """
    if i is None or j is None:
        i = shape[0]
        j = shape[1]
    if not 0 < i <= shape[0] or not 0 < j <= shape[1]:
        return 0
    if i == 1 and j == 1:
        return 1
    return calculate_paths(shape, i - 2, j + 1) + calculate_paths(shape, i - 2, j - 1)\
        + calculate_paths(shape, i - 1, j - 2) + calculate_paths(shape, i + 1, j - 2)


def calculate_paths_2(shape: Tuple[int, int]) -> int:
    count_paths = [[0] * (shape[1] + 1) for _ in range(shape[0] + 1)]
    count_paths[1][1] = 1
    for k in range(1, shape[1] + 1):
        j = k
        i = 1
        while j > 0 and i < shape[0] + 1:
            if 0 < i - 1 <= shape[0] and 0 < j + 2 <= shape[1]:
                count_paths[i - 1][j + 2] += count_paths[i][j]
            if 0 < i + 2 <= shape[0] and 0 < j + 1 <= shape[1]:
                count_paths[i + 2][j + 1] += count_paths[i][j]
            if 0 < i + 2 <= shape[0] and 0 < j - 1 <= shape[1]:
                count_paths[i + 2][j - 1] += count_paths[i][j]
            if 0 < i + 1 <= shape[0] and 0 < j + 2 <= shape[1]:
                count_paths[i + 1][j + 2] += count_paths[i][j]
            i += 1
            j -= 1
    for k in range(2, shape[0] + 1):
        j = shape[1]
        i = k
        while j > 0 and i < shape[0] + 1:
            if 0 < i - 1 <= shape[0] and 0 < j + 2 <= shape[1]:
                count_paths[i - 1][j + 2] += count_paths[i][j]
            if 0 < i + 2 <= shape[0] and 0 < j + 1 <= shape[1]:
                count_paths[i + 2][j + 1] += count_paths[i][j]
            if 0 < i + 2 <= shape[0] and 0 < j - 1 <= shape[1]:
                count_paths[i + 2][j - 1] += count_paths[i][j]
            if 0 < i + 1 <= shape[0] and 0 < j + 2 <= shape[1]:
                count_paths[i + 1][j + 2] += count_paths[i][j]
            i += 1
            j -= 1
    return count_paths[-1][-1]


def calculate_paths_3(shape: tuple[int, int]) -> int:
    current_point = shape
    count_paths = [[None] * (current_point[1] + 1) for _ in range(current_point[0] + 1)]
    count_paths[1][1] = 1
    i = current_point[0]
    j = current_point[1]
    set_points = [(i, j)]
    index_current_point = len(set_points) - 1
    while index_current_point > -1:
        len_set_points = len(set_points)
        if 0 < i - 1 <= shape[0] and 0 < j - 2 <= shape[1] and (i - 1, j - 2) not in set_points:
            set_points.insert(index_current_point + 1, (i - 1, j - 2))
        if 0 < i - 2 <= shape[0] and 0 < j - 1 <= shape[1] and (i - 2, j - 1) not in set_points:
            set_points.insert(index_current_point + 1, (i - 2, j - 1))
        if 0 < i + 1 <= shape[0] and 0 < j - 2 <= shape[1] and (i + 1, j - 2) not in set_points:
            set_points.insert(index_current_point + 1, (i + 1, j - 2))
        if 0 < i - 2 <= shape[0] and 0 < j + 1 <= shape[1] and (i - 2, j + 1) not in set_points:
            set_points.insert(index_current_point + 1, (i - 2, j + 1))
        if len_set_points != len(set_points):
            index_current_point += (len(set_points) - len_set_points)
            current_point = set_points[index_current_point]
            i = current_point[0]
            j = current_point[1]
        else:
            if i == 1 and j == 1:
                count_paths[i][j] = 1
            else:
                count_paths[i][j] = 0
            if 0 < i - 1 <= shape[0] and 0 < j - 2 <= shape[1]:
                count_paths[i][j] += count_paths[i - 1][j - 2]
            if 0 < i - 2 <= shape[0] and 0 < j - 1 <= shape[1]:
                count_paths[i][j] += count_paths[i - 2][j - 1]
            if 0 < i + 1 <= shape[0] and 0 < j - 2 <= shape[1]:
                count_paths[i][j] += count_paths[i + 1][j - 2]
            if 0 < i - 2 <= shape[0] and 0 < j + 1 <= shape[1]:
                count_paths[i][j] += count_paths[i - 2][j + 1]
            index_current_point -= 1
            current_point = set_points[index_current_point]
            i = current_point[0]
            j = current_point[1]
    # for vl in count_paths:
    #     for jk in vl:
    #         print(f"{0 if jk is None else jk:6}", end="", sep="")
    #     print()
    return count_paths[-1][-1]


def traversing_matrix_diagonally(shape: tuple[int, int]) -> list[list[int]]:
    count_paths = [[0] * (shape[1] + 1) for _ in range(shape[0] + 1)]
    for k in range(1, shape[1] + 1):
        j = k
        i = 1
        while j > 0 and i < shape[0] + 1:
            # print((i, j))
            count_paths[i][j] += 1
            i += 1
            j -= 1
    for k in range(2, shape[0] + 1):
        j = shape[1]
        i = k
        while j > 0 and i < shape[0] + 1:
            # print((i, j))
            count_paths[i][j] += 1
            i += 1
            j -= 1
    # for row in count_paths:
    #     for cell in row:
    #         print(f"{0 if cell is None else cell:3}", end="", sep="")
    #     print()
    return count_paths


if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths_2((15, 7)))  # 13309
