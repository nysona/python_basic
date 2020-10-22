"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(arg_1, arg_2):
    try:
        div = arg_1 / arg_2
    except ZeroDivisionError:
        return 'Деление на ноль невозможно!'
    return div


arg_1 = float(input("Укажите число: "))
arg_2 = float(input("Укажите число: "))
print(division(arg_1, arg_2))
