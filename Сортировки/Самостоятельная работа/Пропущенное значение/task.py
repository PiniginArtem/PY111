from typing import List


def missing_number(nums: List[int]) -> int:
    list_nums = [0] * (len(nums) + 1)
    for digit in nums:
        list_nums[digit] = 1
    for i in range(len(list_nums)):
        if list_nums[i] == 0:
            return i
