# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
numerated = []

file = open('text_4.txt', encoding='utf-8')

for i in file:
    el = i.split(' - ')
    if el[0] in translate_dict:
        rus = translate_dict[el[0]]
        numerated.append(rus + ' - ' + el[1])

file.close()

my_file = open('text_4.txt', 'w', encoding='utf-8')

my_file.writelines(numerated)


my_file.close()
