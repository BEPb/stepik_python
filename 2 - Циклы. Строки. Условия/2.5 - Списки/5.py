"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 5.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

'''

string = input()

list_string = sorted(string.split())
new = []
out_str = ""

for i in list_string:
    if list_string.count(i) >= 2:
        while list_string.count(i) >= 3:
            list_string.remove(i)
        list_string.remove(i)
        new.append(i)

for j in range(int(len(new))):
    if j != 0:
        out_str += " " + new[j]
    else:
        out_str += new[j]

if len(out_str) >= 1:
    print(out_str)
