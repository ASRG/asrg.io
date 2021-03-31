from django.urls import path

from .views import sponsor_view

urlpatterns = [
    path("", sponsor_view, name="sponsors"),
]
