from django.contrib import admin
from .models import UserPartner, UserClient, BaseEvent, EventVendors
from django.contrib.auth.admin import UserAdmin

from .models import BaseUser
# Register your models here.

admin.site.register(UserClient)
admin.site.register(UserPartner)
admin.site.register(BaseEvent)
admin.site.register(EventVendors)
