# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Нужно только действительные и целые числа')
        return
    if x <= 0 or y >= 0:
        print('Х - должен быть положительный, а Y - отрицательный')
        return
    return x ** y

print(my_func(10, -4))