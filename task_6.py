# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
start_run = int(input('Введите начальный киллометраж пробежки : '))
print('Каждый день увеличивайте ваш киллометраж на 10%')
finish_run = int(input('Введите максимальный киллометраж пробежки : '))
day_run = 1
while start_run < finish_run:
    start_run = start_run + ((start_run / 100) * 10)
    day_run += 1
print('Вы достигните результата на ', day_run, 'день')