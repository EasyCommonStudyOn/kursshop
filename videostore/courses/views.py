from django.shortcuts import render
from .models import Course
from django.views.generic import ListView


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'  # имя шаьлона который будет обрабатывать эту страницу
    context_object_name = 'courses'  # с этой таблицы будет все вытягиваться
    ordering = ['-id']  # сортировка записей будет происхзодить в обратном порядке добавления

    def get_context_data(self, *, object_list=None, **kwargs):  # для передачи данных в сам шаблон
        ctx = super(HomePage, self).get_context_data(**kwargs)  # обращеие к ListView
        ctx['title'] = 'Главная страница сайта' # передача этих елементов в сам шаблон
        return ctx
