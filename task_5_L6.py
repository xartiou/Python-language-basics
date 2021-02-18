#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def drawning(self):
        print(f'Запуск отрисовки.')
        print(f'Рисует {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawning(self):
        print(f'Рисует {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawning(self):
        print(f'Рисует {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawning(self):
        print(f'Рисует {self.title}')


p = Pen('pen')
pl = Pencil('pencil')
hl = Handle('handle')
br = Stationery('brush')
p.drawning()
pl.drawning()
hl.drawning()
br.drawning()
