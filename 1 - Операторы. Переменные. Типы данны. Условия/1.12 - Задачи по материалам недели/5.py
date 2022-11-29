"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 5.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три
строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

'''
a = int(input())
b = int(input())
c = int(input())

if a == b and (a > c or b > c):
    ma = a
    sr = b
    mi = c

elif a == c and (a > b or c > b):
    ma = a
    sr = c
    mi = b

elif c == b and (c > a or b > c):
    ma = c
    sr = b
    mi = a
    
elif a == b and c == b:
    ma = a
    sr = b
    mi = c

elif a > b and a > c:
    ma = a
    if b > c:
        sr = b
        mi = c
    else:
        sr = c
        mi = b

elif b > a and b > c:
    ma = b
    if a > c:
        sr = a
        mi = c
    else:
        sr = c
        mi = a

elif c > a and c > b:
    ma = c
    if a > b:
        sr = a
        mi = b
    else:
        sr = b
        mi = a

print(ma)
print(mi)
print(sr)
