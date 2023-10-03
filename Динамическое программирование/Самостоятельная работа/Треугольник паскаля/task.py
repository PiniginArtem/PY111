from typing import List
from functools import lru_cache


def generate_0(num_rows: int) -> List[List[int]]:
    list_ = [[1] if i == 0 else ([0] * (i + 1)) for i in range(num_rows)]
    for i in range(1, num_rows):
        for j in range(i + 1):
            if -1 < j < i:
                list_[i][j] += list_[i - 1][j]
            if -1 < j - 1 < i:
                list_[i][j] += list_[i - 1][j - 1]
    return list_


def generate(num_rows: int) -> List[List[int]]:
    list_ = []
    for i in range(num_rows):
        list_.append([])
        for j in range(i + 1):
            if i == j == 0:
                list_[i].append(1)
            else:
                if not -1 < j < i:
                    list_[i].append(1)
                elif not -1 < j - 1 < i:
                    list_[i].append(1)
                else:
                    list_[i].append(list_[i - 1][j] + list_[i - 1][j - 1])
    return list_


if __name__ == "__main__":
    print(generate(5))
