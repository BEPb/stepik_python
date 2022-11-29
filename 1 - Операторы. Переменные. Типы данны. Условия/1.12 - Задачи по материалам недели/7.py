"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 7.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Дополнительная
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

'''
a = str(input())

q = int(a[0])
w = int(a[1])
e = int(a[2])
r = int(a[3])
t = int(a[4])
y = int(a[5])

if (q + w + e) == (r + t + y):
    s = "Счастливый"
else:
    s = "Обычный"

print(s)
