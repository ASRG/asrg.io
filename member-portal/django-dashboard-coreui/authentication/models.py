# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.conf import settings


class ChapterMetaClass(ModelBase):
    def __new__(cls, name, bases, attrs):
        klas = super(ChapterMetaClass, cls).__new__(cls, name, bases, attrs)
        # Add permissions dynamically for all chapters present in Settings -- need to run makemigrations->migrate for every change to chapters
        for chapter in settings.CHAPTERS:
            location = chapter[0].split('-', 1)[1]
            klas._meta.permissions.append((f'ASRG_{location}', f'ASRG_{location}'))
            klas._meta.permissions.append((f'ASRG_local_lead_{location}', f'ASRG_local_lead_{location}',))

        return klas


class Chapter(models.Model, metaclass=ChapterMetaClass):
    location = models.CharField(
        max_length=24, null=False, blank=False, choices=settings.CHAPTERS, default=settings.CHAPTERS[0]
    )
    city = models.CharField(max_length=56, null=False, blank=True)
    country = models.CharField(max_length=56, null=False, blank=True)
    lead = models.CharField(max_length=56, null=False, blank=True)
    foundation = models.DateTimeField(null=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.location

    class Meta:
        # TODO: Talk with the team to see if we want to have this perms elsewhere? probablly not best to be under Chapters as they are not directly related
        permissions = [
            ("ASRG_member", "ASRG_member"),
            ("ASRG_global_lead", "ASRG_global_lead",),
            ("ASRG_global_admin", "ASRG_global_admin",),  # TODO: This should be correlated with is_staff (I think)
            ("ASRG_sponsor_L1", "ASRG_sponsor_L1"),
            ("ASRG_sponsor_L2", "ASRG_sponsor_L2"),
            ("ASRG_sponsor_L3", "ASRG_sponsor_L3"),
            ("ASRG_asip_contributor", "ASRG_asip_contributor"),
        ]
