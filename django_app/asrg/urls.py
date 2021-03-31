# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("filer/", include("filer.urls")),
    path("announcements/", include("announcements.urls")),  # announcements routes
    path("jobs/", include("job.urls")),  # jobs routes
    path("contributors/", include("contributors.urls")),  # contributors routes
    path("events/", include("events.urls")),  # events routes
    path("projects/", include("projects.urls")),  # projects routes
    path("locations/", include("locations.urls")),  # locations routes
    path(
        "technical_committees/", include("technical_committees.urls")
    ),  # technical_committees routes
    path("sponsors/", include("sponsors.urls")),  # sponsors routes
    path("", include("authentication.urls")),  # authentication routes
    path("", include("cms.urls")),
    path("", include("landing_page.urls")),  # landing_page routes
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
