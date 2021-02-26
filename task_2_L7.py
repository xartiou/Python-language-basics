# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from typing import Any


class Clothes:
    _clothes = []

    def __init__(self, parametr: Any):  # общие параметры
        self._parametr = parametr
        self._expense = None
        self._clothes.append(self)

    def _calc_expense(self):
        raise NotImplemented

    @property
    def expense(self) -> float:
        if not self._expense:
            self._calc_expense()
        return self._expense

    @property
    def parametr(self) -> Any:
        return self._parametr

    @parametr.setter
    def parametr(self, parametr: Any):
        self._parametr = parametr
        self._expense = None

    @property
    def total_expense(self):
        return f'Всего понадобится {sum([item.expense for item in self._clothes])}кв. метров ткани'


class Coat(Clothes):

    def _calc_expense(self):
        self._expense = round(self.parametr / 6.5 + 0.5, 2)

    @property
    def Size(self) -> Any:
        return self.parametr

    @Size.setter
    def Size(self, size: Any):
        self.parametr = size

    def __str__(self):
        return f"Для пошива пальто {self.parametr} размера " \
               f"требуется {self.expense} кв. метров ткани"


class Suit(Clothes):

    def _calc_expense(self):
        self._expense = round(2 * self.parametr * 0.01 + 0.3, 2)  # 0.01 чтобы выводить в метрах(т.к. рост в см.)

    @property
    def Height(self) -> Any:
        return self.parametr

    @Height.setter
    def Height(self, height: Any):
        self.parametr = height

    def __str__(self):
        return f"Для костюма на рост {self.parametr} см. " \
               f"требуется {self.expense} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat(48)
    # print(coat)
    coat.Size = 50
    print(coat)

    suit = Suit(178)
    # print(suit)
    suit.Height = 182
    print(suit)

    print(suit.total_expense)
