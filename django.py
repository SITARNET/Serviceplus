# 1. Django

# Виртуальное окружение (venv) -> Python 3..3 + Django 3.1.4 (на Windows)

# localhost - 127.0.0.1

# python -V -> Python 3.9.13
# pip list
# cd C:/Users/SITARNET/python/serviceplus
# python -m venv venv - устанавливаем venv окружение под названием venv
# .\venv\Scripts\activate - запуск вертуального окружения
# python.exe -m pip install --upgrade pip - обновление pip
# deactivate - выйти из вертуального окружения
# открываем проэкт в PyCharm -> (venv) PS C:\Users\SITARNET\Documents\Python\serviceplus>
# pip install django - устанавливаем движок
# pip list -> ...
# django-admin - все комманды django
# django-admin startproject <имя сайта>
# django-admin startproject coolsite
# cd .\coolsite
# python manage.py runserver - запуск сервера
# http://127.0.0.1:8000
# CTRL+C - остановка сервера
# python manage.py runserver 40000 - меняем порт
# http://127.0.0.1:4000
# python manage.py runserver 192.168.1.1:4000 - меняем ip


# 2. Модель MTV. Маршрутизация. Функции представления

# MTV - models, templates, views
# Создаём приложение (пакет). Оно должно быть максимально независимым от других приложений
# python manage.py startapp service

# service -> admin.py -> админпанель сайта
# service -> apps.py -> для конфигурации приложения
# service -> models.py -> для хранения ORM моделей
# service -> tests.py -> тестирующие процедуры
# service -> views.py ->для хранения представления

# serviceplus -> settings.py -> INSTALLED_APPS -> 'service.apps.ServiceConfig' - регистрация пакета
# service -> views.py -> определяем предствление страницы (function или class)
# serviceplus -> urls.py -> path('service/', index) -> импортируем маршрут (связываем функцию index с url)
# serviceplus -> Mark Directory as -> Sources root - для корректного импортирования
# service -> urls.py - создаём свои маршруты в пакете (если будем переносить пакет на другой сайт)
