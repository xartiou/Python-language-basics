#  Реализовать базовый класс Worker (работник),
#  в котором определить атрибуты: name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь,
#  содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#  и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных
#  (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    # name
    # surname
    # wage
    # bonus
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    bill = [
        {
            'name': 'Борис',
            'surname': 'Николаев',
            'position': 'Начальник',
            'wage': 75000,
            'bonus': 12000
        },
        {
            'name': 'Василий',
            'surname': 'Лукьянов',
            'position': 'Бухгалтер',
            'wage': 64000,
            'bonus': 26000
        },
        {
            'name': 'Елена',
            'surname': 'Петрова',
            'position': 'Бульдозерист',
            'wage': 90000,
            'bonus': 45000
        },
    ]
    for i in bill:
        data = Position(**i)

        print()
        print(data.position, '- ', data.get_full_name(), data.get_total_income())
