from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views




urlpatterns = [
    path('profile/', views.ProfileView, name='Profile'),
    path('profile/groups/', views.group_view, name='groups'),
    path('detail/<int:id>', views.detail_profile, name='detail'),
    #path('', include('account.urls'))
   #path('', include('profile.urls'))
    
    
]