Микросервис для вычисления PnL и Index PnL для доллара (USD) относительно биткоина (BTC) за определенныи период, для счета на торговой бирже Deribit

1. Запуск приложения

    - должен быть установлен Docker

    - пример установки Docker для Mac:
        https://www.cprime.com/resources/blog/docker-for-mac-with-homebrew-a-step-by-step-tutorial/

    - комманда для запуска приложения в терминале Mac:
        docker-compose up -d --build


2. Структура приложения

APP3/ - основная папка проекта
    
    APP3/project - папка проекта с основными файлами .py
        APP3/project/templates - папка с html шаблонами
        APP3/project/__init__.py  - файл инициализации пакета приложения с объектами приложения и БД   
        APP3/project/functions.py - файл с определяемыми функциями приложения
        APP3/project/models.py - модель данных
        APP3/project/views.py - функции-обработчики эндпоинтов
   
    manage.py - настройка запуска приложения

    docker-entrypoint.sh - файл определяющий команды терминала для запуска приложения

    _.dev/yml/md/txt - прочие файлы(Докер,зависимости и т.д)    


3. Эндпоинты

     - вывод html шаблона с PnL, PnL_%, Index_PnL, Period(UTC), рассчитанными за весь период работы приложения
        Методы: GET         
        http://127.0.0.1:5000/api/PnL


     - вывод формы для расчета и загрузки PnL, PnL_%, Index_PnL, Period(UTC) за выбранный период работы приложения
        Методы: GET, POST
        http://127.0.0.1:5000/api/PnL_custom_period   