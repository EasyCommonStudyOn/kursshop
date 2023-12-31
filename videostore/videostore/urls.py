from django.contrib import admin
from django.urls import path, include  # функция включения алиасов
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),  # админ панель
    path('', include('courses.urls')),  # главная страница
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass-reset.html'), name='pass-reset'),
    path('password_reset_complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password_reset_confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset_done/',
         authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)  # добавить все статически адреса статических елементов которые можем использовать в проекте
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
