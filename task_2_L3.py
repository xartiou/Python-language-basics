# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# def print_data_user(name, surname, birthday, city, email, phone):
#     return  f'Name - {name}, surname - {surname}, birthday - {birthday}, city - {city},' \
#             f'emai - {email}, phone - {phone}'
#
# print(print_data_user(name = 'Вася', surname = 'Пупкин', birthday = '2001', city = 'Москва', email = 'google@google.ny', phone = '+7 123 456 78 90'))

def print_data_user(**kwargs):
    return ' '.join(kwargs.values())


print(print_data_user(name = input('Введите имя: '), surname = input('Введите фамилию: '), birthday = input('Введите год рождения: '), city = input('Введите ваш город: '), email = input('Введите email: '), phone = input('Введите номер телефона: ')))