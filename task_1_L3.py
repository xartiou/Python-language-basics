# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

<<<<<<< HEAD
# def quotient():
#     a = int(input('Введите делимое: '))
#     b = int(input('Введите делитель: '))
#     if b == 0:
#         b = int(input('На "0" делить нельзя. Введите делитель: '))
#     return (a / b)
#
# print(quotient())

def quotient(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('Devision by zero is forbiden') # Деление на ноль запрещено
    except ValueError:
        print('You should enter integers') # Вы должны ввести целые числа

print(quotient(input('Введите делимое: '), input('Введите делитель: ')))
=======
def quotient():
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        b = int(input('На "0" делить нельзя. Введите делитель: '))
    return (a / b)

print(quotient())
>>>>>>> less_3
