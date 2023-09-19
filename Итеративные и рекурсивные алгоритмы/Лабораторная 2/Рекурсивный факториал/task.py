def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("n должна быть целым числом")
    if n < 0:
        raise ValueError("n должна быть >= 0")
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n
