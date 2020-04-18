from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "login/loginScreen.html")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")
