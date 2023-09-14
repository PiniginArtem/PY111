from typing import Union
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    sin_x = 0
    n = 0
    while True:
        delta_x = (((-1) ** n) / factorial(2 * n + 1)) * (x ** (2 * n + 1))
        sin_x += delta_x
        if abs(delta_x) < DELTA:
            break
        n += 1
    return sin_x
