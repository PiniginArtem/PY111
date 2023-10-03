from typing import List
import math

def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    nums_min, nums_max = min(nums), max(nums)
    if nums_min == nums_max:
        return 0
    bucket_size = math.ceil((nums_max - nums_min) / (len(nums) - 1))
    bucket_list = [[None, None] for _ in range(len(nums))]
    for number in nums:
        bucket = (number - nums_min) // bucket_size
        if bucket_list[bucket][1] is None:
            bucket_list[bucket][1] = number
        elif bucket_list[bucket][1] < number:
            if bucket_list[bucket][0] is None:
                bucket_list[bucket][0] = bucket_list[bucket][1]
            elif bucket_list[bucket][0] > bucket_list[bucket][1]:
                bucket_list[bucket][0] = bucket_list[bucket][1]
            bucket_list[bucket][1] = number
        elif bucket_list[bucket][0] is None:
            bucket_list[bucket][0] = number
        elif bucket_list[bucket][0] > number:
            bucket_list[bucket][0] = number
    print(bucket_list)
    prev = nums_min
    difference = 0
    for list_ in bucket_list:
        if list_[0] is not None:
            if list_[0] - prev > difference:
                difference = list_[0] - prev
            prev = list_[1]
        elif list_[1] is not None:
            if list_[1] - prev > difference:
                difference = list_[1] - prev
            prev = list_[1]
    return difference


def maximum_gap_2(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    nums.sort()
    difference = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        tek = nums[i + 1] - nums[i]
        if tek > difference:
            difference = tek
    return difference


def maximum_gap_3(nums: List[int]) -> int:
    # Временная сложность:
    # худший: O(N)
    # Сложность по памяти:
    # O(N)
    mi, ma, n = min(nums), max(nums), len(nums)
    if mi == ma:
        return 0  # Все элементы одинаковы
    bucket_size = math.ceil((ma - mi) / (n - 1))  # Определение гипотетического среднего размера ведра
    min_bucket = [math.inf] * n  # Заполнение явно наибольшими значениями
    max_bucket = [-math.inf] * n  # Заполнение явно наименьшими значениями
    for x in nums:
        idx = (x - mi) // bucket_size # Определение индекса в какое ведро можно положить значение
        min_bucket[idx] = min(min_bucket[idx], x)  # Определение минимального значения в ведре
        max_bucket[idx] = max(max_bucket[idx], x)  # Определение максимального значения в ведре

    print([list(tup) for tup in zip(min_bucket, max_bucket)])

    max_gap = bucket_size  # Максимальный зазор всегда больше или равен размеру ведра
    prev = max_bucket[0]
    for i in range(1, n):
        if min_bucket[i] == math.inf:
            continue  # Пропуск пустого ведра
        max_gap = max(max_gap, min_bucket[i] - prev)
        prev = max_bucket[i]
    return max_gap


if __name__ == "__main__":
    arr = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
    print(maximum_gap(arr))
    # print(maximum_gap_2(arr))
    print(maximum_gap_3(arr))
