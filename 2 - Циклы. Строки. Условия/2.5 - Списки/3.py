"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 3.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. 

'''

string = input()

list_spring = string.split()
summa = 0

for i in list_spring:
    summa += int(i)

print(summa)
