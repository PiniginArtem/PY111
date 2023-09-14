def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    if not isinstance(n, int):
        raise TypeError("Индекс должен быть типа int")
    fib_left = 0
    fib_right = 1
    if n > 1:
        for i in range(2, n + 1):
            fib_left, fib_right = fib_right, fib_left + fib_right
        return fib_right
    elif n == 0:
        return fib_left
    elif n == 1:
        return fib_right
    elif n < 0:
        raise ValueError("Неправильное n. Индекс последовательности должен быть >= 0")
