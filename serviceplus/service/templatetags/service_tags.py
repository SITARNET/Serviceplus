from django import template

from service.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('service/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('service/list_menu.html')
def show_menu():
    menu = [{'title': "Про нас", 'url_name': 'about'},
            {'title': "Добавити статтю", 'url_name': 'add_page'},
            {'title': "Завдати питання", 'url_name': 'contact'},
            {'title': "Ввійти", 'url_name': 'login'}]

    return {"menu": menu}
