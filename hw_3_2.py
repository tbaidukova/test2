'''Задание 2
Пользователь вводит строку. Разрежьте её на две равные части (если длина строки — чётная,
а если длина строки нечётная, то длина первой части должна быть на один символ больше).
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.'''
def my_f(x):
    n=int(len(x))
    hn=int(n/2)
    l= x[hn:(n)]+x[0:hn] if n%2==0 else x[hn+1:(n)]+x[0:hn+1]
    return l
k=input('Pls, input str')
print(my_f(k))