from django.contrib import admin
from .models import Course, Lesson

admin.site.register(Course) #регистрация таблицы в админке
admin.site.register(Lesson) #регистрация таблицы в админке

