"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 4.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

'''

string = input()

list_spring = string.split()
len_list = len(list_spring) - 1
new_list = []
new_string = ""

if len_list > 0:
    for i in range(len_list):
        if i == 0:
            new_list.append(int(list_spring[len_list]) + int(list_spring[i+1]))
        else:
            new_list.append(int(list_spring[i-1]) + int(list_spring[i+1]))

    new_list.append(int(list_spring[len_list - 1]) + int(list_spring[0]))
    for j in range(len_list+1):
        if j == 0:
            new_string += str(new_list[j])
        else:
            new_string += ' ' + str(new_list[j])
else:
    new_list.append(int(list_spring[0]))
    new_string = str(list_spring[0])

print(new_string)
