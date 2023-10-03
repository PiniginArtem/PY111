from typing import List


def reverse_string(s: List[str]) -> None:
    # s.reverse()
    for i in range(0, len(s) // 2):
        s[i], s[-1 - i] = s[-1 - i], s[i]
