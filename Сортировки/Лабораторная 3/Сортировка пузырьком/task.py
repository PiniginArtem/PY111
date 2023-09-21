from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    flag = False
    n = 1
    while not flag:
        flag = True
        for i in range(len(container) - n):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                flag = False
        n += 1
    return container


if __name__ == "__main__":
    print(sort([-1, 2, 10, -11, 0, 34, 12, -4, -12, 34, 34, 12, -3]))
