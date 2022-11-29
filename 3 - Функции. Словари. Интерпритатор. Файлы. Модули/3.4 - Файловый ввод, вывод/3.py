"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 3.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

'''

with open("file3.txt") as inf:
    text_str = inf.readlines()
    text_string = []
    for lines in text_str:
        text_string.append(lines.strip())

rating_list = []
for txt in text_string:
    small_list = txt.split(';')
    for word in small_list:
        if word.isalpha():
            small_list.remove(word)
    rating_list.append(small_list)

m_math, m_rus, m_eng = 0, 0, 0
for i, ii in enumerate(rating_list):
    all_r = 0
    for j, jj in enumerate(ii):
        all_r += int(jj)
    m_all_r = all_r / len(ii)
    print(m_all_r)
    m_math += int(ii[0]) / len(rating_list)
    m_rus += int(ii[1]) / len(rating_list)
    m_eng += int(ii[2]) / len(rating_list)
print(m_math, m_rus, m_eng)
