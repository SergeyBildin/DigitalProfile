from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Profile
# Create your views here.

def ProfileView(request):
    account = request.user
    account_id = account.id
    template = 'Profile.html'
    context = {
        'prof':Profile.objects.get(user=account_id),
    }
    return render(request, template,context)
        




