from django.urls import path

from . import views

urlpatterns = [
    path('contributors/', views.contributors, name='contributors'),
]
