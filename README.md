<div align="center">


<img src="./art/stepik_logotype_green.png" alt="Bot logo" width="600" height="200.5">

# Программирование на Python

</div>

## Как это работает?

Все очень просто: переходи по [ссылке](https://stepik.org/course/67/syllabus) курса и учись, а если уже все идие закончились обращайся к моим подсказкам.

## Порядок подготовки и работы с ботом

1. Клонировать репозиторий либо скачать архив из github или при помощи следующих команд в командной строке
   ```commandline
   $ cmd
   $ git clone https://github.com/BEPb/github_bot
   $ cd github_bot
   ```

2. Создать виртуальное окружение Python.
3. Установить все необходимые пакеты для работы нашего кода, при помощи следующей команды:

    ```
    pip install -r requirements.txt
    ```
4. После запуска нашего бота он сможет выполнять все свои обязанности только через специфический браузер 
   Chrome Driver, для этих целей, скачайте его с официального сайта хром по следующей ссылке
   [Chrome Driver](https://chromedriver.chromium.org/downloads) только выберите вашу операционную систему.

5. Распакуйте скаченный архив Chrome-Driver, в результате вы увидите внутри всего лишь один файл, это и есть наш 
   специальный браузер. Нам необходимо запомнить полный путь к этому файлу, например:
    ```
    # Путь вашего chromedriver
    CHROME_DRIVER_PATH = "./chromedriver_win32/chromedriver"  # стандартное место размещения в windows
    # или
    CHROME_DRIVER_PATH = "/home/user/Загрузки/chromedriver_linux64/chromedriver"  # стандартное место размещения ubuntu
    ```


6. Укажите путь к драйверу Chrome, учетные данные и имена пользователей Github целевых пользователей в файле 
   конфигурации, он размещен в папке followbot и называется config.py:

    ```python
    # Путь вашего chromedriver
    # CHROME_DRIVER_PATH = "./chromedriver_win32/chromedriver"  # стандартное место размещения в windows
    CHROME_DRIVER_PATH = "/home/user/Загрузки/chromedriver_linux64/chromedriver"  # стандартное место размещения ubuntu
   
    # Указываем логин и пароль от вашей учетной записи
    YOUR_NAME = "BEPb"
    YOUR_PASS = "github.com84"
   
    # Список имен пользователей github, на подписчиков которых вы хотите подписаться
    TARGET_NAMES_LIST = ["torvalds"]
    ```

7. Запустите вашего бота из папки followbot файл bot.py или введите следующую команду:

    ```
    python3 -m followbot.bot
    ```
   
8. Дополнительная информация по файлам:
* bot.py - подписка на подписчиков или подписанных целевого пользователя (задан в конфигурации)
* bot_sql.py - бот который проходит по всем пользователям в БД и подписывается под всеми его подписчиками и на кого 
  он сам подписан
* config.py - конфигурация
* github_login.py - логирование гитхаба
* list_to_csv.csv - список собственных подписчиков
* load_sqlite3.py - код считывания данных из таблицы и преобразования их перед обработкой без изменения самой БД
* madatabase.db - база данных о пользователях сохраненных в csv файле
* parser_followers - сохранить всех своих подписчиков в csv файл
* scan_one_page - сканирование страниц пользователей сохраненных в csv файле
* unfollow_bot - отписка от собственных пользователей

9. Запуск сканирования более 1млн страниц пользователй гитхаба и сбора подробной информации о каждом из них:
```commandline
cd /home/user/PycharmProjects/github_bot/followbot
python3 -m scan_one_page
python -m scan_one_page
```

```commandline
cd C:\Users\root\PycharmProjects\github_bot\followbot
python -m scan_one_page
```


