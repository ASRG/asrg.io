# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal =()
    # list_filter = ('chapter',)
    fieldsets = ()


admin.site.register(UserProfile,UserProfileAdmin)