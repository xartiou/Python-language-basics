# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


from abc import ABC, abstractmethod


class MyKomus:
    goods = []

    @classmethod
    def to_mykomus(cls, device):
        cls.goods.append(device)
        print(device, 'получили на баланс')

    def __str__(self):
        string = '\n'.join(map(str, self.goods))
        return 'Есть в наличии : \n' + string if string else 'Склад пустой.'


class OfficeEquipment(ABC):
    def __init__(self, trademark, model):
        self.trademark = trademark
        self.model = model

    def __str__(self):
        return f'Устройство {self.trademark}{self.model} '

    @abstractmethod
    def to_work(self):
        pass


class Printer(OfficeEquipment):

    def to_work(self):
        print(f'{self.trademark} {self.model} очень быстро печатает.')


class Scanner(OfficeEquipment):

    def to_work(self):
        print(f'{self.trademark} {self.model} очень четко сканирует.')


class Xerox(OfficeEquipment):

    def to_work(self):
        print(f'{self.trademark} {self.model} просто делает копии.')


def main():
    printer = Printer('Ricoh', '150S')
    scanner = Scanner('HP', '205j')
    copier = Xerox('Xerox', 'S-614')
    printer.to_work()
    scanner.to_work()
    copier.to_work()
    print(MyKomus())
    MyKomus.to_mykomus(printer)
    MyKomus.to_mykomus(scanner)
    MyKomus.to_mykomus(copier)
    print(MyKomus())


if __name__ == '__main__':
    main()
