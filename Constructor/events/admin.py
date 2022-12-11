from django.contrib import admin
from .models import UserPartner, UserClient

# Register your models here.

admin.site.register(UserClient)
admin.site.register(UserPartner)