from django.contrib import admin
from django.urls import path, include  # функция включения алиасов
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # админ панель
    path('', include('courses.urls')),  # главная страница
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)  # добавить все статически адреса статических елементов которые можем использовать в проекте
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
