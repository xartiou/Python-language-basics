# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# my_file = open('set_int.txt', 'w')
# my_file.close()

my_int = input('Введите через пробел числа: ')
my_file = open('set_int.txt', 'w')
my_file.writelines(my_int)

my_file.close()

my_file = open('set_int.txt', 'r', encoding='utf-8')
r_file = my_file.read()
s = r_file.split()
s_i = 0
for i in s:
    s_i += int(i)
print('Сумма чисел файла = ', s_i)

my_file.close()
