from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm, ProfileCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Account
from profile.models import Profile


def main(request):
    context = {}
    template = 'main.html'
    return render(request,template, context)


class RegistrationView(CreateView):
    model = Account
    template_name = 'register.html'
    form_class = RegistrationForm
    success_message = 'Пользователь успешно создан'
    success_url = '/secondReg/'

class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'secondReg.html'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('profile.html')
    

    