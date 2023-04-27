from django.urls import path

from .views import *

urlpatterns = [
    path('', index), #http://127.0.0.1:8000/service/
    path('cats/', catigories), #http://127.0.0.1:8000/service/cats/
]