# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, activate
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

from core.settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

