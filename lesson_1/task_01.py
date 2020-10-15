"""
поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

greeting = "Добрый день,"
first_name = input("Введите ваше имя\n>>>: ")
surname = input("Введите вашу фамилию\n>>>: ")
age = input("Введите ваш возраст\n>>>: ")
e_mail = input("Введите ваш e-mail\n>>>: ")
phone_number = input("Введите ваш номер телефона\n>>>: ")
message = (
    f"\n{greeting} {first_name.capitalize()} {surname.capitalize()}! \n"
    f"Вы родились в {2020 - int(age)} г. \n"
    f"Ваш e-mail в домене {e_mail.split('@')[1]}\n"
    f"Ваш номер телефона {phone_number}"
)
print(message)
