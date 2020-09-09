# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import User, Chapter, OCCUPATIONAL_STATUS_CHOICES, GENDER_CHOICES
from authentication.countries import COUNTRIES as COUNTRY_CHOICES

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(),label="",empty_label="Chapter",
        widget=forms.Select(
            attrs={
                "placeholder" : "Chapter",                
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, #empty_label="Gender",
        widget=forms.Select(
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))
    occupational_status = forms.ChoiceField(label='Occupational Status', choices=OCCUPATIONAL_STATUS_CHOICES, #empty_label="Occupational Status",
        widget=forms.Select(
            attrs={
                "placeholder" : "Occupational Status",                
                "class": "form-control"
            }
        ))
    country = forms.ChoiceField(label='Country', choices=COUNTRY_CHOICES, #empty_label="Country",
        widget=forms.Select(
            attrs={
                "placeholder" : "Country",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'password1', 
            'password2', 
            'chapter', 
            'first_name', 
            'last_name', 
            'gender', 
            'occupational_status', 
            'country' 
            )
