# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.
name = 'Masha'
print(name)
print()
name = 'Vladimir'
print(name)
print()
quantity = 15
quantity_1 = quantity + 10
quantity_total = quantity + quantity_1
print(quantity_total)
print()
driver_1 = input('Введите имя: ')
car_1 = int(input('Введите суточный пробег: '))
print(driver_1, 'проехал', car_1, 'км')
car_model = input('Введите марку Вашего авто: ')
mileage_l = (8 / 100) * car_1
print(driver_1, 'на', car_model, 'израсходовал', mileage_l, 'литров бензина.')