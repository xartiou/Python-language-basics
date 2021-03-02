# Продолжить работу над  заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod


class MyKomus:
    goods = {'Printer': [], 'Scanner': [], 'Xerox': []}
    user_goods = {'Printer': [], 'Scanner': [], 'Xerox': []}

    @classmethod
    def to_mykomus(cls, *devices, from_user=False):
        if not from_user:
            for device in devices:
                cls.goods[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')
        else:
            for device in devices:
                cls.user_goods[str(device.__class__.__name__)].remove(device)
                cls.goods[str(device.__class__.__name__)].append(device)
                print(device, 'Принято на склад.')

    @classmethod
    def from_mykomus(cls, device):
        cls.goods[str(device.__class__.__name__)].remove(device)
        cls.user_goods[str(device.__class__.__name__)].append(device)
        print(device, 'Передано со склада.')

    def __str__(self):
        string_mykomus = '\n'.join(map(str, (sum(self.goods.values(), []))))
        string_mykomus = 'Устройства на складе:\n' + string_mykomus if string_mykomus else 'На складе нет устройств'
        string_user = '\n'.join(map(str, (sum(self.user_goods.values(), []))))
        string_user = 'Устройства у пользователей:\n' + string_user if string_user else 'У пользователей устройств'
        return string_mykomus + '\n' + string_user


class OfficeEquipment(ABC):
    def __init__(self, trademark, position, manager='зав.складом'):
        self.trademark = trademark
        self.position = position
        self._manager = manager

    def __str__(self):
        return f'Устройство {self.trademark}, номер - {self.position}, ответственный {self._manager}.'

    def change_manager(self, manager='зав.складом'):
        print(f'Устройство {self.trademark} переписано с {self._manager} на {manager}.')
        self._manager = manager
        if self._manager == 'зав.складом':
            MyKomus.to_mykomus(self, from_user=True)
        else:
            MyKomus.from_mykomus(self)

    @classmethod
    def count_devices(cls, device='All'):
        if str(device) == 'All':
            string_mykomus = {key: len(value) for key, value in MyKomus.goods.items()}
            string_user = {key: len(value) for key, value in MyKomus.user_goods.items()}
        else:
            string_mykomus = {device: len(MyKomus.goods[device])}
            string_user = {device: len(MyKomus.user_goods[device])}
        string_mykomus = 'Устройства на складе:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_mykomus.items()) + '\nИтого: ' + str(
            sum(string_mykomus.values()))
        string_user = 'Устройства у пользователей:\n' + '\n'.join(
            '{}: {}'.format(key, value) for key, value in string_user.items()) + '\nИтого: ' + str(
            sum(string_user.values()))
        return string_mykomus + '\n' + string_user

    @abstractmethod
    def to_work(self):
        return f'Устройство {self.trademark}, номер - {self.position}, есть на складе.'


class Printer(OfficeEquipment):

    def to_work(self):
        if self._manager == 'зав.складом':
            super().to_work()
        else:
            print('Устройство печатает.')

    @classmethod
    def count_devices(cls, device='Printer'):
        return super().count_devices(device)


class Scanner(OfficeEquipment):

    def to_work(self):
        if self._manager == 'зав.складом':
            super().to_work()
        else:
            print('Устройство сканирует.')

    @classmethod
    def count_devices(cls, device='Scanner'):
        return super().count_devices(device)


class Xerox(OfficeEquipment):

    def to_work(self):
        if self._manager == 'зав.складом':
            super().to_work()
        else:
            print('Устройство копирует.')

    @classmethod
    def count_devices(cls, device='Xerox'):
        return super().count_devices(device)


def main():
    print(MyKomus())
    printer = Printer('Ricoh', 101)
    scanner = Scanner('HP', 102)
    copier = Xerox('Xerox', 103)
    printer_2 = Printer('Canon', 104)
    print()
    copier.to_work()
    print()
    MyKomus.to_mykomus(printer, scanner, copier, printer_2)
    print()
    print(MyKomus())
    print()
    printer.change_manager('Антонов С')
    print()
    print(MyKomus())
    print()
    copier.change_manager('Петров В')
    print()
    copier.to_work()
    print()
    printer.change_manager()
    print()
    print(MyKomus())
    print()
    print(OfficeEquipment.count_devices())
    print('zzzzzzzzzzzzzzzzzzzzzzzzzz')
    print(printer.count_devices())


if __name__ == '__main__':
    main()
