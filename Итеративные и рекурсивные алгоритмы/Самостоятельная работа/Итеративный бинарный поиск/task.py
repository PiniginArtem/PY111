from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    left_border = 0
    right_border = len(seq) - 1

    while left_border <= right_border:
        mid = left_border + (right_border - left_border) // 2
        if seq[mid] == value:
            while True:
                if not 0 <= mid - 1 < len(seq) or seq[mid - 1] != value:
                    break
                else:
                    mid -= 1
            return mid
        elif seq[mid] > value:
            right_border = mid - 1
        elif seq[mid] < value:
            left_border = mid + 1
    else:
        raise ValueError("Такого элемента нет")
