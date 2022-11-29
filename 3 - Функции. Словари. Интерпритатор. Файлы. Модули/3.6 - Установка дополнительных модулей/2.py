"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 1.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

'''

import requests

with open("file-2.txt") as inf:
    file_text = inf.readline().strip()

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"
stop_word = "We"
split_site_text = ["text"]
num_urls = 0

while split_site_text[0] != stop_word:
    get_request = requests.get(file_text)
    site_text = get_request.text
    split_site_text = site_text.split()
    file_text = base_url + site_text
    num_urls += 1
    print("Number of url: %s" % num_urls)

print()
print(site_text)

# We are the champions, my friends,
# And we'll keep on fighting 'til the end.
# We are the champions.
# We are the champions.
# No time for losers
# 'Cause we are the champions of the world.