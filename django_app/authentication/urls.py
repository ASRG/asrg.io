# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from .views import (
    login_view,
    register_user,
    index,
    profile_create_view,
    profile_view,
    account_edit_view,
    activate,
    inactive_user,
    reset_password,
)

urlpatterns = [
    re_path("index.html", index, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("reset-password/", reset_password, name="reset_password"),
    path("createprofile/", profile_create_view, name="profile_create"),
    path("profile/", profile_view, name="profile"),
    path("edit-profile/", account_edit_view, name="edit_profile"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="passwordreset/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="passwordreset/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="passwordreset/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="passwordreset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("resend-email-activation/", inactive_user, name="resend-email-activation"),
]
