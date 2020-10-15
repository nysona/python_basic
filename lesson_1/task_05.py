"""
 Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
 или убыток — издержки больше выручки).
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = int(input("Выручка фирмы:\n>"))
expenses = int(input("Издержки фирмы:\n>"))

if proceeds > expenses:
    profit = proceeds - expenses
    profit_margin = profit / proceeds
    print("Ваша фирма работает с прибылью")
    print("Рентабельность вашей фирмы составляет", profit_margin)
    number_of_staff = int(input("сколько сотрудников в вашей фирме?:\n>"))
    profit_per_pax = profit / number_of_staff
    print("Прибыль фирмы на одного сотрудника составляет - ", profit_per_pax)
else:
    print("Ваша фирма работает с убытками")
