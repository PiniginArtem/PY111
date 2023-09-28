from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    i = len(table)
    j = len(table[0])
    list_total_coasts = [[float("inf")] * (j + 1)] + [[float("inf")] + [0] * j for _ in range(i)]
    for index_i in range(1, i + 1):
        for index_j in range(1, j + 1):
            if index_i == 1 and index_j == 1:
                list_total_coasts[index_i][index_j] = table[index_i - 1][index_j - 1]
            else:
                list_total_coasts[index_i][index_j] = table[index_i - 1][index_j - 1] +\
                                                      min(list_total_coasts[index_i - 1][index_j],
                                                          list_total_coasts[index_i][index_j - 1])
    return list_total_coasts


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
