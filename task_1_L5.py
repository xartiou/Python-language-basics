# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# file = input('Файл: ')

file = "new_file.txt"

f = open(file, 'w')
while True:
    s = input('Введите данные файла : ')
    if s == '':
        break
    f.write(s + '\n')
print('Ввод окончен, данные записаны в файл.')
f.close()

#
# while True:
#     data_input = input('Введите данные файла построчно : ')
#     if not data_input:
#         print('Ввод окончен, данные записаны в файл.')
#         break
#
#     try:
#         with open(file, 'w', encoding='utf-8') as fl:
#             fl.write(f'{data_input}\n')
#     except IOError as err:
#         print(err)
#         break
