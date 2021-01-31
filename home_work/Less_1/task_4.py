#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = int(input('Введите положительное число: '))
num_max = 0
while user_number > 0:
    last_num = user_number % 10
    if last_num > num_max:
        num_max = last_num
    user_number = user_number // 10
print('Самая большая цифра в числе - ', num_max)
