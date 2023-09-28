from typing import Union, Sequence
from functools import lru_cache


@lru_cache()
def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    if not stairway:
        return 0
    return stairway[-1] + min(stairway_path(stairway[:-1]), stairway_path(stairway[:-2]))


if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
