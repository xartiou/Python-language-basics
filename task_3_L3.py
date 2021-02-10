# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

<<<<<<< HEAD
# def my_func(a, b, c):
#     if a > c and b > c:
#         return a + b
#     elif a > b and c > b:
#         return a + c
#     else:
#         return b + c
#
#
# print(my_func(15, 5, 68))

def my_function(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return 'Enter only numbers!'


print(my_function(10, 15, 8))

# def sum_max(a, b, c):
#     my_list = [a, b, c]
#     try:
#         my_list.remove(min(my_list))
#         return sum(my_list)
#     except TypeError:
#         return 'Enter only numbers!'
#
#
# print(sum_max(88, 99, 200))

# my_function = lambda a, b, c: sum(sorted([a, b, c])[1:])
#
# print(my_function(1978,2,1))
=======
def my_func(a, b, c):
    if a > c and b > c:
        return a + b
    elif a > b and c > b:
        return a + c
    else:
        return b + c


print(my_func(15, 5, 68))
>>>>>>> less_3
