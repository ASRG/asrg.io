from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('jobs/', views.job_posting, name='job_posting'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
]
