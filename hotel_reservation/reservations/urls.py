from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.create_reservation, name='create_reservation'),
    path('reservations/<int:pk>/', views.get_reservation, name='get_reservation'),
    path('reservations/cancel/<int:pk>/', views.cancel_reservation, name='cancel_reservation'),
]
