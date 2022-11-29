"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 2.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

'''

def f(x):
    ff = 0
    if x <= -2:
        ff = 1 - (x + 2) ** 2

    elif -2 < x <= 2:
        ff = (x / 2) * -1

    elif x > 2:
        ff = (x - 2) ** 2 + 1

    return ff
