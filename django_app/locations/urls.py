# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from .views import location_view

urlpatterns = [
    path("", location_view, name="location_view"),
]
