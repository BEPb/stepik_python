"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 4.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

'''
s = 0
f = 1

while f != 0:
    f = int(input())
    s = s + f

print(s)
