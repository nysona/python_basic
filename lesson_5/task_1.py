"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("some.txt", "w")
print("Ведите данные")

while True:
    user_data = input()
    if user_data:
        my_file.writelines(user_data + '\n')
    else:
        break
my_file.close()
