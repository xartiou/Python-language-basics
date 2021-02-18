# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# торого (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# import time

# print('Нужно подождать 5 сек')
# time.sleep(5)
# print('Работает')
# print('А теперь еще ждем', time.sleep(3))
# time.sleep(3)
# print(' Работает')

from time import sleep


class TrafficLight:
    __color = ['Red\n !STOP!', 'Yellow\n !WARNING!', 'Green\n !GO!']

    def running(self):
        print('Внимание на сигнал светофора !')
        sleep(2)
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(2)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
