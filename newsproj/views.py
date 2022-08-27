from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import New


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = New
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'
    pk_url_kwarg = 'id'