from django import forms
from django.contrib.auth.models import User

from .models import UserPartner, UserClient
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserClientRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label=' Никнейм пользователя ', help_text='Длина менее 150 символов',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " DENDI ..."}))
    email = forms.EmailField(max_length=150, label=' E-mail ',
                             widget=forms.EmailInput(
                                 attrs={"class": "form-control", 'placeholder': 'example@mail.com'}))
    first_name = forms.CharField(max_length=150, label=' Имя пользователя ',
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control", 'placeholder': 'Надежда'}))
    last_name = forms.CharField(max_length=150, label=' Фамилия пользователя ',
                                widget=forms.TextInput(
                                    attrs={"class": "form-control", 'placeholder': 'Бабкина'}))
    phone = forms.CharField(max_length=12, label=' Номер пользователя ',
                            widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Надежда'}))
    password1 = forms.CharField(max_length=150, label=' Пароль ',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", 'placeholder': '*QWERTY12345*'}))
    password2 = forms.CharField(max_length=150, label=' Подтверждение пароля ',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", 'placeholder': '*QWERTY12345*'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2']



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label=' Имя пользователя ', help_text='Длина менее 150 символов',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " DENDI ..."}))

    password = forms.CharField(max_length=150, label=' Пароль ',
                             widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': '*QWERTY12345*'}))

