# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
from django.forms.utils import ErrorList
from django.http import HttpResponse

from .forms import LoginForm, SignUpForm
import authentication.forms as f
from .models import User, Chapter


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/index.html")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):

    msg = None
    success = False
    errors = None

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            chapter = form.cleaned_data.get("chapter")
            user_obj = form.save()
            user_obj.chapter.add(chapter)
            # Add the permissions for the respective chapter as well
            perm = Permission.objects.get(codename=chapter)
            user_obj.user_permissions.add(perm)
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
            # user.chapter.add(chapter)
            # chapter.user.add(user)

            msg = 'User created.'
            success = True

            # return redirect("/login/")

        else:
            # errors = form.errors
            msg = "form not valid"

    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def account_edit_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = f.UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            chapter = form.cleaned_data.get("chapter")
            user_obj = form.save()
            for ch in chapter:
                user_obj.chapter.add(ch)
            # Add the permissions for the respective chapter as well
            perm = Permission.objects.get(codename=chapter)
            user_obj.user_permissions.add(perm)
            return redirect('profile')
    else:
        form = f.UserUpdateForm(
            initial={
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                # 'gender': request.user.gender,
                'chapter': request.user.chapter.all(),
                'occupational_status': request.user.occupational_status,
                'country': request.user.country,
            }
        )
    context['account_form'] = form
    return render(request, 'accounts/account_update.html', context)
