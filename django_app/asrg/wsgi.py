# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.wsgi import get_wsgi_application


def asrg_app():
    os.environ["DJANGO_SETTINGS_MODULE"] = "asrg.settings.asrg"
    application = get_wsgi_application()
    return application


def members_app():
    os.environ["DJANGO_SETTINGS_MODULE"] = "asrg.settings.asrg"
    application = get_wsgi_application()
    return application
