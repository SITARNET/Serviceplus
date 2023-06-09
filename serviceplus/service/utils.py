from django.db.models import Count

from .models import *

menu = [{'title': "Про нас", 'url_name': 'about'},
        {'title': "Добавити статтю", 'url_name': 'add_page'},
        {'title': "Завдати питання", 'url_name': 'contact'},
        {'title': "Політика конфіденційності", 'url_name': 'privacy'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('service'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
