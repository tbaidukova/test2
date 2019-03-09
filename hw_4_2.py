'''Задание 2
Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
Учитываем, что может быть повторяющиеся значения аргументов.'''

def premax_value(*args):
    mx=0.0
    premx=0.0
    for i in args:
        if float(i)>mx:
            premx=mx
            mx=float(i)
        elif float(i)<mx and float(i)>=premx:
            premx=float(i)
        else:
            pass
        print(mx,premx)
    return premx

print(premax_value(10,9,55.5,55.5,3,8,8,8,55.4))