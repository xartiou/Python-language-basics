# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


file = open('file_task2.txt', encoding='utf-8')

line = 0
for i in file:
    line += 1
    words = i.split()
    count_w = 0
    for w in words:
        count_w += 1
    print(line, 'строка содержит', count_w, 'слов')

print('Итого ', line, 'строки.')
file.close()
