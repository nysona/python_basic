"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_f = open("task_3.txt", "r")
content = my_f.readlines()

staff_with_low_salary = [el.split()[0] for el in content if int(el.split()[1]) < 20000]
salary_list = [int(el.split()[1]) for el in content]
average_income_of_employees = round(sum(salary_list) / len(salary_list), 2)

print(f"Cотрудники с окладом менее 20 тыс: {', '.join(staff_with_low_salary)}")
print(f"Средний доход сотрудников: {average_income_of_employees} руб.")

my_f.close()
