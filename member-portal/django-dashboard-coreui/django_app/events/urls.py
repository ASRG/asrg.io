from django.urls import path

from events import views

urlpatterns = [
    path('events/', views.events_view, name='events'),
    path('events/<int:event_id>/', views.event_detail_view, name='event_details')

]