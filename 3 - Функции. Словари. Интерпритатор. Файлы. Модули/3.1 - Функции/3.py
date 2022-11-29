"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 3.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

'''

def modify_list(l):
    a = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            l[i] //= 2
            a.append(l[i])
    del l[:]
    for i in range(len(a)):
        l.append(a[i])

lst = [1, 2, 3, 4, 5, 6]
#print(modify_list(lst))  # None
#print(lst)               # [1, 2, 3]
modify_list(lst)
#print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
#print(lst)               # [5, 4]
