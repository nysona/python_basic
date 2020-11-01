"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator

translator = Translator()
with open("task_4.txt", "r") as f:
    contents = f.read()
    result = translator.translate(contents, dest='ru')
with open('task_4_ru.txt', 'w') as f:
    f.write(result.text)
