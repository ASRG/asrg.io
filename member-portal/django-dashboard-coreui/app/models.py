# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
# from django.contrib.auth.models import User

from core.settings import CHAPTERS as CHAPTER_CHOICES
from .countries import COUNTRIES as COUNTRY_CHOICES
from authentication.models import User, Chapter

GENDER_CHOICES = (
    ("", "Gender"),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer Not To Say", "Prefer Not to Say"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=False, default=GENDER_CHOICES[0]
    )
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(default=' ', blank=True, null=True)
    status = models.CharField(
        max_length=256, default=' ', blank=True, null=True)
    skills = models.CharField(
        max_length=350, default=' ', blank=True, null=True)
    pp_src = ProcessedImageField(upload_to='users/profile_pictures',
                                 blank=True, verbose_name='Profile Picture')  # processedimagefield
    profile_picture = ImageSpecField(source='pp_src',  processors=[
                                     ResizeToFill(350, 350)])  # sized image
    fb_link = models.URLField(blank=True, verbose_name="Facebook Proifle Link")
    tw_link = models.URLField(blank=True, verbose_name="Twitter Proifle Link")
    ig_link = models.URLField(
        blank=True, verbose_name="Instagram Proifle Link")

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)

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
