from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact-us', views.contact, name='contact-us')
]