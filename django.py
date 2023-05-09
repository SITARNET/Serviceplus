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

# 5. Django

# CRUD - Create, Read, Update, Delete
# ORM фркймворка Django

# python manage.py shell -> консоль фрймворка
# >>> from service.models import Service
# >>> Service(title='Ремонт ноутбуков', content='Ми делаем комплекс. Чистка, замена термопасты, настройка Windows')
# >>> w1 = _ - ссылка на объект Service
# >>> w1.save() - запись в таблицу
# >>> w1.id -> 1
# >>> w1.title -> Ремонт ноутбуков
# >>> w1.pk (=w1.id) -> 1
# >>> from django.db import connection
# >>> connection.queries - посмотреть SQL-запросы
# >>> w3 = Service()
# >>> w3.title = 'Ремонт системного блока'
# >>> w3.content = 'Полный комплекс работ по ремонту системного блока'
# >>> w3.save()

# Или используем другой метод
# >>> Service.objects
# >>> w4 = Service.objects.create(title='Заправка картриджей', content='Заправка или регенирация лазерных картриджей') - записываеться сразу в базу
# >>> w4
# >>> w4.title
# >>> w4.pk

# Можно без присвоения переменной
# >>> Service.objects.create(title='Кира Найтли', content='Биография Киры Найтли')
# >>> Service.objacts.all() - все текущие записи
# models.py -> def __str__(self): return self.title в классе Women
# >>> exit() - выходим из оболочки Django (перезапускаем)
# >>> python manage.py shell
# >>> from service.models import Service
# >>> Service.objects.all() -> <QuerySet [<Service: Анджелина Джоли>, <Service: Энн.... -> ограничение на 21 запись!
# >>> w = _ - присваеваем список
# >>> w[0] -> <Service: Анджелина Джоли>
# >>> w[0].title -> 'Анджелина Джоли'
# >>> len(w) -> 5
# >>> for wi in w: print(wi.title) -> Анджелина Джоли, Энн Хэтэуэй, Джулия Робертс, Ума Турман, Кира Найтли

# >>> Service.objects.filter(title='Энн Хэтэуэй') - выбока с помощью фильтра
# >>> Service.objects.filter(pk=2) -> <QuerySet [<Service: Энн Хэтэуэй>]>
# >>> Service.objects.filter() => <имя_атрибута>__gte - сравнение больше или равно (>=)
# >>> Service.objects.filter() => <имя_атрибута>__lte - сравнение меньше или равно (<=)
# >>> Service.objects.filter(pk__gte=2) => <QuerySet [<Service: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>...

# >>> Service.objects.exclude(pk=2) => выбирает все записи, которые НЕ соответствуют критерию

# >>> Service.objects.get(pk=2) => выбирает если точно знаем что запись есть, иначе генерирует исключение

# >>> Service.objects.filter(pk__lte=4).order_by('title') - сортировка
# >>> Service.objects.order_by('time_update')
# >>> Service.objects.order_by('-time_update') - обратная сортировка

# >>> wu = Service.objects.get(pk=2)
# >>> wu.tutle = 'Ремонт мониторов' - присваеваем новое значение
# >>> wu.content = 'Качественный ремонт мониторов любой сложности.' - присваеваем новое значение
# >>> wu.save() - сохраняем

# >>> wd = Service.objects.filter(pk__gte=4)
# >>> wd -> <QuerySet [<Service: Ума Турман>, <Women: Кира Найтли>]>
# >>> wd.delete() -> (2, {'service.Service': 2}) - удалили две записи

# http://djbook.ru/rel3.0/topics/db/queries.html


# 6. Шаблоны (templates). Начало

# MTV (models, templates, views)

# (venv) PS C:\Users\SITARNET\PycharmProjects\Serviceplus\serviceplus> python manage.py runserver
# http://127.0.0.1:8000/

# https://djbook.ru/rel3.0/topics/templates.html

# {% extends 'women/base.html' %} # наследование общего шаблона


# 7. Подключение статических файлов. Фильтры шаблонов

# CSS, JavaScript
# serviceplus/static -> общая папка для реального сервера
# serviceplus/serviceplus/static -> не стандартный путь
# serviceplus/service/static -> не стандартный путь

