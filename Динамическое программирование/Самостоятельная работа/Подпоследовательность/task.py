def is_subsequence(s: str, str_: str) -> bool:
    n = 0  # начальная позиция
    for letter in s:
        n += find_index(letter, str_[n:]) + 1
        if n > len(str_):
            return False
    return True


def find_index(letter: str, str_: str):
    for i in range(len(str_)):
        if letter == str_[i]:
            return i
    return len(str_)


if __name__ == "__main__":
    print(is_subsequence("abc", "ahbgdc"))  # True
    print(is_subsequence("axc", "ahbgdc"))  # False
    print(is_subsequence("", "ahbgdc"))  # True
    print(is_subsequence("abcd", "ahbgdc"))  # False
