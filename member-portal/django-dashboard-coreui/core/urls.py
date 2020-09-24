# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # authentication routes
    path("", include("website.urls")),
    path("", include("app.urls")),  # app routes
    path("", include("events.urls")), # events routes
]

if DEBUG:
        urlpatterns += static(MEDIA_URL,
                              document_root=MEDIA_ROOT)