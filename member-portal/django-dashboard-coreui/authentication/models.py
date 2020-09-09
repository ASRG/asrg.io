# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

from authentication.countries import COUNTRIES as COUNTRY_CHOICES

OCCUPATIONAL_STATUS_CHOICES = (
    ('', 'Occupational Status'),
    ('student', 'Student'),
    ('undergraduate student', 'Undergraduate Student'),
    ('graduate student', 'Graduate Student'),
    ('professional', 'Professional'),
)
    

GENDER_CHOICES = (('', 'Gender'),("Male", "Male"), ("Female", "Female"), ("Prefer Not To Say", "Prefer Not to Say"))

class ChapterMetaClass(ModelBase):
    def __new__(cls, name, bases, attrs):
        klas = super(ChapterMetaClass, cls).__new__(cls, name, bases, attrs)
        for chapter in settings.CHAPTERS:
            location = chapter[0].split('-', 1)[1]
            klas._meta.permissions.append((f'ASRG-{location}', f'ASRG-{location}'))
            klas._meta.permissions.append((f'ASRG-local-lead-{location}', f'ASRG-local-lead-{location}',))

        return klas


class Chapter(models.Model, metaclass=ChapterMetaClass):
    location = models.CharField(
        max_length=24, null=False, blank=False, choices=settings.CHAPTERS, default=settings.CHAPTERS[0]
    )
    city = models.CharField(max_length=56, null=False, blank=True)
    country = models.CharField(max_length=56, null=False, blank=True)
    lead = models.CharField(max_length=56, null=False, blank=True)
    foundation = models.DateTimeField(blank=True, default=timezone.now)
    user = models.ManyToManyField('User', related_name="chapters", blank=True)

    def __str__(self):
        return self.location

    class Meta:
        permissions = []


class User(AbstractUser):
    chapter = models.ManyToManyField('Chapter', blank=False, related_name='users')
    # first_name = models.CharField(max_length=25, blank=False)
    # last_name = models.CharField(max_length=25, blank=False)
    gender = models.CharField(max_length=17, choices=GENDER_CHOICES, blank=False, default=GENDER_CHOICES[0])
    occupational_status = models.CharField(max_length=25, choices=OCCUPATIONAL_STATUS_CHOICES, blank=False, default=OCCUPATIONAL_STATUS_CHOICES[0])
    country = models.CharField(max_length=150, choices=COUNTRY_CHOICES, default=COUNTRY_CHOICES[0])

    def __str__(self):
        return self.username
