# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        real_unit = ComplexNumber.parsing_number(self.number)[0] + ComplexNumber.parsing_number(other.number)[0]
        imaginary_unit = ComplexNumber.parsing_number(self.number)[1] + ComplexNumber.parsing_number(other.number)[1]
        return ComplexNumber(
            str(real_unit) + '+' + str(imaginary_unit) + 'i' if imaginary_unit >= 0 else str(real_unit) + str(
                imaginary_unit) + 'i')

    def __mul__(self, other):
        x1, y1 = ComplexNumber.parsing_number(self.number)
        x2, y2 = ComplexNumber.parsing_number(other.number)
        real_unit = x1 * x2 - y1 * y2
        imaginary_unit = x1 * y2 + x2 * y1
        return ComplexNumber(
            str(real_unit) + '+' + str(imaginary_unit) + 'i' if imaginary_unit >= 0 else str(real_unit) + str(
                imaginary_unit) + 'i')

    def __str__(self):
        return self.number

    @staticmethod
    def parsing_number(number):
        number = number[:-1:]
        if '+' in number:
            new_number = number.split('+')
        else:
            new_number = number.split('-')
            if number[0] == '-':
                new_number.pop(0)
                new_number[0] = '-' + new_number[0]
            new_number[1] = '-' + new_number[1]
        return tuple(map(int, new_number))


def main():
    number_1 = ComplexNumber('-5+3i')
    number_2 = ComplexNumber('-2+4i')
    print(number_1 + number_2)
    print(number_1 * number_2)


if __name__ == '__main__':
    main()
