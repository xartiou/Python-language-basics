# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

tip_int = 25
tip_float = 36.6
tip_complex = complex(12, 24)
tip_str = 'вот такая строка'
tip_list = ['ordinary list']
tip_tuple = ('3', 'февраля')
tip_set = {'parampampam'}
tip_dict = {'day': 'sunday', 'months': 'june'}
tip_bool = True
tip_none = None

task_list = [tip_int, tip_float, tip_complex, tip_str, tip_list, tip_tuple, tip_set, tip_dict, tip_bool, tip_none]
for i in task_list:
    print(f'{i} is {type(i)}')