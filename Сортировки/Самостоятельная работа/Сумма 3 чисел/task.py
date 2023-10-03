from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    quicksort(nums)
    res = []
    for i in range(len(nums)):
        j_ = i + 1
        for j in range(j_, len(nums)):
            k_ = j + 1
            for k in range(k_, len(nums)):
                if i != j and j != k and i != k and nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in res:
                        res.append([nums[i], nums[j], nums[k]])
            k_ += 1
        j_ += 1
    return res


def quicksort(container: List[int], left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(container) - 1
    if left >= right:
        return
    i, j = left, right
    pivot = container[right]
    while i <= j:
        while container[i] < pivot:
            i += 1
        while container[j] > pivot:
            j -= 1
        if i <= j:
            container[i], container[j] = container[j], container[i]
            i, j = i + 1, j - 1
    quicksort(container, left, j)
    quicksort(container, i, right)


def three_sum_2(nums: List[int]) -> List[List[int]]:

    res = []

    """1. Split nums into three lists: negative numbers, positive numbers, and zeros"""
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)
    p.sort()
    n.sort()

    """2. Create a separate set for negatives and positives for O(1) look-up times"""
    N, P = set(n), set(p)

    """3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    i.e. (-3, 0, 3) = 0"""
    if z:
        for num in P:
            if -1 * num in N:
                res.append([-1*num, 0, num])

    """3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0"""
    if len(z) >= 3:
        res.append([0, 0, 0])

    """4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    exists in the positive number set"""
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            triplet = [n[i], n[j], target]
            if target in P and triplet not in res:
                res.append(triplet)

    """5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    exists in the negative number set"""
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            triplet = [p[i], p[j], target]
            if target in N and triplet not in res:
                res.append(triplet)

    res.sort()
    return res


if __name__ == "__main__":
    list_ = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 0, 4]
    print(three_sum(list_))
    print(three_sum_2(list_))
