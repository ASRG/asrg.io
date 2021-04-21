from django.urls import path, re_path

from .views import security_lab

urlpatterns = [
    path("security-lab", security_lab, name="security_lab"),
]