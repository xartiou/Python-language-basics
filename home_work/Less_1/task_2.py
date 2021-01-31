# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
quantity_sec = int(input("Введите время в секундах "))
hours = quantity_sec // 3600
minutes = (quantity_sec - hours * 3600) // 60
seconds = quantity_sec - (hours * 3600 + minutes * 60)
print(f'Секунды в формате чч:мм:сс   {hours} : {minutes} : {seconds}')