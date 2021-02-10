# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

# def my_func():
#     summ = 0
#     in_list = input('Введите числа через пробел, для выхода нажмите Q : ').upper().split()
#     for i in in_list:
#         if i == 'Q':
#             return summ, True
#         try:
#             summ += int(i)
#         except ValueError:
#             pass
#         return summ, False
#
#
# result = 0
# while True:
#     a, b = my_func()
#     result += a
#     print(result)
#     if b:
#         break


def summarize():
    s = 0
    while True:
        in_list = input('Введите числа через пробел, для выхода нажмите Q : ').upper().split()
        for i in in_list:
            if i == 'Q':
                print(s)
                break
            try:
                s += float(i)
            except ValueError:
                print(f'Значение {i} не было учтено при подсчете суммы т.к неверный тип')
        else:
            #если не завершили через Q , продолжаем ввод
            print(s)
            continue
        break
    return s
summarize()