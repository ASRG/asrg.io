from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('privacy/', views.privacy, name='privacy'),
    path('security/', views.security, name='security'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('threatq/', views.threatq, name='threatq'),
]
