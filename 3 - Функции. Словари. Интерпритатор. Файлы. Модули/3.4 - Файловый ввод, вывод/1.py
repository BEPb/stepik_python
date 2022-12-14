"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.


'''

with open("file.txt") as inf:
    text_string = inf.readline()

int_num = ""
list_int_num = []

short_str = ""
list_short_str = []

output_text = ""

# Поиск чисел и отдельных символов:
for char in text_string:
    if char.isdigit():
        int_num += char
    else:
        if int_num != "":
            list_int_num.append(int(int_num))
            int_num = ""
        list_short_str.append(char)

if int_num != "":
    list_int_num.append(int(int_num))


for i, ii in enumerate(list_int_num):
    for x in range(int(ii)):
        output_text += list_short_str[i]

print(output_text)
