"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу:

Тимофей обычно спит ночью XX часов и устраивает себе днем тихий час на YY минут. Определите, сколько всего минут 
Тимофей спит в сутки.

Внимание, программа принимает значения XX и YY из стандартного потока ввода (функция input), результат надо выводить в 
стандартный поток вывода (функция print). Обратите внимание на то, что приглашение, переданное в качестве аргумента в
 функцию input, считается выводом вашей программы. Используйте эту функцию без аргументов:

values = input()  # без строки приглашения!
Для этой задачи введён корректный шаблон, так что решать ничего не нужно, разберитесь с тем, что происходит в решении и
 как нужно оформлять код для сдачи его в систему.

Также обратите внимание, что в этой задаче (и во всех последующих задачах, где вам надо будет написать программу), 
предлагается пример входных (Sample Input) и выходных данных (Sample Output). Вы можете использовать эти данные для 
того, чтобы проверить, что ваша программа работает правильно (по крайней мере на одном примере), и вы используете 
верный формат ввода-вывода (например, если в задаче несколько чисел надо вывести в одну строку, а вы выводите 
каждое число на отдельной строке, то такой вывод будет считаться неверным). Имейте в виду, что проверяться ваша 
программа будет на большом наборе тестов, поэтому рекомендуем вам перед отправкой решения самостоятельно запустить 
вашу программу на еще каких-нибудь данных помимо примера из условия.

Обратите также внимание на ответ от проверяющей системы, доступный по кнопке "Feedback". Там может сообщаться о том, на
 каком тесте ваше решение выдаёт неверный ответ или о другой ошибке времени выполнения.

Примечание: обратите внимание, что приведённый код правильно работает для каждого из примеров по отдельности.
'''

X = int(input())
Y = int(input())
print(X*60 + Y)
