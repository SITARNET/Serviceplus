from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .utils import *


class ServiceHome(DataMixin, ListView):
    model = Service
    template_name = 'service/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return context | c_def

    def get_queryset(self):
        return Service.objects.filter(is_published=True).order_by('-pk').select_related('cat')


def about(request):
    return render(request, 'service/about.html', {'title': 'О сайте', 'menu': menu})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'service/addpage.html'
    success_url = reverse_lazy('home')
    raise_exception = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return context | c_def


# def contact(request):
#     return HttpResponse("Обратная связь")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'service/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = Service
    template_name = 'service/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'], cat_selected=context['post'].cat_id)
        return context | c_def


class ServiceCategory(DataMixin, ListView):
    model = Service
    template_name = 'service/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).order_by('-pk').select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'service/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'service/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def Logout_user(request):
    logout(request)
    return redirect('login')
