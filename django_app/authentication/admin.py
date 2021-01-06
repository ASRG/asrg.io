# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.utils import timezone

# from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from authentication.models import Chapter, User


class ChapterInLine(admin.StackedInline):
    model = User.chapter.through
    extra = 0
    show_change_link = True


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ('first_name', 'last_name', 'country',
                    'date_joined', 'last_login')
    search_fields = ('country', 'first_name', 'last_name')
    inlines = [ChapterInLine]
    readonly_fields = ('date_joined', 'last_login')

    def save_model(self, request, obj, form, change):
        # add chapter permissions if chapter is changed -- need to save for all perms
        obj.save()
        if obj.chapter:
            for chapter in obj.chapter.all():
                perm = Permission.objects.get(codename=chapter)
                print(perm)
                obj.user_permissions.add(perm)

        return super(UserAdmin, self).save_model(request, obj, form, change)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['location', 'city', 'country', 'lead', 'foundation', 'age']
    list_filter = ('city', 'country')
    readonly_fields = ['age']

    def age(self, obj):
        now = timezone.now()
        delta = now - obj.foundation
        fraction = delta.days / 365.25
        return f"{fraction:.2f}"
