# Реализовать класс Matrix (матрица). 
# Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() 
# для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# Подсказка:  сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем 
# с первым элементом первой строки второй матрицы и т.д.

from random import randint
from typing import List


# подсказки
# line = int(input('Введите количество строк матрицы : '))
# column = int(input('Введите количество столбцов матрицы : '))
# map(function, iterable, ...) Вернуть итератор, который применяет функцию к каждому элементу итерации
# join(iterable) Return a string
# '\t' item
# '\n' str

class Matrix:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.matrix = [[0] * column for i in range(line)]
        for i in range(line):
            for j in range(column):
                self.matrix[i][j] = randint(1, 9)

    def __add__(self, other):
        result = []
        for item in zip(self.matrix, other.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])
        return '\n'.join(['\t'.join(map(str, row)) for row in result])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


a = Matrix(3, 3)
print(a)
print('*****')
b = Matrix(3, 3)
print(b)
print('*****')
print(a + b)
