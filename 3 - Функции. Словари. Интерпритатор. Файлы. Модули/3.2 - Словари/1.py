"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

'''

def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif key * 2 in d.keys():
        d[key * 2].append(value)
    else:
        d.update({key * 2: [value]})


if __name__ == '__main__':
    d = {}
    #print(update_dictionary(d, 1, -1))  # None
    #print(d)  # {2: [-1]}
    update_dictionary(d, 2, -2)
    #print(d)  # {2: [-1, -2]}
    update_dictionary(d, 1, -3)
    #print(d)  # {2: [-1, -2, -3]}