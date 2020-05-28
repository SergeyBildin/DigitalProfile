from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
        path('',views.main, name = 'welcome'),
        path('register/', views.RegistrationView.as_view(), name = 'register'),
        path('secondReg/', views.ProfileCreateView.as_view(), name = 'secondReg'),
        
]