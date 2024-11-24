from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('cars/', views.car_list, name='car_list'),
    path('repairs/', views.repair_list, name='repair_list'),
]