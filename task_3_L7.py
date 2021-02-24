# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.


class Cells:
    def __init__(self, count):
        self._count = count

    def __add__(self, other: 'Cells') -> 'Cells':
        return Cells(self._count + other._count)

    def __sub__(self, other: 'Cells') -> 'Cells':
        if self._count > other._count:
            return Cells(self._count - other._count)
        print(f'Операция невозможна')

    def __mul__(self, other: 'Cells') -> 'Cells':
        return Cells(self._count * other._count)

    def __truediv__(self, other: 'Cells') -> 'Cells':
        return Cells(self._count // other._count)

    def make_order(self, count_sell: int) -> str:
        rows, rest = self._count // count_sell, self._count % count_sell
        return '\n'.join(['*' * count_sell] * rows + (['*' * rest] if rest else []))

    def __str__(self) -> str:
        return f"Общее количество: {self._count} кл."


if __name__ == '__main__':
    cell_1 = Cells(17)
    # print(c1)
    cell_2 = Cells(15)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print()
    print(cell_2 - cell_1)
    print(cell_2 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 / cell_2)
    print()
    print((cell_1 + cell_2).make_order(5))
