# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config, Csv
from unipath import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="S#perS3crEt_1122")
SITE_ID = config("SITE_ID", default=1)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

# load production server from .env
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1, localhost", cast=Csv())

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = config("EMAIL_HOST", "NOT_THIS_ONE")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", "NOT_THIS_ONE")
EMAIL_PORT = config("EMAIL_PORT", "NOT_THIS_ONE")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", "NOT_THIS_ONE")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "NOT_THIS_ONE")

# Application definition

INSTALLED_APPS = [
    "djangocms_admin_style",  # for the admin skin. (CMS)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "authentication",
    # CMS Apps:
    "djangocms_file",
    # "djangocms_flash",
    "djangocms_googlemap",
    "djangocms_style",
    "djangocms_picture",
    # "djangocms_snippet",
    "djangocms_video",
    # "djangocms_link",
    "djangocms_text_ckeditor",  # note this needs to be above the 'cms' entry
    "cms",  # django CMS itself
    "mptt",  # utilities for implementing a tree
    "treebeard",
    "easy_thumbnails",
    "filer",
    "menus",  # helper for model independent hierarchical website navigation
    "sekizai",  # for javascript and css management
    # Internal Apps:
    "cms_app",
    "announcements",
    "job",
    "landing_page",
    "contributors",
    "leaflet",
    "events",
    "locations",
    "projects",
    "technical_committees",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "asrg.urls"
LOGIN_REDIRECT_URL = "home"  # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "asrg/templates")  # ROOT dir for templates
CMS_TEMPLATES = (
    ("cms_app/landing_template.html", "Landing page template"),
    ("cms_app/article.html", "Article template"),
)


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
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ],
        },
    },
]
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "easy_thumbnails.processors.scale_and_crop",
    "easy_thumbnails.processors.filters",
)

WSGI_APPLICATION = "asrg.wsgi.application"

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
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGES = [
    ("en-us", "English(US)"),
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


AUTH_USER_MODEL = "authentication.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = config("STATIC_ROOT", default=os.path.join(BASE_DIR, "staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "asrg/static"),
    os.path.join(BASE_DIR, "landing_page/static"),
)
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)
THUMBNAIL_HIGH_RESOLUTION = True


MEDIA_ROOT = os.path.join(BASE_DIR, "asrg/media")
MEDIA_URL = "/media/"

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
LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (6.0, 45.0),
    "DEFAULT_ZOOM": 3,
    "MIN_ZOOM": 3,
    "MAX_ZOOM": 18,
    "DEFAULT_PRECISION": 6,
}

# Google API Key <- Before Production need to save secret key somewhere.
DJANGOCMS_GOOGLEMAP_API_KEY = "AIzaSyDNoQBsyC9-L8M-YuCvdsyamnbRUnb7P4s"
