from django.urls import path

from . import views

urlpatterns = [
    path('jobs/', views.job_posting, name='job_posting'),
    path('jobs/<int:pk>/', views.job_details, name='job_details'),
]
