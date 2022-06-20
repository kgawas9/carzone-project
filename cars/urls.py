from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_details, name='car-details'),
    path('search', views.search, name='search'),
]