from django.shortcuts import render
from django.http import HttpResponse

def index(request): #httprequest
    return HttpResponse("Страница приложения Service")

def catigories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")