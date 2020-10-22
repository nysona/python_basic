"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

summa = 0


def my_sort(*args):
    sorted_list = []
    user_list = list(args)
    for _ in args:
        maximum = 0
        for value in user_list:
            if value > maximum:
                maximum = value
        user_list.remove(maximum)
        sorted_list.append(maximum)
    return sorted_list


def my_sum(*args):
    global summa
    for el in args:
        x = int(el)
        summa += x
    return summa


def my_func(a, b, c):
    srt = my_sort(a, b, c)
    summ = my_sum(srt[0], srt[1])
    return summ


print(my_func(3, 1, 2))
