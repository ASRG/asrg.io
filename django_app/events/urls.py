from django.urls import path

from events import views

urlpatterns = [
    path("webinars/", views.events_view, name="events"),
    path("webinars/<int:event_id>/", views.event_detail_view, name="event_details"),
]
