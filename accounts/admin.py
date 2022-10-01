from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User,UserProfile

class CustomerUserAdmin(UserAdmin):
    list_display = ("email","first_name","last_name","role","username","is_active")
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User,CustomerUserAdmin)
admin.site.register(UserProfile)
