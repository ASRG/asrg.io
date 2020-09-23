# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="S#perS3crEt_1122")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True)

# load production server from .env
ALLOWED_HOSTS = ["localhost", "127.0.0.1", config("SERVER", default="127.0.0.1")]

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend "

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",  # Enable the inner app
    "authentication",
    "website",
    "mapwidgets",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"
LOGIN_REDIRECT_URL = "home"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": config(
        "DATABASE_URL",
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"),
        cast=dj_database_url.parse,
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = "authentication.User"
#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "website/templates/static"),
    os.path.join(BASE_DIR, "core/static"),
)
#############################################################
#############################################################


MEDIA_ROOT = os.path.join(BASE_DIR, "app/media")
MEDIA_URL = "/app/media/"

CHAPTERS = (
    ("ASRG-S", "ASRG-Stuttgart"),
    ("ASRG-D", "ASRG-Detroit"),
    ("ASRG-TLV", "ASRG-Tel Aviv"),
    ("ASRG-C", "ASRG-Cluj-Napoca"),
    ("ASRG-SIN", "ASRG-Singapore"),
    ("ASRG-MUC", "ASRG-Munich"),
    ("ASRG-CAI", "ASRG-Cairo"),
    ("ASRG-SHA", "ASRG-Shanghai"),
    ("ASRG-BER", "ASRG-Berlin"),
    ("ASRG-PIT", "ASRG-Pittsburgh"),
    ("ASRG-SFO", "ASRG-San Francisco"),
    ("ASRG-FRA", "ASRG-Darmstadt"),
    ("ASRG-JPN", "ASRG-Tokyo"),
    ("ASRG-OXF", "ASRG-Oxford"),
    ("ASRG-SYD", "ASRG-Sydney"),
    ("ASRG-IASI", "ASRG-Iasi"),
    ("ASRG-DNCR", "ASRG-Delhi"),
    ("ASRG-DAY", "ASRG-Dayton"),
    ("ASRG-REC", "ASRG-Recife"),
    ("ASRG-BLR", "ASRG-Bangalore"),
    ("ASRG-LAX", "ASRG-Los Angeles"),
    ("ASRG-BUC", "ASRG-Bucharest"),
    ("ASRG-QRO", "ASRG-Querétaro"),
    ("ASRG-CGN", "ASRG-Cologne"),
    ("ASRG-TOR", "ASRG-Toronto"),
    ("ASRG-WIN", "ASRG-Windsor"),
    ("ASRG-KER", "ASRG-Kochi"),
    ("ASRG-VIE", "ASRG-Vienna"),
    ("ASRG-HYD", "ASRG-Hyderabad"),
)
