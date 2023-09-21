from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container
    max_container = max(container)
    list_counter = [0] * (max_container + 1)
    list_output = []
    for value in container:
        list_counter[value] += 1
    for value in range(len(list_counter)):
        while list_counter[value] != 0:
            list_output.append(value)
            list_counter[value] -= 1
    return list_output


if __name__ == "__main__":
    list_1 = [1, 6, 3, 1, 6, 3, 5, 0, 7, 7, 2, 3, 5, 6, 5, 0, 4, 3, 2, 1, 7]
    print(list_1)
    print(sort(list_1))
    print(sort([]))
