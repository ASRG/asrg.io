from django.urls import path, re_path
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # The landing page
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('privacy/', views.privacy, name='privacy'),
    path('security/', views.security, name='security'),
    path('register/', views.register, name='register'),
    # path('events/', views.events, name='events'),
    # path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('jobs/', views.job_posting, name='job_posting'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('contributors/', views.contributors, name='contributors')
]


urlpatterns += staticfiles_urlpatterns()
