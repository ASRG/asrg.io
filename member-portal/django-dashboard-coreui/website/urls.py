from django.urls import path, re_path
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # The landing page
    path('', views.landing, name='landing'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event_details, name='event_details')

]


urlpatterns += staticfiles_urlpatterns() 