from django.urls import path

from . import views

urlpatterns = [
    path("", views.contributors, name="contributors"),
]
