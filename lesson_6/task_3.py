"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 20000, "bonus": 5000}


class Position(Worker):
    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_total_income(self):
        return sum([el for el in self._income.values()])


worker_1 = Worker()
worker_1.position = Position()
director = Position()
director.name = "Анна"
director.surname = "Мельникова"
worker_1._Worker__income = {"wage": 10000, "bonus": 1000}

print(director.get_full_name())
print(director.get_total_income())
