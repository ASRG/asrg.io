# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
import datetime

from authentication.models import Chapter, User


class ChapterInLine(admin.StackedInline):
    model = Chapter.user.through
    extra = 0
    show_change_link = True


# Unregister the previous User admin
# admin.site.unregister(User)

# Extend UserAdmin to add inlines
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    inlines = [ChapterInLine]
    readonly_fields = ('date_joined', 'last_login')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['location', 'city', 'country', 'lead', 'foundation',]# 'age']
    list_filter = ('location', 'city', 'country')
    # readonly_fields = ['age']

    # def age(self, obj):
    #     now = timezone.now()
    #     delta = now - obj.foundation
    #     fraction = delta.days / 365.25
    #     return f"{fraction:.2f}" 

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ChapterAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)