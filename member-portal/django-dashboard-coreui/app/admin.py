# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'field_of_study', 'date_joined', 'last_login')
    search_fields = ('country', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal =()
    # list_filter = ('chapter',)
    fieldsets = ()


admin.site.register(UserProfile,UserProfileAdmin)