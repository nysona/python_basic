"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# возведение числа в отрицательную степень: 1/x**y

def check(x, y):
    try:
        x = int(x)
        y = int(y)
        if x < 0 or y > 0:
            raise ValueError
    except ValueError:
        return "Ошибка ввода данных"


def exponentiation_simple(x, y):
    if check(x, y):
        return check(x, y)
    return x ** y


def exponentiation_cycle(x, y):
    if check(x, y):
        return check(x, y)
    r = 1
    while (y < 0):
        r *= x
        y += 1
    return 1 / r


def my_func(x, y):
    return exponentiation_cycle(x, y)


print(my_func(2, -4))
