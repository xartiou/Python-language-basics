# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# https://docs.python.org/3/
# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.


my_file = open('text_6.txt', 'r', encoding='utf-8')
content_file = my_file.readlines()
# print(content_file) # для посмотреть

my_dict = {}
for i in content_file:
    content_list = i.replace('(', ' ').split()
    # print(content_list) # для посмотреть
    my_dict[content_list[0]] = sum(
        int(j) for j in content_list if j.isdigit()
    )
print(my_dict)

my_file.close()
