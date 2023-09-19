"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError("В пустом массиве нет минимума")
    min_value = arr[0]
    min_index = 0
    for index, value in enumerate(arr):
        if value < min_value:
            min_value = value
            min_index = index
    return min_index


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 2]
    assert min_search(list_1) == 0
    list_2 = [-5, -1, 0, 15, -30, 2]
    assert min_search(list_2) == 4
    list_3 = []
    print(list_3)
