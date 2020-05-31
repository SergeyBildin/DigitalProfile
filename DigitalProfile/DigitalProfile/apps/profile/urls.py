from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views




urlpatterns = [
    path('profile/', views.ProfileView, name='Profile'),
    #path('', include('account.urls'))
   #path('', include('profile.urls'))
    
    
]