"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import (
    count,
    cycle,
)
from sys import argv

file_name, star_el, end_el, step = argv
star_el = int(star_el)
end_el = int(end_el)
step = int(step)
my_list = []

for el in count(star_el, step):
    if el > end_el:
        break
    else:
        print(el)
        my_list.append(el)

сcl = 0
for el in cycle(my_list):
    if сcl > end_el - 1:
        break
    print("-", el)
    сcl += 1
