from django.urls import path, include  # функция включения алиасов
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # home это название url обработчика
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    # slug передаеться url адрес детализированной страницы
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail')
]
