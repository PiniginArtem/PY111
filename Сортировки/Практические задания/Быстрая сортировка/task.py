from typing import List
from random import randint


def sort(container: List[int], left: int = 0, right: int = None) -> None:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    if right is None:
        right = len(container) - 1

    if left >= right:
        return

    i, j = left, right
    pivot = container[randint(left, right)]

    while i <= j:
        while container[i] < pivot:
            i += 1
        while container[j] > pivot:
            j -= 1
        if i <= j:
            container[i], container[j] = container[j], container[i]
            i, j = i + 1, j - 1
    sort(container, left, j)
    sort(container, i, right)


if __name__ == "__main__":
    list_1 = [2, 7, 11, 15, 5, 4, 6]
    sort(list_1)
    assert list_1 == [2, 4, 5, 6, 7, 11, 15]
    list_2 = [-2, -7, -11, -15, -5, -4, -6, 0]
    sort(list_2)
    assert list_2 == [-15, -11, -7, -6, -5, -4, -2, 0]
