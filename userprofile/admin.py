# -*- coding: utf-8 -*-
from django.contrib import admin
from models import UserProfile, User


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'latest_editing')


admin.site.register(UserProfile, UserProfileAdmin)
