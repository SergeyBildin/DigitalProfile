from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views.generic import CreateView
from .forms import AuthUserForm, RegisterUserForm

def main(request):
    return render(request, 'main.html')

class LoginsysLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home_page')



class LoginsysRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_message = 'Пользователь успешно создан'
    success_url = reverse_lazy('home_page')

