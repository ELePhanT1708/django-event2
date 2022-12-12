from django.contrib import messages
from .models import UserPartner, UserClient
from .forms import UserClientRegisterForm, UserLoginForm

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
