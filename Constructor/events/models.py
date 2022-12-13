from django.contrib.auth.models import AbstractUser
from django import utils
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy

from .enums import ServiceTypes, Locations, EventTypes


# Create your models here.
class BaseUser(models.Model):
    username = models.CharField(max_length=40, verbose_name='Никнейм')
    description = models.TextField(blank=True, verbose_name='Описание')  # can be empty
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата регистрации')  # only in first attempt rewrite date
    email = models.EmailField(blank=True, max_length=60)

    class Meta:
        abstract = True


class UserClient(BaseUser):  # Client user who wants to create event
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    django_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # location = models.CharField(max_length=255, choices=Locations.choices, blank=True, verbose_name='Локация')
    # location more about event not user ! Right ?

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_absolute_url(self):
        return reverse_lazy('clients', kwargs={'id_client': self.pk})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class UserPartner(BaseUser):  # vendors
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=60, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    location = models.CharField(max_length=255, choices=Locations.choices, default=Locations.MOSCOW, blank=False,
                                verbose_name='Город')
    service_type = models.CharField(max_length=255, choices=ServiceTypes.choices, blank=False,
                                    verbose_name='Тип услуги')

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('vendor', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'


class BaseEvent(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название события')
    description = models.TextField(blank=True, verbose_name='Описание')  # can be empty
    planning_day = models.DateField(verbose_name='Планируемое день события', blank=True,
                                    default=utils.timezone.now)
    planning_time = models.TimeField(verbose_name='Планируемое время события', blank=True)
    event_type = models.CharField(max_length=60, verbose_name='Тип события',
                                  choices=EventTypes.choices, default=EventTypes.PARTY)
    location = models.CharField(max_length=60, verbose_name='Геопозиция',
                                choices=Locations.choices, default=Locations.MOSCOW)
    owner = models.ForeignKey(UserClient, on_delete=models.CASCADE)
    partners = models.ManyToManyField(UserPartner, through='EventVendors', through_fields=('event', 'partner'))

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def get_absolute_url(self):
        return reverse_lazy('event', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'


class EventVendors(models.Model):
    partner = models.ForeignKey(UserPartner, on_delete=models.CASCADE)
    event = models.ForeignKey(BaseEvent, on_delete=models.CASCADE)
    conditions = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Партнеры в событие'
        verbose_name_plural = 'Партнеры в событиях'
