#Пункт A.
#Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
def foo(s):
    return s.replace('!', '')
print("Hi! Hello!")
print("")
print(foo("Oh, no!!!"))

#Пункт B.
#Удалите восклицательный знак из конца строки.
def remove(s):
    if s.endswith('!'):
        return s[:-1]
    else:
        return s
print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi"))