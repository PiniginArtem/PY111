"""
1.
Оценить асимптотическую сложность приведенного ниже алгоритма:
"""


a = len(arr) - 1  # O(1)
out = list()  # O(1) Для создания пустого листа
while a > 0:  # O(log(N)) т.к. а кратно уменьшается от целочисленного деления
    out.append(arr[a])  # O(1) т.к. обращение по индексу и присвоение - O(1) + O(1) = O(1)
    a = a // 1.7  # O(1) для алгебраических вычислений
out.merge_sort()  # O(N * log(N)) сортировка слиянием, работающая за фиксированную сложность

# Итоговая сложность алгоритма O(N * log(N))