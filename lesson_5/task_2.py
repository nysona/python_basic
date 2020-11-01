"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open("task_2.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))

for index, value in enumerate(lines):
    number_of_words = len(value.split())
    print(f'В строке {index + 1} содержится {number_of_words} слов.\n')
