# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

<<<<<<< HEAD
# word = input('Введите слово маленькими латинскими буквами : ')
#
# def int_func(word):
#     word = word.title()
#     return word
#
#
# print(int_func(word))
#
# string = input().split()
# res_string = []
#
# for word in string:
#     res_string.append(int_func(word))  # добавляем нашу функцию
# print(' '.join(res_string))  # возвращаем строку

def int_func(word):
    return word[0].upper() + word[1:].lower()


s = input().split()
for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('error!')
    else:
        s[i] = int_func(word)
print(' '.join(s))

# def int_func():
#     for word in input('Enter words with a space (lower latin script):\n').split():
#         chars = 0
#         for char in word:
#             if 97 <= ord(char) <= 122:
#                 chars += 1
#             print(word.title() if chars == len(word) else f"{word} - only small latin letters!")
#
# int_func()
=======
word = input('Введите слово маленькими латинскими буквами : ')


def int_func(word):
    word = word.title()
    return word


print(int_func(word))

string = input().split()
res_string = []

for word in string:
    res_string.append(int_func(word))  # добавляем нашу функцию
print(' '.join(res_string))  # возвращаем строку
>>>>>>> less_3
