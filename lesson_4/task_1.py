"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

Script_name, output_in_hours, rate_in_hour, bonus = argv
output_in_hours = int(output_in_hours)
rate_in_hour = int(rate_in_hour)
bonus = int(bonus)
salary = output_in_hours*rate_in_hour+bonus
print(salary)
