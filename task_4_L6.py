# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    auto_count = 0

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if is_police == True:
            print(f'Внимание {self.name} - это полицейская машина')

    def on_start(self):
        print(f'Завели мотор. {self.name}.')

    def on_go(self):
        print(f'Едем на {self.name} скорость {self.speed}')

    def turn(self, direction):
        if direction == 'право':
            print(f'{self.name} Едем на {direction}')
        elif direction == 'лево':
            print(f'{self.name} Едем на {direction}')

    def show_speed(self):
        print(f'{self.name} Ваша скорость {self.speed}')

    def on_stop(self):
        print(f'{self.name} СТОП')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        Car.auto_count += 1

    def show_speed(self):
        if self.speed >= 60:
            print(f'Превышение скорости. Ваша скорость {self.speed}.')
        else:
            print(f'Ваша скорость {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        Car.auto_count += 1


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        Car.auto_count += 1

    def show_speed(self):
        if self.speed >= 40:
            print(f'Превышение скорости. Ваша скорость {self.speed}.')
        else:
            print(f'Ваша скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

        Car.auto_count += 1


maserati = SportCar(100, 'Красный', 'Maserati', False)
gazel = TownCar(70, 'Белый', 'Газель', False)
taxi = WorkCar(50, 'Желтый', 'Mercedes', False)
ford = PoliceCar(110, 'Серый', 'Ford', True)

count_auto = Car.auto_count
print('Мы создали', count_auto, 'авто')

maserati.on_start()
gazel.on_start()
taxi.on_start()
ford.on_start()
maserati.on_go()
gazel.on_go()
taxi.on_go()
ford.on_go()
maserati.turn('лево')
gazel.show_speed()
taxi.show_speed()
ford.turn('право')
maserati.show_speed()
maserati.on_stop()
gazel.on_stop()
taxi.on_stop()
ford.on_stop()
