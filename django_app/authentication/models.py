# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from geopy.geocoders import Nominatim
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from .countries import COUNTRIES as COUNTRY_CHOICES
from .languages import LANGUAGES

OCCUPATIONAL_STATUS_CHOICES = (
    ("", "Occupational Status"),
    ("Student", "Student"),
    ("Engineer", "Engineer"),
    ("Manager", "Manager"),
    ("Executive", "Executive Management"),
    ("Researcher", "Researcher"),
)

GENDER_CHOICES = (
    ("", "Gender"),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer Not To Say", "Prefer Not to Say"),
)


class Chapter(models.Model):
    location = models.CharField(max_length=56, null=False, blank=False)
    city = models.CharField(max_length=56, null=False, blank=True)
    country = models.CharField(max_length=56, null=False, blank=True)
    lead = models.CharField(max_length=56, null=False, blank=True)
    foundation = models.DateTimeField(blank=True, default=timezone.now)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    description = models.TextField()
    meetup_link = models.URLField()
    picture_src = ProcessedImageField(
        upload_to="chapters/cover", blank=True, verbose_name="picture"
    )
    picture = ImageSpecField(
        source="picture_src", processors=[ResizeToFill(611, 180)]
    )  # sized image
    email = models.EmailField(
        verbose_name="Location email address", null=True, blank=True
    )

    def get_coordinates(self):
        if (self.latitude == 0 or self.longitude == 0) and self.city:
            geolocator = Nominatim(user_agent="asrg-app", scheme="http")
            location = geolocator.geocode(self.city)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
                self.save()
        return (self.latitude, self.longitude)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        permissions = []


class User(AbstractUser):
    chapter = models.ManyToManyField("Chapter", blank=True, related_name="users")
    occupational_status = models.CharField(
        max_length=50,
        choices=OCCUPATIONAL_STATUS_CHOICES,
        blank=False,
        default=OCCUPATIONAL_STATUS_CHOICES[0],
    )
    country = models.CharField(
        max_length=150, choices=COUNTRY_CHOICES, default=COUNTRY_CHOICES[0]
    )
    verification_email_sent_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=False, default=GENDER_CHOICES[0]
    )
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(default="", blank=True, null=True)
    status = models.CharField(max_length=256, default="", blank=True, null=True)
    skills = models.CharField(max_length=350, default="", blank=True, null=True)
    pp_src = models.ImageField(
        upload_to="users/profile_pictures", blank=True, verbose_name="Profile Picture"
    )
    profile_picture = ImageSpecField(
        source="pp_src", processors=[ResizeToFill(350, 350)]
    )  # sized image
    fb_link = models.URLField(
        blank=True, verbose_name="Facebook Proifle Link", null=True
    )
    tw_link = models.URLField(
        blank=True, verbose_name="Twitter Proifle Link", null=True
    )
    ig_link = models.URLField(
        blank=True, verbose_name="Instagram Proifle Link", null=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = [
            ("ASRG_member", "ASRG_member"),
            (
                "ASRG_global_lead",
                "ASRG_global_lead",
            ),
            (
                "ASRG_global_admin",
                "ASRG_global_admin",
            ),
            ("ASRG_sponsor_L1", "ASRG_sponsor_L1"),
            ("ASRG_sponsor_L2", "ASRG_sponsor_L2"),
            ("ASRG_sponsor_L3", "ASRG_sponsor_L3"),
            ("ASRG_asip_contributor", "ASRG_asip_contributor"),
        ]


class Language(models.Model):
    language = models.CharField(
        max_length=150, choices=LANGUAGES, default=LANGUAGES[0][0]
    )

    def __str__(self):
        return self.get_language_display()
