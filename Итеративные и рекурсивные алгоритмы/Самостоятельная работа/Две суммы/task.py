from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_ = {target - value: key for key, value in enumerate(nums)}
    for key, value in enumerate(nums):
        if value in dict_ and dict_[value] != key:
            return [key, dict_[value]]


if __name__ == "__main__":
    list_ = [1, 3, 4, 2]
    target_ = 6
    print(two_sum(list_, target_))
    list_2 = [3, 2, 4]
    print(two_sum(list_2, target_))