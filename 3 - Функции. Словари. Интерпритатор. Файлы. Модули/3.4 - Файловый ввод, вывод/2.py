"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

'''

with open("file2.txt") as inf:
    text_str = inf.readlines()
    text_string = ""
    for lines in text_str:
        text_string += lines.strip() + " "

new_list = []
new_word = ""
max_count = 0

# Перевод слов в список:
for char in text_string:
    if char != " ":
        new_word += char
    else:
        new_list.append(new_word.lower())
        new_word = ""

if new_word != "":
    new_list.append(new_word.lower())

max_word = new_list[0]

for word in new_list:
    if new_list.count(word) >= max_count:
        max_count = new_list.count(word)
        if len(word) < len(max_word):
            max_word = word

print(max_word, max_count)