# python manage.py collectstatic -> берутся все файлы из не стандартных путей и перемещаються в serviceplus/static

# В пакете кофигураций надо определить (serviceplus/settings.py):
# STATIC_URL - префикс URL-адреса для статических файлов
# STATIC_ROOT - путь к общей статической папке, исп. реальным сервером
# STATICFILES_DIRS - список нестандартных путей к статическим файлам, исп. для сбора и для режима откладки

# serviceplus/service/static/service -> пространство имён
# serviceplus/service/static/service/css
# serviceplus/service/static/service/js
# serviceplus/service/static/service/images

# {% load static %} - служит для подключения статических файлов
# https://djbook.ru/rel3.0/ref/templates/builtins.html#ref-templates-builtins-filters - фильтры


# 8. Формирование URL-адресов в шаблонах

# {% имя_тега %}  {{ имя_переменной }}  {{ value|имя_фильтра }}
# <a href="#">...</a>
# {% url'<URL-адрес или имя маршрута>'[параметры ссылки] %}


# 9. Создание связей между моделями через класс ForeignKey

# Нормализация данных

# ForeignKey - для связей Many to One (поля отношений)
# ManyToManyField - для связей Many to Many (многие к многим)
# OneToOneField - для связей One to One (один к одному)

# ForeignKey(<ссылка на первичную модель>, on_delete=<ограничения при удалении>)

# models.CASCADE - при удалении записи из первичной модели (таблица Category) происходит удаление всех записей
# из вторичной модели (Service), связанных с удаляемой категорией

# models.PROTECT - запрет удаление записи из первичной модели, если она используется во вторичной (выдаёт исключение)

# models.SET_NULL - при удалении записи первичной модели устанавливает значение foreign key в NULL у соответствующих
# записей вторичной модели

# models.SET_DEFAULT - то же самое, что и SET_NULL, только вместо NULL устанавливает значение по умолчанию, каторое
# должно быть определено через класс ForeignKey

# models.SET() - то же самое, только устанавливает пользовательское значение

# models.DO_NOTHING - удаление записи в первичной модели не вызывает никаких действий у вторичных моделей

# djbook.ru/rel3.0/topics/db/models.html#relationships

# python manage.py makemigrations -> python manage.py migrate - создали таблицы
# python manage.py shell
# from service.models import *
# Category.objects.create(name='Расходники')
# Category.objects.create(name='Техника')
# w_list = Service.objects.all()
# w_list.update(cat_id=1)


# 10. Начинаем работу с админ-панелью

# setting.py -> LANGUAGE_CODE = 'ru'
# 127.0.0.1:8000/admin/

# создаём администратора
# ...serviceplus/serviceplus -> python mange.py createsuperuser

# Регистрируем наше приложение Women
# ...serviceplus/service/admin.py -> from .models import * -> admin.site.register(Service)

# используем вложенный класс для настройки админ-панели -> class Meta в models.py
# apps.py -> verbose_name = 'Сервис' # если settings.py -> INSTALLED_APPS -> service.apps.ServiceConfig (а не service)
# Добавляем поля ->admin.py

# list_display = ('',...) - список полей которые мы хотим видеть
# list_display_links = ('',...) - список полей на которые мы можем кликнуть
# search_fields = ('',...) - по каким полям можно производить поиск
# list_editable = ('',) - поле будет редактируемым
# list_filter = ('',...) - поля по которым сможем фильтровать список полей
# admin.site.register(Women, WomenAdmin) # регистрируем класс

# Переводим названия title, time create, photo, is published
# models.py -> в class Service -> добавляем к каждому полю verbose_name='...'

# Регистрируем Category

# Вносим в таблицы базы данных мета описания
# Создаём файл миграции
# ../serviceplus -> python manage.py makemigrations -> создаётся файл
# python manage.py migrate -> применяем все миграции для базы данных


# 11. Пользовательские теги шаблонов

# Убираем дублирование с помощью пользовательских тегов в models.py
# simple tags - простые теги
# inclusion tags - включающие теги, формирует свой шаблон и возвращает html

# service/templatetags -> __init__.py

# https://djbook.ru/rel3.0/howto/custom-template-tags.html