# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
from django.forms.utils import ErrorList
from django.http import HttpResponse

from .forms import LoginForm, SignUpForm
from app.forms import UserProfileForm
import authentication.forms as f
from .models import User, Chapter
from app.models import UserProfile


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
            if chapter:
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

            return redirect("/login/")

        else:
            # errors = form.errors
            msg = "form not valid"

    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
def account_edit_view(request):
    context = {}
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    context['profile'] = profile

    if request.POST:
        acc_form = f.UserUpdateForm(request.POST, instance=request.user)
        prof_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if acc_form.is_valid() and prof_form.is_valid():
            acc_form.save(commit=False)
            chapter = acc_form.cleaned_data.get("chapter")
            user_obj = acc_form.save()
            for ch in chapter:
                user_obj.chapter.add(ch)
            # Add the permissions for the respective chapter as well
            perms = Permission.objects.filter(codename__in=chapter.values_list("location", flat=True))
            user_obj.user_permissions.add(*perms)
            profile = prof_form.save(commit=False)
            profile.user = request.user
            # profile.chapter = request.user.chapter.all
            if request.FILES:
                profile.profile_picture = request.FILES.get("profile_picture")
            else:
                profile.profile_picture = profile.profile_picture
            # profile.date_joined = datetime.now()
            # profile.last_login = datetime.now()
            if profile.dob and profile.field_of_study and profile.bio and profile.status and profile.skills:
                profile.is_complete = True
            profile.save()
            return redirect('profile')
        else:
            context['account_form'] = acc_form
            context["profile_form"] = prof_form

        # prof_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        # if prof_form.is_valid():
        #     profile = prof_form.save(commit=False)
        #     profile.user = request.user
        #     # profile.chapter = request.user.chapter.all
        #     if request.FILES:
        #         profile.profile_picture = request.FILES.get("profile_picture")
        #     else:
        #         profile.profile_picture = profile.profile_picture
        #     # profile.date_joined = datetime.now()
        #     # profile.last_login = datetime.now()
        #     if profile.dob and profile.field_of_study and profile.bio and profile.status and profile.skills:
        #         profile.is_complete = True
        #     profile.save()
        # else:
        #     context["profile_form"] = prof_form
        # return redirect('profile')#######################################################################
    else:
        acc_form = f.UserUpdateForm(
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

        prof_form = UserProfileForm(
            initial={
                # 'first_name': profile.first_name,
                # 'last_name': profile.last_name,
                "dob": profile.dob,
                'gender': profile.gender,
                # 'occupational_status': profile.occupational_status,
                "field_of_study": profile.field_of_study,
                # 'chapter': profile.chapter.all,
                # 'country': profile.country,
                "bio": profile.bio,
                "status": profile.status,
                "skills": profile.skills,
                "fb_link": profile.fb_link,
                "tw_link": profile.tw_link,
                "ig_link": profile.ig_link,
                "profile_picture": profile.profile_picture,
            }
        )
    context['account_form'] = acc_form
    context["profile_form"] = prof_form

    return render(request, 'accounts/account_update.html', context)
