from django.db import models
from django.utils.translation import gettext_lazy as _


class Locations(models.TextChoices):
    MOSCOW = 'MSC', _('Moscow')
    SAIT_PETERSBURG = 'SPB', _('Saint-Petersburg')
    KAZAN = 'KZN', _('Kazan')


class ServiceTypes(models.TextChoices):
    PHOTOGRAPH = 'photo', _('Photographer')
    DJ = 'DJ'
    FOOD = 'Food'
    PLACE = 'Place'
    MAKEUP = 'MakeUp'


