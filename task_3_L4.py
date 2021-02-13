# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

int_list = list(range(20, 240))
# print(int_list)
new_int_list = []
for i in int_list:
    if i % 20 == 0 or i % 21 == 0:
        new_int_list.append(i)
print(new_int_list)
