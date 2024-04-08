from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_of_birth', 'gender', 'employment']


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
