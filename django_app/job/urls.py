from django.urls import path

from . import views

urlpatterns = [
    path("", views.job_posting, name="job_posting"),
    path("<int:pk>/", views.job_details, name="job_details"),
]
