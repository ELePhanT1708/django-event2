from django.db import models
from django.utils.translation import gettext_lazy as _


class Locations(models.TextChoices):
    MOSCOW = 'MSC', _('Moscow')
    SAIT_PETERSBURG = 'SPB', _('Saint-Petersburg')
    KAZAN = 'KZN', _('Kazan')


class ServiceTypes(models.TextChoices):
    PHOTOGRAPH = 'Photographer'
    DJ = 'DJ'
    FOOD = 'Food'
    PLACE = 'Place'
    MAKEUP = 'MakeUp'


class EventTypes(models.TextChoices):
    BIRTHDAY = 'Birthday'
    WEDDING = 'Wedding'
    TEAM_BUILDING = 'Team Building'
    NEW_YEAR_EVE = "New Year's Eve"
    PARTY = 'PARTY'
