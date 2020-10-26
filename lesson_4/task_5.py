"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


# from functools import reduce

def my_range(start, end, step=1):
    my_list = []
    while start <= end:
        my_list.append(start)
        start += step
    return my_list


def my_reduce(func, seq, default=None):
    it = iter(seq)
    x = next(it) if default is None else default
    for y in it:
        x = func(x, y)
    return x


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in my_range(1, 20) if not el & 1]
print(my_reduce(my_func, my_list))
