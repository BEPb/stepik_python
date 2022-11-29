"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 2.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Дополнительная
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

'''

def encryption_decryption(text: str, orig_char: str, cod_char: str):
    result = ""
    list_text = list(text)
    list_orig_char = list(orig_char)
    list_cod_char = list(cod_char)

    for i, ii in enumerate(list_text):
        for j, jj in enumerate(list_orig_char):
            if ii == jj:
                list_text[i] = list_cod_char[j]
        result += list_text[i]

    return result


if __name__ == '__main__':
    orig = input()
    cod = input()
    text_en = input()
    text_de = input()

    encryption = encryption_decryption(text_en, orig, cod)
    decryption = encryption_decryption(text_de, cod, orig)

    print(encryption)
    print(decryption)

