from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Введите email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    username = forms.CharField(label='Введите login', required=True, help_text='Нельзя вводить символы бла бла бла',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label='Введите пароль', required=True, help_text='ну пароль не можеть быть малениким',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Введите email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    username = forms.CharField(label='Введите login', required=True, help_text='Нельзя вводить символы бла бла бла',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(label='Загрузить фото', required=False,
                           widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['img']
