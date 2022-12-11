from django.db import models
from django.urls import reverse_lazy

from .enums import ServiceTypes, Locations


# Create your models here.
class BaseUser(models.Model):
    username = models.CharField(max_length=40, verbose_name='Никнейм')
    description = models.TextField(blank=True, verbose_name='Описание')  # can be empty
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата регистрации')  # only in first attempt rewrite date

    class Meta:
        abstract = True


class UserClient(BaseUser):  # Client user who wants to create event
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=255, choices=Locations.choices, blank=True)

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('clients', kwargs={'id_client': self.pk})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class UserPartner(BaseUser):  # vendors
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=255, choices=Locations.choices, default=Locations.MOSCOW, blank=False)
    service_type = models.CharField(max_length=255, choices=ServiceTypes.choices, blank=False)

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('partners', kwargs={'id_partner': self.pk})

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'