# Реализовать класс Road (дорога), в котором определить
# атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
# length, width, thickness, norm_weight, total_weight

class Road:
    _length = None
    _width = None

    def __init__(self, length, width, norm_weight=25, thickness=5):
        self.length = length
        self.width = width
        self.norm_weight = norm_weight
        self.thickness = thickness
        print('Будем строить дорогу.')

    def total_weight(self):
        mass_asf = self.norm_weight * self.thickness / 1000
        total_weight = int(self.length * self.width * mass_asf)
        print(f'Для создания дороги нужно {total_weight} тонн асфальта.')


ratio = Road(5000, 20)
ratio.total_weight()
