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
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False)

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Enable the inner app
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'core/static'),)
#############################################################
#############################################################
# TODO: Should we store the CHAPTERS in settings? I think this will be used in multiple components so it might be a better idea? (discuss with the team)
CHAPTERS = (
    ("ASRG-S", "ASRG-S"),
    ("ASRG-D", "ASRG-D"),
    ("ASRG-TLV", "ASRG-TLV"),
    ("ASRG-C", "ASRG-C"),
    ("ASRG-SIN", "ASRG-SIN"),
    ("ASRG-MUC", "ASRG-MUC"),
    ("ASRG-CAI", "ASRG-CAI"),
    ("ASRG-SHA", "ASRG-SHA"),
    ("ASRG-BER", "ASRG-BER"),
    ("ASRG-PIT", "ASRG-PIT"),
    ("ASRG-SFO", "ASRG-SFO"),
    ("ASRG-FRA", "ASRG-FRA"),
    ("ASRG-JPN", "ASRG-JPN"),
    ("ASRG-OXF", "ASRG-OXF"),
    ("ASRG-SYD", "ASRG-SYD"),
    ("ASRG-IASI", "ASRG-IASI"),
    ("ASRG-DNCR", "ASRG-DNCR"),
    ("ASRG-DAY", "ASRG-DAY"),
    ("ASRG-REC", "ASRG-REC"),
    ("ASRG-BLR", "ASRG-BLR"),
    ("ASRG-LAX", "ASRG-LAX"),
    ("ASRG-BUC", "ASRG-BUC"),
    ("ASRG-QRO", "ASRG-QRO"),
    ("ASRG-CGN", "ASRG-CGN"),
    ("ASRG-TOR", "ASRG-TOR"),
    ("ASRG-WIN", "ASRG-WIN"),
    ("ASRG-KER", "ASRG-KER"),
    ("ASRG-VIE", "ASRG-VIE"),
    ("ASRG-HYD", "ASRG-HYD"),
)
