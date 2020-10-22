"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().
"""


def check(a):
    try:
        if a.islower() is False or a.isalpha() is False:
            raise ValueError
    except ValueError:
        return "Ошибка ввода данных"


def int_func(a):
    if check(a):
        return check(a)
    return (str(a.capitalize()))


print(int_func("hello"))

string = "i love python".split(" ")
string_up = []
for el in string:
    if check(el):
        check(el)
    string_up.append(int_func(el))
print(' '.join(string_up))
