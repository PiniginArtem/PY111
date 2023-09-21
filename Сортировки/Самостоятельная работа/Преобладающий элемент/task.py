from typing import List


def majority_element(nums: List[int]) -> int:
    if not nums:
        return None
    counter = 0
    majority_el = nums[0]
    counter += 1
    for i in range(1, len(nums)):
        if counter == 0:
            majority_el = nums[i]
            counter += 1
        elif nums[i] == majority_el:
            counter += 1
        else:
            counter -= 1
    return majority_el


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
