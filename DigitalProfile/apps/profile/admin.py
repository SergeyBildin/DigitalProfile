from django.contrib import admin
from .models import Profile, Groups, Membership
from django.contrib.auth.admin import UserAdmin


class ProfileAdmin(UserAdmin):
    list_display = ('id','surname', 'name','patronymic', 'skills', )
    search_fields = ('surname',)
    #readonly_fields = ('date_joined','last_login',)
    ordering = ('id','surname',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Groups)
admin.site.register(Membership)

