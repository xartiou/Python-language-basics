# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

py_file = 'text_7.txt'
# name_firm
# form_firm
# deb_firm
# kr_firm
# setdefault - Если ключ находится в словаре, вернет его значение.
# Если нет, вставит ключ со значением по умолчанию и вернет значение по умолчанию
# . по умолчанию - None.
# round - округляет
# update - обновляем ключи
profit = {}
profitable = {}
sum_profit = 0
aver_profit = 0
i = 0

with open(py_file, encoding='utf-8') as file_head:
    for line in file_head:
        name_firm, form_firm, deb_firm, kr_firm = line.split()
        profit[name_firm] = int(deb_firm) - int(kr_firm)
        if profit.setdefault(name_firm) >= 0:
            sum_profit = sum_profit + profit.setdefault(name_firm)
            i += 1
    if i != 0:
        aver_profit = sum_profit / i
    else:
        print(f'Нет прибыли')

    profitable = {'Average profit': round(aver_profit)}

    # print(profit)
    # print(profitable)
total_profit = [profit, profitable]
#print(total_profit)

with open('text_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(total_profit, write_js, ensure_ascii=False)

    js_str = json.dumps(total_profit)
    new_js_str = json.loads(js_str)

    #print(new_js_str)
