from django.contrib import messages
from .models import UserPartner, UserClient, BaseEvent, EventVendors
from .forms import UserClientRegisterForm, \
    UserLoginForm, AddEventForm, AddPartnerForm, CreateCooperationForm

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
    context_object_name = 'partners'
    template_name = 'events/view_partners.html'
    extra_context = {'title': 'EVENTS PLATFORM'}

    def get_queryset(self):
        return UserPartner.objects.all()


class ViewPartner(DetailView):
    model = UserPartner
    template_name = 'events/view_partner.html'
    extra_context = {'title': 'EVENTS PLATFORM'}
    context_object_name = 'partner'


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


def add_event(request):
    if request.method == "POST":
        form = AddEventForm(request.POST)
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
        form = AddEventForm()
    return render(request, 'events/add_event.html', {'form': form})


class ViewMyEvents(ListView):
    model = BaseEvent
    template_name = 'events/my_events.html'
    context_object_name = 'events'
    extra_context = {'title': 'EVENTS PLATFORM'}
    allow_empty = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.object_list = super().get_queryset()
        context = super(ViewMyEvents, self).get_context_data(**kwargs)
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        queryset = BaseEvent.objects.filter(owner__django_user_id=self.get_context_data()['user'])
        return queryset


class EventView(DetailView):
    template_name = 'events/view_event.html'
    model = BaseEvent
    context_object_name = 'event'
    extra_context = {'title': 'EVENTS PLATFORM',
                     }

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data()
        context['eventvendors'] = EventVendors.objects.filter(event__owner__django_user_id=self.request.user.id, )
        return context


def add_partner(request):
    if request.method == "POST":
        form = AddPartnerForm(request.POST)
        if form.is_valid():
            event = UserPartner(username=form.cleaned_data.get('username'),
                                description=form.cleaned_data.get('description'),
                                email=form.cleaned_data.get('email'),
                                name=form.cleaned_data.get('name'),
                                surname=form.cleaned_data.get('surname'),
                                phone=form.cleaned_data.get('phone'),
                                service_type=form.cleaned_data.get('service_type'),
                                location=form.cleaned_data.get('location'))
            event.save()
            messages.success(request, 'Partner was created ! ')
            return redirect('home')
    else:
        form = AddPartnerForm()
    return render(request, 'events/add_partner.html', {'form': form})


def create_cooperation(request, id_partner):
    if request.method == "POST":
        form = CreateCooperationForm(data=request.POST)
        for key in request.POST:
            print(key)
        if form.is_valid():
            cooperation = EventVendors(conditions=form.cleaned_data.get('conditions'),
                                       partner=UserPartner.objects.get(pk=id_partner),
                                       event=form.cleaned_data.get('event'))
            cooperation.save()
            messages.success(request, 'Cooperation was created ! ')
            return redirect('home')
    else:
        form = CreateCooperationForm()
        for key, value in request:
            print(key, value)
    return render(request, 'events/create_cooperation.html', {'form': form,
                                                              'partner': UserPartner.objects.get(pk=id_partner)})
