# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from app import views
from authentication.views import account_view

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('createprofile/', views.profile_create_view, name='profile_create'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', account_view, name='edit_profile'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordreset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='passwordreset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwordreset/password_reset_form.html'), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
     name='password_reset_complete'),

]
