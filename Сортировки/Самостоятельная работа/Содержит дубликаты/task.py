from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    if not nums:
        return False
    dict_ = {}
    for value in nums:
        if value in dict_:
            return True
        else:
            dict_[value] = 1
    return False
