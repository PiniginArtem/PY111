def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """

    if not isinstance(n, int):
        raise TypeError("Индекс должен быть типа int")
    if n < 0:
        raise ValueError("Неправильное n. Индекс последовательности должен быть >= 0")

    if n == 0:
        return 0
    if n == 1:
        return 1
    left, right = fib_recursive(n - 2), fib_recursive(n - 1)

    return left + right


if __name__ == "__main__":
    print(fib_recursive(9))
