from django.urls import path, include  # функция включения алиасов
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home')  # home это название url обработчика

]
