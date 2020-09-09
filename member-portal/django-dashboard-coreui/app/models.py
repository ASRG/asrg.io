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



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    field_of_study = models.CharField(max_length=100,blank=True, null=True)
    bio = models.TextField(default=' ',blank=True, null=True)
    status = models.CharField(max_length=256, default=' ',blank=True, null=True)
    skills = models.CharField(max_length=350, default=' ',blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile pictures', default='def.jpg')

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

