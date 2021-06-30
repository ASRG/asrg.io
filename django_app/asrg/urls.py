# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("filer/", include("filer.urls")),
    path("announcements/", include("announcements.urls")),  # announcements routes
    path("contributors/", include("contributors.urls")),  # contributors routes
    path("projects/", include("projects.urls")),  # projects routes
    path("locations/", include("locations.urls")),  # locations routes
    path(
        "technical_committees/", include("technical_committees.urls")
    ),  # technical_committees routes
    path("sponsors/", include("sponsors.urls")),  # sponsors routes
    path("landing/", include("landing_page.urls")),  # landing_page routes
    # Organizational
    path("organizational/team/", views.team_view, name="team_view"),
    path("organizational/strategy/", views.strategy_view, name="strategy_view"),
    path("organizational/history/", views.history_view, name="history_view"),
    path("organizational/press/", views.press_view, name="press_view"),
    path("organizational/benefits/", views.benefits_view, name="benefits_view"),
    path("organizational/supporters/", views.supporters_view, name="supporters_view"),
    path("organizational/sponsors/", views.sponsors_view, name="sponsors_view"),
    path("organizational/privacy/", views.privacy_view, name="privacy_view"),
    path("organizational/terms-of-use/", views.termsofuse_view, name="termsofuse_view"),
    # Events
    path("events/", include("events.urls")),  # events routes
    # Knowledge
    path("knowledge/awareness/", views.awareness_view, name="awareness_view"),
    path("knowledge/asip/", views.knowledge_asip_view, name="knowledge_asip_view"),
    path("knowledge/blog/", views.blog_view, name="blog_view"),
    path("knowledge/podcast/", views.podcast_view, name="podcast_view"),
    path("knowledge/library/", views.library_view, name="library_view"),
    path("knowledge/resources/", views.resources_view, name="resources_view"),
    path(
        "knowledge/supplier-directory/",
        views.supplier_directory_view,
        name="supplier_directory_view",
    ),
    path(
        "knowledge/threat-catalog/",
        views.threat_catalog_view,
        name="threat_catalog_view",
    ),
    path(
        "knowledge/solutions-catalog/",
        views.solutions_catalog_view,
        name="solutions_catalog_view",
    ),
    path("knowledge/tools/", views.tools_view, name="tools_view"),
    path("knowledge/links/", views.links_view, name="links_view"),
    # Networking
    path("networking/channels/", views.channels_view, name="channels_view"),
    path("networking/social-media/", views.social_media_view, name="social_media_view"),
    path("networking/forums/", views.forums_view, name="forums_view"),
    path("networking/newsletter/", views.newsletter_view, name="newsletter_view"),
    # Collaboration
    path(
        "collaboration/overview/",
        views.collaboration_overview_view,
        name="collaboration_overview_view",
    ),
    path(
        "collaboration/asip/",
        views.collaboration_asip_view,
        name="collaboration_asip_view",
    ),
    path("collaboration/asvm/", views.asvm_view, name="asvm_view"),
    path(
        "collaboration/member-portal/",
        views.member_portal_view,
        name="member_portal_view",
    ),
    # Academia
    path(
        "academia/overview/",
        views.academia_overview_view,
        name="academia_overview_view",
    ),
    path("academia/learning/", views.learning_view, name="learning_view"),
    path(
        "academia/technical_committees/",
        views.technical_committees_view,
        name="technical_committees_view",
    ),
    path(
        "academia/student_organizations/",
        views.student_organizations_view,
        name="student_organizations_view",
    ),
    path("academia/research/", views.research_view, name="research_view"),
    # Industry
    path("industry/career-dev/", views.career_dev_view, name="career_dev_view"),
    path("industry/jobs/", include("job.urls")),  # jobs routes
    path("industry/trainings/", include("training.urls")),  # trainings routes
    path(
        "industry/competency-mgmt/",
        views.competency_mgmt_view,
        name="competency_mgmt_view",
    ),
    # Authentication
    path("", include("authentication.urls")),  # authentication routes
    # CMS
    path("", include("cms.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
