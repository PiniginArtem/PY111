def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("n должна быть целым числом")
    if n > -1:
        factorial_n = 1
        for i in range(1, n + 1):
            factorial_n *= i
        return factorial_n
    else:
        raise ValueError("n должна быть >= 0")


if __name__ == "__main__":
    assert factorial_iterative(12) == 479001600
