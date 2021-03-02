# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

# Создайте собственный класс
class MyDivisionByNull:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    # обрабатывающий ситуацию деления на нуль
    @staticmethod
    def division_by_zerro(dividend, divisor):
        try:
            return dividend / divisor
        except:
            return f'На ноль делить низзя'


d_1 = MyDivisionByNull(8, 4)
print(d_1.division_by_zerro(4, 0))
