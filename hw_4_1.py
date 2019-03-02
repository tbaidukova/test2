'''Задание 1. Со значениями по умолчанию
Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка,
если 1, то в конце стоит «!». По умолчанию 0'''
def song_generator(row_q=3,La_q=3,punctuation=0):
    row_constructor=''
    for i in range(1,La_q+1):
        row_constructor+='La-' if i<La_q else 'La'
    punct_constructor='.' if punctuation==0 else '!' if punctuation==1 else '.'
    song_constructor=(row_constructor+'\n\r')*(row_q-1)+row_constructor+punct_constructor
    return song_constructor

k=song_generator(5,2,1)
print(k)
