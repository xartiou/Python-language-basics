#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# working_hours
# rate_per_hor
# working_bonus
# salary
# salary = (working_hors * rate_per_hor) + working_bonus


def salary(working_hors, rate_per_hor, working_bonus):
    pay = (working_hors * rate_per_hor) + working_bonus
    return pay


print(salary(10, 500, 600))
