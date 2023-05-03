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

# 4. Определение моделей. Миграции: создание и выполнение

# SQLite, MySQL, PortageSQL, Oracle...
# WSGI-приложение -> API интерфейс -> Django ORM -> Драйвер ORN -> SQLite....
# ORM (Object-Relation Mapping) - объектно-реляционное отображение
# sudo apt update
# sudo apt-cache search sqlite
# sudo apt install sqlite3
# sudo apt update
# sudo apt install sqlitebrowser

# serviceplus -> service -> models.py
# id: integer, primary key
# title: Varchar
# content: Text
# photo: Image
# time_create: DataTime
# Time_update: DataTime
# is_published: Boolean

# djbook.ru/rel3.0/ref/models/fields.html
# Чтобы Django могло сохранять фото, надо настроить две константы: FileField -> MEDIA_ROOT, MEDIA_URL
# serviceplus -> settings.py -> MEDIA_ROOT = os.path.join(BASE_DIR, 'media') -> import os
# MEDIA_URL = '/media/'

# Это настраиваеться только в откладочном режиме (не на реальном сервере) -> DEBUG = True
# serviceplus -> urls.py
# from django.conf.urls.static import static
# from serviceplus import settings
# if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавляем файлы миграций в папку "migration" -> чтобы добавить структуру таблиц
# ../serviceplus$ python manage.py makemigrations
# python -m pip install Pillow -> пакет для работы с фото
# service/migrations/0001_initial.py
# python manage.py sqlmigrate service 0001 -> посмотреть SQL-запрос для модели women под номером 0001
# python manage.py migrate -> запускаем миграцию (sql-запрос)