def switch_it_up(number):
    return {
    0: 'Ноль',
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
    5: 'Пять',
    6: 'Шесть',
    7: 'Семь',
    8: 'Восемь',
    9: 'Девять'
    }.get(number, None)
print(switch_it_up())