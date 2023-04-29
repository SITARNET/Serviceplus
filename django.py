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

# 3. Маршрутизация, обработка исключений запросов, перенаправления

# path('cats/<int:catsid>/', categories)
# str - любая не пустая строка, исключая символ /
# int - любое положительное, целое число включая 0
# slug - слаг, то есть, латиница ASCII таблицы, символы дефиса и подчёркивания
# uuid - цыфры, малые латинские ASCII, дефис
# path - любая не пустая строка, включая символ /
# re_path() - для использования регулярных выражений

# Обработка GET и POST запросов
# http://127.0.0.1:8000/?name=Gagarina&cat=music - GET запрос
# request.GET (POST)

# Обработка искючений при запросах к серверу
# serviceplus -> settings.py -> DEBUG = False - режим откладки отключён
# serviceplus -> settings.py -> ALLOWED_HOSTS = ['127.0.0.1']

# handler404 = pageNotFound -> serviceplus/urls.py
# serviceplus/view.py -> pageNotFound(request, exception)

# Обработка исключений при запросах к серыеру
# hundler500 - ошибка сервера
# hundler403 - доступ запрещён
# hundler400 - невозможно обработать запрос

# Создание 301 и 302 редиректов
# 301 - страница перемещена на другой постоянный URL-адрес
# 302 - страница перемещена на другой временный URL-адрес

# import django.shortcuts
# django.shortcuts.redirect

# return redirect('/', permanent=True)
# без параметра permanent -> 302
# c параметром permanent=True -> 301

# name='home' - используем имя для редиректа (serviceplus/urls.py)