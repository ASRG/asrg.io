# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from authentication.models import Chapter


class ChapterInLine(admin.StackedInline):
    model = Chapter
    extra = 0
    show_change_link = True


# Extend UserAdmin to add inlines
class UserAdmin(AuthUserAdmin):
    inlines = [ChapterInLine]


# Unregister the previous User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
