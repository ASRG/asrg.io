# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Chapter, OCCUPATIONAL_STATUS_CHOICES, GENDER_CHOICES
from authentication.countries import COUNTRIES as COUNTRY_CHOICES
from .models import User

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

    # error_messages = {
    #     'password_mismatch': "Your Password Mismatch For 'UserCreationForm' class",
    # }

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
    # gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, #empty_label="Gender",
    #     widget=forms.Select(
    #         attrs={
    #             "placeholder" : "Gender",                
    #             "class": "form-control"
    #         }
    #     ))
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
            # 'gender', 
            'occupational_status', 
            'country' 
            )
        # error_messages = {
        #     'username': {
        #         'unique': 'Your Custom Error Message here !!!',
        #     },
        # }


    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' %(user.email))
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use' %(user.username))

    def clean_password2(self):
        if self.is_valid():
            pass1 = self.cleaned_data.get('password1')
            pass2 = self.cleaned_data.get('password2')
            username = self.cleaned_data.get('username')
            if pass1 == pass2:
                if pass1.lower() in username.lower():
                    raise forms.ValidationError("Password is similar to username.<br>Try a different Password")
                else:
                    return pass2
            else:
                raise forms.ValidationError("Passwords Don't match")

    # def clean(self):
    #     self.clean_username()
    #     self.clean_email()
    #     self.clean_password2()


    

class UserUpdateForm(forms.ModelForm):
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


    # password1 = forms.CharField(
    # widget=forms.PasswordInput(
    #     attrs={
    #         "placeholder" : "Password",                
    #         "class": "form-control"
    #     }
    # ))
    # password2 = forms.CharField(
    # widget=forms.PasswordInput(
    #     attrs={
    #         "placeholder" : "Password check",                
    #         "class": "form-control"
    #     }
    # ))
    
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
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, required=False,
    widget=forms.Select(
        attrs={
            # "placeholder" : "Gender",                
            "class": "form-control"
        }
    ))

    chapter = forms.ModelMultipleChoiceField(queryset=Chapter.objects.all(),
    widget=forms.SelectMultiple(
        attrs={
            "placeholder" : "Chapter",                
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
            # 'password1', 
            # 'password2', 
            # 'chapter', 
            'first_name', 
            'last_name', 
            'gender', 
            'occupational_status', 
            'country',
            )


    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' %(user.email))
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use' %(user.username))

    # def clean_password2(self):
    #     if self.is_valid():
    #         pass1 = self.cleaned_data.get('password1')
    #         pass2 = self.cleaned_data.get('password2')
    #         username = self.cleaned_data.get('username')
    #         if pass1 == pass2:
    #             if pass1.lower() in username.lower():
    #                 raise forms.ValidationError("Password is similar to username.<br>Try a different Password")
    #         else:
    #             raise forms.ValidationError("Passwords Don't match")


