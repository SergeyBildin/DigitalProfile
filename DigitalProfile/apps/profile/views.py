from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Profile,Groups,Membership
from .forms import EditProfile, AvatarUpload
from profile.models import Account
# Create your views here.

def ProfileView(request):
    account = request.user
    if account == 'AnonymousUser':
        redirect('login')
    template = 'Profile.html'
    profile = Profile.objects.get(user=account.id)

    if request.method == 'POST':
        edit_form = EditProfile(request.POST, instance= profile)
        if edit_form.is_valid():
            edit_form.save()
    if request.method == 'POST':
        avatar_form = EditProfile(request.POST, instance= profile)
        if avatar_form.is_valid():
            avatar_form.save()
    context = {
        'prof': profile,
        'edit_form': EditProfile(instance = profile),
        'avatar_form': AvatarUpload(instance=profile)
    }
    return render(request, template,context)

def get_members(groups):
    membership = {}
    mem_list = []
    for group in groups:
        query = Membership.objects.filter(group=group.group)
        mem_list.clear()
        for member in query:
            #full_name = member.person.surname + ' ' + member.person.name
            mem_list.append(member.person)
        membership[group.group.name] = mem_list
    return membership
        

def group_view(request):
    account = request.user
    template = 'Groups.html'
    profile = Profile.objects.get(user=account.id)
    groups = Membership.objects.filter(person=profile)
    members = get_members(groups)
    print(members)
    context = {
        'groups': groups,
        'profile': profile,
        'members': members,
    }
    return render(request,template, context)

def detail_profile(request, id):
    user = Account.objects.get(id=id)
    prof = Profile.objects.get(user=user.id)
    template = 'Detail.html'
    context = {
        'prof': prof,
    }
    return render(request,template, context)


