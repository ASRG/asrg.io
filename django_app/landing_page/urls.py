from django.urls import path
from landing_page import views

urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("privacy/", views.privacy, name="privacy"),
    path("security/", views.security, name="security"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("asip/", views.threatq, name="asip"),
]
