"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self._queue = deque()

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди с учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        if not isinstance(priority, int):
            raise TypeError("Приоритет должен быть целым числом")
        if not self.HIGH_PRIORITY <= priority <= self.LOW_PRIORITY:
            raise ValueError("Приоритет должен быть от 0 до 10 включительно")
        for index, item in enumerate(self._queue):
            if item[0] <= priority:
                self._queue.insert(index, (priority, elem))
                break
        else:
            self._queue.append((priority, elem))

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self._queue) == 0:
            raise IndexError("Очередь пуста")
        return self._queue.pop()[1]

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: Индекс элемента (отсчет с начала,
        0 - первый с начала элемент в очереди,
        1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)

        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if len(self._queue) == 0:
            raise IndexError("Очередь пуста")
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целым числом")
        if not -1 < ind < len(self._queue):
            raise ValueError(f"Индекс должен быть от 0 до {len(self._queue) - 1} включительно")

        counter = -1
        deq = self._queue.copy()
        deq.reverse()
        for value in deq:
            if value[0] == priority:
                counter += 1
            if counter == ind:
                return value[1]

    def clear(self) -> None:
        """ Очистка очереди. """
        self._queue.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._queue)
