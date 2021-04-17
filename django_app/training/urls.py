from django.urls import path

from . import views

urlpatterns = [
    path("", views.training_postings, name="training_postings"),
]
