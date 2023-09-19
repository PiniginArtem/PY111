from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_ = {target - value: key for key, value in enumerate(nums)}
    for key, value in enumerate(nums):
        if dict_.get(value) and not dict[value] == key:
            return [dict_[value], key]
