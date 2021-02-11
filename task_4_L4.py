# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# f_list = []
# for el in init_list:
#     if init_list.count(el) == 1:
#         f_list.append(el)
# print(f_list)

from random import random

init_list = []
for el in range(20):
    init_list.append(int(random() * 100))
print(init_list)
print()

fin_list = []
for el in init_list:
    if init_list.count(el) == 1:
        fin_list.append(el)
print(fin_list)
