from django.shortcuts import render
from django.views.generic import ListView
from .models import UserPartner
from .utils import MyMixin


# Create your views here.
class HomeView(MyMixin, ListView):
    model = UserPartner
    template_name = 'events/view_partners.html'
    extra_context = {'title': 'EVENTS PLATFORM', 'partners': UserPartner.objects.all()}

    def get_queryset(self):
        return UserPartner.objects.all()
