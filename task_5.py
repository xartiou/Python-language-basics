#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
val_profit = int(input('Введите сумму выручки фирмы : '))
spending = int(input('Введите сумму издержек фирмы : '))
profit = val_profit - spending
if val_profit > spending:
    rentability = profit * 100 / val_profit
    print('OK, profitable')
    print('Рентабельность : ', rentability, '%')
    quant_workers = int(input('Введите количество сотрудников : '))
    profit_workers = profit / quant_workers
    print('Каждый сотрудник принес прибыли : ', profit_workers)
else:
    print('No good')