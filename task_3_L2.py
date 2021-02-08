# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = [
    ['Зима-валенки', ['12', '1', '2']],
    ['Весна-сапоги', ['3', '4', '5']],
    ['Лето-сандали', ['6', '7', '8']],
    ['Осень-', ['9', '10', '11']]
]

season_dict = {
    'Зима-лыжи': ['12', '1', '2'],
    'Весна-лодка': ['3', '4', '5'],
    'Лето-велосипед': ['6', '7', '8'],
    'Осень-трактор': ['9', '10', '11']
}

while True:
    month_num = input('Пожалуйста введите номер месяца: ')
    if month_num not in sum(season_dict.values(), []):
        print('В году 12 месяцев. Попробуйте еще раз')
        continue
    break

for season, months in season_list:
    if month_num in months:
        print(f'Месяц с номером {month_num} это {season}')

for season, months in season_dict.items():  # функция с доступом по ключу
    if month_num in months:
        print(f'Месяц с номером {month_num} это {season}')