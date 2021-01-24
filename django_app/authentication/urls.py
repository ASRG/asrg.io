# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

from .views import login_view, register_user, activate, resend_email_activation
from core.settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("resend-email-activation/<uidb64>/", resend_email_activation, name="resend-email-activation"),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

