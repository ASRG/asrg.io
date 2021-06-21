from django.urls import path

from events import views

urlpatterns = [
    path("webinars/", views.webinars_view, name="events"),
    path("<int:event_id>/", views.event_detail_view, name="event_details"),
    path("meetigns/", views.meetings_view, name="meetings_view"),
    path("conferences/", views.conferences_view, name="conferences_view"),
    path("ctfs/", views.ctfs_view, name="ctfs_view"),
    path("workshop/", views.workshop_view, name="workshop_view"),
]
