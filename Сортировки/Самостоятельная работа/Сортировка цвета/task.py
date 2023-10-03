from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    count_list = [0] * 3
    for i in range(len(nums)):
        count_list[nums[i]] += 1

    k = 0
    for i in range(3):
        while count_list[i] != 0:
            nums[k] = i
            k += 1
            count_list[i] -= 1
