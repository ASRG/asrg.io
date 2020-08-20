from django.urls import path, re_path
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    # The landing page
    path('', views.landing, name='landing'),
]


urlpatterns += staticfiles_urlpatterns() 