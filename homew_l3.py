'''Задание 7
* Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
* Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
* Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
Усложнённое ** (можно сначала его не делать):
* Посчитать, сколько раз встречается каждое слово.
(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)'''

def restruct_text(x):
    x = x.split()
    keys_tosort = []
    for i in x:
        i = (i.strip(",!()'.?")).upper()
        keys_tosort.append(i)
    return sorted(keys_tosort)
def create_dict(keys):
    keys_sorted=restruct_text(keys)
    dict_article = {}
    for i in keys_sorted:
        if i not in (",","(",")","?",".","!"):
            dict_article[i]=dict_article.get(i,0)+1
    return dict_article

article='''We are not what we should be!
We are not what we  we we we need to be be. be
be But at least we are not what we used to be
(Football Coach)'''
m=create_dict(article)
print(m)