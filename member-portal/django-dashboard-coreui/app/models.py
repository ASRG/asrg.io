# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
# from django.contrib.auth.models import User

from core.settings import CHAPTERS as CHAPTER_CHOICES
from .countries import COUNTRIES as COUNTRY_CHOICES
from authentication.models import User, Chapter

OCCUPATIONAL_STATUS_CHOICES = (
    ('student', 'Student'),
    ('undergraduate student', 'Undergraduate Student'),
    ('graduate student', 'Graduate Student'),
    ('professional', 'Professional'),
)

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("P", "Prefer Not to Say"))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    dob = models.DateField(verbose_name='Date of Birth', blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    occupational_status = models.CharField(max_length=25, choices=OCCUPATIONAL_STATUS_CHOICES, blank=True)
    field_of_study = models.CharField(max_length=100,)
    # chapter = models.CharField(max_length=12, choices=CHAPTER_CHOICES)
    # chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=150, choices=COUNTRY_CHOICES)
    bio = models.TextField()
    status = models.CharField(max_length=256)
    skills = models.CharField(max_length=350)
    profile_picture = models.ImageField(upload_to='profile pictures')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        permissions = [
            ("ASRG_member", "ASRG_member"),
            ("ASRG_global_lead", "ASRG_global_lead",),
            ("ASRG_global_admin", "ASRG_global_admin",),
            ("ASRG_sponsor_L1", "ASRG_sponsor_L1"),
            ("ASRG_sponsor_L2", "ASRG_sponsor_L2"),
            ("ASRG_sponsor_L3", "ASRG_sponsor_L3"),
            ("ASRG_asip_contributor", "ASRG_asip_contributor"),
        ]

