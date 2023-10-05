from typing import Union, Any
"""2.	Считалочка 
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека. 
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек. 
Для данных N и К дать номер последнего оставшегося человека. """


def last_name(n_people: Union[int, list[Any]], k_number: int) -> list[Any]:
    """
    Функция, которая выбирает победителя по средствам "считалки". На каждой итерации человек, на который указала
    считалочка вылетает. Возвращаем оставшегося победителя.

    :param n_people: Список из людей, может быть как списком, так и целым числом
    :param k_number: Считалка из слогов
    :return: Вывод последнего человека

    >>> people = ["Коля", "Света", "Ольга", "Саша", "Витя"]
    >>> last_name(people, 4)
    ['Света']
    >>> last_name(people, 10)
    ['Ольга']
    """
    if not isinstance(k_number, int):
        raise TypeError("Кол-во слогов в 'считалочке' должно быть целым числом")
    if k_number < 1:
        raise ValueError("Кол-во слогов должно быть больше 0")

    if isinstance(n_people, int):
        if n_people < 1:
            raise ValueError("Список людей должен быть больше 0")
        list_ = [f"Игрок {i + 1}" for i in range(n_people)]
        if len(list_) == 1:
            return list_
    elif isinstance(n_people, list):
        if len(n_people) == 0:
            raise ValueError("Список людей должен быть не пустой")
        list_ = n_people.copy()
        if len(list_) == 1:
            return list_
    else:
        raise TypeError("Список людей должен быть либо список или целое число")

    while len(list_) > 1:
        index = (k_number % len(list_)) - 1
        del list_[index]
    return list_


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
