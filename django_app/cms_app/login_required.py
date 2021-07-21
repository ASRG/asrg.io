# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.conf import settings


class LoginRequired(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = getattr(settings, "LOGIN_URL", "/login/")

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith("/members") and not request.user.is_authenticated:
            return HttpResponseRedirect("%s?next=%s" % (self.login_url, request.path))
        return response
