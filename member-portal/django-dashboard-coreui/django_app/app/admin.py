# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'dob', 'gender', 'field_of_study')
    search_fields = ('username', 'field_of_study')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal =()
    # list_filter = ('chapter',)
    fieldsets = ()

    def username(self, obj):
        return obj.user.username


admin.site.register(UserProfile,UserProfileAdmin)