"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 3.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

'''

count_words = int(input())
words_list = set()

for i in range(count_words):
    word = str(input()).lower()
    words_list.add(word)

count_lines = int(input())
word_for_check = set()

for j in range(count_lines):
    line = str(input().lower()).split()
    word_for_check.update(line)

for c_word in word_for_check:
    if c_word not in words_list:
        print(c_word)
