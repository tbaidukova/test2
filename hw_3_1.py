'''Задание 1
Входные данные
Пользователь вводит строку.
Выходные данные
Воспользуйтесь одним print(), но при этом выводите с новой строки:
* Сначала выведите третий символ этой строки.
* Во второй строке выведите предпоследний символ этой строки.
* В третьей строке выведите первые пять символов этой строки.
* В четвертой строке выведите всю строку, кроме последних двух символов.
* В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся, начиная с первого).
* В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
* В седьмой строке выведите все символы в обратном порядке.
* В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
* В девятой строке выведите все символы в обратном порядке без первого и последнего элемента.
* В десятой строке выведите длину данной строки.
PS: Выловите исключения, если введённая строка слишком короткая. Какого типа исключение надо выловить?'''
x=[1,2,3,4,5,6,7,8,9,10,11]
print(x[2],x[-2],x[0:5],x[:-2],x[::2],x[1::2],x[1::2],x[::-1],x[::-2],x[(len(x)-2):0:-1],len(x),sep='\n')