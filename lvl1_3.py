# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
months = [
    ['Январь', 31],
    ['Февраль', 28],
    ['Март', 31],
    ['Апрель', 30],
    ['Май', 31],
    ['Июнь', 30],
    ['Июль', 31],
    ['Август', 31],
    ['Сентябрь', 30],
    ['Октябрь', 31],
    ['Ноябрь', 30],
    ['Декабрь', 31],
]
print("Ввидите номер месяца")
choise = int(input())-1
if choise > 12 or choise < 0 :
    print('Номер месяца некорректен')
else:
    print(f"В месяце {months[choise][0]} {months[choise][1]} дней")