from django.shortcuts import render
from django.views.generic import ListView
from .models import UserPartner


# Create your views here.

class ViewPartners(ListView):
    model = UserPartner
    template_name = 'events/view_partners.html'
    extra_context = {'title': 'EVENTS PLATFORM',
                     'partners': UserPartner.objects.all()
                     }


class ViewHome(ListView):
    model = UserPartner
    template_name = 'events/home_page.html'
    extra_context = {'title': 'EVENTS PLATFORM',
                     }
