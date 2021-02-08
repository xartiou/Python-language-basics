# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a > c and b > c:
        return a + b
    elif a > b and c > b:
        return a + c
    else:
        return b + c


print(my_func(15, 5, 68))