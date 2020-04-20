from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main, name='home_page'),
    path('login/', views.LoginsysLoginView.as_view(), name='login_page'),
    path('register/', views.LoginsysRegisterView.as_view(), name='register_page')
]