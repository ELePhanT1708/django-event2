from django import forms
from django.contrib.auth.models import User
from datetimepicker.widgets import DateTimePicker
from .models import UserPartner, UserClient, BaseEvent
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
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control", 'placeholder': '*QWERTY12345*'}))


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class AddPartnerForm(forms.ModelForm):
    class Meta:
        model = BaseEvent
        fields = ['title', 'description', 'planning_day', 'planning_time',
                  'event_type', 'location']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "My wedding day"}),

            'description': forms.Textarea(attrs={"class": "form-control", "rows": 3,
                                                 "placeholder": "Я хочу ..."}),
            'planning_day': DateInput(),
            'planning_time': TimeInput(),
            'event_type': forms.Select(attrs={"class": "form-control"}),
            'location': forms.Select(attrs={"class": "form-control"}),
        }

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")  # store value of request
    #     super().__init__(*args, **kwargs)

    def __str__(self):
        return "Добавить событие"
