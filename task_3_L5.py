# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
file = open('text_3.txt', encoding='utf-8')
count_empl = 0
summa_salary = 0
for line in file:
    count_empl += 1
    bill = line.split()
    if bill[1] < '20000':
        print(bill[0], 'имеет зарплату менее 20 тыс.р.')
    summa_salary += float(bill[1])

print('Средняя зарплата сотрудников = ', summa_salary / count_empl, 'р.')
file.close()
