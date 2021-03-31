# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from .views import project_view

urlpatterns = [
    path("", project_view, name="project_view"),
]
