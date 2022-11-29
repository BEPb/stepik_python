"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 2.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Сколько итераций цикла будет выполнено в этом фрагменте программы?
'''
i = 0
num_iter = 0
while i <= 10:
    i = i + 1
    num_iter +=1
    if i > 7:
        i = i + 2

print(num_iter)
# Ответ:
# 9