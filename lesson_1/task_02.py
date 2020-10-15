"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
seconds = int(input("Ведите время в секундах\n>>> "))
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
