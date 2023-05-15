from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *


def index(request):
    posts = Service.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'service/index.html', context=context)


def about(request):
    return render(request, 'service/about.html', {'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)

            try:
                Service.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления статьи!')
    else:
        form = AddPostForm()
    return render(request, 'service/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Service, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'service/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Service.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по категориям',
        'cat_selected': cat[0].id,
    }
    return render(request, 'service/index.html', context=context)

