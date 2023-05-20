from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class ServiceHome(ListView):
    model = Service
    template_name = 'service/index.html'
    context_object_name = 'posts'
    #extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Service.objects.filter(is_published=True).order_by('-pk')

# def index(request):
#     posts = Service.objects.all()
#
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'service/index.html', context=context)


def about(request):
    return render(request, 'service/about.html', {'title': 'О сайте'})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #Service.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'service/addpage.html', {'form': form, 'title': 'Добавление статьи'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'service/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):
#     post = get_object_or_404(Service, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'service/post.html', context=context)


class ShowPost(DetailView):
    model = Service
    template_name = 'service/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['cat_selected'] = context['post'].cat_id
        return context


# def show_category(request, cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = Service.objects.filter(cat_id=cat[0].id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'Отображение по категориям',
#         'cat_selected': cat[0].id,
#     }
#     return render(request, 'service/index.html', context=

class ServiceCategory(ListView):
    model = Service
    template_name = 'service/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
