def check_brackets(brackets_row: str) -> bool:  # O(N)
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    unclosed_parenthesis = 0
    for letter in brackets_row:
        if letter == "(":
            unclosed_parenthesis += 1
        if letter == ")":
            unclosed_parenthesis -= 1
        if unclosed_parenthesis == -1:
            return False
    else:
        if unclosed_parenthesis > 0:
            return False
    return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
