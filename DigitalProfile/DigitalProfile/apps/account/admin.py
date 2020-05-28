from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('id','email', 'vk_id','date_joined', 'last_login', 'is_admin')
    search_fields = ('email',)
    readonly_fields = ('date_joined','last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account)

