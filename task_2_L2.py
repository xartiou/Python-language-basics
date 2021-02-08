# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


#task_list = [i for i in range(int(input('Сколько элементов списка вы хотите? :')))]

#.append(el) Добавить элемент el в конец списка

task_list = []
el_count = int(input("Введите количество элементов списка "))
i = 0
while i < el_count:
    task_list.append(input("Введите элемент списка ").split())
    i += 1

print(task_list)  # для просмотра списка

for el in range(1, len(task_list), 2):
    task_list[el - 1], task_list[el] = task_list[el], task_list[el - 1]

print(task_list)