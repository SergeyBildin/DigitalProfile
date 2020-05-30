from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm, ProfileCreationForm, AuthForm
from django.views.generic import CreateView, View, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Account
from profile.models import Profile
from .tasks import get_user_skills



def main(request):
    context = {}
    template = 'main.html'
    return render(request,template, context)

class AuthView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm
    success_url = reverse_lazy('profile')


class RegistrationView(FormView):
    model = Account
    template_name = 'register.html'
    form_class = RegistrationForm
    success_message = 'Пользователь успешно создан'
    #skills = analysis_user(get_user_id(Account.objects.get(email=self.request.user.email)),)
    success_url = '/secondReg/'
    def form_valid(self,form):
        form.save()

        email = self.request.POST['email']
        password = self.request.POST['password1']        
        user = authenticate(email=email, password=password)
        print('USer:', user)
        login(self.request, user)
        return super(RegistrationView,self).form_valid(form)

class ProfileCreateView(CreateView):
    #user = Account.objects.get(id=pk)
    model = Profile
    template_name = 'secondReg.html'
    form_class = ProfileCreationForm
    success_url = '/profile/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        user = Account.objects.get(email=self.object.user)
        print(user)
        print(user.vk_id)
        self.object.skills = get_user_skills.delay(user.vk_id)
        self.object.save()
        return super().form_valid(form)
    

    