from django.contrib import messages
from .models import UserPartner, UserClient, BaseEvent
from .forms import UserClientRegisterForm, UserLoginForm, AddPartnerForm

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class ViewPartners(ListView):
    model = UserPartner
    template_name = 'events/view_partners.html'
    extra_context = {'title': 'EVENTS PLATFORM',
                     'partners': UserPartner.objects.all()
                     }


# class ViewPartners(DetailView):
#
#     model = UserPartner
#     template_name = 'events/view_partners.html'
#     extra_context = {'title': 'EVENTS PLATFORM',
#                      'partners': UserPartner.objects.all()
#                      }

class ViewMyEvents(ListView):
    model = BaseEvent
    template_name = 'events/my_events.html'
    context_object_name = 'events'
    extra_context = {'title': 'EVENTS PLATFORM'}

    def get_context_data(self, **kwargs):
        context = super(ViewMyEvents, self).get_context_data(**kwargs)
        q = self.request.user.id
        context['user'] = q
        return context

    def get_queryset(self):
        queryset = BaseEvent.objects.filter(owner__django_user_id=self.get_context_data()['user'])
        return queryset


class ViewHome(ListView):
    model = UserPartner
    template_name = 'events/home_page.html'
    extra_context = {'title': 'EVENTS PLATFORM',
                     }


def register(request):
    if request.method == 'POST':
        form = UserClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            client = UserClient(django_user_id=user.id,
                                username=form.cleaned_data.get('username'),
                                email=form.cleaned_data.get('email'),
                                first_name=user.first_name,
                                last_name=user.last_name,
                                phone=form.cleaned_data.get('phone'))

            client.save()
            messages.success(request, 'User was created ! ')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ' User was NOT created ! ')
    else:
        form = UserClientRegisterForm()
    return render(request, 'events/register.html', {'form': form,
                                                    'title': 'Sign in'}
                  )


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ' Authentication is FAILED! ')
    else:
        form = UserLoginForm()

    return render(request, 'events/login.html', {'form': form,
                                                 'title': 'Log In'})


# class CreateEvent(LoginRequiredMixin, CreateView):
#     form_class = AddPartnerForm
#     template_name = 'events/add_event.html'
#     login_url = "/login/"
#     success_url = reverse_lazy('home')
#
#     def get_form_kwargs(self):
#         """ Passes the request object to the form class.
#          This is necessary to only display members that belong to a given user"""
#
#         kwargs = super(CreateEvent, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs

def add_event(request):
    if request.method == "POST":
        form = AddPartnerForm(request.POST)
        if form.is_valid():
            event = BaseEvent(title=form.cleaned_data.get('title'),
                              description=form.cleaned_data.get('description'),
                              planning_day=form.cleaned_data.get('planning_day'),
                              planning_time=form.cleaned_data.get('planning_time'),
                              event_type=form.cleaned_data.get('event_type'),
                              location=form.cleaned_data.get('location'),
                              owner=UserClient.objects.get(django_user_id=request.user.id))
            event.save()
            messages.success(request, 'Event was created ! ')
            return redirect('home')
    else:
        form = AddPartnerForm()
    return render(request, 'events/add_event.html', {'form': form})
