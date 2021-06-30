# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import User, Chapter, OCCUPATIONAL_STATUS_CHOICES, GENDER_CHOICES
from authentication.countries import COUNTRIES as COUNTRY_CHOICES
from .models import User, UserProfile

DOB_CHOICES = []
for i in range(1901, 2099):
    DOB_CHOICES.append(str(i))


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class ResendEmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("email",)


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )
    chapter = forms.ModelChoiceField(
        queryset=Chapter.objects.all(),
        label="",
        empty_label="I don't know",
        required=False,
        widget=forms.Select(attrs={"placeholder": "Chapter", "class": "form-control"}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        )
    )
    occupational_status = forms.ChoiceField(
        label="Occupational Status",
        choices=OCCUPATIONAL_STATUS_CHOICES,  # empty_label="Occupational Status",
        widget=forms.Select(
            attrs={"placeholder": "Occupational Status", "class": "form-control"}
        ),
    )
    country = forms.ChoiceField(
        label="Country",
        choices=COUNTRY_CHOICES,  # empty_label="Country",
        widget=forms.Select(attrs={"placeholder": "Country", "class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "chapter",
            "first_name",
            "last_name",
            "occupational_status",
            "country",
        )

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' % (user.email))

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                'Username "%s" is already in use' % (user.username)
            )

    def clean_password2(self):
        if self.is_valid():
            pass1 = self.cleaned_data.get("password1")
            pass2 = self.cleaned_data.get("password2")
            username = self.cleaned_data.get("username")
            if pass1 == pass2:
                if pass1.lower() in username.lower():
                    raise forms.ValidationError(
                        "Password is similar to username.<br>Try a different Password"
                    )
                else:
                    return pass2
            else:
                raise forms.ValidationError("Passwords Don't match")


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        )
    )
    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    chapter = forms.ModelMultipleChoiceField(
        queryset=Chapter.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"placeholder": "Chapter", "class": "form-control"}
        ),
    )

    occupational_status = forms.ChoiceField(
        label="Occupational Status",
        choices=OCCUPATIONAL_STATUS_CHOICES,
        widget=forms.Select(
            attrs={"placeholder": "Occupational Status", "class": "form-control"}
        ),
    )

    country = forms.ChoiceField(
        label="Country",
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={"placeholder": "Country", "class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "occupational_status",
            "country",
        )

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' % (user.email))

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                'Username "%s" is already in use' % (user.username)
            )


class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=DOB_CHOICES,
            attrs={"Placeholder": "Date of Birth", "class": "form-control"},
        ),
    )
    field_of_study = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Field of Study",
                "class": "form-control",
                "required": False,
            }
        ),
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Your short bio", "class": "form-control"}
        ),
    )
    status = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Status message", "class": "form-control"}
        ),
    )
    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Skills", "class": "form-control"}
        ),
    )
    fb_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={"placeholder": "Facebook Profile Link", "class": "form-control"}
        ),
    )
    tw_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={"placeholder": "Twitter Profile Link", "class": "form-control"}
        ),
    )
    ig_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={"placeholder": "Instagram Profile Link", "class": "form-control"}
        ),
    )

    class Meta:
        model = UserProfile
        fields = (
            "dob",
            "field_of_study",
            "bio",
            "status",
            "skills",
            "fb_link",
            "tw_link",
            "ig_link",
            "pp_src",
        )
