# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


# Реализовать класс «Дата»
class MyData(object):
    def __init__(self, calendar_day):
        self.calendar_day = str(calendar_day)

    # В рамках класса реализовать два метода.
    # должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    @classmethod
    def extract(cls, calendar_day):
        may_data = []
        for el in calendar_day.split():
            if el != '-':
                may_data.append(el)
        return int(may_data[0]), int(may_data[1]), int(may_data[2])

    # должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 3073:
                    return f'Хороший денек!'
                else:
                    return f'Ввели неправильный год'
            else:
                return f'Ввели неправильный месяц'
        else:
            return f'Ввели неправильный день'

    def __str__(self):
        return f'Вы ввели дату {MyData.extract(self.calendar_day)}'


d_1 = MyData('27 - 02 - 2021')
print(d_1)
print(MyData.valid(37, 11, 2022))
print(MyData.valid(25, 16, 2022))
print(MyData.extract('01 - 03 - 2021'))
print(d_1.extract('17 - 05 - 2021'))
