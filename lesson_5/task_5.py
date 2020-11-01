"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

with open('task_5.txt', 'w') as f:
    for i in range(20):
        f.write(str(randint(-500, 500)) + " ")

with open('task_5.txt', 'r') as f:
    num_sum = sum([int(el) for el in f.read().split()])
    print(f"Сумма чисел = {num_sum}")
