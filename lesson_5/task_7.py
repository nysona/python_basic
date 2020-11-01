"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

firms = {}
profits = {}
with open("task_7.txt", "r") as f:
    for line in f:
        comp_name = str(line.split()[1] + " " + line.split()[0])
        profit = int(line.split()[2]) - int(line.split()[3])
        firms[comp_name] = profit
tmp_profit = [profit for profit in firms.values() if profit > 0]
profits["average_profit"] = int(sum(tmp_profit) / len(tmp_profit))
firms_profit_list = [firms, profits]
print(firms_profit_list)

with open("task_7.json", "w", encoding='utf8') as write_f:
    json.dump(firms_profit_list, write_f, ensure_ascii=False)
