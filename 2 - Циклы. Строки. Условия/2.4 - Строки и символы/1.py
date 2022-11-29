"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.

Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов G и C равно 

где 4 -- это количество символов G и C,  а 10 -- это длина строки.

'''

a = str(input())

f = 0

for i in a:
    if i == 'c' or i == 'C' or i == 'G' or i == 'g':
        f += 1

s = (f / len(a)) * 100

print(s)
